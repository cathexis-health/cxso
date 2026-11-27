# Cathexis Somatic Ontology (CSO), release 2.0.0

Generated from `cxso.ttl`. Where this file and the ontology differ, the ontology is right.

- **Namespace:** https://w3id.org/cxso/ (prefix `cxso`, CURIE prefix `CXSO`)
- **Ontology:** https://w3id.org/cxso (version https://w3id.org/cxso/releases/2.0.0/cxso.ttl)
- **Modules:** core (`cxso-core.ttl`) and clinical extension (`cxso-clinical.ttl`, which imports the core)
- **License:** CC BY 4.0. Publisher: Cathexis Health LLC. Author: Justin DeGarbo.
- **Concept DOI:** 10.5281/zenodo.18859896. Registered on BioPortal as CXSO.
- **Paper:** A Somatic Ontology for Computational Therapeutics, version 2.3.

Codes carry no meaning and are never reused. Labels, definitions and synonyms can be corrected in any release; codes do not change. Zone links to UBERON are close matches, because a zone is the area a person reports, not a precise anatomical boundary. SNOMED CT codes are not part of the open release (paper, Section 6.3).

## Core

### Body zones

| Code | # | Zone | Definition | Synonyms | UBERON |
|---|---|---|---|---|---|
| CXSO:0000011 | Zone 1 | Head / Scalp | Tension headaches, pressure, cognitive overwhelm. |  | UBERON:0000033 (close), UBERON:0000403 (close) |
| CXSO:0000012 | Zone 2 | Forehead | Tension, pressure, furrowing; cognitive strain and worry patterns. |  | UBERON:0008200 (close) |
| CXSO:0000013 | Zone 3 | Eyes | Strain, pressure, burning, tears; hypervigilance, crying suppression. |  | UBERON:0000970 (close) |
| CXSO:0000014 | Zone 4 | Jaw / TMJ | Clenching, grinding, tightness; RAGE suppression. Clinically informative. | Jaw | UBERON:0003700 (close), UBERON:0011595 (close) |
| CXSO:0000015 | Zone 5 | Mouth / Lips | Tightness, numbness, trembling; speech suppression, grief expression. |  | UBERON:0000165 (close), UBERON:0001833 (close) |
| CXSO:0000016 | Zone 6 | Throat | Constriction, lump; suppressed expression across multiple territories. |  | UBERON:0000341 (close) |
| CXSO:0000017 | Zone 7 | Neck (Front) | Tightness, vulnerability; exposure anxiety. |  | UBERON:0000974 (broad) |
| CXSO:0000018 | Zone 8 | Neck (Back) | Tension, stiffness, bracing; protective posture. |  | UBERON:0012477 (close) |
| CXSO:0000019 | Zone 9 | Shoulders | Carrying, tension, elevation; extremely common across territories. |  | UBERON:0001467 (close) |
| CXSO:0000020 | Zone 10 | Upper Chest | Tightness, pressure, racing; FEAR system activation, cardiac awareness. |  | UBERON:0001443 (close) |
| CXSO:0000021 | Zone 11 | Solar Plexus | Churning, butterflies, knot; core anxiety, diaphragmatic tension. |  | UBERON:0035276 (close) |
| CXSO:0000022 | Zone 12 | Stomach / Abdomen | Nausea, churning, sinking; gut-brain axis, visceral distress. | Stomach | UBERON:0000916 (close), UBERON:0000945 (close) |
| CXSO:0000023 | Zone 13 | Lower Abdomen / Pelvis | Tension, numbness, dissociation; trauma-sensitive zone. | Lower Abdomen | UBERON:0002355 (close), UBERON:0013203 (close) |
| CXSO:0000024 | Zone 14 | Upper Back | Tension, aching, bracing; protective posture, chronic guarding. |  | UBERON:0008231 (close) |
| CXSO:0000025 | Zone 15 | Lower Back | Aching, tension, weakness; structural support anxiety. |  | UBERON:0005462 (close) |
| CXSO:0000026 | Zone 16 | Arms (Upper) | Heaviness, weakness, restlessness; reaching, holding and pushing gestures. |  | UBERON:0003822 (close) |
| CXSO:0000027 | Zone 17 | Forearms | Tension, tingling, weakness; action readiness or suppression. |  | UBERON:0002386 (close) |
| CXSO:0000028 | Zone 18 | Hands | Clenching, tingling, numbness, sweating; highly expressive zone. |  | UBERON:0002398 (close) |
| CXSO:0000029 | Zone 19 | Hips | Tightness, restriction; mobility, procedural tension patterns. |  | UBERON:0001464 (close) |
| CXSO:0000030 | Zone 20 | Upper Legs / Thighs | Heaviness, tension, restlessness; flight readiness or collapse. | Upper Legs | UBERON:0000376 (close) |
| CXSO:0000031 | Zone 21 | Knees | Weakness, instability; structural anxiety. Clinically informative. |  | UBERON:0001465 (close) |
| CXSO:0000032 | Zone 22 | Lower Legs / Calves | Heaviness, restlessness, cramping; grounding connection. | Lower Legs | UBERON:0003823 (close), UBERON:8480048 (close) |
| CXSO:0000033 | Zone 23 | Feet | Numbness, tingling, groundedness; grounding anchor zone. |  | UBERON:0002387 (close) |
| CXSO:0000034 | Zone 24 | Pelvic Floor | Deep guarding, tension, numbness; trauma-sensitive, sexual and attachment associations. |  | UBERON:0008612 (close) |
| CXSO:0000035 | Zone 25 | Vestibular / Balance | Dizziness, unsteadiness, groundlessness; dissociative and transition states. |  | UBERON:0004681 (related) |
| CXSO:0000036 | Zone 26 | Heart | Racing, pounding, skipping; cardiac interoception distinct from chest wall tightness. |  | UBERON:0000948 (close) |
| CXSO:0000037 | Zone 27 | Diaphragm | Constriction, catching, restriction; breath holding, autonomic regulation anchor. |  | UBERON:0001103 (close) |
| CXSO:0000038 | Zone 28 | Whole Body / Systemic | Non-localizable sensations: diffuse fatigue, buzzing, heaviness. Genuinely systemic sensations that forcing localization would misrepresent. | Whole Body |  |
| CXSO:0000039 | Zone 29 | Unspecified | Present but not yet localized. Therapeutically important for people who are developing interoceptive capacity. The ratio of unspecified-to-localized reports over time measures developing body awareness. | Can't Pinpoint |  |

