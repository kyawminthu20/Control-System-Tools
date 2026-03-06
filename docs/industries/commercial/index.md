---
layout: default
title: "Commercial Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Commercial"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/commercial.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Commercial</span>
  <h1>Commercial Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Commercial building, light industrial, HVAC, building automation |
| **Markets** | US primary |
| **Special concern** | Building codes, AHJ requirements, lighter safety burden than heavy industry |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC | Complete |
| Building electrical | NEC (commercial articles) | Complete |
| Machinery electrical | NFPA 79 (if machinery present) | Complete |
| Building codes | IBC, local building codes | Not in corpus |
| HVAC | ASHRAE, NFPA 90A | Not in corpus |
| Building automation | BACnet, LON | Not in corpus |

## Key Differences from Industrial

- **Lighter safety burden:** Commercial applications typically do not require PL/SIL safety function design unless specific hazards exist
- **Building codes govern:** IBC (International Building Code) and local codes take precedence; NEC is adopted within building codes
- **AHJ has broader authority:** Building departments (not just electrical inspectors) have approval authority

## When NFPA 79 Applies in Commercial

NFPA 79 applies to industrial machinery in commercial facilities (e.g., a manufacturing line in a warehouse or commercial building). It does not apply to general commercial electrical systems — those are governed by NEC commercial articles.

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/commercial.md`
