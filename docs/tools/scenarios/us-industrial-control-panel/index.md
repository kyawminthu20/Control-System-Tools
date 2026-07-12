---
layout: default
title: "Scenario 01 — US Industrial Control Panel"
description: "Standards routing for a US-market industrial control panel requiring UL listing: UL 508A, NEC, NFPA 79."
breadcrumb:
  - name: "Scenarios"
    url: "/tools/scenarios/"
  - name: "US Control Panel"
repo_path: "control-standards/rag/standards_intelligence/us/"
related_standards:
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
  - name: "NEC"
    url: "/standards/us-electrical/nec/"
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
crosswalk_refs:
  - name: "UL 508A / NEC / NFPA 79 Overlap"
    url: "/tools/crosswalks/ul508a-nec-nfpa79/"
redirect_from:
  - /implementation/scenarios/us-industrial-control-panel/
  - /scenarios/us-industrial-control-panel/
  - /scenarios/us-industrial-control-panel/index.html
---

<div class="page-header">
  <span class="page-header__label">Scenario 01</span>
  <h1>US Industrial Control Panel</h1>
</div>

## Project Summary

| Field | Detail |
|-------|--------|
| **Market** | United States |
| **Application** | Standalone industrial control panel, UL listing required |
| **Machine context** | Panel is part of an industrial machine |
| **Listing requirement** | UL listing required (insurance / AHJ) |

---

## Starting Standards

| Standard | Role | Status |
|----------|------|--------|
| **UL 508A 2022** | Panel construction and UL listing | Reviewed |
| **NEC 2023** | Installation code — legally enforced | Reviewed |
| **NFPA 79 2024** | Machine electrical design (if machine context) | Reviewed |

---

## Standards Decision Logic

```
US market panel with UL listing required:
  ├── UL 508A       → panel construction, SCCR calculation, listing requirements
  ├── NEC Art. 409  → installation requirements; requires SCCR label
  ├── NEC Art. 250  → grounding and bonding (legally required)
  └── NFPA 79       → applies if panel is part of a machine
                       (NEC Art. 670 references NFPA 79)
```

---

## Key Engineering Decisions

### 1. Panel Scope and Listing Basis

- The panel is evaluated as a complete assembly — not just individually listed parts mounted in a box
- A UL-marked enclosure is **not** the same as a UL 508A listed panel; the enclosure label only addresses the enclosure
- What inspectors and AHJs verify: the listing mark, the permanent nameplate, and a marked SCCR with documented basis

### 2. Enclosure Selection and Rating Preservation

- Match the enclosure type to the actual installation environment: indoor clean, dusty, washdown, outdoor, corrosive
- All cutouts, penetrations, and fittings must preserve the intended enclosure type rating after modification
- Adding door-mounted HMIs, communication devices, or service ports without checking rating impact is a common failure
- Cooling method (vents, fans, heat exchangers) must not unintentionally defeat the enclosure type rating

### 3. Panel Layout and Construction

- Separate incoming power and high-energy distribution from low-voltage control electronics
- Group motor starters, contactors, and drives to manage heat and fault-energy exposure
- Keep PLCs, communication gear, and HMIs away from the hottest and noisiest enclosure zones
- Reserve space for wire bending, terminal access, and device replacement
- Use wire duct for organized routing; use terminal blocks for field terminations

Common UL construction failures: cramped layouts that ignore service access, unsupported conductors, relying on the enclosure label as evidence of panel listing.

### 4. Spacing, Creepage, and Clearance

- **Clearance** = shortest distance through air between conductive parts; prevents flashover
- **Creepage** = shortest distance along insulation surface; prevents surface tracking

High-priority areas: incoming disconnect, power distribution blocks, line side of contactors and starters, drive input terminals, unfinger-safe terminal areas.

Working heuristics for layout screening (verify against UL 508A tables and component listing before finalizing):

| Voltage range | Clearance | Creepage |
|---------------|-----------|----------|
| 0–150 V | ~3.2 mm (0.125 in) | ~3.2 mm (0.125 in) |
| 151–300 V | ~6.4 mm (0.25 in) | ~6.4 mm (0.25 in) |
| 301–600 V | ~12.7 mm (0.5 in) | ~12.7 mm (0.5 in) |

Mitigation options: insulating barriers, finger-safe components, organized duct routing, physical separation of voltage classes.

### 5. Wiring and Conductors

- Route conductors in wire duct; segregate power, control, and communication zones
- Terminate field wiring on terminal blocks — not loose internal splices
- Identify conductors where they enter duct or dense terminal areas
- **Communication cable rule:** `300 V` rated Ethernet/network cable is not acceptable in wiring spaces shared with `480 V` power conductors — use `600 V` rated cable or establish physical segregation
- Temperature: conductor selection must account for localized heat from drives, starters, and power supplies — not just the conductor's nominal rating

### 6. Overcurrent Protection and SCCR

**Weakest-link rule:** Panel SCCR equals the lowest-rated component in the relevant power circuit — not the interrupting rating of the main breaker.

Common limiting components that are often missed: contactors, motor starters, fuse holders, power distribution blocks, surge protective devices.