### Sensation qualities

| Code | Quality | Definition | Synonyms |
|---|---|---|---|
| CXSO:0000041 | Tightness | Constriction, gripping, clenching. FEAR activation, muscular bracing, suppressed expression. Most commonly reported quality across populations. | clenching, constriction, gripping, knot, stiffness, tense, tension, tight |
| CXSO:0000042 | Heat / Warmth | Radiating temperature increase, flushing. RAGE activation, shame response (facial heat), inflammatory processes. | Heat, burning, facial heat, flushing, hot, warm |
| CXSO:0000043 | Cold | Temperature decrease, chilling. Dissociative states, withdrawal, circulatory changes in freeze responses. | chilled, chilly, icy |
| CXSO:0000044 | Pressure | Compression, weight, bearing down. Overwhelm, suppressed affect, tension accumulation. | bearing down, compression, fullness, lump, weight on |
| CXSO:0000045 | Tingling | Fine electrical sensation, pins and needles. Autonomic arousal, hyperventilation, peripheral nervous system activation. | pins and needles, prickling |
| CXSO:0000046 | Numbness | Absence of sensation, deadness, blankness. Dissociation, shutdown, protective disconnection from interoceptive signal. | blank, can't feel it, dead, numb |
| CXSO:0000047 | Pain | Sharp, specific, localized nociception. Chronic pain territories, acute somatic distress, body-as-alarm. | hurting, sharp, stabbing |
| CXSO:0000048 | Heaviness | Weight, density, gravitational pull. SEEKING suppression (Living in Shutdown), fatigue, depressive somatization. | heavy, leaden, weighed down |
| CXSO:0000049 | Lightness | Buoyancy, ease. Post-regulation shift, PLAY activation, reduced sympathetic tone. | buoyant, light |
| CXSO:0000050 | Pulsing | Rhythmic beat, throbbing. Cardiovascular awareness, autonomic oscillation, activation pattern. | beating, pounding, throbbing |
| CXSO:0000051 | Hollowness | Emptiness, void, absence of substance. Grief (Living in Loss), existential states (Living in Existential Confrontation), identity emptiness (Living Behind a Mask). | Hollow, empty, void |
| CXSO:0000052 | Buzzing | An electrical hum or fizz. Anxiety activation, restlessness, autonomic hyperarousal. | electric, fizzing, humming, wired |
| CXSO:0000053 | Nausea | Stomach turning, queasiness. Gut-brain axis distress, disgust, overwhelming affect, medication effects. | churning, queasy, sick to the stomach |
| CXSO:0000054 | Aching | Deep, diffuse, persistent discomfort. Chronic tension patterns, grief somatization, sustained stress. | Ache, dull ache, sore |
| CXSO:0000055 | Vibration | An inner oscillation felt through a zone, without visible movement. High activation, trauma-related activation, release of accumulated tension. | thrumming, vibrating |
| CXSO:0000056 | Stillness | Calm absence of movement. Living in Shutdown: stillness as arrival, not absence. Living in Existential Confrontation: presence without action. A rare positive signal. | quiet, settled, still |
| CXSO:0000057 | Expansion | Outward-radiating warmth, spaciousness. A positive somatic signal, often during successful regulation. Distinct from Heat / Warmth, which has urgency: expansion is spacious. | opening, spacious, widening |
| CXSO:0000058 | Contraction | Inward-pulling compression. Withdrawal, bracing, protective narrowing. Living in Disconnection, Living in Shame: pulling inward. | collapsing inward, pulling in, shrinking |
| CXSO:0000059 | Floating | Untethered, drifting sensation. Living in an Unfamiliar Life: groundlessness. Living Under Siege: dissociative lightness. Distinct from Lightness, which has buoyancy: floating has no anchor. | drifting, spacey, unanchored |
| CXSO:0000060 | Trembling | Fine involuntary shaking, felt or seen as movement. Somatic discharge: can be regulatory (release after activation) or a sign of distress (Living Under Siege freeze-thaw, Living in Overwhelm spillover). | quivering, shaking, shivering |

### Evidence kinds

| Code | Evidence kind | Definition |
|---|---|---|
| CXSO:0000176 | Said by the person | Obtained as something said by the person. |
| CXSO:0000177 | Measured by an instrument | Obtained as a measurement by an instrument. |
| CXSO:0000178 | Sensed by a device | Obtained as something sensed by a device. |
| CXSO:0000179 | Done in an intervention | Obtained as something done in an intervention. |
| CXSO:0000180 | Noticed by the system | Obtained as something noticed by the system. |

### Classes and properties

