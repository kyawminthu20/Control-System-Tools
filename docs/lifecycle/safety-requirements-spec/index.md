---
layout: default
title: "Lifecycle Stage 3.5 — Safety Requirements Specification"
description: "The SRS is the contract between risk assessment and architecture — every safety function defined with required PL/SIL, inputs, outputs, and response time."
redirect_from:
  - /verification/safety-requirements-spec/
  - /lifecycle/safety-requirements-spec/index.html
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "3.5. Safety Requirements Spec"
related_standards:
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 03.5</span>
  <h1>Safety Requirements Specification</h1>
  <p>The contract between risk assessment and architecture — defines every safety function in engineering terms before design begins.</p>
</div>

## 1. Purpose

The Safety Requirements Specification (SRS) is the formal document that captures every safety function identified in the risk assessment and expresses each one as an engineering requirement. It is the contract between "what risk was found" (Stage 3) and "what are we designing" (Stage 4).

The SRS translates qualitative hazard findings into quantitative, traceable engineering requirements. For each safety function, it specifies what the function must do, how quickly it must respond, what the required integrity level is, and what devices are involved — in enough detail that an architect or designer can act on it without ambiguity.

Standards basis for this stage:

- **IEC 62061 §5.3** — Safety function specification, including required SILCL, I/O definition, demand mode, and response time
- **IEC 61511-1 §10** — Safety requirements specification for each Safety Instrumented Function (SIF), including SIL, demand mode, PFDavg, response time, process inputs and outputs
- **ISO 13849-1 §5** — Safety function specification including required PLr, input devices, logic controller, and output devices
- **IEC 61508-1 §7.3** — Safety requirements specification as a core deliverable of the overall safety lifecycle

---

## 2. Why the SRS Is the Most Important Deliverable

The SRS is the single most referenced document in safety audits. It is the anchor point for every downstream deliverable:

- **Architecture** (Stage 4) cannot be designed without knowing what each safety function must achieve
- **PL/SIL calculations** cannot be performed without knowing the required PLr or SIL target per function
- **Verification and validation** (Stage 10) cannot be completed without SRS requirements to test against
- **Traceability** — from hazard to safety function to SRS entry to design to test case — is impossible without the SRS as the central link

> **Without the SRS, architecture decisions become guesses. Every subsequent stage depends on it.**

The SRS is also the document that demonstrates to an auditor, customer, or certification body that the safety engineering process was systematic and not ad hoc. A project with a complete, well-structured SRS can defend every design decision. A project without one cannot.

---

## 3. Entry Criteria

This stage begins when **all** of the following are true:

| # | Criterion | Source |
|---|-----------|--------|
| 1 | Stage 3 Risk Assessment is complete and signed off | Stage 3 gate review record |
| 2 | Safety Function Register (preliminary) exists from Stage 3 | Risk assessment output |
| 3 | PL/SIL targets have been assigned to each safety function | Risk assessment (ISO 13849-1 risk graph, IEC 62061 risk estimation, or IEC 61511-1 LOPA/risk graph) |

**Do not begin writing the SRS until the risk assessment gate is closed.** An SRS written before the risk assessment is finalized will need to be revised when the risk assessment changes, creating version control problems and potential for the two documents to diverge.

---

## 4. Standards Requirements

| Standard | Section | SRS Requirement |
|----------|---------|-----------------|
| IEC 62061 | §5.3 | Safety function specification including required SILCL, I/O definition, demand mode, and response time |
| IEC 61511-1 | §10 | Safety requirements specification for each SIF including SIL, demand mode, PFDavg, response time, process inputs/outputs |
| ISO 13849-1 | §5 | Safety function specification including required PLr, input devices, logic controller, output devices |
| IEC 61508-1 | §7.3 | Safety requirements specification as a core deliverable of the overall safety lifecycle |

Each standard requires the SRS to be a distinct, versioned, approved document — not a set of informal notes or a section buried inside a risk assessment report.

---

## 5. Engineering Activities

### 5.1 Write One SRS Line Item Per Safety Function

For each safety function identified in Stage 3, document the following:

| Field | What to Define |
|-------|---------------|
| Safety function ID | Unique identifier (e.g., SF-01) for traceability |
| Plain-language description | What the function does, in unambiguous terms |
| Required PL (PLr) or SIL/SILCL | The integrity level determined by the risk assessment |
| Input devices | What triggers the function (e.g., light curtain, emergency stop, pressure transmitter) |
| Output devices | What the function controls or de-energises (e.g., safety relay, valve, drive) |
| Demand mode | High demand, low demand, or continuous mode (this changes the calculation method under IEC 61511) |
| Response time requirement | Maximum allowable time from input trigger to safe state — in milliseconds or seconds |
| Process parameters | Process conditions under which the function operates (pressure, temperature, flow, speed, etc.) |
| Architectural requirement | Any specified architectural constraint (e.g., "dual-channel," "Category 3," "no single fault shall prevent the safe state") |

Each line item must be complete before moving to Stage 4. Partial entries are not acceptable.

### 5.2 SRS Template

Use this table as the core SRS structure. One row per safety function. Do not merge rows or combine functions.

| SF ID | Safety Function Description | Required PLr/SIL | Input Devices | Logic Controller | Output Devices | Demand Mode | Response Time | Process Parameters | Architectural Requirement |
|-------|---------------------------|-----------------|---------------|-----------------|----------------|-------------|---------------|-------------------|--------------------------|
| SF-01 | | | | | | | | | |
| SF-02 | | | | | | | | | |

Add rows as needed. Every safety function from the Stage 3 Safety Function Register must appear in this table.

### 5.3 Verify Completeness

Before closing this stage, verify the following:

