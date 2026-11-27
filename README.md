# Cathexis Somatic Ontology (CSO)

An open, machine-readable vocabulary for first-person somatic experience: where a sensation is felt, what it is like, how intense it is, and what it means within a clinical framework. It is built so that clinicians, researchers and software can record the same experience in the same way, and map it to the standards around it.

- **Release:** 2.0.0 (described by the paper *A Somatic Ontology for Computational Therapeutics*, version 2.3)
- **Author:** Justin DeGarbo. **Publisher:** Cathexis Health LLC
- **License:** CC BY 4.0 (see `LICENSE`)
- **Concept DOI:** [10.5281/zenodo.18859896](https://doi.org/10.5281/zenodo.18859896). **BioPortal:** [CXSO](https://bioportal.bioontology.org/ontologies/CXSO)
- **Ontology IRI:** `https://w3id.org/cxso`. **Term namespace:** `https://w3id.org/cxso/`

The ontology is named CSO. Its codes use the prefix CXSO, the acronym it is registered under on BioPortal, where CSO was taken.

## What is in it

The CSO has two parts in one namespace.

- **The core** can be used without any clinical theory: 29 body zones, 20 sensation qualities, an optional intensity from 0 to 10, a record that nothing stood out, the time, and the kind of evidence. A report is a *data point* (one zone, one quality); a *snapshot* holds the data points of one moment; a *trajectory* holds snapshots over time.
- **The clinical extension** imports the core and adds the Human Experience Framework: 16 territories, blanket configurations and components, affect systems, change and risk mechanisms, mechanism and practice types, learning levels, territory status, HES layers, and related brain and ecological terms.

## Identifiers

Every class, property and term has a permanent code: `CXSO_` followed by seven digits, for example `https://w3id.org/cxso/CXSO_0000020` (written `CXSO:0000020`), which is Upper Chest, Zone 10. Codes carry no meaning, are assigned in sequence and are never reused. Labels, definitions and synonyms can be corrected in any release; codes do not change.

This release holds 216 live codes and 1 retired code. Every one of the 171 identifiers from CSO v1.1 (`https://cathexis.health/ontology/cso/v1.1/...`) is kept, marked deprecated, and points to its new code, so data recorded with v1.1 stays readable.

## Files

| File | What it is |
|---|---|
| `cxso.ttl` / `cxso.owl` | The whole ontology (Turtle and RDF/XML; the same graph) |
| `cxso-core.ttl` / `.owl` | The core module |
| `cxso-clinical.ttl` / `.owl` | The clinical extension (imports the core) |
| `cxso-context.jsonld` | JSON-LD context: readable keys for every code |
| `cxso-2.0.0-identifiers.csv` | Every code with its label, notation, module, status, v1.1 identifier and definition |
| `CXSO_2.0.0_Spec.md` | The specification, generated from `cxso.ttl` |
| `cxso-shapes.ttl` | Data rules (SHACL) that check a report is valid CSO |
| `shapes-examples/` | Valid and deliberately invalid reports the rules are tested on |
| `fhir/` | FHIR R4 package: a CodeSystem and value sets generated from the ontology, profiles for a data point and a snapshot, and examples (FHIR Shorthand source and generated JSON) |
| `scripts/` | The checks run on every change |
| `releases/2.0.0/` | This release's files, at the address its version IRI points to |
| `index.html` | The browsable specification that term addresses open (served by GitHub Pages) |

## A report in practice

Tightness at the upper chest, intensity 6, said by the person, in Turtle:

```turtle
@prefix cxso: <https://w3id.org/cxso/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/> .

ex:snapshot1 a cxso:CXSO_0000003 ;                       # Somatic Snapshot
    cxso:CXSO_0000174 "2026-11-26T08:30:00-08:00"^^xsd:dateTime ;   # timestamp
    cxso:CXSO_0000216 ex:point1 .                         # has data point

ex:point1 a cxso:CXSO_0000002 ;                          # Somatic Data Point
    cxso:CXSO_0000158 cxso:CXSO_0000020 ;                 # zone: Upper Chest
    cxso:CXSO_0000159 cxso:CXSO_0000041 ;                 # quality: Tightness
    cxso:CXSO_0000163 6 ;                                 # intensity
    cxso:CXSO_0000175 cxso:CXSO_0000176 .                 # evidence kind: Said by the person
```

The same report in FHIR is an Observation whose `bodySite` is the zone and whose `valueCodeableConcept` is the quality, with the intensity as a component; see `fhir/fsh-generated/resources/`.

To check a report: `pyshacl -s cxso-shapes.ttl your-report.ttl`.

## Mappings

- **UBERON:** 27 of the 29 zones and every brain region link to UBERON, the open anatomy ontology. Zone links are close matches, because a zone is the area a person reports, not a precise anatomical boundary.
- **HL7 FHIR:** profiles in `fhir/`.
- **SNOMED CT:** SNOMED CT is licensed, and its codes are not in this open release. A system that needs SNOMED CT codes obtains its own license and maps within it; in the United States the license is free through the National Library of Medicine's UMLS. See the paper, Section 6.3.
- **ICD-11 and LOINC:** mapping files are not yet published.

## Status

The vocabulary is version 1 of an open standard. It was derived from clinical practice and theory and has **not yet been validated empirically**. The paper's Section 10.6 sets out how it will be tested (coverage, agreement between clinicians, stability, usability) and how it changes as evidence accumulates.

## Versions

The ontology and the paper are numbered separately: ontology release 2.0.0 is described by paper version 2.3. The ontology's number follows semantic versioning: a major number for changes that break existing data, a minor number for additions, a patch number for corrections.

## Contributing

Propose a term, a synonym or a correction through this repository's issue forms. How proposals are judged is in `CONTRIBUTING.md`.

## Citing

Cite the ontology as https://w3id.org/cxso, and a specific release by its version IRI or Zenodo DOI. `CITATION.cff` holds the citation.

## Use of AI tools

The author used AI assistants for drafting, file conversion, consistency checks and locating primary sources. Every conceptual decision, definition and change was made or approved by the author. The author takes full responsibility for the content.

The paper (version 2.3) carries the full statement, under "Use of AI Tools".

CATHEXIS is a trademark of Justin DeGarbo.
