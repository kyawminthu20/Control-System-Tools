---
layout: default
title: "Scenario 02 — Global Machine (US + EU)"
description: "Standards routing for machinery sold in both US and EU markets: NFPA 79 + IEC 60204-1 + ISO 12100."
breadcrumb:
  - name: "Scenarios"
    url: "/tools/scenarios/"
  - name: "Global Machine"
repo_path: "control-standards/rag/standards_intelligence/"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
crosswalk_refs:
  - name: "NFPA 79 ↔ IEC 60204-1 Crosswalk"
    url: "/tools/crosswalks/nfpa79-iec60204/"
redirect_from:
  - /implementation/scenarios/global-machine/
  - /scenarios/global-machine/
  - /scenarios/global-machine/index.html
---

<div class="page-header">
  <span class="page-header__label">Scenario 02</span>
  <h1>Global Machine — US + EU Markets</h1>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Markets** | United States + European Union |
| **Application** | Industrial machine sold in both US and EU |
| **US requirement** | NFPA 79 + NEC + UL 508A (if panel listing required) |
| **EU requirement** | CE marking — Machinery Directive compliance |

## Starting Standards

| Standard | Market | Status |
|----------|--------|--------|
| **NFPA 79 2024** | US | Reviewed |
| **IEC 60204-1:2016+AMD1:2021** | EU / International | Reviewed |
| **ISO 12100 2010** | EU (CE marking foundation) | Planned <span class="badge badge--verify">Review pending</span> |
| **ISO 13849-1 2023** | Both (if safety functions) | Planned <span class="badge badge--verify">Review pending</span> |

## Design Strategy

**Design to the most restrictive requirement from each standard.**

Key principle: Both standards cover the same technical topics (electrical equipment of machines) but differ in some requirements. For each topic, identify which standard is more restrictive and design to that level.

```
For each topic area:
  1. Check NFPA 79 requirement
  2. Check IEC 60204-1 requirement
  3. Apply the more restrictive of the two
  4. Document compliance to both
```

## Critical Differences

| Aspect | US (NFPA 79) | EU (IEC 60204-1) | Resolution |
|--------|-------------|------------------|-----------|
| PE wire color | Green or bare | **Yellow-green required** | Use yellow-green |
| Voltage scope | 600 V max | 1000 V AC / 1500 V DC | IEC 60204-1 covers higher voltages |
| Documentation requirements | Chapter 19 | Clause 17 (more prescriptive) | Follow IEC 60204-1 Clause 17 |
| Neutral conductor | Less explicit | More explicit treatment | Follow IEC 60204-1 |

## CE Marking Foundation

**What the law requires.** EU machinery legislation requires the manufacturer to perform and
document a risk assessment, identify the applicable essential health and safety requirements
(EHSRs), implement suitable risk reduction, and complete the appropriate conformity-assessment
procedure. It does not mandate any particular standard.

**How that is normally satisfied.** Applying a harmonized standard is **voluntary**, but where
one is properly applied and cited, it confers **presumption of conformity** for the EHSRs within
its scope:

1. **EN ISO 12100** — risk assessment and risk reduction (the usual route to the required, documented risk assessment)
2. **IEC 60204-1** — electrical equipment requirements
3. **ISO 13849-1 or IEC 62061** — where safety functions exist (alternative routes, chosen on project and architecture grounds)
4. Technical file and Declaration of Conformity — required by the legislation itself

> **⚠ Machinery Regulation transition.** Machinery Directive **2006/42/EC applies through
> 19 January 2027**. Machinery Regulation **(EU) 2023/1230 applies from 20 January 2027**, when
> the Directive is repealed. Note that the Regulation as first published in the OJ said
> *14 January 2027*; a **corrigendum (OJ L 169, 4.7.2023)** changed that date to **20 January
> 2027**. Cite Article 54 as corrected. Machines placed on the EU market from that date must
> conform to the Regulation.

## Repository Paths

| Standard | Repository Path |
|----------|----------------|
| NFPA 79 | `rag/us/nfpa79/` |
| IEC 60204-1 | `rag/international/machinery/iec_60204_1/` |
| ISO 12100 | `rag/international/functional_safety/iso_12100/` [planned] |
| Crosswalk | `rag/tools/crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md` |

## Recommended Next Steps

1. [NFPA 79 ↔ IEC 60204-1 crosswalk — see the differences]({{ '/tools/crosswalks/nfpa79-iec60204/' | relative_url }})
2. [ISO 12100 — risk assessment foundation]({{ '/standards/functional-safety/iso-12100/' | relative_url }})
3. [ISO 13849-1 — if safety functions exist]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }})
