<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_12100
EDITION: 2010

HIERARCHY:
  clause: "4"
  clause_title: "Risk assessment principles and methodology"

INDEX_TAGS:
  topics: ["risk_assessment", "machinery_safety", "hazard_identification", "iterative_process"]
  systems: ["machinery"]
-->

# ISO 12100:2010 — Clause 4 — Risk Assessment Principles and Methodology

## 0. Why this clause matters

ISO 12100 Clause 4 defines the iterative risk assessment process that underpins CE marking under the EU Machinery Directive and all subsequent safety function design. Without a documented risk assessment structured according to Clause 4, neither an ISO 13849-1 PL determination nor an IEC 62061 SIL determination is valid — those standards explicitly require risk assessment inputs from ISO 12100. Clause 4 is therefore the logical and legal starting point for every machinery safety project.

## 1. The iterative process

ISO 12100 Clause 4 defines a closed-loop, iterative methodology. The process does not stop after a single pass — it repeats until residual risk is judged acceptable.

The four steps of the loop are:

| Step | Activity | Clause Reference |
|------|----------|-----------------|
| 1 | Hazard identification — systematically identify all hazards, hazardous situations, and hazardous events | 4.2 / Annex A |
| 2 | Risk estimation — estimate the level of risk for each identified hazard using severity (S), frequency/exposure (F), and possibility of avoidance (P) | Clause 5 |
| 3 | Risk evaluation — judge whether the estimated risk is acceptable or requires reduction | Clause 6 |
| 4 | Risk reduction — apply measures in priority order (inherently safe design, safeguarding, information for use); then return to Step 1 to verify no new hazards have been introduced | Clause 7 |

After any risk reduction measure is applied, the designer must re-enter the loop from Step 1 to confirm that:
- the original hazard has been adequately reduced,
- no new hazards have been introduced by the protective measure itself.

## 2. Scope of the risk assessment

The risk assessment must cover the entire machinery lifecycle. ISO 12100 Clause 4.4 lists the stages explicitly:

| Lifecycle Stage | Examples of hazards considered |
|----------------|-------------------------------|
| Design and construction | Sharp edges, unguarded moving parts, electrical layout |
| Transport and installation | Manual handling loads, installation clearances, commissioning energisation |
| Setting, teaching, process changeover | Access during motion, exposure to hazardous energy |
| Normal operation | Intended production cycles, operator interaction |
| Cleaning and maintenance | Access to internal zones, stored energy release |
| Fault-finding and troubleshooting | Bypassed guards, partial energisation |
| Decommissioning and disposal | Hazardous materials, structural instability |

The assessment must also account for all reasonably foreseeable misuse, not only intended use. Foreseeable misuse includes predictable operator shortcuts and behaviours that, while not intended, are plausible.

## 3. Inputs required before starting

Before beginning the hazard identification, the following must be defined:

- **Machine limits** (Clause 4.3): spatial limits (reach, movement envelopes), time limits (design life, service intervals), power limits (voltage, pressure, speed), and use limits (operator skill level, permitted tasks).
- **Intended use**: the full range of tasks the machine is designed to perform.
- **Reasonably foreseeable misuse**: predictable uses beyond the intended use that the designer can anticipate.

Failure to define machine limits before beginning hazard identification is a common error that leads to incomplete assessments.

## 4. Documentation requirements

ISO 12100 Clause 4.5 specifies what must be recorded. A compliant risk assessment file must contain:

- Description of the machine, including its limits and intended use.
- Assumptions made during the assessment.
- List of identified hazards, hazardous situations, and hazardous events.
- Risk estimation results for each hazard.
- Risk evaluation outcomes (acceptable or requires reduction).
- Risk reduction measures applied and the method used to verify their effectiveness.
- Residual risks remaining after all measures have been applied.
- Reference to information for use (warnings, labels, instructions) addressing residual risks.

The documentation must be sufficient to allow a third party (e.g., notified body, market surveillance authority) to reconstruct and verify the assessment.

## 5. Relationship to other standards

ISO 12100 occupies the top of the Type A / B / C hierarchy for machinery safety:

| Standard Type | Role | Examples |
|--------------|------|---------|
| Type A | Basic safety concepts and principles | ISO 12100 |
| Type B | Generic safety aspects applicable across machine types | ISO 13849-1, IEC 60204-1, ISO 13850, ISO 14119 |
| Type C | Machine-type-specific requirements | Robot safety (ISO 10218), press brakes, woodworking machines |

Clause 4 is the entry point that feeds all downstream standards:

- **ISO 13849-1**: Uses the S/F/P parameters from Clause 5 to determine Performance Level required (PLr) via Annex A graph.
- **IEC 62061**: Uses severity (Se), frequency of exposure (Fr), and probability of avoidance (Av) — a parallel parameterisation of the same risk estimation concepts — to determine SIL target.
- **IEC 60204-1**: Electrical safety requirements applied during design; compliance with IEC 60204-1 satisfies some protective measures identified by ISO 12100.
- **Type C standards**: Where a Type C standard specifies a risk assessment or risk reduction method for a particular machine type, it takes precedence over ISO 12100 for those specific points; ISO 12100 still fills the gaps.
