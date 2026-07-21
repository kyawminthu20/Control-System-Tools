---
layout: default
title: "Industry Matrix"
description: "Standards matrix for 9 confirmed industry overlays: semiconductor, food and beverage, energy, petroleum, marine, medical, nuclear, offshore, commercial."
breadcrumb:
  - name: "Industries"
repo_path: "control-standards/rag/standards_intelligence/scenario/mini_machine_safety_design_v2/industry_overlays/"
review:
  standard: "Multiple — industry overlay matrix"
  edition: "exact governing revisions not yet recorded — verify on the linked standards pages"
  status: "Review pending"
  coverage: "Overlay matrix routing 9 industries to their standards stacks; overview level, not a compliance determination."
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Industry Matrix</span>
  <h1>Industry Standards Matrix</h1>
  <p>9 confirmed industry overlays showing which standards apply per sector. Source: <code>rag/scenario/mini_machine_safety_design_v2/industry_overlays/</code></p>
</div>

## Matrix Overview

| Industry | US Standards Path | International Path | Safety Method | Special Overlays |
|----------|------------------|--------------------|---------------|-----------------|
| [Semiconductor]({{ '/industries/semiconductor/' | relative_url }}) | NEC, NFPA 79, UL 508A | IEC 60204-1, ISO 13849-1 | PL or SIL | SEMI S2/S8/S14 <span class="badge badge--reviewed">Reviewed</span> |
| [Food &amp; Beverage]({{ '/industries/food-and-beverage/' | relative_url }}) | NEC, NFPA 79, UL 508A | IEC 60204-1 | PL | Washdown, hygienic design |
| [Energy]({{ '/industries/energy/' | relative_url }}) | NEC, NFPA 79 | IEC 60204-1, IEC 62443 | SIL | Outdoor, process safety, cybersecurity |
| [Petroleum / Oil &amp; Gas]({{ '/industries/petroleum/' | relative_url }}) | NEC, NFPA 79 | IEC 61511, IEC 60079 | SIL | Hazardous area <span class="badge badge--reviewed">Reviewed</span> |
| [Marine]({{ '/industries/marine/' | relative_url }}) | NEC | IEC 60204-1 | PL / SIL | Marine class rules |
| [Medical]({{ '/industries/medical/' | relative_url }}) | NEC, FDA regs | IEC 60204-1, IEC 62304 | SIL | FDA, software lifecycle |
| [Nuclear]({{ '/industries/nuclear/' | relative_url }}) | NEC, IEEE | IEC 60204-1 | SIL | Nuclear QA |
| [Offshore]({{ '/industries/offshore/' | relative_url }}) | NEC | IEC 60204-1, IEC 61511 | SIL | Offshore electrical, corrosion |
| [Commercial]({{ '/industries/commercial/' | relative_url }}) | NEC, building codes | IEC 60204-1 | — | Building codes, lighter industrial |
