# Changelog

## 2.0.0 (November 2026)

Described by the paper, version 2.3.

**Breaking changes**
- Permanent codes (`CXSO_0000001` onward) under `https://w3id.org/cxso/` replace identifiers based on names. Every v1.1 identifier is kept, marked deprecated, and points to its new code.
- Intensity is a whole number from 0 to 10 (it was 0.0 to 1.0), and may be used on a data point or a snapshot.

**Structure**
- The ontology is split into a core module and a clinical extension that imports it, in one namespace. The combined file holds both.
- New core properties `has data point` (CXSO_0000216) and `has snapshot` (CXSO_0000217) link a snapshot to its data points and a trajectory to its snapshots.

**Added**
- Evidence kind, nothing stands out and timestamp (core); practice types including Activation, HES layers, risk mechanisms and territory status (clinical extension); Prediction, Prediction Check and Prediction Delta (clinical extension).
- A definition for every term. Synonyms for every sensation quality.
- Links to UBERON for 27 zones and every brain region.
- Data rules (SHACL), a FHIR R4 package, and the checks that run on every change.

**Changed**
- Memory Reconsolidation is one concept with one code (CXSO_0000131); CXSO_0000151 is retired and points to it.
- Somatic Experiencing is relabelled Titrated Somatic Contact, because Somatic Experiencing is a registered trademark. The code and definition are unchanged.
- Brain regions are labelled by anatomy (Amygdala), not by psychological function.
- Properties are labelled "has ...", so no property shares a class's label.
- Blanket configurations are patterns, not disorders. Intelligence layers are numbered I1 to I4 and carry no regulatory claims.
- Each everyday word is a synonym of one quality only; emotion words are removed from the synonyms.
- Valence is a candidate, not a coded term.

**Removed from the vocabulary**
- Implementation details of the Cathexis app (visualization architecture, rendering language, routing). The ontology describes experience, not one app.

## 1.1.1

Territory labels changed to match the Human Experience Framework v3.0.1 (T7, T9, T10, T14). Identifiers unchanged.

## 1.1

29 zones and 20 sensation qualities; published on BioPortal (CXSO) and Zenodo.
