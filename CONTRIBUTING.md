# Contributing to the CSO

The CSO is meant to be shared infrastructure, so it changes in the open and by evidence.

## Proposing a change

Open an issue with the form that fits:

- **New term**: a sensation, zone or other term that existing terms cannot code.
- **Synonym**: an everyday word or phrase for an existing term.
- **Correction**: an error in a label, definition, mapping or file.

## What a proposal needs

- **For a new term:** the descriptions it would code, in people's own words where possible; why no existing term or synonym codes them; and any agreement data or clinical rationale.
- **For a synonym:** the word, the term it belongs to, and where it is used. A word codes to one term only.
- **For a correction:** what is wrong and what the source says.

A term is added only when evidence shows a recurring experience that existing terms cannot code. A near-synonym is added as a synonym, not as a new term.

## How changes are made

- Every accepted change is recorded in `CHANGELOG.md` with its reason.
- **Codes are permanent.** A published code is never deleted, reused or reassigned.
- **Retiring a term:** it stays in the ontology, marked `owl:deprecated true`. If one term replaces it, it points there with `dcterms:isReplacedBy`; otherwise a `skos:historyNote` says why it was retired and where to look instead.
- Labels, definitions and synonyms can be corrected in any release; codes do not change when they do.
- Every change must pass the checks in `scripts/`, which run automatically on each pull request.

## Who decides

The author reviews proposals and decides, and records the reason for each decision on the issue. A clinical and research advisory group is planned.
