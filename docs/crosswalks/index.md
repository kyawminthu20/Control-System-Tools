---
layout: default
title: "Crosswalks and Standards Overlap"
description: "Side-by-side comparison tables: NFPA 79 ↔ IEC 60204-1, UL 508A / NEC / NFPA 79, and decision workflow."
breadcrumb:
  - name: "Crosswalks"
repo_path: "control-standards/rag/standards_intelligence/crosswalks/overlap_matrix/"
---

<div class="page-header">
  <span class="page-header__label">Crosswalks</span>
  <h1>Standards Crosswalks and Overlap Tables</h1>
  <p>Side-by-side requirement mappings between related standards. Use when designing for multiple markets or resolving conflicts between standards.</p>
</div>

## Available Crosswalks

| Crosswalk | Standards | Use When |
|-----------|-----------|---------|
| [NFPA 79 ↔ IEC 60204-1]({{ '/crosswalks/nfpa79-iec60204/' | relative_url }}) | NFPA 79:2024, IEC 60204-1:2018 | Machine sold in US + EU markets |
| [UL 508A / NEC / NFPA 79]({{ '/crosswalks/ul508a-nec-nfpa79/' | relative_url }}) | UL 508A:2022, NEC 2023, NFPA 79:2024 | US panel design with all three standards |
| [Standards Decision Workflow]({{ '/crosswalks/standards-decision-workflow/' | relative_url }}) | All major standards | Selecting which standards apply to your project |
| [Standards Comparison Tool]({{ '/crosswalks/compare/' | relative_url }}) | All 9 standards | Select any two standards to view their overlap matrix |

## When to Use Crosswalks

**NFPA 79 ↔ IEC 60204-1:** Use when designing for both US and EU markets. Both standards cover the same technical scope but differ in structure, wiring color conventions, and some specific requirements. Design to the most restrictive from each.

**UL 508A / NEC / NFPA 79:** Use when building a US industrial control panel. All three interact — understanding which standard "owns" each topic prevents conflicts and gaps.

**Decision Workflow:** Use at the beginning of a project when you need to determine which standards apply based on machine type, market, and safety requirements.

---

## Source Files

All crosswalk content is ported from:
- `rag/crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md`
- `rag/crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md`
- `rag/crosswalks/overlap_matrix/standards_decision_workflow.md`
