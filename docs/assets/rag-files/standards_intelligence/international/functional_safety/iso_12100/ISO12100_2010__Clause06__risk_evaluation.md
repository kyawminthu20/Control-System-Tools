<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_12100
EDITION: 2010

HIERARCHY:
  clause: "6"
  clause_title: "Risk evaluation — acceptability decision"

INDEX_TAGS:
  topics: ["risk_evaluation", "risk_acceptability", "state_of_the_art", "machinery_safety"]
  systems: ["machinery"]
-->

# ISO 12100:2010 — Clause 6 — Risk Evaluation

## 0. Why this clause matters

Clause 6 is the decision gate of the iterative risk assessment process. After risk has been estimated (Clause 5), the designer must make a structured judgement: is the estimated risk acceptable as-is, or must it be reduced? This judgement determines whether the design proceeds to Clause 7 risk reduction or exits the loop with documented residual risk. A poorly reasoned risk evaluation — either too lenient (accepting risks that should be reduced) or too conservative (requiring unnecessary measures) — can have serious consequences for safety or commercial viability. Clause 6 provides the framework for making this judgement defensible and auditable.

## 1. Acceptability criteria

ISO 12100 does not prescribe a single numerical threshold for risk acceptability. There is no universal "acceptable risk level" defined in the standard. Instead, acceptability is a contextual judgement informed by:

- The state of the art of technology for the machine type concerned
- Applicable legal requirements (EU Machinery Directive Essential Health and Safety Requirements; national regulations)
- Common technical practice as reflected in Type B and Type C standards
- The reasonable expectations of persons who will use the machine
- Known incidents and claims data for similar machines

This approach is intentional. A numeric threshold would be either too conservative for simple machinery or too permissive for high-hazard applications. The standard trusts the designer to reason from the evidence.

## 2. Factors influencing acceptability

ISO 12100 Clause 6 identifies the following factors that must be considered when judging acceptability:

| Factor | Guidance |
|--------|---------|
| **Relevant legal requirements** | National regulations and EU Directive Essential Requirements are baseline minimums. Meeting them is necessary but may not be sufficient. |
| **State of the art** | Current technical knowledge, including published standards, industry codes, and established good practice. A risk that can be readily reduced using available technology cannot be accepted simply because it is below a numeric threshold. |
| **Reasonable expectations of use** | Includes both intended use and foreseeable misuse. If a predictable misuse creates significant risk, that risk cannot be dismissed as user fault. |
| **Common technical practice** | What comparable machines on the market achieve. Significantly higher risk than comparable machines is difficult to justify. |
| **Known incidents** | Accident and near-miss data for the machine type or hazard category. Known incidents provide evidence that a hazard is not merely theoretical. |

## 3. Outcome of risk evaluation

The outcome of risk evaluation is binary:

| Outcome | Meaning | Next action |
|---------|---------|------------|
| **Risk acceptable** | The estimated risk is judged tolerable in the context of the factors above | Document the judgement and the reasons for it; record residual risk; proceed to finalise information for use |
| **Risk not acceptable** | The estimated risk is not tolerable | Proceed to Clause 7 risk reduction; re-enter the iterative loop after applying measures |

When risk is judged acceptable, the documentation must record:
- Which hazards were evaluated
- The risk estimation results (S/F/P parameters)
- The factors considered in the acceptability judgement
- The conclusion and the reasoning supporting it

Accepting a risk without documented reasoning is not compliant with ISO 12100. Market surveillance authorities and notified bodies routinely examine risk evaluation records for the adequacy of reasoning, not merely the conclusion.

## 4. Relationship to risk reduction

Risk evaluation feeds directly into the decision to enter Clause 7 or exit the loop:

- If risk is not acceptable → apply Clause 7 risk reduction → repeat from hazard identification
- If risk is acceptable → record residual risk → address in information for use (Step 3 of the three-step method)

The iterative nature means risk evaluation is performed multiple times for the same hazard — once before any measures, and again after each tier of risk reduction is applied. Each iteration must be documented separately so that the reduction achieved by each measure can be traced.