| Step | Requirement |
|------|-------------|
| Calculate | Use UL 508A Supplement SB weakest-link method |
| Verify | Every power-circuit component must be evaluated, not just the main protective device |
| Mark | NEC Article 409.110 requires SCCR permanently marked on the panel nameplate |
| Document | Retain the calculation method and basis — inspectors can ask for it |

Common errors: equating main breaker interrupting rating with panel SCCR; using a generic breaker when the SCCR basis requires a specific current-limiting fuse combination.

### 7. Grounding and Bonding

Three-layer requirement for a machine panel:

| Standard | What it covers |
|----------|---------------|
| NEC Art. 250 | Safety grounding baseline — legally required |
| NFPA 79 Ch. 8 | Machine bonding — door jumpers, PE routing through machine |
| UL 508A | Panel bonding workmanship — internal bonding paths and sizing |

Key distinction: **protective grounding** (fault clearing, personnel protection) and **functional/EMC grounding** (noise reference, shield termination) are different functions — functional grounding must not compromise the protective-earth path.

Door bonding jumpers are required — hinges and paint are not reliable bond paths.

### 8. Control Circuits and Devices

- PLCs, HMIs, switches, and indicating devices must match the control-power architecture and be placed away from high-heat and high-noise zones
- PLC outputs typically drive relays or contactors rather than switching larger loads directly — the logic-to-power transition should be traceable in the schematic
- Communication and network equipment placement should support cable routing and maintenance without compromising voltage segregation

### 9. Motor Controllers and Drives

- Motor branches are evaluated as a coordinated set: branch protective device + starter/motor-protective device + overload relay + contactor
- VFDs add heat, EMC sensitivity, and specific branch protection requirements — keep drives physically distinct from PLCs and low-voltage I/O
- Overload settings must match the motor application basis; contactors are switching devices, not overload protection
- Review with NEC Article 430 and NFPA 79 Chapter 12 when the panel is part of a machine

### 10. Transformers and Power Supplies

- Control transformers (480 V → 120 VAC): size to control load; coordinate primary and secondary protection
- DC power supplies (24 VDC direct input): verify input range; evaluate branch protection, heat, and surge exposure
- Surge protective devices protect sensitive electronics from overvoltage — they do not replace overcurrent protection
- Secondary circuit grounding must be deliberate and documented

### 11. Marking and Documentation

Required on the external nameplate:

- Manufacturer identity and unique panel identifier
- Supply ratings — voltage, phase, frequency
- Full-load or maximum current
- **SCCR** — must be marked and visible for comparison with site available fault current
- Enclosure type designation
- Grounding terminal identification

Documentation to retain: schematic and layout drawings, BOM, component instructions and listing conditions, SCCR basis and calculation.

Audit reminder: enclosure label ≠ panel listing mark ≠ external nameplate. All three are separate; all three are needed.

### 12. Emergency Stop (if machine context)

- NFPA 79 Chapter 9: E-stop behavior, stop categories (0, 1, 2), de-energization logic
- UL 508A: E-stop device construction and listing requirements
- For formal PL or SIL verification: apply [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) or [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }})

---

## Inspection Readiness Checklist

| Area | Common failure |
|------|---------------|
| Enclosure | Cutouts or fittings that defeat the intended enclosure type rating |
| Layout | Cramped build with no wire-bending or service access |
| Spacing | 480 VAC terminals without protection; open power distribution points |
| Wiring | 300 V comm cable in 480 V wiring spaces; unsupported conductors |
| Grounding | Door bonding jumpers missing; no identified PE terminal |
| SCCR | Marked value not supported by weakest downstream component |
| Nameplate | Missing or incomplete; SCCR not externally visible |
| Documentation | No retained SCCR calculation or BOM to support marked values |

---

## Repository Paths

| Standard | Repository Path |
|----------|----------------|
| UL 508A | `rag/us/ul_508a/` |
| NEC | `rag/us/nec/` |
| NFPA 79 | `rag/us/nfpa79/` |

---

## Recommended Next Steps

1. [UL 508A panel construction requirements]({{ '/standards/us-electrical/ul-508a/' | relative_url }})
2. [NEC Article 409 and 430]({{ '/standards/us-electrical/nec/' | relative_url }})
3. [NFPA 79 Chapter 9 — control circuits]({{ '/standards/us-electrical/nfpa-79/' | relative_url }})
4. [UL 508A / NEC / NFPA 79 overlap crosswalk]({{ '/tools/crosswalks/ul508a-nec-nfpa79/' | relative_url }})
5. [Wire colour coding reference gallery]({{ '/design/wiring/wire-color-coding/' | relative_url }}) — the NFPA 79 conductor identification convention this panel is wired to
6. [What a design package contains]({{ '/tools/templates/' | relative_url }}) — the full set of drawings and documents this scenario produces

---

## Assumptions and Limitations

- This scenario assumes a US-only market panel. For EU or global markets, see [Scenario 02]({{ '/tools/scenarios/global-machine/' | relative_url }}).
- Safety function design (PL/SIL) is not the primary focus of this scenario. If safety functions are required, add ISO 13849-1 and see [Scenario 04]({{ '/tools/scenarios/networked-safety-plc/' | relative_url }}).
- Content is derived from the project's reference library. Verify against current published editions of each standard.