1. Every hazard in the Stage 3 risk assessment that requires a safety function has a corresponding SRS line item
2. Every SRS line item has a required PL/SIL value — no blank integrity level fields
3. Every SRS line item has defined inputs, outputs, and response time
4. Demand mode is specified for every SRS entry
5. Traceability is documented: Hazard → Safety Function → SRS entry

If any safety function from Stage 3 does not appear in the SRS, it will not be designed to the correct integrity level. If any SRS entry has blank fields, the architecture cannot be verified.

---

## 6. Key Deliverables

| # | Deliverable | Description |
|---|------------|-------------|
| 1 | SRS document | One row per safety function — required PL/SIL, inputs, outputs, response time, demand mode, process parameters, architectural requirement |
| 2 | Traceability matrix | Hazard → Safety Function → SRS row mapping, showing that every hazard requiring a safety function is covered |
| 3 | Signed approval | SRS must be reviewed and approved (signed and dated) by the responsible engineer before Stage 4 begins |

---

## 7. Exit Criteria — Gate Review

This stage is complete when **all** of the following are true:

| # | Criterion |
|---|-----------|
| 1 | Every safety function from Stage 3 has a corresponding SRS entry |
| 2 | Every SRS entry has a required PL/SIL target assigned |
| 3 | Every SRS entry has defined inputs, outputs, and response time |
| 4 | Demand mode is specified for every SRS entry |
| 5 | SRS has been reviewed and signed off by the responsible engineer |
| 6 | Traceability from hazard to SRS entry is documented |

**Stage 4 (Safety Architecture) does not begin until this gate is closed.** An architecture designed against an incomplete or unapproved SRS is not a valid safety design.

---

## 8. Common Mistakes

| Mistake | Consequence | How to Avoid |
|---------|-------------|-------------|
| Writing only a summary sentence per safety function rather than engineering-level detail | Architecture cannot be designed or verified — "detect personnel in the hazard zone" is not sufficient; you need input device type, response time, and required PLr/SIL | Use the SRS template table. If a field cannot be filled in, that is a gap that must be resolved before proceeding. |
| Omitting response time requirements | Architecture cannot be verified for timing — the system may meet the SIL but fail to respond in time | Every SRS entry must have a response time. If the customer has not defined it, derive it from the process parameters and document the assumption. |
| Omitting demand mode | Changes the calculation method entirely for IEC 61511 — high demand vs. low demand uses different metrics (PFH vs. PFDavg) | Specify demand mode for every SIF. If uncertain, consult the process description and document the basis for the classification. |
| Letting the SRS grow by copy-paste from a previous project without reviewing applicability | Requirements from a different machine or process that do not apply to the current project create false obligations or miss real ones | Start from the current project's risk assessment. Review every row before including it. Never copy without reviewing. |
| Treating the SRS as optional when a safety PLC is used ("the PLC is already rated SIL 2") | The PLC rating is a hardware property — it does not specify what the system must do, how quickly, or for which hazards | The SRS is required regardless of hardware used. The PLC rating is an input to Stage 4, not a substitute for the SRS. |

---

## 9. Relationship to Adjacent Stages

```
┌──────────────────────────────────┐
│  STAGE 3: RISK ASSESSMENT         │
│                                  │
│  Outputs used by SRS:            │
│  • Safety Function Register      │
│  • PL/SIL targets per function   │
│  • Hazard descriptions           │
│  • Process parameters            │
└─────────────────┬────────────────┘
                  │
                  │  Stage 3 provides the safety function list
                  │  and PL/SIL targets; SRS converts these into
                  │  engineering requirements
                  │
                  ▼
┌──────────────────────────────────┐
│  STAGE 3.5: SAFETY REQUIREMENTS  │  ◄── You are here
│  SPECIFICATION (SRS)             │
│                                  │
│  Outputs:                        │
│  • SRS document (one row/SF)     │
│  • Traceability matrix           │
│  • Signed approval               │
└─────────────────┬────────────────┘
                  │
                  │  SRS is the primary input to Stage 4 —
                  │  no architecture work begins until SRS
                  │  is complete and approved
                  │
                  ▼
┌──────────────────────────────────┐
│  STAGE 4: SAFETY ARCHITECTURE    │
│                                  │
│  Uses SRS as primary input:      │
│  • Required PLr/SIL per function │
│  • Inputs, outputs, logic        │
│  • Response time constraints     │
│  • Architectural requirements    │
└──────────────────────────────────┘
```

- **Stage 3 → Stage 3.5**: Risk Assessment provides the safety function list and PL/SIL targets; SRS converts these into engineering requirements with sufficient detail for design
- **Stage 3.5 → Stage 4**: Safety Architecture uses the SRS as its primary input — no architecture work begins until the SRS is complete, reviewed, and approved

---

## 10. Templates and Tools

| Tool / Template | Purpose |
|----------------|---------|
| SRS template table | Blank table structure (Section 5.2 above) for documenting each safety function — one row per function |
| SISTEMA | Used in Stage 4 for ISO 13849-1 PL calculations — requires SRS inputs (PLr, input devices, logic, output devices) for each subsystem |
| SILver / exSILentia | Used in Stage 4 for IEC 62061 / IEC 61511 SIL calculations — SRS defines the required SIL and functional parameters as inputs to these tools |
| IEC 62061 Annex E | Guidance on SRECS (Safety-Related Electrical Control System) specification — useful when structuring SRS entries for machinery applications |

*Link to your internal SRS template here.*

---

← [Stage 3: Risk Assessment]({{ '/lifecycle/risk-assessment/' | relative_url }}) | → [Stage 4: Safety Architecture]({{ '/lifecycle/safety-architecture/' | relative_url }})
