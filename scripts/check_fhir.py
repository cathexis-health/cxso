# Usage: python scripts/check_fhir.py <fhir folder>
"""Check the CSO FHIR package: every file against the FHIR R4B data model, and the profiles' rules
(bindings, cardinalities, invariants) against good and deliberately broken examples."""
import copy, glob, json, os, sys
from fhir.resources.R4B.codesystem import CodeSystem
from fhir.resources.R4B.valueset import ValueSet
from fhir.resources.R4B.structuredefinition import StructureDefinition
from fhir.resources.R4B.observation import Observation
from fhir.resources.R4B.patient import Patient
from fhirpathpy import evaluate
from fhirpathpy.models import models as FP_MODELS
R4 = FP_MODELS['r4']
D = sys.argv[1]
MODELS = {"CodeSystem": CodeSystem, "ValueSet": ValueSet, "StructureDefinition": StructureDefinition, "Observation": Observation, "Patient": Patient}
files = sorted(glob.glob(os.path.join(D, "input/resources/*.json")) + glob.glob(os.path.join(D, "fsh-generated/resources/*.json")))
bad = 0
for f in files:
    j = json.load(open(f))
    try:
        MODELS[j["resourceType"]].model_validate(j); print("model ok   ", os.path.basename(f))
    except Exception as e:
        bad += 1; print("MODEL FAIL ", os.path.basename(f), str(e)[:300])

vs = {json.load(open(f))["url"]: {c["code"] for c in json.load(open(f))["compose"]["include"][0]["concept"]}
      for f in glob.glob(os.path.join(D, "input/resources/ValueSet-*.json"))}
cs_codes = {c["code"] for c in json.load(open(os.path.join(D, "input/resources/CodeSystem-cxso.json")))["concept"]}
SYS = "https://w3id.org/cxso"; BASE = "https://w3id.org/cxso/fhir/ValueSet/"
sd = {json.load(open(f))["id"]: json.load(open(f)) for f in glob.glob(os.path.join(D, "fsh-generated/resources/StructureDefinition-*.json"))}
inv = {}
for p in sd.values():
    for el in p["snapshot"]["element"] if "snapshot" in p else p["differential"]["element"]:
        for c in el.get("constraint", []):
            if c["key"].startswith("cxso-"): inv.setdefault(p["id"], []).append((el["path"], c["key"], c["expression"]))

def comp(o, code):
    return [c for c in o.get("component", []) if any(x.get("system") == SYS and x.get("code") == code for x in c["code"]["coding"])]
def check_point(o):
    errs = []
    z = o.get("bodySite", {}).get("coding", [])
    if len(z) != 1 or z[0].get("code") not in vs[BASE + "zones"]: errs.append("bodySite must be one CSO zone")
    q = o.get("valueCodeableConcept", {}).get("coding", [])
    if len(q) != 1 or q[0].get("code") not in vs[BASE + "qualities"]: errs.append("value must be one CSO quality")
    for c in comp(o, "CXSO:0000175"):
        if c["valueCodeableConcept"]["coding"][0]["code"] not in vs[BASE + "evidence-kinds"]: errs.append("evidence kind not in value set")
    if len(comp(o, "CXSO:0000163")) > 1: errs.append("more than one intensity")
    if not any(x.get("system") == SYS and x.get("code") == "CXSO:0000002" for x in o["code"]["coding"]): errs.append("code must be CXSO:0000002")
    errs += invariants(o, "cxso-somatic-data-point")
    return errs
def check_snapshot(o):
    errs = []
    if "effectiveDateTime" not in o: errs.append("effectiveDateTime required")
    if not any(x.get("system") == SYS and x.get("code") == "CXSO:0000003" for x in o["code"]["coding"]): errs.append("code must be CXSO:0000003")
    errs += invariants(o, "cxso-somatic-snapshot")
    return errs
def invariants(o, prof):
    errs = []
    for path, key, expr in inv.get(prof, []):
        if path == "Observation":
            full = expr
        else:  # component-level rule, reached from the Observation as the validator does
            full = f"component.where(code.coding.exists(system = '{SYS}' and code = 'CXSO:0000163')).all({expr})"
        r = evaluate(o, full, {}, R4)
        if r != [True]: errs.append(f"{key} fails")
    return errs

ex = {os.path.basename(f): json.load(open(f)) for f in glob.glob(os.path.join(D, "fsh-generated/resources/Observation-*.json"))}
cases = []
for n, o in ex.items():
    kind = "snapshot" if "snapshot" in n else "point"
    cases.append((n, kind, o, True))
P = ex["Observation-example-point-upper-chest.json"]; S = ex["Observation-example-snapshot-morning.json"]; N = ex["Observation-example-snapshot-nothing-stands-out.json"]
def broken(name, kind, base, fn):
    o = copy.deepcopy(base); fn(o); cases.append((name, kind, o, False))
broken("intensity 11", "point", P, lambda o: [c.update(valueInteger=11) for c in comp(o, "CXSO:0000163")])
broken("quality used as zone", "point", P, lambda o: o["bodySite"]["coding"][0].update(code="CXSO:0000041"))
broken("retired code as quality", "point", P, lambda o: o["valueCodeableConcept"]["coding"][0].update(code="CXSO:0000151"))
broken("unknown evidence kind", "point", P, lambda o: [c["valueCodeableConcept"]["coding"][0].update(code="CXSO:0000020") for c in comp(o, "CXSO:0000175")])
broken("empty snapshot", "snapshot", S, lambda o: o.pop("hasMember"))
broken("nothing stands out with points", "snapshot", S, lambda o: o["component"].append({"code": {"coding": [{"system": SYS, "code": "CXSO:0000173"}]}, "valueBoolean": True}))
broken("snapshot without time", "snapshot", N, lambda o: o.pop("effectiveDateTime"))
for name, kind, o, should in cases:
    errs = check_point(o) if kind == "point" else check_snapshot(o)
    ok = (not errs) == should
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:46} {'valid' if not errs else '; '.join(errs)}")
missing = [c for f in glob.glob(os.path.join(D, "input/resources/ValueSet-*.json")) for c in json.load(open(f))["compose"]["include"][0]["concept"] if c["code"] not in cs_codes]
print("value set codes missing from the CodeSystem:", len(missing))
print("invariants found:", {k: [i[1] for i in v] for k, v in inv.items()})
print("ALL CHECKS PASS" if not bad and not missing else f"{bad} problems")
sys.exit(1 if bad or missing else 0)
