---
layout: default
title: "Nuclear Industry Standards Overlay"
breadcrumb:
  - name: "Industries"
    url: "/industries/"
  - name: "Nuclear"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/nuclear.md"
---

<div class="page-header">
  <span class="page-header__label">Industry Overlay — Nuclear</span>
  <h1>Nuclear Industry Standards</h1>
</div>

## Industry Profile

| Field | Value |
|-------|-------|
| **Industry** | Nuclear power generation and fuel processing |
| **Typical systems** | Reactor protection, plant control, radiation monitoring |
| **Markets** | US (NRC) and international (IAEA) |
| **Special concern** | Nuclear QA (10 CFR 50 Appendix B), seismic qualification, strict traceability |

## Standards Path

| Category | Standards | Corpus Status |
|----------|-----------|---------------|
| US electrical | NEC | Complete |
| International electrical | IEC 60204-1 | Complete |
| Nuclear QA | 10 CFR 50 Appendix B | Not in corpus |
| Nuclear I&C | IEEE 603, IEEE 7-4.3.2 | Not in corpus |
| IEC nuclear I&C | IEC 61513, IEC 62138 | Not in corpus |
| Safety classification | RG 1.152, IEEE 279 | Not in corpus |

## Key Overlays

**Nuclear QA requirements:**
- All safety-related systems require full documentation trail
- 10 CFR 50 Appendix B (Quality Assurance Criteria) is mandatory for US nuclear
- Vendors must be qualified under 10 CFR 50 App. B or ASME NQA-1
- **None of these are in this corpus**

**Seismic qualification:**
- Safety-related equipment must be seismically qualified
- IEEE 344 or equivalent provides the qualification methodology

**I&C standards:**
- IEEE 603 — functional requirements for safety systems
- IEC 61513 — I&C instrumentation for nuclear power plants
- These are **not in this corpus**

## Repository Path

`rag/scenario/mini_machine_safety_design_v2/industry_overlays/nuclear.md`
