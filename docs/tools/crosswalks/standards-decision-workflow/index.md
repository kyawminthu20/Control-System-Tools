---
layout: default
title: "Standards Decision Workflow"
description: "Which standards apply to your project? Decision tree routing by machine type, market, and safety requirements."
last_reviewed: "2026-03-08"
standards_editions:
  - "NEC 2023"
  - "NFPA 79 2024"
  - "UL 508A 2022"
  - "IEC 60204-1:2016+AMD1:2021"
  - "ISO 12100 2010"
  - "ISO 13849-1 2023"
breadcrumb:
  - name: "Crosswalks"
    url: "/tools/crosswalks/"
  - name: "Decision Workflow"
repo_path: "control-standards/rag/standards_intelligence/routing/standards_applicability.md"
related_standards:
  - name: "US Electrical Standards"
    url: "/standards/us-electrical/"
  - name: "International Machinery"
    url: "/standards/machinery/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
redirect_from:
  - /crosswalks/standards-decision-workflow/
  - /crosswalks/standards-decision-workflow/index.html
---

<div class="page-header">
  <span class="page-header__label">Crosswalk — Decision Workflow</span>
  <h1>Standards Selection Decision Workflow</h1>
  <p>Use this page at the start of a project to determine which standards apply.</p>
</div>

## Purpose

This workflow helps engineers determine **which standards apply at each stage of industrial machine design and installation**, with a primary focus on US requirements and guidance for EU/CE and international standards (IEC 60204-1, ISO 12100, ISO 13849-1).

**Intended for:**
- Control engineers
- Machine builders
- Panel designers
- System integrators

**Standards covered:**

| Standard | Role |
|----------|------|
| ISO 12100 | Risk assessment methodology |
| ISO 13849-1 / IEC 62061 | Functional safety architecture |
| NFPA 79 | Machine electrical design |
| UL 508A | Control panel construction |
| NEC | Electrical installation in buildings |

> **Scope note:** This workflow covers US-market industrial machines. EU/CE requirements add IEC 60204-1 and the Machinery Directive. Process safety systems follow IEC 61511 instead of ISO 13849.

---

## Quick Decision Tree

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Start: Define System] --> B{Primary risk context?}
    B -->|Machine motion / access / entrapment| C[Machinery route]
    B -->|Process containment / pressure / chemical shutdown| D[Process route]

    C --> E[ISO 12100 risk assessment]
    E --> F{Safety framework?}
    F -->|PL route| G[ISO 13849-1]
    F -->|Machinery SIL route| H[IEC 62061]
    G --> I[IEC 60204-1 / NFPA 79 / UL 508A]
    H --> I

    D --> J[IEC 61511]
    J --> K[IEC 61508 lifecycle foundation]
    K --> L[IEC 60079 if hazardous area]
    L --> M[NEC / local electrical code]
</pre>
</div>

---

## Lifecycle Workflow

The diagram below shows the **sequence** standards apply across a machine's design and installation lifecycle.

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Machine Concept] --> B[Risk Assessment<br/>ISO 12100]
    B --> C[Safety Function Requirements]
    C --> D{Safety framework?}
    D -->|PL route| E[ISO 13849-1]
    D -->|SIL route| F[IEC 62061]
    E --> G[Machine Electrical Design<br/>NFPA 79]
    F --> G
    G --> H[Control Panel Construction<br/>UL 508A]
    H --> I[Electrical Installation<br/>NEC]
    I --> J[Inspection & Approval<br/>AHJ]
</pre>
</div>

---

## Step 1 — Identify Your Market

**Key question:** What markets will this machine be sold or installed in?

**Outputs:**
- Required standard set
- Whether CE marking applies

| Market | Required Standards |
|--------|-------------------|
| **US only** | NEC + NFPA 79 + UL 508A (if listing required) |
| **EU / CE marking** | IEC 60204-1 + ISO 12100 + ISO 13849-1 or IEC 62061 |
| **Global (US + EU)** | NFPA 79 + IEC 60204-1 + ISO 13849-1 (design to most restrictive) |
| **Process industry** | IEC 61511 + IEC 61508 (foundation) |

---

## Step 2 — Identify Machine / System Type

**Key question:** What is the machine or system doing, and what is its risk context?

**Outputs:**
- Core applicable standards
- Whether functional safety standards apply

| System Type | Core Standards | Notes |
|-------------|---------------|-------|
| Standalone control panel (US, UL listing) | UL 508A + NEC Art. 409 | NFPA 79 if machine context |
| Industrial machinery (US) | NFPA 79 + NEC Art. 670 + UL 508A | E-stop, guarding apply |
| Industrial machinery (EU / CE) | IEC 60204-1 + ISO 12100 + ISO 13849-1 | Risk assessment first |
| Industrial machinery (global) | NFPA 79 + IEC 60204-1 + ISO 13849-1 | Most restrictive from each |
| Conveyor / material handling | NFPA 79 / IEC 60204-1 | ISO 13849-1 if guarding |
| Robotic cell | NFPA 79 / IEC 60204-1 | ISO 13849-1 PLd or PLe common |
| Process control skid | NEC + IEC 60204-1 | IEC 61511 if SIS present |
| Process SIS / ESD | IEC 61511 + IEC 61508 | SIL determination via LOPA |

---

## Step 3 — Identify Safety Requirements

**Key question:** Does this system perform safety functions, and in what environment?

**Outputs:**
- Additional standards required
- Safety integrity target (PL or SIL)

