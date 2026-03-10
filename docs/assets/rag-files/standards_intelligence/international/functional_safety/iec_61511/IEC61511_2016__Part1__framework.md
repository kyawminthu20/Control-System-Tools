<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61511
EDITION: 2016

HIERARCHY:
  clause: "Part 1"
  clause_title: "Framework, Definitions, System, Hardware and Application Requirements"

INDEX_TAGS:
  topics: ["functional_safety", "sis", "sif", "sil", "pfdavg", "process_safety", "safety_lifecycle", "lopa"]
  systems: ["process_industry", "oil_gas", "chemical", "power", "control_system"]
-->

# IEC 61511:2016 — Part 1 — Framework, Key Concepts, and Lifecycle Overview

## 0. Why this matters

IEC 61511 is the process industry application standard for functional safety. It applies the IEC 61508 framework specifically to Safety Instrumented Systems (SIS) in the oil and gas, chemical, petrochemical, and power industries. Most process engineers and safety engineers work with IEC 61511 rather than IEC 61508 directly — it is scoped to their domain and provides the practical tools (LOPA, PFDavg calculations, proof test guidance) they need.

In the US, ISA 84 (ANSI/ISA-84.00.01-2004/IEC 61511-1 Mod) is the US adoption of IEC 61511 and is essentially equivalent for most practical purposes.

Understanding IEC 61511 explains how process plants manage safety instrumented systems through their full lifecycle: from concept and SIL determination through design, commissioning, proof testing, and decommissioning.

## 1. Scope and application domain

IEC 61511 applies to:
- Safety instrumented systems used in the process industry
- Sensors, logic solvers, and final elements that form the SIS
- The complete SIS lifecycle from concept through decommissioning
- All process industry sectors: oil and gas, chemical, pharmaceutical, food and beverage, power generation

IEC 61511 does **not** apply to:
- Machinery safety control systems → use ISO 13849-1 or IEC 62061
- Safety PLC or safety device manufacturers certifying their products → use IEC 61508 directly
- Aviation, nuclear, or rail → sector-specific standards apply

**Key difference from machinery:** Process safety operates in **low-demand mode** — the safety function is rarely called upon. A burner management system may demand its safety function once in months or years. This means PFDavg (probability of failure on demand, average) is the metric, and proof test interval drives the PFDavg calculation. This is fundamentally different from machinery safety (IEC 62061), which uses PFHd because safety functions are demanded frequently.

## 2. Three-part structure

| Part | Title | Type |
|------|-------|------|
| Part 1 | Framework, definitions, system, hardware and application requirements | Normative |
| Part 2 | Guidelines for application of IEC 61511-1 | Informative |
| Part 3 | Guidance for determining required SIL | Informative |

Part 1 is normative. Parts 2 and 3 provide guidance and worked examples. Part 3 includes a risk graph method and LOPA guidance as alternative SIL determination approaches.

## 3. Key concepts and definitions

### Safety Instrumented System (SIS)

A system composed of sensors (input devices), logic solver, and final elements (output devices) that implements one or more Safety Instrumented Functions. A single SIS may implement multiple SIFs. The SIS is separate from the Basic Process Control System (BPCS) — they share no common cause failure mode and are independent protection layers.

**SIS components:**
- **Sensors/transmitters:** Process variable measurement (pressure, temperature, level, flow)
- **Logic solver:** Safety PLC or safety relay logic — evaluates inputs and triggers outputs
- **Final elements:** Control valves, shut-off valves, motor disconnects — takes the process to a safe state

### Safety Instrumented Function (SIF)

A single safety function implemented by the SIS with a specific SIL requirement. Each SIF has:
- A defined safe state (e.g., close valve, trip compressor)
- A SIL target derived from the hazard and risk assessment
- A specific PFDavg requirement matching that SIL
- A defined proof test interval

One SIS typically implements multiple SIFs, each with its own SIL target and PFDavg calculation.