| Code | Term | Kind | Definition |
|---|---|---|---|
| CXSO:0000001 | Somatic Entity | class | The root class for every entity in the Cathexis Somatic Ontology. |
| CXSO:0000002 | Somatic Data Point | class | A single sensation report: where in the body (zone), what kind (quality), and optionally how intense (a whole number from 0 to 10). The atomic unit of somatic data. |
| CXSO:0000003 | Somatic Snapshot | class | A complete body state at a single moment. It holds zero or more data points; with none, nothing stands out may record that the person attended to their sensations and found nothing standing out. |
| CXSO:0000004 | Somatic Trajectory | class | A body state over time: an ordered series of snapshots for one person. Aggregates computed from the series are an implementation concern, not part of the ontology. |
| CXSO:0000010 | Body Zone | class | An area of the body where a person reports a sensation. A zone is the area a person reports, not a precise anatomical boundary; it is linked to UBERON where a corresponding structure exists. |
| CXSO:0000040 | Sensation Quality | class | A phenomenological sensation descriptor. Somatic qualities, not emotional labels. Defined phenomenologically (what it feels like) rather than mechanistically (what causes it). |
| CXSO:0000172 | Evidence Kind | class | How a data point was obtained: said by the person, measured by an instrument, sensed by a device, done in an intervention, or noticed by the system. |
| CXSO:0000158 | zone | property | The anatomical zone where a sensation was reported. |
| CXSO:0000159 | quality | property | The phenomenological sensation quality reported. |
| CXSO:0000163 | intensity | property | An optional whole-number rating of how intense a sensation is, from 0 (not noticeable) to 10 (the most intense the person can imagine). Used on a data point, and optionally on a snapshot for the body state as a whole. |
| CXSO:0000166 | zone number | property | The number of a zone, from 1 to 29, as used in clinical practice ("Zone 10"). |
| CXSO:0000173 | nothing stands out | property | The person attended to their sensations and found nothing standing out. This is a report, distinct from the Numbness quality (a felt absence of sensation) and from a snapshot never taken. |
| CXSO:0000174 | timestamp | property | The time of a somatic snapshot. |
| CXSO:0000175 | has evidence kind | property | The kind of evidence by which a data point was obtained. |
| CXSO:0000216 | has data point | property | A data point that is part of a snapshot. A snapshot with nothing stands out set to true has none. |
| CXSO:0000217 | has snapshot | property | A snapshot that is part of a trajectory. A trajectory's snapshots are ordered by their timestamps. |

## Clinical extension

### Territories

| Code | # | Territory | Predictive pattern | Affect configuration | Blanket configuration |
|---|---|---|---|---|---|
| CXSO:0000062 | T1 | Living in Threat | High-precision threat predictions; ambiguous stimuli interpreted as dangerous. | FEAR up, SEEKING down, PLAY down | Porosity pattern |
| CXSO:0000063 | T2 | Living in Shutdown | Collapsed generative model; predictions of low return suppress approach behavior. | SEEKING down, PLAY down | Rigidity pattern |
| CXSO:0000064 | T3 | Living in Loss | The model of the world with the person in it persists after the person is gone; prediction errors on absence. | PANIC/GRIEF up, SEEKING variable | Damage pattern |
| CXSO:0000065 | T4 | Living in Disconnection | Relational predictions suppressed; intimacy modeled as dangerous. | PANIC/GRIEF suppressed, CARE down | Rigidity pattern |
| CXSO:0000066 | T5 | Living in Overwhelm | Multiple high-precision predictions competing simultaneously; regulatory capacity exceeded. | All systems competing | Porosity pattern |
| CXSO:0000067 | T6 | Living Under Siege | Locked threat predictions with extreme precision; inability to update despite safety. | FEAR locked, all potentially dysregulated | Damage pattern |
| CXSO:0000068 | T7 | Living in Inner Conflict | Contradictory predictions with high precision in opposing directions. | SEEKING vs FEAR, or RAGE vs FEAR | Boundary pattern |
| CXSO:0000069 | T8 | Living in the Body Under Strain | Brain's pain predictions maintained despite changed peripheral input; pain as construct. | Variable by presentation | Existential / Neurological pattern |
| CXSO:0000070 | T9 | Living Under Pressure From Outside | Accurate predictions of genuine systemic threat; the stress response is appropriate. | Contextually appropriate | Porosity pattern |
| CXSO:0000071 | T10 | Living in an Unfamiliar Life | Generative model of self under active reconstruction; predictions temporarily unreliable. | SEEKING disrupted, PANIC/GRIEF active | Boundary pattern |
| CXSO:0000072 | T11 | Living in Shame | Self-model prediction of unworthiness; core identity prediction of defectiveness. | PANIC/GRIEF + self-model damage | Damage pattern |
| CXSO:0000073 | T12 | Living in Addiction and Compulsion | SEEKING system hijacked by a substance or behavior; reward predictions distorted. | SEEKING hijacked, underlying varies | Boundary pattern |
| CXSO:0000074 | T13 | Living Behind a Mask | False-self predictions maintained; authentic predictions suppressed. | SEEKING misdirected, PLAY down | Rigidity pattern |
| CXSO:0000075 | T14 | Living in a World Built for Someone Else | Sensory processing differences; predictions calibrated to atypical neurology. | Variable | Existential / Neurological pattern |
| CXSO:0000076 | T15 | Living in Existential Confrontation | Confrontation with predictions that cannot be resolved: mortality, meaning, freedom. | SEEKING confronting limits | Existential / Neurological pattern |
| CXSO:0000077 | T16 | Living With a Changing Brain | Memory systems themselves degrading; predictions increasingly unreliable. Procedural memory is the most resilient system. | RAGE (frustration), FEAR, PANIC/GRIEF | Existential / Neurological pattern |

### Blanket configurations

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000079 |  | Porosity pattern | A blanket organization in which sensory translations are overactive: the boundary is too thin. |
| CXSO:0000080 |  | Rigidity pattern | A blanket organization in which sensory signals are suppressed: the boundary is too thick. |
| CXSO:0000081 |  | Boundary pattern | A blanket organization in which the boundary is distorted: it is misshapen. |
| CXSO:0000082 |  | Damage pattern | A blanket organization in which the boundary is ruptured: it is torn. |
| CXSO:0000083 |  | Existential / Neurological pattern | A blanket organization in which predictions may be accurate, or cannot be tested. |

### Blanket components

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000006 |  | Internal State | The person's physiological and psychological condition as experienced through interoception. What the person builds observer capacity for. |
| CXSO:0000007 |  | External State | Environmental conditions influencing internal experience. What the person cannot directly control but must relate to. |
| CXSO:0000008 |  | Sensory State | The boundary where external becomes internal: the translation mechanism. Where prediction lives. The most clinically important component. |
| CXSO:0000009 |  | Active State | The person's repertoire of responses: actions to minimize prediction error. The intervention library as a toolkit of active states. |

