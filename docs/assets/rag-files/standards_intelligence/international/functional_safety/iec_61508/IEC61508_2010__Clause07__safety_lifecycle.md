<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61508
EDITION: 2010

HIERARCHY:
  clause: "7"
  clause_title: "Overall Safety Lifecycle"

INDEX_TAGS:
  topics: ["functional_safety", "safety_lifecycle", "hazard_analysis", "safety_requirements", "functional_safety_management"]
  systems: ["all_industries", "control_system"]
-->

# IEC 61508:2010 — Clause 7 — Overall Safety Lifecycle

## 0. Why this matters

Clause 7 defines the 16-phase overall safety lifecycle that is the structural backbone of IEC 61508. Both IEC 62061 and IEC 61511 adapt and simplify this lifecycle for their respective domains. Understanding the 16 phases explains why both sector standards are structured as they are — every clause in IEC 62061 and IEC 61511 maps to one or more of these 16 phases.

The lifecycle is also the framework for functional safety management documentation: safety plans, safety cases, safety validation reports, and functional safety assessments all trace to specific lifecycle phases.

## 1. The 16 phases

The 16 phases group into four logical blocks:

### Concept block (phases 1–3)

| Phase | Name | Key activities |
|-------|------|----------------|
| 1 | Concept | Define the system boundary and operational context |
| 2 | Overall Scope Definition | Define EUC (equipment under control) and EUC control system; establish the scope of the safety lifecycle |
| 3 | Hazard and Risk Analysis | Identify hazardous events; estimate risk; establish tolerable risk targets |

**Purpose:** Understand what the system does, what can go wrong, and how much risk is acceptable. This block establishes the basis for all subsequent decisions.

### Requirements block (phases 4–7)

| Phase | Name | Key activities |
|-------|------|----------------|
| 4 | Overall Safety Requirements | Define all safety functions required to achieve tolerable risk |
| 5 | Safety Requirements Allocation | Assign safety functions to protection layers (E/E/PE system, other technology, external facilities) |
| 6 | Overall Operation and Maintenance Planning | Plan for ongoing inspection, testing, and maintenance of safety functions |
| 7 | Overall Safety Validation Planning | Plan the validation activities that will confirm safety requirements are met |

**Purpose:** Translate the risk analysis into specific, testable requirements and assign them to the correct part of the system.

### Realisation block (phases 8–13)

| Phase | Name | Key activities |
|-------|------|----------------|
| 8 | Overall Planning (Safety Assessment) | Plan the independent safety assessment |
| 9 | E/E/PE System Realization | Design, build, integrate, and test the E/E/PE safety-related system per Parts 2 and 3 |
| 10 | Other Technology Realization | Design and implement non-E/E/PE safety measures (mechanical guards, pneumatic interlocks, etc.) |
| 11 | External Risk Reduction Facilities Realization | Implement risk reduction not part of the EUC or EUC control system (e.g., exclusion zones, PPE procedures) |
| 12 | Overall Installation and Commissioning Planning | Plan installation and commissioning |
| 13 | Overall Safety Validation | Execute validation; confirm all safety functions perform as required |

**Purpose:** Build and verify the system. Phase 9 is where Parts 2 (hardware) and 3 (software) requirements are applied.

### Operation block (phases 14–16)

| Phase | Name | Key activities |
|-------|------|----------------|
| 14 | Overall Operation, Maintenance and Repair | Operate the system per the validated safety case; maintain records; perform proof tests |
| 15 | Overall Modification | Apply change control; revalidate affected safety functions after modification |
| 16 | Decommissioning | Safely remove the system; manage any new hazards created by removal |

**Purpose:** Maintain the safety integrity of the system throughout its operational life. The safety lifecycle does not end at commissioning.

## 2. Functional safety management

Clause 7 includes functional safety management (FSM) requirements that span all 16 phases. These are not a separate activity — they are management obligations that apply throughout the lifecycle.

Key FSM requirements:
- **Documentation:** A functional safety plan must be established and maintained; it defines the activities, responsible parties, and records for the entire lifecycle
- **Competency:** Persons performing safety lifecycle activities must be competent for those activities; competency is documented
- **Independence:** The level of independence required between the team that develops the E/E/PE system and the team that validates it increases with SIL:
  - SIL 1: Independence recommended but not mandatory
  - SIL 2: Independent person within the same project team
  - SIL 3–4: Independent team or department; organizational separation
- **Functional safety assessment:** An independent assessment that the safety lifecycle has been followed and the safety requirements are met; required at SIL 2 and above in most interpretations

**Why independence matters:** At SIL 3+, the person who designed the system cannot be the sole person who validates it. Cognitive bias — the designer's assumptions — must be challenged by someone who did not make those assumptions.

## 3. Lifecycle in practice for machinery

For a machine builder implementing IEC 62061 (the machinery sector standard), the 16-phase IEC 61508 lifecycle maps as follows:

| IEC 61508 phases | IEC 62061 equivalent | Practical activity |
|------------------|---------------------|-------------------|
| Phases 1–3 (Concept, Scope, Hazard & Risk) | ISO 12100 risk assessment + IEC 62061 Clause 5 (SRECS scope) | Risk assessment on the machine; identify required safety functions |
| Phases 4–5 (Safety Requirements, Allocation) | IEC 62061 Clauses 5–6 (SIL determination, safety function specification) | Determine SIL for each safety function; allocate to SRECS subsystems |
| Phase 6–7 (O&M planning, Validation planning) | IEC 62061 Clause 5 (validation planning) + operation documentation | Write the safety validation plan; define proof test intervals |
| Phases 8–13 (Realisation) | IEC 62061 Clauses 6–8 (design, build, integrate) | Select and configure safety PLC and I/O; write application software; verify PFHd calculations |
| Phase 13 (Validation) | IEC 62061 Clause 8 (safety validation) | Execute validation test plan; confirm all safety functions operate correctly |
| Phases 14–16 (Operation, Modification, Decommission) | IEC 62061 Clause 8 + maintenance documentation | Perform periodic proof tests; manage changes with change control; document decommissioning |

**Key insight:** IEC 62061 does not replace the lifecycle — it implements it in machinery terms. An engineer who understands the 16 phases can navigate both IEC 62061 and IEC 61511 because both are structured as implementations of the same lifecycle.

## 4. Change log

- 2026-03-06 — Phase 3 corpus creation; Clause 7 safety lifecycle document established.
