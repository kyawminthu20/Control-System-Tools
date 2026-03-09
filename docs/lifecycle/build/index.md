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

**Panel build (UL 508A):**

*Layout and construction:*
- Install components per approved layout — separate power and control areas, drive/starter heat zones from PLCs and communication gear
- Mount all components on rigid backpanel, DIN rail, or frame per component instructions (orientation, ventilation clearance, accessory combinations)
- Install wire duct or equivalent routing support before pulling conductors

*Wiring and conductors:*
- Wire per approved schematics — use correct conductor type, voltage rating, and temperature rating
- Terminate field wiring on terminal blocks, not loose internal splices
- Verify communication/Ethernet cable voltage rating matches wiring environment (300 V vs 600 V as required by segregation)
- Identify conductors where they enter wire duct, bundles, or dense terminal areas

*Grounding and bonding:*
- Install bonding jumpers on door assemblies — hinges and paint are not reliable bond paths
- Verify bond continuity to removable subpanels and mounting plates
- Confirm protective-earth path is sized and routed for fault-clearing duty, not just for noise management

*Enclosure integrity:*
- Verify all cutouts, penetrations, and fittings preserve the intended enclosure type rating
- Confirm cooling method (vents, fans, heat exchangers) does not defeat the enclosure rating

*SCCR and marking:*
- Verify SCCR basis — identify the weakest-rated power-circuit component (contactors, fuse holders, power distribution blocks, SPDs are common limiting items, not just the main breaker)
- Apply permanent external nameplate: manufacturer, panel ID, supply ratings, FLA/MCA, SCCR, enclosure type, grounding terminal identification
- Apply SCCR label where visible externally for installer/inspector comparison with site available fault current
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
