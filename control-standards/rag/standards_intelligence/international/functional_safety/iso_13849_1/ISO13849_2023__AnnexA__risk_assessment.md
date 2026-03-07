<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_13849
EDITION: 2023

HIERARCHY:
  clause: "Annex A"
  clause_title: "PLr Determination — S/F/P Risk Parameters Graph"

INDEX_TAGS:
  topics: ["PLr", "risk_assessment", "S_F_P_parameters", "risk_graph", "ISO_12100"]
  systems: ["machinery", "control_system"]
-->

# ISO 13849-1:2023 — Annex A — PLr Determination: S/F/P Risk Parameters Graph

## 0. Why this annex matters

Annex A is the normative bridge between ISO 12100 (risk assessment) and ISO 13849-1 (safety system design). It converts the qualitative risk parameters estimated in ISO 12100 Clause 5 — severity (S), frequency (F), and avoidance probability (P) — into a required Performance Level (PLr) that the safety system must achieve. Without Annex A, there is no structured basis for specifying PLr, and the design has no verified safety objective. Every ISO 13849-1 design must be traceable back to a PLr established through this annex (or an equivalent documented risk assessment method).

## 1. Risk parameters

Annex A uses the same three parameters as ISO 12100 Annex A:

| Parameter | Values | Definition |
|-----------|--------|------------|
| **S — Severity of injury** | S1: Reversible injury (minor, recoverable) | The consequence if the safety function fails and the hazard is realized |
| | S2: Irreversible injury (serious, permanent, or fatal) | |
| **F — Frequency / exposure** | F1: Seldom to less often, and/or short exposure time | How often and how long a person is exposed to the hazard |
| | F2: Frequent to continuous, and/or long exposure time | |
| **P — Possibility of avoidance** | P1: Possible under specific conditions | Ability to avoid the hazard or limit the harm if the safety function fails |
| | P2: Scarcely possible | |

These parameters are estimated during the risk assessment (ISO 12100 Clause 5) by the risk assessment team. They are not calculated — they are informed engineering judgments based on the hazard scenario, machine design, and expected use.

## 2. PLr determination table

The combination of S, F, and P maps to a PLr. All eight combinations:

| S | F | P | PLr |
|---|---|---|-----|
| S1 | F1 | P1 | PLa |
| S1 | F1 | P2 | PLb |
| S1 | F2 | P1 | PLb |
| S1 | F2 | P2 | PLc |
| S2 | F1 | P1 | PLc |
| S2 | F1 | P2 | PLd |
| S2 | F2 | P1 | PLd |
| S2 | F2 | P2 | PLe |

**Important:** This table is a representation of the normative Annex A risk graph. The normative source is the graph itself (ISO 13849-1:2023, Annex A, Figure A.1). In borderline cases (S/F/P parameters near a boundary), the graph may permit one PLr step lower with documented justification, or one step higher may be warranted by engineering judgment.

The PLr from this table is the minimum. Risk assessors may specify a higher PLr if the residual risk after all other risk reduction measures warrants it.

## 3. Worked example — E-stop on robot cell

**Scenario:** Collaborative robot cell where an operator enters the work zone to load/unload parts during each production cycle.

**Hazard:** Contact with robot arm during motion — risk of arm striking operator, causing crushing or fracture injury.

**Parameter estimation:**
- **S = S2** — robot arm contact at operational speed can cause serious or permanent injury (fracture, crush). Irreversible.
- **F = F2** — operator enters the zone every production cycle for load/unload. Frequent to continuous exposure.
- **P = P1** — operator can hear the restart warning signal and has a clear sightline to the hazard zone; avoidance is possible under specific conditions.

**PLr from table:** S2 / F2 / P1 → **PLd required**

**Architecture selection to meet PLd:**
- Category: **3** (dual-channel, cross-monitored)
- MTTFd: **High** (≥ 30 years per channel — select E-stop device with published B10d data yielding High MTTFd)
- DC: **Medium** (cross-monitoring by safety relay or safety PLC detects channel faults)
- Category 3 + MTTFd High + DC Medium → achieves **PLd** (from Clause 5 table)
- CCF: **≥ 65 points** scored per Annex F — separation of input wiring, diverse technology for input devices, protection against environmental stresses

**Result:** The design achieves PLd = PLr. The safety function is valid for this application.

## 4. When PLe is required

PLe is the highest requirement and is rare in standard industrial machinery. It arises from S2/F2/P2 combinations (see PLr table: S2/F2/P2 → PLe), or where:

- The safety function is the only risk reduction measure and there is no other barrier between the operator and a catastrophic hazard.
- Collaborative robot applications where the robot is in the nearest-operator zone with no physical guarding and the speed/force monitoring is the only protection.
- Some press guarding applications where a die-setting operator is at the point of operation with only the safety function as protection.
- Any application where the risk assessment team determines that PLd is insufficient given the actual severity and exposure.

PLe requires Category 4 architecture (dual-channel, DC High). It significantly increases design, component, and validation cost. Where possible, risk assessors should evaluate whether additional engineering risk reduction measures (physical guarding, reduced speed/force limits) can reduce the PLr from PLe to PLd before committing to Category 4.