### Primary affect systems

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000085 |  | SEEKING | Dopaminergic motivation, exploration, curiosity. Suppression is a hallmark of Living in Shutdown. |
| CXSO:0000086 |  | FEAR | Threat detection and defensive behavior. The primary driver of Living in Threat. Locked activation of this system is central to Living Under Siege. |
| CXSO:0000087 |  | RAGE | Frustration, assertive response. Suppressed RAGE appears as jaw tension. |
| CXSO:0000088 |  | PANIC/GRIEF | Separation distress, attachment. Primary system in Living in Loss. Suppressed in Living in Disconnection. |
| CXSO:0000089 |  | CARE | Nurturing, bonding. Suppression indicates relational territory involvement. |
| CXSO:0000090 |  | PLAY | Social learning, joy, boundary-testing. Suppression is a sensitive clinical marker across all territories. |
| CXSO:0000091 |  | LUST | Sexual motivation. Relevant to Living in Disconnection, Living Under Siege, and relational territories. |

### Change mechanisms

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000131 |  | Memory Reconsolidation | Opens and updates emotional memory during the reconsolidation window (approximately 4 to 6 hours). |
| CXSO:0000132 |  | New Habit Formation | Builds new procedural patterns through repetition and reward. |
| CXSO:0000133 |  | Model Updating | Updates explicit beliefs and self-narratives through new information and reflection. |

### Mechanism types

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000131 |  | Memory Reconsolidation | Opens and updates emotional memory during the reconsolidation window (approximately 4 to 6 hours). |
| CXSO:0000147 |  | Autonomic Regulation | Shifts autonomic state via parasympathetic or sympathetic modulation. |
| CXSO:0000148 |  | Interoceptive Awareness | Builds precision of body signal detection (anterior insular cortex). |
| CXSO:0000149 |  | Titrated Somatic Contact | Titrated contact with somatic activation patterns; controlled nervous system processing. |
| CXSO:0000150 |  | Prediction Error Generation | Creates controlled mismatch between prediction and experience. |
| CXSO:0000152 |  | Interoceptive Exposure | Graduated contact with avoided body sensations. |
| CXSO:0000153 |  | Relational Somatic | Body awareness in interpersonal context. |

### Practice types

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000192 |  | Breathwork | Breath-based regulation; exhale-dominant patterns support parasympathetic activity. |
| CXSO:0000193 |  | Body Scan | Attention moved through the body, building interoceptive awareness and observer capacity. |
| CXSO:0000194 |  | Grounding | Attention anchored in present external sensory input. |
| CXSO:0000195 |  | Bilateral Stimulation | Alternating left-right stimulation, such as tapping. |
| CXSO:0000196 |  | Muscular Release | Cycles of tension and release that build awareness of the difference between them. |
| CXSO:0000197 |  | Containment | Practices that build a felt sense of boundary and limit how much is held at once. |
| CXSO:0000198 |  | Psychoeducation | Learning how predictions shape experience and how sensations are constructed; supports model updating. |
| CXSO:0000199 |  | Activation | Small movements and contact that raise arousal a little, for states of shutdown, heaviness or flatness (for example Living in Shutdown and Living in Shame), where regulation needs to move upward rather than toward calm. |

### Learning levels

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000135 | L1 | Somatic Awareness | The person notices body signals with increasing precision. |
| CXSO:0000136 | L2 | Regulation Capacity | The person shifts their own physiological state through practice. |
| CXSO:0000137 | L3 | Pattern Recognition | The person recognizes their predictions as predictions. |
| CXSO:0000138 | L4 | Prediction Testing | The person tests predictions through action in daily life. |
| CXSO:0000139 | L5 | Integration | New experience consolidates into an updated self-model. |
| CXSO:0000140 | L6 | Autonomous Practice | The person continues on their own and recognizes early warning signs. |

### Intelligence layers

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000142 | I1 | Reactive | Pattern detection over internal states only. |
| CXSO:0000143 | I2 | Adaptive | Pattern detection over internal and external states. |
| CXSO:0000144 | I3 | Pattern | Pattern detection over internal, external and sensory states. |
| CXSO:0000145 | I4 | Predictive | Pattern detection over the full blanket, over time. |

### Risk mechanisms

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000210 |  | Motivation | A reason for ending that is specific to the territory, for example "there's no point" in Living in Shutdown or "I'm the problem" in Living in Shame. |
| CXSO:0000211 |  | FEAR attenuation | The biological barrier lowering, so the person is less prevented rather than more motivated; for example metabolic conservation in Living in Shutdown, alcohol in Living in Addiction and Compulsion, dissociation in Living Under Siege. |
| CXSO:0000212 |  | Disinhibition and access to means | For example intoxication in Living in Addiction and Compulsion, impulsivity in Living in Overwhelm, or means available in the environment. |
| CXSO:0000213 |  | Isolation | The absence of a co-regulating other; for example withdrawal in Living in Disconnection, or the intact mask in Living Behind a Mask that makes a person appear fine. |

### Territory status

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000214 | active | Active | Currently organizing the person's experience. |
| CXSO:0000215 | dormant | Dormant | Installed predictions not currently active, which a later trigger may activate. |

### HES layers

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000200 | somatic | The Somatic Layer | The somatic layer of the Human Experience System. |
| CXSO:0000201 | predictive | The Predictive Layer | The predictive layer of the Human Experience System. |
| CXSO:0000202 | affective | The Affective Layer | The affective layer of the Human Experience System. |
| CXSO:0000203 | neural | The Neural Layer | The neural layer of the Human Experience System. |
| CXSO:0000204 | memory | The Memory Layer | The memory layer of the Human Experience System. |
| CXSO:0000205 | relational | The Relational Layer | The relational layer of the Human Experience System. |
| CXSO:0000206 | ecological | The Ecological Layer | The ecological layer of the Human Experience System. |
| CXSO:0000207 | generational | The Generational Layer | The generational layer of the Human Experience System. |
| CXSO:0000208 | technological | The Technological Layer | The technological layer of the Human Experience System. |
| CXSO:0000209 | temporal | The Temporal Dimension | The temporal dimension of the Human Experience System, the tenth of its layers. |

