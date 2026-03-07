<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_12100
EDITION: 2010

HIERARCHY:
  clause: "5"
  clause_title: "Risk estimation — severity, probability, avoidance"

INDEX_TAGS:
  topics: ["risk_estimation", "severity_of_harm", "frequency_exposure", "avoidance", "PLr", "machinery_safety"]
  systems: ["machinery"]
-->

# ISO 12100:2010 — Clause 5 — Risk Estimation

## 0. Why this clause matters

Risk estimation is the quantitative and qualitative characterisation step that converts a identified hazard into a set of parameters used for decision-making. The S/F/P parameters defined in Clause 5 are not abstract — they feed directly into ISO 13849-1 Annex A, where they determine the required Performance Level (PLr) for each safety function. An incorrect risk estimation therefore propagates into an incorrect PLr, which may result in a safety function that is under-designed (unsafe) or over-designed (unnecessarily costly). Clause 5 must be applied rigorously and documented.

## 1. Elements of risk

ISO 12100 defines risk as the combination of two elements:

**Risk = Severity of harm × Probability of harm occurring**

The probability of harm is itself determined by three sub-elements:

| Sub-element | Symbol | Description |
|-------------|--------|-------------|
| Frequency and duration of exposure to the hazard | F | How often and for how long a person is in the hazard zone |
| Probability of occurrence of a hazardous event | — | Reliability of machinery, human error likelihood, sudden failure possibility |
| Technical and human possibilities to avoid or limit harm | P | Whether the hazard can be detected and the harm avoided or limited |

ISO 12100 Clause 5 defines the parameters S, F, and P as the primary inputs for risk estimation, acknowledging that some elements (e.g., probability of occurrence of a hazardous event) are implicitly reflected in the overall judgement.

## 2. Severity parameters (S)

Severity of harm characterises the worst credible outcome if the hazardous event occurs and harm results. ISO 12100 uses a two-level scale:

| Parameter | Definition | Examples |
|-----------|-----------|---------|
| **S1** | Slight — normally reversible injury | Bruising, minor laceration, short-term hearing discomfort, minor burn |
| **S2** | Serious — normally irreversible injury including death | Amputation, crush injury resulting in permanent disability, fatal outcome, permanent hearing loss, severe burn |

Key guidance points:
- The assessment must consider the most credible worst case, not the average case.
- Reversibility is the primary discriminating criterion between S1 and S2.
- Multiple persons at risk increases the severity weighting in some Type C standards; ISO 12100 itself focuses on the individual but notes the number of persons exposed.
- Permanent injuries that do not result in death but are irreversible (e.g., loss of a finger) are classified S2.

## 3. Frequency and exposure (F)

Frequency and duration of exposure characterises how often and for how long persons are exposed to the hazard zone during the expected lifecycle:

| Parameter | Definition | Typical indicators |
|-----------|-----------|-------------------|
| **F1** | Seldom to infrequent exposure, and/or short duration | Infrequent maintenance access; occasional setup; short time in hazard zone relative to total operating time |
| **F2** | Frequent to continuous exposure, and/or long duration | Continuous operator presence; repeated frequent access for loading/unloading; prolonged cleaning cycles |

Key guidance points:
- F1/F2 is a judgement based on both frequency (how often) and duration (how long each exposure).
- Where access is infrequent but each visit is prolonged, this may still warrant F2.
- The threshold between F1 and F2 is not numerically defined in ISO 12100; many practitioners apply F2 when exposure frequency exceeds once per shift or duration exceeds a few minutes per visit.

## 4. Possibility of avoiding or limiting harm (P)

The possibility of avoidance characterises whether a person exposed to the hazard has a realistic chance of perceiving the hazard and avoiding or limiting the resulting harm:

| Parameter | Definition | Typical indicators |
|-----------|-----------|-------------------|
| **P1** | Possible under specific conditions | Hazard is slow-acting or visible; person has sufficient reaction time and space to withdraw; hazard is easily detected |
| **P2** | Scarcely possible | Hazard acts without warning; high speed; sudden failure; no reliable means of detection; person is trapped or constrained |

Key guidance points:
- P considers the skill and awareness of the operator in the intended operating context.
- If a guard is the only means by which a person would know the hazard exists, P2 is typically appropriate when the guard is open.
- Trained operators may achieve P1 in some situations where untrained persons would be P2; the assessment should use the least-skilled person who is permitted to perform the task.

## 5. Relationship to ISO 13849-1

The S/F/P parameters from ISO 12100 Clause 5 feed directly into ISO 13849-1 Annex A. The Annex A graph (risk graph) accepts these three parameters and outputs a required Performance Level (PLr):

| ISO 12100 Parameter | ISO 13849-1 Annex A Input |
|--------------------|--------------------------|
| S1 or S2 | Severity branch of risk graph |
| F1 or F2 | Frequency/exposure branch |
| P1 or P2 | Possibility of avoidance branch |

The six possible combinations of S, F, P yield PLr values from PLr a through PLr e:

| S | F | P | Typical PLr |
|---|---|---|------------|
| S1 | F1 | P1 | a |
| S1 | F1 | P2 | b |
| S1 | F2 | P1 | b |
| S1 | F2 | P2 | c |
| S2 | F1 | P1 | c |
| S2 | F1 | P2 | d |
| S2 | F2 | P1 | d |
| S2 | F2 | P2 | e |

Note: PLr e is the highest requirement; PLr a is the lowest. The ISO 13849-1 Annex A graph is normative — where the risk graph is used, its output is mandatory, not advisory.

IEC 62061 uses a parallel but numerically different scheme: severity (Se), frequency of exposure (Fr), and probability of avoidance (Av) combine into a Cl (class) value that maps to a SIL target. The underlying risk estimation concepts are the same; only the parameterisation and arithmetic differ.
