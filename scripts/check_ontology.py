"""Check the CSO ontology files: Turtle and RDF/XML agree, codes are sound, the modules are clean.
Usage: python scripts/check_ontology.py <repository folder>"""
import csv, os, sys
import rdflib
from rdflib.compare import to_isomorphic
from rdflib.namespace import OWL, SKOS, DCTERMS, RDFS
R = sys.argv[1] if len(sys.argv) > 1 else "."
CX = "https://w3id.org/cxso/"
problems = []
graphs = {}
for name in ["cxso", "cxso-core", "cxso-clinical"]:
    t = rdflib.Graph().parse(os.path.join(R, f"{name}.ttl"), format="turtle")
    o = rdflib.Graph().parse(os.path.join(R, f"{name}.owl"), format="xml")
    if to_isomorphic(t) != to_isomorphic(o): problems.append(f"{name}.ttl and {name}.owl differ")
    graphs[name] = t
    print(f"{name}: {len(t)} statements; Turtle and RDF/XML {'agree' if to_isomorphic(t) == to_isomorphic(o) else 'DIFFER'}")
g = graphs["cxso"]
codes = {s for s in g.subjects() if str(s).startswith(CX + "CXSO_")}
live = {s for s in codes if (s, OWL.deprecated, None) not in g}
nums = sorted(int(str(s)[-7:]) for s in codes)
if nums != list(range(1, len(nums) + 1)): problems.append("codes are not a gap-free sequence from 1")
labels, alts = {}, {}
for s in live:
    pl = list(g.objects(s, SKOS.prefLabel))
    if len(pl) != 1: problems.append(f"{s} has {len(pl)} preferred labels")
    if (s, SKOS.definition, None) not in g: problems.append(f"{s} has no definition")
    k = str(pl[0]).lower() if pl else ""
    if k in labels: problems.append(f"label '{k}' is used twice")
    labels[k] = s
for s in live:
    for a in g.objects(s, SKOS.altLabel):
        k = str(a).lower()
        if k in alts and alts[k] != s: problems.append(f"synonym '{k}' belongs to two terms")
        if k in labels and labels[k] != s: problems.append(f"synonym '{k}' is another term's label")
        alts[k] = s
for s in g.subjects(OWL.deprecated, rdflib.Literal(True)):
    r = list(g.objects(s, DCTERMS.isReplacedBy))
    if len(r) != 1: problems.append(f"retired {s} has {len(r)} replacements")
    elif (r[0], OWL.deprecated, None) in g: problems.append(f"retired {s} points at a retired code")
mod = {r["code"]: r["module"] for r in csv.DictReader(open(os.path.join(R, "cxso-2.0.0-identifiers.csv")))}
for s, p, o in graphs["cxso-core"]:
    for x in (p, o):
        c = str(x)[len(CX):] if str(x).startswith(CX + "CXSO_") else None
        if c and mod.get(c) == "clinical": problems.append(f"core refers to clinical term {c}")
heads = {rdflib.URIRef(CX[:-1]), rdflib.URIRef(CX + "core"), rdflib.URIRef(CX + "clinical")}
def terms(gr):
    out = rdflib.Graph()
    for t in gr:
        if t[0] not in heads: out.add(t)
    return out
if to_isomorphic(terms(graphs["cxso-core"]) + terms(graphs["cxso-clinical"])) != to_isomorphic(terms(g)):
    problems.append("core plus clinical does not equal the combined file")
print(f"{len(live)} live codes, {len(codes) - len(live)} retired")
for p in problems: print("PROBLEM:", p)
print("ontology checks pass" if not problems else f"{len(problems)} problems")
sys.exit(1 if problems else 0)