### Bronfenbrenner layers

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000125 |  | Microsystem | Immediate relationships and settings: partner, family, close friends, workplace team, home. |
| CXSO:0000126 |  | Mesosystem | Interactions between microsystems: work-family conflict, school-home dynamics. |
| CXSO:0000127 |  | Exosystem | Indirect environments that affect the individual: partner's workplace stress, community resources, media. |
| CXSO:0000128 |  | Macrosystem | Broad cultural and societal patterns: economic conditions, political climate, cultural norms. |
| CXSO:0000129 |  | Chronosystem | Transitions and shifts over time: life transitions, historical events, developmental changes. |

### Brain regions

| Code | Notation | Term | Definition | UBERON |
|---|---|---|---|---|
| CXSO:0000093 |  | Ventromedial Prefrontal / Orbitofrontal Cortex | A brain region: the ventromedial prefrontal and orbitofrontal cortex, named by the neural layer of the HES. | UBERON:0004167 (close) |
| CXSO:0000094 |  | Anterior Cingulate Cortex | A brain region: the anterior cingulate cortex, named by the neural layer of the HES. | UBERON:0009835 (exact) |
| CXSO:0000095 |  | Posterior Cingulate Cortex / Precuneus | A brain region: the posterior cingulate cortex and precuneus, named by the neural layer of the HES. | UBERON:0006093 (close), UBERON:0022353 (close) |
| CXSO:0000096 |  | Hippocampus | A brain region: the hippocampus, named by the neural layer of the HES. | UBERON:0002421 (close) |
| CXSO:0000097 |  | Thalamus | A brain region: the thalamus, named by the neural layer of the HES. | UBERON:0001897 (close) |
| CXSO:0000098 |  | Amygdala | A brain region: the amygdala, named by the neural layer of the HES. | UBERON:0001876 (exact) |
| CXSO:0000099 |  | Anterior Insula | A brain region: the anterior insula, named by the neural layer of the HES. | UBERON:0034891 (close) |
| CXSO:0000100 |  | Posterior Insula | A brain region: the posterior insula, named by the neural layer of the HES. | UBERON:0034891 (close) |
| CXSO:0000101 |  | Somatosensory Cortex | A brain region: the somatosensory cortex, named by the neural layer of the HES. | UBERON:0008930 (exact) |
| CXSO:0000102 |  | Hypothalamus | A brain region: the hypothalamus, named by the neural layer of the HES. | UBERON:0001898 (exact) |
| CXSO:0000103 |  | Brainstem | A brain region: the brainstem, including the periaqueductal gray, the nucleus of the solitary tract and the raphe nuclei, named by the neural layer of the HES. | UBERON:0002298 (close) |
| CXSO:0000104 |  | Dorsolateral Prefrontal Cortex | A brain region: the dorsolateral prefrontal cortex, named by the neural layer of the HES. | UBERON:0009834 (exact) |
| CXSO:0000105 |  | Temporal Pole | A brain region: the temporal pole, named by the neural layer of the HES. | UBERON:0002576 (exact) |
| CXSO:0000106 |  | Lateral Temporal Cortex | A brain region: the lateral temporal cortex, named by the neural layer of the HES. | UBERON:0016538 (close) |
| CXSO:0000107 |  | Parietal Cortex | A brain region: the parietal cortex, named by the neural layer of the HES. | UBERON:0016530 (exact) |
| CXSO:0000108 |  | Occipital Cortex | A brain region: the occipital cortex, named by the neural layer of the HES. | UBERON:0016540 (exact) |
| CXSO:0000109 |  | Motor / Premotor Cortex | A brain region: the primary motor and premotor cortex, named by the neural layer of the HES. | UBERON:0001384 (close), UBERON:0016634 (close) |
| CXSO:0000110 |  | Basal Ganglia | A brain region: the basal ganglia, including the nucleus accumbens, caudate and putamen, named by the neural layer of the HES. | UBERON:0010011 (close) |
| CXSO:0000111 |  | Cerebellum | A brain region: the cerebellum, named by the neural layer of the HES. | UBERON:0002037 (exact) |

### Brain networks

| Code | Notation | Term | Definition |
|---|---|---|---|
| CXSO:0000113 |  | Default Mode Network | Self-referential processing, autobiographical memory, mind-wandering, future simulation. Active during rest. Overactive in rumination (Living in Shutdown). |
| CXSO:0000114 |  | Salience Network | Detects what matters: threat, novelty, reward, social significance. The switchboard that routes attention between internal and external processing. |
| CXSO:0000115 |  | Central Executive Network | Cognitive control, working memory, goal-directed behavior, strategic planning. |
| CXSO:0000116 |  | Interoceptive Network | Body signal processing. Where the body's internal state becomes conscious felt experience. |
| CXSO:0000117 |  | Threat / Fear Circuit | Rapid threat detection and defensive response. Panksepp's FEAR system plus cortical monitoring. |
| CXSO:0000118 |  | Reward / Motivation Network | Panksepp's SEEKING system. Dopaminergic circuits that drive exploration, engagement, and approach behavior. |
| CXSO:0000119 |  | Social Brain Network | Social cognition: reading faces, voices, intentions, and relational context. Models other minds and tracks social dynamics. |
| CXSO:0000120 |  | Memory Consolidation Network | Consolidates experience into durable learning and contextualizes the present with the past. Active during reconsolidation and model updating. |
| CXSO:0000121 |  | Attachment / Loss Network | Panksepp's PANIC/GRIEF circuitry. Processes separation distress, proximity-seeking, and the somatic weight of loss (Living in Loss, Living in Disconnection). |
| CXSO:0000122 |  | PLAY Network | Panksepp's PLAY system. Social joy, spontaneity, and boundary-testing. Suppression is a cross-territory marker of chronic strain; its return marks recovery. |
| CXSO:0000123 |  | Somatomotor Network | Motor execution, body schema, proprioception. The action network, engaged by movement-based regulation practices. |

