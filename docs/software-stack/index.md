---
layout: default
title: "Software Stack and Cybersecurity"
description: "Routing guide for software safety standards: IEC 61131-3, IEC 62443, intrinsic safety, and related topics."
breadcrumb:
  - name: "Software Stack"
repo_path: "control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Software Stack and Cybersecurity</span>
  <h1>Software Safety, Redundancy, and Cybersecurity Routing</h1>
  <p>Source: <code>rag/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md</code></p>
</div>

## Scope Boundary

This page is a **routing guide only**. Key limits:

- `IEC 61131-3` is a PLC programming language standard. It does **not** by itself create a SIL or PL claim.
- SIL and PL claims apply to the full safety function chain: sensors, logic solver, software, final elements, diagnostics, and proof-test assumptions.
- Detailed SIL calculations, hardware fault tolerance tables, proof-test equations, and intrinsic-safety entity calculations are **not confirmed in this local corpus** — verify against published standards.

---

## Fast Routing Table

| Question | Start With | Also Add |
|----------|-----------|---------|
| Machinery safety PLC software | IEC 62061 or ISO 13849-1 | ISO 12100, IEC 60204-1, NFPA 79 |
| Process / chemical shutdown software | IEC 61511 | IEC 61508-2/-3/-6 |
| Generic safety-related software lifecycle | IEC 61508-3 | IEC 61508-2/-6 |
| PLC programming language / code structure | **IEC 61131-3** | A safety lifecycle standard if any safety claim is made |
| Secure PLC software development | **IEC 62443-4-1** | IEC 62443-4-2, IEC 62443-3-3 |
| Redundancy, voting, sensor count | IEC 61508-2/-6, IEC 61511, ISO 13849-1 | Device safety manuals |
| Cable routing and shielding | IEC 60204-1, NFPA 79, NEC, UL 508A | EMC requirements |
| Intrinsically safe loops | IEC 60079-11, IEC 60079-14, IEC 60079-25 | NEC hazardous location if US |

---

## IEC 61131-3 — PLC Programming Languages

IEC 61131-3 defines five PLC programming languages:

| Language | Abbreviation | Type | Description |
|----------|-------------|------|-------------|
| Ladder Diagram | LD | Graphical | Contact-and-coil logic; most common in US |
| Function Block Diagram | FBD | Graphical | Block interconnection; common for drives, process |
| Structured Text | ST | Text | High-level; resembles Pascal; growing adoption |
| Instruction List | IL | Text | Low-level; deprecated in 2013 edition |
| Sequential Function Chart | SFC | Graphical | State machine; batch and sequential processes |

**Key point:** IEC 61131-3 is a language standard, not a safety standard. For safety function code, pair with IEC 62061 or ISO 13849-1 (machinery) or IEC 61511 (process).

---

## IEC 62443 — Industrial Cybersecurity

IEC 62443 is a series of standards for industrial automation and control system (IACS) security:

| Standard | Scope | Corpus Status |
|----------|-------|---------------|
| IEC 62443-2-1 | Security management system | <span class="badge badge--verify">TO VERIFY</span> |
| IEC 62443-3-3 | System security requirements (SL levels) | <span class="badge badge--verify">TO VERIFY</span> |
| IEC 62443-4-1 | Secure product development lifecycle | <span class="badge badge--verify">TO VERIFY</span> |
| IEC 62443-4-2 | Component security requirements | <span class="badge badge--verify">TO VERIFY</span> |

**When IEC 62443 applies:**
- PLC or controller software is networked, remotely maintained, or productized
- System connects to factory network, historian, or external networks
- Customer security requirements reference IEC 62443

---

## Safety Route Decision

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Safety software question] --> B{Application domain?}
    B -->|Machinery| C[ISO 13849-1 or IEC 62061]
    B -->|Process industry| D[IEC 61511]
    B -->|Generic / product| E[IEC 61508-3]

    C --> F[IEC 60204-1 / NFPA 79 for electrical impl]
    D --> G[IEC 61508-2/-3 for architecture depth]
    E --> G

    A --> H{PLC language only?}
    H -->|Yes| I[IEC 61131-3]
    H -->|No - safety claim| C
</pre>
</div>

---

## Intrinsic Safety Routing

For sensors, barriers, and I/O in classified (hazardous) locations:

| Topic | Standards | Corpus Status |
|-------|-----------|---------------|
| Intrinsically safe apparatus | IEC 60079-11 | <span class="badge badge--gap">NOT CONFIRMED IN CORPUS</span> |
| Installation (IS circuits) | IEC 60079-14 | <span class="badge badge--gap">NOT CONFIRMED IN CORPUS</span> |
| Field buses in hazardous areas | IEC 60079-25 | <span class="badge badge--gap">NOT CONFIRMED IN CORPUS</span> |
| US hazardous locations | NEC Articles 500–516 | Corpus covers NEC; hazardous location articles not confirmed |

**If hazardous area I/O is required:** IEC 60079-11 / IEC 60079-14 are the starting points. These are **not confirmed in the local corpus** — verify against published IEC 60079 documents.

---

## 7-Layer Industrial Machine Architecture

<div class="mermaid-wrap">
<pre class="mermaid">
graph TD
    L1[Layer 1: Process / Machine Function] --> L2[Layer 2: Actuators and Power Conversion]
    L2 --> L3[Layer 3: Sensors and Feedback]
    L3 --> L4[Layer 4: Standard Control]
    L4 --> L5[Layer 5: Safety Control]
    L5 --> L6[Layer 6: HMI / SCADA / Logging]
    L6 --> L7[Layer 7: Site / Enterprise / Historian]

    L4 -. standards .-> S1[IEC 61131-3]
    L5 -. standards .-> S2[ISO 13849 / IEC 62061 / IEC 61511]
    L2 -. standards .-> S3[IEC 60204-1 / NFPA 79 / UL 508A]
    L6 -. standards .-> S4[IEC 62443]
</pre>
</div>

Source: `rag/reference_models/7-Layer Industrial Machine Architecture Model.md`