| Safety Situation | Add This Standard |
|------------------|------------------|
| Safety functions present (machine guards, E-stop) | ISO 13849-1 (PL path) or IEC 62061 (SIL path) |
| Process safety instrumented function | IEC 61511 |
| Networked / connected control system | IEC 62443 (cybersecurity) |
| Hazardous area (classified locations) | IEC 60079 family <span class="badge badge--reviewed">Reviewed</span> |
| Safety PLC software | IEC 61508-3 (via IEC 62061 or IEC 61511) |

---

## Standard Scope Boundaries

Many engineers confuse these three overlapping standards. The table below clarifies where each one applies.

| Standard | Governs | Applies To |
|----------|---------|------------|
| **NFPA 79** | Electrical design of the machine itself | Machine wiring, enclosures, control devices |
| **UL 508A** | Construction of industrial control panels | Panel shop fabrication, listing |
| **NEC** | Electrical installation in buildings | Facility wiring from the panel to the machine |

> **Key boundary:** NFPA 79 stops at the machine connection point. NEC governs everything from the building supply to that point. UL 508A governs how the panel is built, not where it connects.

---

## Step 4 — Confirm Coverage in This Repository

| Standard | Corpus Status |
|----------|--------------|
| NEC (NFPA 70) | <span class="badge badge--pending">Review pending</span> |
| NFPA 79 2024 | <span class="badge badge--pending">Review pending</span> |
| UL 508A (Ed. 3) | <span class="badge badge--pending">Review pending</span> |
| IEC 60204-1:2016+AMD1:2021 | <span class="badge badge--pending">Review pending</span> |
| ISO 12100 2010 | <span class="badge badge--pending">Review pending</span> |
| ISO 13849-1 2023 | <span class="badge badge--pending">Review pending</span> |
| IEC 62061 2021 | <span class="badge badge--revalidate">Needs revalidation</span> |
| IEC 61508 2010 | <span class="badge badge--reviewed">Reviewed</span> |
| IEC 61511 2016 | <span class="badge badge--reviewed">Reviewed</span> |
| IEC 62443 | Routing reference only <span class="badge badge--verify">Review pending</span> |
| IEC 60079 family | <span class="badge badge--reviewed">Reviewed</span> |
| SEMI S2/S8/S14 | <span class="badge badge--reviewed">Reviewed</span> |

---

## Common Engineering Mistakes

1. **Designing safety circuits before risk assessment** — the required Performance Level (PLr) comes from ISO 12100 risk assessment; skipping this step produces safety circuits with no verified integrity basis.
2. **Assuming NEC defines machine electrical design** — NEC governs facility installation; NFPA 79 governs the machine. Using NEC rules inside a machine is a compliance error.
3. **Ignoring SCCR when selecting components** — Short Circuit Current Rating must be coordinated across all panel components. Mismatches cause failures at listing.
4. **Installing panels without verifying available fault current** — UL 508A SCCR must meet or exceed the available fault current at the installation point (NEC 110.10).
5. **Mixing NFPA 79 and UL 508A requirements incorrectly** — NFPA 79 governs machine-mounted enclosures; UL 508A governs separately mounted control panels. Requirements differ.
6. **Skipping AHJ coordination** — The Authority Having Jurisdiction has final approval authority. Engage early on non-standard installations.

---

## Typical Machine Compliance Stack

For a standard US industrial machine with safety functions, the full compliance stack is:

| Layer | Standard | Edition |
|-------|----------|---------|
| Risk assessment | ISO 12100 | 2010 |
| Functional safety architecture | ISO 13849-1 or IEC 62061 | 2023 / 2021 |
| Machine electrical design | NFPA 79 | 2024 |
| Control panel construction | UL 508A | 2022 |
| Facility electrical installation | NEC | 2023 |
| Final inspection | AHJ jurisdiction | — |

> For EU/CE markets, add **IEC 60204-1 (2016+AMD1:2021)** alongside NFPA 79 and design to the more restrictive requirement at each point.

---

## Worked Example — Automated Conveyor System

The following traces a US-market conveyor through the full workflow.

**System:** Belt conveyor with automated loading, pinch points at drive and tail sections, maintenance access door.

| Step | Action | Standard Applied |
|------|--------|-----------------|
| 1 | US market, no CE marking required | NEC + NFPA 79 + UL 508A |
| 2 | Industrial machinery with guarding | NFPA 79 + NEC Art. 670 + UL 508A |
| 3 | Risk assessment identifies pinch hazard at access door | ISO 12100 |
| 4 | Safety function required: guard door interlock (Category 3, PLd) | ISO 13849-1 |
| 5 | Machine wiring designed to NFPA 79 | NFPA 79 2024 |
| 6 | Control panel built and listed to UL 508A | UL 508A 2022 |
| 7 | Machine installed per NEC, SCCR verified against available fault current | NEC 2023 |
| 8 | AHJ inspection completed, permit issued | AHJ |

**Key decisions made:**
- ISO 13849-1 chosen over IEC 62061 (single machine, PL route simpler)
- PLd required (ISO 12100 risk graph: severe injury possible, frequent access, avoidance difficult)
- Category 3 dual-channel interlock with cross-monitoring

---

## Routing Source

This decision workflow is derived from `rag/routing/standards_applicability.md` and `rag/tools/crosswalks/overlap_matrix/standards_decision_workflow.md`. See also `rag/standards_intelligence/_standards_map.md` for the full applicability matrix.