### Classes and properties

| Code | Term | Kind | Definition |
|---|---|---|---|
| CXSO:0000005 | Blanket Component | class | One of the four components of Friston's Markov blanket formalism (internal, external, sensory and active states). The clinical extension uses them to organize the classes that describe a person. |
| CXSO:0000061 | Territory of Human Experience | class | A distinct pattern of neurobiological organization. Not a diagnosis; describes how a person's nervous system is currently organized and what that organization feels like from the inside. In Pessoa's terms, a characteristic pattern of dynamic functional coalition formation. |
| CXSO:0000078 | Blanket Configuration | class | A characteristic pattern of Markov blanket organization shared by related territories. |
| CXSO:0000084 | Primary Affect System | class | One of Panksepp's seven genetically encoded primary affect systems with distinct neural circuitry. |
| CXSO:0000092 | Brain Region | class | An anatomical structure of the brain named by the neural layer of the HES. Each region is linked to its term in UBERON, the standard anatomy ontology, with skos:exactMatch, or skos:closeMatch where the match is not exact. The CSO does not define brain anatomy. UBERON does. |
| CXSO:0000112 | Brain Network | class | A functional system of interacting brain regions, as described in the research the HES draws on. Networks are concepts of the theory, not anatomical structures, so the CSO defines them itself. |
| CXSO:0000124 | Bronfenbrenner Layer | class | An ecological systems layer from Bronfenbrenner's developmental ecology. Used to classify external state entities by their proximity and influence type. |
| CXSO:0000130 | Change Mechanism | class | A therapeutic change mechanism, each engaging a distinct memory system. |
| CXSO:0000134 | Learning Level | class | One of six capacities a person builds. They tend to develop in this order, and each earlier capacity supports the ones after it, but people move between levels and may work on several at once. |
| CXSO:0000141 | Intelligence Layer | class | A level of pattern detection over somatic data, from reflecting back what the person reported to predicting what comes next. |
| CXSO:0000146 | Mechanism Type | class | A type of therapeutic intervention mechanism with defined neurobiological action. |
| CXSO:0000172 | Evidence Kind | class | How a data point was obtained: said by the person, measured by an instrument, sensed by a device, done in an intervention, or noticed by the system. |
| CXSO:0000181 | Practice Type | class | A practice type names what the person does in an intervention. |
| CXSO:0000182 | HES Layer | class | One of the ten layers of the Human Experience System (somatic, predictive, affective, neural, memory, relational, ecological, generational, technological, temporal). |
| CXSO:0000183 | Risk Mechanism | class | A mechanism of suicide risk, following HEF Chapter 25. The ontology names the mechanisms and defines no thresholds or scores, which remain clinical and implementation decisions. |
| CXSO:0000184 | Territory Status | class | Whether a territory is currently organizing the person's experience (active) or holds installed predictions that are not currently active (dormant). |
| CXSO:0000185 | Prediction | class | An expectation recorded before a period of experience. |
| CXSO:0000186 | Prediction Check | class | A record of what happened, made after the period a prediction described. |
| CXSO:0000187 | Prediction Delta | class | The difference between a prediction and a later check. |
| CXSO:0000154 | has blanket component | property | The primary Markov blanket component this entity belongs to. |
| CXSO:0000155 | has blanket configuration | property | The characteristic blanket organization pattern for a territory. |
| CXSO:0000156 | primary territories | property | Territories for which a brain region carries the strongest clinical signal. |
| CXSO:0000157 | Panksepp affects | property | Primary affect systems associated with a brain region. |
| CXSO:0000158 | zone | property | The anatomical zone where a sensation was reported. |
| CXSO:0000159 | quality | property | The phenomenological sensation quality reported. |
| CXSO:0000160 | has change mechanism | property | The primary therapeutic change mechanism for a territory. |
| CXSO:0000161 | serves territory | property | A mechanism type that serves a specific territory. |
| CXSO:0000162 | has region | property | A brain network that includes a specific brain region. |
| CXSO:0000163 | intensity | property | An optional whole-number rating of how intense a sensation is, from 0 (not noticeable) to 10 (the most intense the person can imagine). Used on a data point, and optionally on a snapshot for the body state as a whole. |
| CXSO:0000164 | is rich club hub | property | Whether this brain region is a Pessoa rich club hub with dense cross-network connectivity. |
| CXSO:0000165 | anatomical name | property | The neuroanatomical name of a brain region. |
| CXSO:0000166 | zone number | property | The number of a zone, from 1 to 29, as used in clinical practice ("Zone 10"). |
| CXSO:0000167 | territory number | property | The number of a territory, from 1 to 16, as used in clinical practice ("T1"). |
| CXSO:0000168 | affect configuration | property | The characteristic Panksepp affect system configuration for a territory. |
| CXSO:0000169 | neural substrate | property | The brain structures in which an affect system's circuitry lies. |
| CXSO:0000170 | memory system | property | The memory system a change mechanism engages. |
| CXSO:0000171 | therapeutic direction | property | The direction of therapeutic work for a blanket configuration. |
| CXSO:0000188 | has practice type | property | The practice type of an intervention: what the person does. |
| CXSO:0000189 | has HES layer | property | The Human Experience System layer in which a data point occurred. |
| CXSO:0000190 | has risk mechanism | property | Associates a record with one of the four risk mechanisms. |
| CXSO:0000191 | has territory status | property | Whether a territory is active or dormant for a person. |

## Retired identifiers

Every CSO v1.1 identifier stays in the ontology, marked deprecated, and points to its new code.

