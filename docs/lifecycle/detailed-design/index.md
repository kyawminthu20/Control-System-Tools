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

- **Wire sizing** — NEC Art. 310 for field conductors; UL 508A wiring and conductors rules for internal panel; IEC 60204-1 Clause 12 (international); account for temperature rating relative to heat sources (drives, starters, power supplies)
- **Motor protection** — coordinated branch design: protective device + starter + overload relay + contactor; NEC Art. 430 / UL 508A motor controllers module / IEC 60204-1 Clause 13
- **SCCR** — weakest-link method per UL 508A Supplement SB; evaluate every power-circuit component (not just the main breaker: contactors, fuse holders, power distribution blocks, SPDs are common limiting items); result must appear on the panel nameplate per NEC Art. 409.110
- **Grounding design** — three-layer approach: NEC Art. 250 baseline / NFPA 79 Ch. 8 machine bonding / UL 508A panel bonding workmanship; keep protective grounding and functional/EMC grounding separate; door bonding jumpers required
- **Spacing, creepage, and clearance** — review high-voltage power zones, mixed-voltage areas, and communication cable routing; use finger-safe components and barriers as mitigation; verify final minimums against UL 508A tables and component listing conditions (voltage-based heuristics are screening tools only)
- **Control circuit design** — control-power architecture (transformer vs direct DC supply), PLC/relay interface design, safety circuit implementation per safety architecture

## Key Deliverables

| Deliverable | Standard Reference |
|-------------|-------------------|
| Bill of Materials (BOM) | — |
| Circuit diagrams / schematics | NFPA 79 Ch. 19 / IEC 60204-1 Clause 17 |
| Wire schedule | NEC Art. 310 / UL 508A wiring and conductors |
| Panel layout drawing | UL 508A general construction / IEC 60204-1 Clause 11 |
| SCCR calculation worksheet | UL 508A Supplement SB (weakest-link method) |
| Grounding drawing | NEC Art. 250 / NFPA 79 Ch. 8 / UL 508A grounding and bonding |
| Safety function verification plan | ISO 13849-1 / IEC 62061 |

## See Also

→ [Safety Wiring Practices]({{ '/lifecycle/safety-wiring/' | relative_url }}) — 24 VDC rationale, NC contact logic, wire gauge, color coding, and dual-channel input specification

## Next Stage

→ [Draft Documentation]({{ '/lifecycle/draft-documentation/' | relative_url }})
