Alias: $cxso = https://w3id.org/cxso
Alias: $obscat = http://terminology.hl7.org/CodeSystem/observation-category

Instance: example-point-upper-chest
InstanceOf: CXSOSomaticDataPoint
Title: "Tightness at the upper chest, intensity 6, said by the person"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* text.status = #generated
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Tightness at the upper chest, intensity 6 on a scale of 0 to 10, said by the person. Recorded 26 November 2026 at 08:30 (UTC-08:00).</p></div>"
* subject = Reference(Patient/example-person) "Example person"
* performer = Reference(Patient/example-person) "Example person"
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
* text.status = #generated
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Pressure in the throat. Recorded 26 November 2026 at 08:30 (UTC-08:00).</p></div>"
* subject = Reference(Patient/example-person) "Example person"
* performer = Reference(Patient/example-person) "Example person"
* effectiveDateTime = "2026-11-26T08:30:00-08:00"
* bodySite = $cxso#CXSO:0000016 "Throat"
* valueCodeableConcept = $cxso#CXSO:0000044 "Pressure"

Instance: example-snapshot-morning
InstanceOf: CXSOSomaticSnapshot
Title: "A morning snapshot holding two data points"
Usage: #example
* status = #final
* category[survey] = $obscat#survey
* text.status = #generated
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Morning snapshot, 26 November 2026 at 08:30 (UTC-08:00): tightness at the upper chest and pressure in the throat. Intensity of the body state as a whole: 5 on a scale of 0 to 10.</p></div>"
* subject = Reference(Patient/example-person) "Example person"
* performer = Reference(Patient/example-person) "Example person"
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
* text.status = #generated
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Evening snapshot, 26 November 2026 at 21:00 (UTC-08:00): nothing stood out.</p></div>"
* subject = Reference(Patient/example-person) "Example person"
* performer = Reference(Patient/example-person) "Example person"
* effectiveDateTime = "2026-11-26T21:00:00-08:00"
* component[nothingStandsOut].valueBoolean = true

Instance: example-person
InstanceOf: Patient
Title: "The example person (not a real person)"
Description: "The person in the CSO examples. They report their own sensations, so they are both the subject and the performer of each observation."
Usage: #example
* text.status = #generated
* text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p>Example person, used only in the CSO examples. Not a real person.</p></div>"
* name.text = "Example person"