| v1.1 identifier | Replaced by | Label |
|---|---|---|
| cso:ActiveState | CXSO:0000009 | Active State |
| cso:AffectSystem | CXSO:0000084 | Primary Affect System |
| cso:BlanketComponent | CXSO:0000005 | Blanket Component |
| cso:BlanketConfiguration | CXSO:0000078 | Blanket Configuration |
| cso:BodyZone | CXSO:0000010 | Body Zone |
| cso:Boundary | CXSO:0000081 | Boundary pattern |
| cso:BrainNetwork | CXSO:0000112 | Brain Network |
| cso:BrainRegion | CXSO:0000092 | Brain Region |
| cso:BronfenbrennerLayer | CXSO:0000124 | Bronfenbrenner Layer |
| cso:CARE | CXSO:0000089 | CARE |
| cso:ChangeMechanism | CXSO:0000130 | Change Mechanism |
| cso:Damage | CXSO:0000082 | Damage pattern |
| cso:ExistentialNeurological | CXSO:0000083 | Existential / Neurological pattern |
| cso:ExternalState | CXSO:0000007 | External State |
| cso:FEAR | CXSO:0000086 | FEAR |
| cso:IL1 | CXSO:0000142 | Reactive |
| cso:IL2 | CXSO:0000143 | Adaptive |
| cso:IL3 | CXSO:0000144 | Pattern |
| cso:IL4 | CXSO:0000145 | Predictive |
| cso:IntelligenceLayer | CXSO:0000141 | Intelligence Layer |
| cso:InternalState | CXSO:0000006 | Internal State |
| cso:L1 | CXSO:0000135 | Somatic Awareness |
| cso:L2 | CXSO:0000136 | Regulation Capacity |
| cso:L3 | CXSO:0000137 | Pattern Recognition |
| cso:L4 | CXSO:0000138 | Prediction Testing |
| cso:L5 | CXSO:0000139 | Integration |
| cso:L6 | CXSO:0000140 | Autonomous Practice |
| cso:LUST | CXSO:0000091 | LUST |
| cso:LearningLevel | CXSO:0000134 | Learning Level |
| cso:MechanismType | CXSO:0000146 | Mechanism Type |
| cso:PANIC_GRIEF | CXSO:0000088 | PANIC/GRIEF |
| cso:PLAY | CXSO:0000090 | PLAY |
| cso:Porosity | CXSO:0000079 | Porosity pattern |
| cso:RAGE | CXSO:0000087 | RAGE |
| cso:Rigidity | CXSO:0000080 | Rigidity pattern |
| cso:SEEKING | CXSO:0000085 | SEEKING |
| cso:SensationQuality | CXSO:0000040 | Sensation Quality |
| cso:SensoryState | CXSO:0000008 | Sensory State |
| cso:SomaticDataPoint | CXSO:0000002 | Somatic Data Point |
| cso:SomaticEntity | CXSO:0000001 | Somatic Entity |
| cso:SomaticSnapshot | CXSO:0000003 | Somatic Snapshot |
| cso:SomaticTrajectory | CXSO:0000004 | Somatic Trajectory |
| cso:Territory | CXSO:0000061 | Territory of Human Experience |
| cso:ache | CXSO:0000054 | Aching |
| cso:addiction | CXSO:0000073 | Living in Addiction and Compulsion |
| cso:affectConfiguration | CXSO:0000168 | affect configuration |
| cso:alteredBodyMind | CXSO:0000075 | Living in a World Built for Someone Else |
| cso:amygdala | CXSO:0000098 | Amygdala |
| cso:anatomicalName | CXSO:0000165 | anatomical name |
| cso:anteriorCingulate | CXSO:0000094 | Anterior Cingulate Cortex |
| cso:anteriorInsula | CXSO:0000099 | Anterior Insula |
| cso:attachmentLoss | CXSO:0000121 | Attachment / Loss Network |
| cso:autonomicRegulation | CXSO:0000147 | Autonomic Regulation |
| cso:basalGanglia | CXSO:0000110 | Basal Ganglia |
| cso:blanketComponent | CXSO:0000154 | has blanket component |
| cso:blanketConfiguration | CXSO:0000155 | has blanket configuration |
| cso:body | CXSO:0000069 | Living in the Body Under Strain |
| cso:brainstem | CXSO:0000103 | Brainstem |
| cso:buzzing | CXSO:0000052 | Buzzing |
| cso:centralExecutive | CXSO:0000115 | Central Executive Network |
| cso:cerebellum | CXSO:0000111 | Cerebellum |
| cso:changeMechanism | CXSO:0000160 | has change mechanism |
| cso:changingBrain | CXSO:0000077 | Living With a Changing Brain |
| cso:chrono | CXSO:0000129 | Chronosystem |
| cso:cold | CXSO:0000043 | Cold |
| cso:conflict | CXSO:0000068 | Living in Inner Conflict |
| cso:contraction | CXSO:0000058 | Contraction |
| cso:defaultMode | CXSO:0000113 | Default Mode Network |
| cso:diaphragm | CXSO:0000037 | Diaphragm |
| cso:disconnection | CXSO:0000065 | Living in Disconnection |
| cso:dorsolateralPFC | CXSO:0000104 | Dorsolateral Prefrontal Cortex |
| cso:existential | CXSO:0000076 | Living in Existential Confrontation |
| cso:exo | CXSO:0000127 | Exosystem |
| cso:expansion | CXSO:0000057 | Expansion |
| cso:eyes | CXSO:0000013 | Eyes |
| cso:feet | CXSO:0000033 | Feet |
| cso:floating | CXSO:0000059 | Floating |
| cso:forearms | CXSO:0000027 | Forearms |
| cso:forehead | CXSO:0000012 | Forehead |
| cso:hands | CXSO:0000028 | Hands |
| cso:hasRegion | CXSO:0000162 | has region |
| cso:headScalp | CXSO:0000011 | Head / Scalp |
| cso:heart | CXSO:0000036 | Heart |
| cso:heat | CXSO:0000042 | Heat / Warmth |
| cso:heaviness | CXSO:0000048 | Heaviness |
| cso:hippocampus | CXSO:0000096 | Hippocampus |
| cso:hips | CXSO:0000029 | Hips |
| cso:hollow | CXSO:0000051 | Hollowness |
| cso:hypothalamus | CXSO:0000102 | Hypothalamus |
| cso:intensity | CXSO:0000163 | intensity |
| cso:interoceptive | CXSO:0000116 | Interoceptive Network |
| cso:interoceptiveAwareness | CXSO:0000148 | Interoceptive Awareness |
| cso:interoceptiveExposure | CXSO:0000152 | Interoceptive Exposure |
| cso:isRichClubHub | CXSO:0000164 | is rich club hub |
| cso:jaw | CXSO:0000014 | Jaw / TMJ |
| cso:knees | CXSO:0000031 | Knees |
| cso:lateralTemporalCortex | CXSO:0000106 | Lateral Temporal Cortex |
| cso:lightness | CXSO:0000049 | Lightness |
| cso:loss | CXSO:0000064 | Living in Loss |
| cso:lowerAbdomen | CXSO:0000023 | Lower Abdomen / Pelvis |
| cso:lowerBack | CXSO:0000025 | Lower Back |
| cso:lowerLegs | CXSO:0000032 | Lower Legs / Calves |
| cso:macro | CXSO:0000128 | Macrosystem |
| cso:mask | CXSO:0000074 | Living Behind a Mask |
| cso:memoryConsolidation | CXSO:0000120 | Memory Consolidation Network |
| cso:memoryReconsolidationMechanism | CXSO:0000131 | Memory Reconsolidation |
| cso:memorySystem | CXSO:0000170 | memory system |
| cso:meso | CXSO:0000126 | Mesosystem |
| cso:micro | CXSO:0000125 | Microsystem |
| cso:modelUpdating | CXSO:0000133 | Model Updating |
| cso:motorCortex | CXSO:0000109 | Motor / Premotor Cortex |
| cso:mouthLips | CXSO:0000015 | Mouth / Lips |
| cso:nausea | CXSO:0000053 | Nausea |
| cso:neckBack | CXSO:0000018 | Neck (Back) |
| cso:neckFront | CXSO:0000017 | Neck (Front) |
| cso:neuralSubstrate | CXSO:0000169 | neural substrate |
| cso:newHabitFormation | CXSO:0000132 | New Habit Formation |
| cso:numbness | CXSO:0000046 | Numbness |
| cso:occipitalCortex | CXSO:0000108 | Occipital Cortex |
| cso:overwhelm | CXSO:0000066 | Living in Overwhelm |
| cso:pain | CXSO:0000047 | Pain |
| cso:pankseppAffects | CXSO:0000157 | Panksepp affects |
| cso:parietalCortex | CXSO:0000107 | Parietal Cortex |
| cso:pelvicFloor | CXSO:0000034 | Pelvic Floor |
| cso:play | CXSO:0000122 | PLAY Network |
| cso:posteriorCingulate | CXSO:0000095 | Posterior Cingulate Cortex / Precuneus |
| cso:posteriorInsula | CXSO:0000100 | Posterior Insula |
| cso:predictionErrorGeneration | CXSO:0000150 | Prediction Error Generation |
| cso:prefrontalCortex | CXSO:0000093 | Ventromedial Prefrontal / Orbitofrontal Cortex |
| cso:pressure | CXSO:0000044 | Pressure |
| cso:primaryTerritories | CXSO:0000156 | primary territories |
| cso:pulsing | CXSO:0000050 | Pulsing |
| cso:quality | CXSO:0000159 | quality |
| cso:reconsolidation | CXSO:0000131 | Memory Reconsolidation |
| cso:relationalSomatic | CXSO:0000153 | Relational Somatic |
| cso:salience | CXSO:0000114 | Salience Network |
| cso:seeking | CXSO:0000118 | Reward / Motivation Network |
| cso:sensorimotor | CXSO:0000123 | Somatomotor Network |
| cso:servesTerritory | CXSO:0000161 | serves territory |
| cso:shame | CXSO:0000072 | Living in Shame |
| cso:shoulders | CXSO:0000019 | Shoulders |
| cso:shutdown | CXSO:0000063 | Living in Shutdown |
| cso:siege | CXSO:0000067 | Living Under Siege |
| cso:socialBrain | CXSO:0000119 | Social Brain Network |
| cso:solarPlexus | CXSO:0000021 | Solar Plexus |
| cso:somaticExperiencing | CXSO:0000149 | Titrated Somatic Contact |
| cso:somatosensoryCortex | CXSO:0000101 | Somatosensory Cortex |
| cso:stillness | CXSO:0000056 | Stillness |
| cso:stomach | CXSO:0000022 | Stomach / Abdomen |
| cso:systemPressure | CXSO:0000070 | Living Under Pressure From Outside |
| cso:temporalPole | CXSO:0000105 | Temporal Pole |
| cso:territoryNumber | CXSO:0000167 | territory number |
| cso:thalamus | CXSO:0000097 | Thalamus |
| cso:therapeuticDirection | CXSO:0000171 | therapeutic direction |
| cso:threat | CXSO:0000062 | Living in Threat |
| cso:threatFear | CXSO:0000117 | Threat / Fear Circuit |
| cso:throat | CXSO:0000016 | Throat |
| cso:tightness | CXSO:0000041 | Tightness |
| cso:tingling | CXSO:0000045 | Tingling |
| cso:transition | CXSO:0000071 | Living in an Unfamiliar Life |
| cso:trembling | CXSO:0000060 | Trembling |
| cso:unspecified | CXSO:0000039 | Unspecified |
| cso:upperArms | CXSO:0000026 | Arms (Upper) |
| cso:upperBack | CXSO:0000024 | Upper Back |
| cso:upperChest | CXSO:0000020 | Upper Chest |
| cso:upperLegs | CXSO:0000030 | Upper Legs / Thighs |
| cso:vestibular | CXSO:0000035 | Vestibular / Balance |
| cso:vibration | CXSO:0000055 | Vibration |
| cso:wholeBody | CXSO:0000038 | Whole Body / Systemic |
| cso:zone | CXSO:0000158 | zone |
| cso:zoneNumber | CXSO:0000166 | zone number |
| CXSO:0000151 | CXSO:0000131 | Memory Reconsolidation |
