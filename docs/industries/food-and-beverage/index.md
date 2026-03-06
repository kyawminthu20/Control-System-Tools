---
layout: default
title: "Food and Beverage Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Food and Beverage"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/food_and_beverage.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Food and Beverage</span>
  <h1>Food and Beverage Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Food and beverage processing |
| **Typical machines** | Filling lines, conveyors, mixers, packaging, CIP systems |
| **Markets** | US and international |
| **Special concern** | Washdown environments, hygienic design, food-contact materials |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC, NFPA 79, UL 508A | Complete |
| International electrical | IEC 60204-1 | Complete |
| Risk assessment | ISO 12100 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Safety functions (guarding, E-stop) | ISO 13849-1 (PLd typical) | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Hygienic design | EHEDG, NSF, or 3-A standards | Not in corpus |
| IP ratings | IEC 60529 | Referenced; not separately covered |

## What Changes vs Standard Industrial Machine

**Washdown environments:**
- IP ratings increase — typically IP65 or IP69K for wet areas
- Stainless steel enclosures required in food-contact zones
- IEC 60204-1 / NFPA 79 enclosure requirements still apply, but IP rating selection is more critical

**Hygienic design:**
- No horizontal surfaces where water can pool
- Smooth surfaces, drainage by design
- Materials must be food-compatible (316 SS, approved plastics)
- EHEDG or NSF guidelines apply — **not covered in local corpus**

**Safety guarding:**
- Frequent machine access (sanitation/CIP) requires well-designed interlocked guards
- ISO 13849-1 PLd common for guard interlocking on high-speed machinery

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/food_and_beverage.md`

<a href="{{ '/industries/' | relative_url }}" class="card__link">&larr; Industry matrix</a>
