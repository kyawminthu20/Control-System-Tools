---
layout: default
title: "Lifecycle Stage 5 — Detailed Design and Part Sizing"
breadcrumb:
  - name: "Lifecycle"
    url: "/lifecycle/"
  - name: "5. Detailed Design"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
---

<div class="page-header">
  <span class="page-header__label">Lifecycle Stage 05</span>
  <h1>Detailed Design and Part Sizing</h1>
</div>

## Standards Influence

| Standard | Role at This Stage |
|----------|-------------------|
| **NFPA 79** | Wire sizing, circuit design, panel layout (US) |
| **IEC 60204-1** | Electrical design requirements (international) |
| **UL 508A** | Panel construction requirements, SCCR calculation |
| **NEC** | Wire sizing, grounding, motor protection calculations |

## Key Activities

- **Wire sizing** — per NEC Article 310 / UL 508A Section 5 / IEC 60204-1 Clause 12
- **Motor protection** — overcurrent protection, overload relay sizing (NEC 430 / IEC 60204-1 Clause 13)
- **Short-circuit current rating (SCCR)** — panel SCCR calculation per UL 508A Section SB
- **Grounding design** — per NEC 250 / NFPA 79 Ch 8 / IEC 60204-1 Clause 8
- **Panel layout** — clearance, creepage, component spacing
- **Control circuit design** — safety circuit implementation per safety architecture

## Key Deliverables

| Deliverable | Standard Reference |
|-------------|-------------------|
| Bill of Materials (BOM) | — |
| Circuit diagrams / schematics | NFPA 79 Ch 19 / IEC 60204-1 Clause 17 |
| Wire schedule | NEC 310 / UL 508A Sec. 5 |
| Panel layout drawing | UL 508A / IEC 60204-1 Clause 11 |
| SCCR calculation worksheet | UL 508A Section SB |
| Grounding drawing | NEC 250 / NFPA 79 Ch 8 |
| Safety function verification plan | ISO 13849-1 / IEC 62061 |

## Next Stage

→ [Draft Documentation]({{ '/lifecycle/draft-documentation/' | relative_url }})