### SIL levels in IEC 61511

IEC 61511 uses SIL 1–3 only. SIL 4 is excluded from the process industry domain.

| SIL | PFDavg (low-demand mode) | Risk reduction factor |
|-----|--------------------------|-----------------------|
| SIL 1 | ≥ 10⁻² to < 10⁻¹ | 10 to 100 |
| SIL 2 | ≥ 10⁻³ to < 10⁻² | 100 to 1,000 |
| SIL 3 | ≥ 10⁻⁴ to < 10⁻³ | 1,000 to 10,000 |

**PFDavg, not PFHd:** All IEC 61511 calculations use PFDavg. This is the metric for low-demand mode. Converting to PFHd (as used in IEC 62061) gives the wrong number and is inappropriate for process SIS.

### Basic Process Control System (BPCS)

The system that controls the normal process operation. The BPCS is **not** the SIS — it is an independent protection layer. In LOPA, the BPCS and SIS are separate layers with independent failure modes. A SIF implemented in the BPCS cannot be credited as an independent protection layer in the LOPA for the same SIF — the SIS must be separate and independent.

## 4. The IEC 61511 safety lifecycle

IEC 61511 structures the SIS lifecycle around the IEC 61508 framework. The key phases are:

| Lifecycle phase | Key activities | Key deliverables |
|-----------------|----------------|-----------------|
| **Hazard and risk assessment** | HAZOP, LOPA, or risk graph; identify hazardous events and required SIL per SIF | SIL target for each SIF |
| **Safety requirements specification (SRS)** | Define all SIF requirements, safe states, response times, proof test intervals | Safety requirements specification document |
| **SIS design** | Select logic solver, sensors, final elements; calculate PFDavg; verify architectural constraints | SIS design basis, PFDavg calculations |
| **Factory acceptance testing (FAT)** | Vendor testing of logic solver; confirm configuration | FAT records |
| **Installation and commissioning** | Physical installation; loop checks; site acceptance testing (SAT) | SAT records |
| **Safety validation** | Functional testing of all SIFs; confirm safe states are achieved | Safety validation report |
| **Operation and maintenance** | Proof testing to detect dangerous undetected failures; maintain SIS | Proof test records |
| **Modification** | Change control; re-assessment of SIL for affected SIFs; revalidation | Change records, updated SRS |
| **Decommissioning** | Remove SIS; confirm no new hazards from removal | Decommissioning records |

## 5. Relationship to IEC 61508

IEC 61511 is a sector application of IEC 61508. The differences:

| Aspect | IEC 61508 | IEC 61511 |
|--------|-----------|-----------|
| Domain | All industries | Process industry |
| Demand mode | Both high and low | Low-demand mode only |
| Metric | PFHd (high-demand) or PFDavg (low-demand) | PFDavg only |
| SIL range | SIL 1–4 | SIL 1–3 |
| SIL determination methods | Risk graph, LOPA, FTA | LOPA preferred; risk graph and FTA also permitted |
| Software | Full Part 3 software SIL | Application programming on a certified logic solver — less onerous |
| Proof testing | Both modes addressed | Central requirement; proof test interval drives PFDavg |

**Prior use clause (IEC 61511 Clause 11.5.3):** IEC 61511 allows field devices (sensors and final elements) with a documented history of successful operation to be used without the full IEC 61508 certification process. This is a significant practical relief relative to IEC 61508 — not available in the machinery sector standard IEC 62061.

## 6. Relationship to ISA 84

ISA 84 (ANSI/ISA-84.00.01-2004/IEC 61511-1 Mod) is the US national standard for SIS in the process industry. It is an adoption of IEC 61511-1 with minor modifications. For practical engineering purposes, compliance with IEC 61511 and ISA 84 is equivalent. US process plants typically reference ISA 84; global or export projects reference IEC 61511 directly.

## 7. Change log

- 2026-03-07 — Phase 3 corpus creation; Part 1 framework document established.
