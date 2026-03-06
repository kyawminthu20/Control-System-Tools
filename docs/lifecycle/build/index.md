---
layout: default
title: "Lifecycle Stage 7 — Control System Build"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "7. Build"
related_standards:
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 07</span>
  <h1>Control System Build and Software Implementation</h1>
</div>

## Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **UL 508A** | Panel construction compliance during build |
| **NFPA 79** | Machine electrical construction requirements |
| **IEC 61131-3** | PLC programming languages and software structure |
| **IEC 62443** | Secure development practices if networked control system |

## Activities

**Panel build:**
- Wire per approved schematics
- Component installation per BOM
- Point-to-point wire check
- SCCR labeling
- UL field evaluation (if required but not factory listed)

**Software implementation:**
- PLC programming per IEC 61131-3 languages (Ladder, FBD, ST, IL, SFC)
- Safety PLC configuration and safety function programming
- Cybersecurity hardening per IEC 62443 if networked

## Key Deliverable

**Shop Traveler / Build Record:**
- Component verification checklist
- Wire check records
- Software version control records
- Any NCR (non-conformance reports) and dispositions

## Next Stage

→ [Installation]({{ '/lifecycle/installation/' | relative_url }})
