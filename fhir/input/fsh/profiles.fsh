Alias: $cxso = https://w3id.org/cxso
Alias: $obscat = http://terminology.hl7.org/CodeSystem/observation-category

Invariant: cxso-intensity
Description: "Intensity is a whole number from 0 to 10."
Expression: "value.ofType(integer).all($this >= 0 and $this <= 10)"
Severity: #error

Invariant: cxso-snapshot-content
Description: "A snapshot holds at least one data point, or records that nothing stands out."
Expression: "hasMember.exists() or component.where(code.coding.exists(system = 'https://w3id.org/cxso' and code = 'CXSO:0000173')).value.ofType(boolean).where($this = true).exists()"
Severity: #error

Invariant: cxso-snapshot-nothing
Description: "A snapshot that records nothing stands out holds no data points."
Expression: "component.where(code.coding.exists(system = 'https://w3id.org/cxso' and code = 'CXSO:0000173')).value.ofType(boolean).where($this = true).exists() implies hasMember.empty()"
Severity: #error

RuleSet: SurveyCategory
* category ^slicing.discriminator.type = #pattern
* category ^slicing.discriminator.path = "$this"
* category ^slicing.rules = #open
* category contains survey 1..1 MS
* category[survey] = $obscat#survey

RuleSet: ComponentSlicing
* component ^slicing.discriminator.type = #pattern
* component ^slicing.discriminator.path = "code"
* component ^slicing.rules = #open

Profile: CXSOSomaticDataPoint
Parent: Observation
Id: cxso-somatic-data-point
Title: "CSO somatic data point"
Description: "A single sensation report in the Cathexis Somatic Ontology: where it is felt (a CSO zone, in bodySite), what it is like (a CSO sensation quality, in value), and optionally how intense it is (a whole number from 0 to 10). Release 2.0.0."
* status MS
* insert SurveyCategory
* code = $cxso#CXSO:0000002 "Somatic Data Point"
* code MS
* subject MS
* effective[x] MS
* bodySite 1..1 MS
* bodySite from https://w3id.org/cxso/fhir/ValueSet/zones (required)
* value[x] 1..1 MS
* value[x] only CodeableConcept
* valueCodeableConcept from https://w3id.org/cxso/fhir/ValueSet/qualities (required)
* insert ComponentSlicing
* component contains intensity 0..1 MS and evidenceKind 0..1 MS and hesLayer 0..1
* component[intensity].code = $cxso#CXSO:0000163 "intensity"
* component[intensity].value[x] 1..1
* component[intensity].value[x] only integer
* component[intensity] obeys cxso-intensity
* component[evidenceKind].code = $cxso#CXSO:0000175 "has evidence kind"
* component[evidenceKind].value[x] 1..1
* component[evidenceKind].value[x] only CodeableConcept
* component[evidenceKind].valueCodeableConcept from https://w3id.org/cxso/fhir/ValueSet/evidence-kinds (required)
* component[hesLayer] ^short = "HES layer (clinical extension)"
* component[hesLayer].code = $cxso#CXSO:0000189 "has HES layer"
* component[hesLayer].value[x] 1..1
* component[hesLayer].value[x] only CodeableConcept
* component[hesLayer].valueCodeableConcept from https://w3id.org/cxso/fhir/ValueSet/hes-layers (required)

Profile: CXSOSomaticSnapshot
Parent: Observation
Id: cxso-somatic-snapshot
Title: "CSO somatic snapshot"
Description: "A complete body state at one moment in the Cathexis Somatic Ontology. It groups its data points through hasMember, or records that nothing stood out. Release 2.0.0."
* obeys cxso-snapshot-content and cxso-snapshot-nothing
* status MS
* insert SurveyCategory
* code = $cxso#CXSO:0000003 "Somatic Snapshot"
* code MS
* subject MS
* effective[x] 1..1 MS
* effective[x] only dateTime
* value[x] 0..0
* hasMember MS
* hasMember only Reference(CXSOSomaticDataPoint)
* insert ComponentSlicing
* component contains nothingStandsOut 0..1 MS and intensity 0..1 MS
* component[nothingStandsOut].code = $cxso#CXSO:0000173 "nothing stands out"
* component[nothingStandsOut].value[x] 1..1
* component[nothingStandsOut].value[x] only boolean
* component[intensity] ^short = "Intensity of the body state as a whole"
* component[intensity].code = $cxso#CXSO:0000163 "intensity"
* component[intensity].value[x] 1..1
* component[intensity].value[x] only integer
* component[intensity] obeys cxso-intensity
