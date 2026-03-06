---
layout: default
title: "Petroleum / Oil and Gas Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Petroleum"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/petroleum.md"
related_standards:
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Petroleum / Oil and Gas</span>
  <h1>Petroleum and Oil and Gas Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Petroleum, oil and gas upstream/midstream/downstream |
| **Typical systems** | ESD, F&amp;G, HIPPS, wellhead control, pipeline control |
| **Markets** | US, international |
| **Special concern** | Hazardous areas (Ex), SIS/ESD, process safety |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC, NFPA 79 | Complete |
| International electrical | IEC 60204-1 | Complete |
| Process safety (SIS) | IEC 61511 | Planned — limited <span class="badge badge--verify">TO VERIFY</span> |
| SIS foundation | IEC 61508 | Planned <span class="badge badge--verify">TO VERIFY</span> |
| Hazardous area (Ex) | IEC 60079 family | <span class="badge badge--gap">NOT CONFIRMED IN CORPUS</span> |
| API standards | API 14C, API 670 | Not in corpus |

## Hazardous Area Classification

A key requirement for oil and gas that is **not fully covered in this corpus:**

**US classification (NEC):**
- Class I, Division 1 / Division 2 (flammable gases and vapors)
- Zone 0, 1, 2 (NEC Article 505)

**International (IEC 60079):**
- Zone 0 / 1 / 2 classification
- Equipment categories (1G, 2G, 3G)

IEC 60079 detail pages are **not confirmed in this corpus** — verify against published IEC 60079 documents.

## Process Safety / SIS

Oil and gas process safety uses IEC 61511:
- HAZOP for hazard identification
- LOPA for SIL determination
- SIF design and proof test procedures
- Emergency shutdown (ESD) and fire and gas (F&G) systems

IEC 61511 coverage in this corpus is **limited** — see [IEC 61511 page]({{ '/standards/functional-safety/iec-61511/' | relative_url }}).

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/petroleum.md`
