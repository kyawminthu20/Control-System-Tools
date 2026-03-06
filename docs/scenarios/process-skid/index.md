---
layout: default
title: "Scenario 03 — Process Skid Shutdown System"
description: "Standards routing for a process skid with SIS/ESD: IEC 61511 + IEC 61508. Limited local corpus coverage."
breadcrumb:
  - name: "Scenarios"
    url: "/scenarios/"
  - name: "Process Skid"
repo_path: "control-standards/rag/standards_intelligence/international/functional_safety/"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
  - name: "IEC 61508"
    url: "/standards/functional-safety/iec-61508/"
---

<div class="page-header">
  <span class="page-header__label">Scenario 03</span>
  <h1>Process Skid Shutdown System</h1>
  <span class="badge badge--verify">LIMITED LOCAL COVERAGE — TO VERIFY</span>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Application** | Process skid with SIS / ESD (Emergency Shutdown) system |
| **Industry** | Process industry — oil and gas, chemicals, or similar |
| **Safety standard** | IEC 61511 (application) + IEC 61508 (foundation) |
| **Corpus coverage** | Limited — IEC 61511 details planned but not confirmed complete |

**Important note:** The local RAG corpus has **limited IEC 61511 coverage**. Content on this page provides routing and framework information only. For detailed SIL calculation and SIS lifecycle design, verify against the published IEC 61511 standard.

## Starting Standards

| Standard | Role | Status |
|----------|------|--------|
| **IEC 61511 2016** | SIS application standard for process industry | Planned — limited <span class="badge badge--verify">TO VERIFY</span> |
| **IEC 61508 2010** | Foundation safety lifecycle standard | Planned <span class="badge badge--verify">TO VERIFY</span> |
| **NEC / local code** | Electrical installation | Complete for US |
| **IEC 60204-1** | Machine electrical (if machine elements present) | Complete |

## Standards Decision Logic

```
Process skid with shutdown system:
  ├── IEC 61511   → SIS application standard (HAZOP → LOPA → SIL → SIF design)
  ├── IEC 61508   → Foundation lifecycle (referenced by IEC 61511)
  ├── IEC 60079   → If hazardous area (classified location) [NOT IN CORPUS]
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
| IEC 61511 | `rag/international/functional_safety/iec_61511/` [planned] |
| Scenario reference | `rag/scenario/mini_machine_safety_design/` |

## Limitations

- IEC 61511 detail pages are **not confirmed complete** in this corpus
- IEC 60079 (hazardous area) is **not in this corpus**
- For SIL calculations and proof test intervals, consult the published IEC 61511 standard
- This scenario does not cover API 670 (machinery protection) or other process-specific standards

<a href="{{ '/industries/petroleum/' | relative_url }}" class="card__link">See Petroleum / Oil &amp; Gas industry overlay &rarr;</a>
