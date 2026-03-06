---
layout: default
title: "Medical Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Medical"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/medical.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Medical</span>
  <h1>Medical Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Medical devices and medical equipment |
| **Typical systems** | Diagnostic equipment, treatment devices, medical manufacturing |
| **Markets** | US (FDA) and EU (MDR) |
| **Special concern** | FDA regulation, IEC 62304 software lifecycle, patient safety |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC | Complete |
| International electrical | IEC 60204-1 | Complete |
| Medical electrical safety | IEC 60601 series | Not in corpus |
| Software lifecycle | IEC 62304 | Not in corpus |
| Risk management | ISO 14971 | Not in corpus |
| US regulatory | FDA 21 CFR Part 820 | Not in corpus |
| EU regulatory | EU MDR 2017/745 | Not in corpus |

## Key Overlays

**FDA and regulatory:**
- Medical devices in the US require FDA clearance/approval
- Quality Management System per ISO 13485 / FDA QSR
- **These requirements are NOT in this corpus** — IEC 60204-1 and NEC provide the electrical baseline only

**IEC 62304 — Medical Device Software:**
- Software safety classification (Class A, B, C)
- Software lifecycle requirements
- Not in this corpus

**IEC 60601 — Medical Electrical Equipment:**
- Electrical safety and EMC requirements specific to medical equipment
- Stricter than IEC 60204-1 for patient-connected equipment
- Not in this corpus

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/medical.md`
