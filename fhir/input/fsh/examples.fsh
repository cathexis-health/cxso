Alias: $cxso = https://w3id.org/cxso
Alias: $obscat = http://terminology.hl7.org/CodeSystem/observation-category

Instance: example-point-upper-chest
InstanceOf: CXSOSomaticDataPoint
Title: "Tightness at the upper chest, intensity 6, said by the person"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* subject.display = "Example person"
* effectiveDateTime = "2026-11-26T08:30:00-08:00"
* bodySite = $cxso#CXSO:0000020 "Upper Chest"
* valueCodeableConcept = $cxso#CXSO:0000041 "Tightness"
* component[intensity].valueInteger = 6
* component[evidenceKind].valueCodeableConcept = $cxso#CXSO:0000176 "Said by the person"

Instance: example-point-throat
InstanceOf: CXSOSomaticDataPoint
Title: "Pressure in the throat"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* subject.display = "Example person"
* effectiveDateTime = "2026-11-26T08:30:00-08:00"
* bodySite = $cxso#CXSO:0000016 "Throat"
* valueCodeableConcept = $cxso#CXSO:0000044 "Pressure"

Instance: example-snapshot-morning
InstanceOf: CXSOSomaticSnapshot
Title: "A morning snapshot holding two data points"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* subject.display = "Example person"
* effectiveDateTime = "2026-11-26T08:30:00-08:00"
* hasMember[0] = Reference(Observation/example-point-upper-chest)
* hasMember[1] = Reference(Observation/example-point-throat)
* component[intensity].valueInteger = 5

Instance: example-snapshot-nothing-stands-out
InstanceOf: CXSOSomaticSnapshot
Title: "An evening snapshot in which nothing stood out"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* subject.display = "Example person"
* effectiveDateTime = "2026-11-26T21:00:00-08:00"
* component[nothingStandsOut].valueBoolean = true
