---
layout: default
title: "Standards Decision Workflow"
description: "Which standards apply to your project? Decision tree routing by machine type, market, and safety requirements."
last_reviewed: "2026-03-08"
standards_editions:
  - "NEC 2023"
  - "NFPA 79 2024"
  - "UL 508A 2022"
  - "IEC 60204-1 2018"
  - "ISO 12100 2010"
  - "ISO 13849-1 2023"
breadcrumb:
  - name: "Crosswalks"
    url: "/crosswalks/"
  - name: "Decision Workflow"
repo_path: "control-standards/rag/standards_intelligence/routing/standards_applicability.md"
related_standards:
  - name: "US Electrical Standards"
    url: "/standards/us-electrical/"
  - name: "International Machinery"
    url: "/standards/machinery/"
  - name: "Functional Safety"
    url: "/standards/functional-safety/"
---

<div class="page-header">
  <span class="page-header__label">Crosswalk — Decision Workflow</span>
  <h1>Standards Selection Decision Workflow</h1>
  <p>Use this page at the start of a project to determine which standards apply.</p>
</div>

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

## Step 1 — Identify Your Market

| Market | Required Standards |
|--------|-------------------|
| **US only** | NEC + NFPA 79 + UL 508A (if listing required) |
| **EU / CE marking** | IEC 60204-1 + ISO 12100 + ISO 13849-1 or IEC 62061 |
| **Global (US + EU)** | NFPA 79 + IEC 60204-1 + ISO 13849-1 (design to most restrictive) |
| **Process industry** | IEC 61511 + IEC 61508 (foundation) |

---

## Step 2 — Identify Machine / System Type

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

| Safety Situation | Add This Standard |
|------------------|------------------|
| Safety functions present (machine guards, E-stop) | ISO 13849-1 (PL path) or IEC 62061 (SIL path) |
| Process safety instrumented function | IEC 61511 |
| Networked / connected control system | IEC 62443 (cybersecurity) |
| Hazardous area (classified locations) | IEC 60079 family <span class="badge badge--verify">TO VERIFY</span> |
| Safety PLC software | IEC 61508-3 (via IEC 62061 or IEC 61511) |

---

## Step 4 — Confirm Coverage in This Repository

| Standard | Corpus Status |
|----------|--------------|
| NEC 2023 | Complete |
| NFPA 79 2024 | Complete |
| UL 508A 2022 | Complete |
| IEC 60204-1 2018 | Complete |
| ISO 12100 2010 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| ISO 13849-1 2023 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| IEC 62061 2021 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| IEC 61508 2010 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| IEC 61511 2016 | Planned — limited coverage <span class="badge badge--verify">TO VERIFY</span> |
| IEC 62443 | Routing reference only <span class="badge badge--verify">TO VERIFY</span> |
| IEC 60079 family | Not confirmed in corpus <span class="badge badge--gap">TO VERIFY</span> |
| SEMI S2/S8/S14 | Not in corpus <span class="badge badge--gap">NOT IN CORPUS</span> |

---

## Routing Source

This decision workflow is derived from `rag/routing/standards_applicability.md` and `rag/crosswalks/overlap_matrix/standards_decision_workflow.md`. See also `rag/standards_intelligence/_standards_map.md` for the full applicability matrix.
