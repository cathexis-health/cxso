"""Check the CSO data rules: every valid-* example conforms and every invalid-* example is caught.
Usage: python scripts/check_shapes.py <repository folder>"""
import glob, os, sys
import rdflib
from pyshacl import validate
R = sys.argv[1] if len(sys.argv) > 1 else "."
shapes = rdflib.Graph().parse(os.path.join(R, "cxso-shapes.ttl"), format="turtle")
bad = 0
files = sorted(glob.glob(os.path.join(R, "shapes-examples", "*.ttl")))
for f in files:
    name = os.path.basename(f)
    should = name.startswith("valid-")
    conforms, _, report = validate(rdflib.Graph().parse(f, format="turtle"), shacl_graph=shapes, advanced=True)
    ok = conforms == should
    bad += not ok
    msg = next((l.strip() for l in report.splitlines() if l.strip().startswith("Message:")), "")
    print(f"{'PASS' if ok else 'FAIL'}  {name:44} {msg}")
if not files: bad += 1; print("no examples found")
print("data rule checks pass" if not bad else f"{bad} examples did not behave as expected")
sys.exit(1 if bad else 0)
