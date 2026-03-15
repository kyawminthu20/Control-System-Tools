---
layout: default
title: "Scenario 05 — Semiconductor Equipment Compliance"
description: "15-standard minimum compliance stack for semiconductor fab equipment. SEMI S2/S8/S14 corpus complete."
breadcrumb:
  - name: "Scenarios"
    url: "/scenarios/"
  - name: "Semiconductor Equipment"
repo_path: "control-standards/rag/standards_intelligence/reference_models/15-Standard Minimum Compliance Stack.md"
related_standards:
  - name: "ISO 12100"
    url: "/standards/functional-safety/iso-12100/"
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
  - name: "SEMI S2/S8/S14"
    url: "/standards/semiconductor/semi/"
  - name: "IEC 60079"
    url: "/standards/hazardous-area/iec-60079/"
industries:
  - name: "Semiconductor"
    slug: "semiconductor/"
---

<div class="page-header">
  <span class="page-header__label">Scenario 05</span>
  <h1>Semiconductor Equipment Compliance</h1>
  <span class="badge badge--complete">SEMI S2/S8/S14 — Phase 10 Complete</span>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Application** | Semiconductor fab equipment (process tool, metrology, handler) |
| **Markets** | US fabs + EU fabs + Asian fabs (global) |
| **Standards approach** | 15-Standard Minimum Compliance Stack |
| **Unique requirement** | SEMI standards (S2, S8, S14) — [corpus complete](/standards/semiconductor/semi/) |

## The 15-Standard Compliance Stack

Source: `rag/reference_models/15-Standard Minimum Compliance Stack.md`

### Domain 1 — Core Machinery Safety

| # | Standard | Purpose | Corpus Status |
|---|----------|---------|---------------|
| 1 | ISO 12100 | Risk assessment foundation | Planned <span class="badge badge--verify">TO VERIFY</span> |
| 2 | ISO 13849-1 | Performance Level safety design | Planned <span class="badge badge--verify">TO VERIFY</span> |
| 3 | ISO 13850 | Emergency stop requirements | Not separately covered |
| 4 | IEC 60204-1 | Electrical machine design | Complete |

### Domain 2 — US Electrical Compliance

| # | Standard | Purpose | Corpus Status |
|---|----------|---------|---------------|
| 5 | NFPA 79 | US machine electrical | Complete |
| 6 | NEC (NFPA 70) | US installation code | Complete |
| 7 | UL 508A | US control panel listing | Complete |

### Domain 3 — Functional Safety

| # | Standard | Purpose | Corpus Status |
|---|----------|---------|---------------|
| 8 | IEC 62061 | SIL-based machinery safety | Planned <span class="badge badge--verify">TO VERIFY</span> |
| 9 | IEC 61508 | Foundation standard | Planned <span class="badge badge--verify">TO VERIFY</span> |

### Domain 4 — Hazardous Materials and Gas Systems

**These standards are unique to semiconductor fabs.**

| # | Standard | Purpose | Corpus Status |
|---|----------|---------|---------------|
| 10 | SEMI S2 | Semiconductor equipment safety | <span class="badge badge--complete">Complete</span> |
| 11 | SEMI S8 | Operator safety | <span class="badge badge--complete">Complete</span> |
| 12 | SEMI S14 | Fire hazards in tools | <span class="badge badge--complete">Complete</span> |
| — | NFPA 318 | Fab safety requirements | Not confirmed in corpus |

### Domain 5 — Cybersecurity

| # | Standard | Purpose | Corpus Status |
|---|----------|---------|---------------|
| 13 | IEC 62443 | Industrial automation security | Routing reference <span class="badge badge--verify">TO VERIFY</span> |
| 14 | NIST SP 800-82 | US ICS security guidance | Not in corpus |

---

## Safety Level Target

Typical semiconductor equipment safety target:

```
PLd or PLe  (per ISO 13849-1)
```

The high safety level is driven by:
- Hazardous process gases (toxic, flammable, pyrophoric)
- High-voltage power supplies
- Robotic handling
- Confined spaces for maintenance

---

## Repository Path

```
rag/reference_models/15-Standard Minimum Compliance Stack.md
rag/scenario/mini_machine_safety_design_v2/industry_overlays/semiconductor.md
```

<a href="{{ '/industries/semiconductor/' | relative_url }}" class="card__link">View Semiconductor industry overlay &rarr;</a>

## Related References

- [7-Layer Machine Architecture Model]({{ '/reference/architecture/machine-architecture-model/' | relative_url }}) — layer-by-layer breakdown with applicable standards per layer
