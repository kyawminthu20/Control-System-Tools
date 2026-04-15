---
layout: default
title: "Scenario 03 — Process Skid Shutdown System"
description: "Standards routing for a process skid with SIS/ESD: IEC 61511 + IEC 61508, with hazardous-area routing to IEC 60079 when needed."
breadcrumb:
  - name: "Scenarios"
    url: "/implementation/scenarios/"
  - name: "Process Skid"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
redirect_from:
  - /scenarios/process-skid/
  - /scenarios/process-skid/index.html
---

<div class="page-header">
  <span class="page-header__label">Scenario 03</span>
  <h1>Process Skid Shutdown System</h1>
  <span class="badge badge--complete">Corpus Complete</span>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Application** | Process skid with SIS / ESD (Emergency Shutdown) system |
| **Industry** | Process industry — oil and gas, chemicals, or similar |
| **Safety standard** | IEC 61511 (application) + IEC 61508 (foundation) |
| **Corpus coverage** | IEC 61511 and IEC 61508 functional-safety pages are present; IEC 60079 coverage is available for hazardous-area routing |

**Important note:** The local RAG corpus covers the IEC 61511 routing and lifecycle basics needed to place a process skid on the correct standards path. Project SIL calculations, proof-test intervals, and hazardous-area design details still need direct engineering verification against the published standards and the plant basis of design.

## Starting Standards

| Standard | Role | Status |
|----------|------|--------|
| **IEC 61511 2016** | SIS application standard for process industry | <span class="badge badge--complete">Complete</span> |
| **IEC 61508 2010** | Foundation safety lifecycle standard | <span class="badge badge--complete">Complete</span> |
| **NEC / local code** | Electrical installation | Complete for US |
| **IEC 60204-1** | Machine electrical (if machine elements present) | Complete |

## Standards Decision Logic

```
Process skid with shutdown system:
  ├── IEC 61511   → SIS application standard (HAZOP → LOPA → SIL → SIF design)
  ├── IEC 61508   → Foundation lifecycle (referenced by IEC 61511)
  ├── IEC 60079   → If hazardous area (classified location)
  └── NEC hazardous location articles → US installation
```

## SIS Lifecycle Overview

Per IEC 61511, the SIS lifecycle includes:

1. Hazard and risk analysis (HAZOP)
2. Safety requirements specification
3. SIL determination (LOPA or risk graph)
4. Safety system design (SIF allocation)
5. Installation and commissioning
6. Operation and maintenance (proof testing)
7. Decommissioning

## Key Concepts

**SIF (Safety Instrumented Function):** A safety function implemented by the SIS. One SIS may have multiple SIFs, each with its own SIL target and proof test interval.

**PFDavg (Average Probability of Failure on Demand):** The key reliability metric for SIS/SIF. SIL target determines the required PFDavg range.

**LOPA (Layer of Protection Analysis):** Most common SIL determination method in process industry. Credits independent protection layers (IPLs) against the demand rate to determine required SIL.

## Repository Paths

| Standard | Repository Path |
|----------|----------------|
| IEC 61511 | `rag/international/functional_safety/iec_61511/` |
| IEC 60079 | `rag/international/hazardous_area/iec_60079/` |
| Scenario reference | `rag/scenario/mini_machine_safety_design/` |

## Limitations

- For SIL calculations, proof test intervals, and plant-specific SRS requirements, consult the published IEC 61511 standard and project procedures
- For classified locations, use the IEC 60079 family plus the applicable NEC hazardous-location articles and AHJ requirements
- This scenario does not cover API 670 (machinery protection) or other process-specific standards

<a href="{{ '/industries/petroleum/' | relative_url }}" class="card__link">See Petroleum / Oil &amp; Gas industry overlay &rarr;</a>
