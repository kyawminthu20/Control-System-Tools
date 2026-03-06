<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MATRIX_ID: UL508A_NEC_NFPA79_OVERLAP
STANDARDS: UL_508A_2022, NEC_2023, NFPA_79_2024
JURISDICTION: US
-->

# UL 508A ↔ NEC (NFPA 70) ↔ NFPA 79 Overlap Matrix

## Purpose

This matrix maps overlapping requirements across three US standards for industrial control systems:
- **NEC (NFPA 70)**: National Electrical Code - legally enforced installation code
- **NFPA 79**: Electrical Standard for Industrial Machinery
- **UL 508A**: Industrial Control Panels - listing and construction standard

## Legend

- **NEC**: Article-based, legally adopted by most US jurisdictions
- **NFPA 79**: Chapter-based, machinery electrical design standard
- **UL 508A**: Section-based, panel construction and testing standard
- **Primary Owner**: Which standard typically leads the engineering decision

## Topic-Based Overlap Matrix

| Topic Area | NEC Anchor | NFPA 79 Anchor | UL 508A Anchor | Primary Owner | Tool Notes |
|------------|------------|----------------|----------------|---------------|------------|
| **Scope boundary** | Art. 409 (panels)<br>Art. 670 (machinery) | Scope/Admin chapters | Scope & panel definition | NFPA 79 (machine)<br>UL 508A (panel)<br>NEC (installation) | Decision router: Which standard drives this decision? |
| **Component listing** | Art. 110 (listing/labeling) | General requirements | General construction | NEC + UL | Evidence pack: manuals, listings, markings |
| **Disconnecting means** | Installation-dependent | Ch. 5 Disconnecting Means | Panel disconnect integration | NFPA 79 (behavior)<br>NEC (installation) | Checklist: location, accessibility, labeling, LOTO |
| **Overcurrent protection** | Art. 240, 430 (motors) | Ch. 6 Overcurrent Protection | Overcurrent protection requirements | NEC + UL 508A | Tie to SCCR strategy |
| **Grounding & bonding** | Art. 250 | Ch. 8 Grounding & Bonding | Grounding/bonding requirements | NEC baseline<br>NFPA 79 machine specifics | Bonding jumpers, door bonding, PE routing |
| **Wiring methods** | Art. 300, 310 | Ch. 16 Wiring Methods<br>Ch. 17 Cables/Cords | Wiring methods & conductors | NEC baseline<br>UL 508A inside panel<br>NFPA 79 inside machine | Separation rules: power vs control vs comms |
| **Control circuits** | As applicable | Ch. 9 Control Circuits & Functions | Control circuit construction | NFPA 79 (behavior) | Behavioral rules in NFPA 79, hardware in UL |
| **Emergency stop** | Indirect via requirements | Ch. 9 (stop functions/e-stop) | Safety device integration | NFPA 79 (behavior) | What it must do (NFPA), how built (UL) |
| **Panel construction** | Art. 409 (marking/installation) | Ch. 11 Control Equipment | Core construction/testing | UL 508A | UL is panel build bible; NFPA adds machinery gaps |
| **SCCR determination** | Art. 409 (marking required) | Machinery SCCR concept | Supplement SB (SCCR method) | NEC requires<br>UL provides method | (1) Require SCCR label (NEC), (2) compute via SB (UL) |
| **Marking & documentation** | Art. 409 marking | Ch. 19 Marking & Documentation | Marking & documentation | All three overlap | Handover pack generator |
| **Motors/controllers** | Art. 430 | Motors chapters | Motor controllers/drives | NEC (circuits)<br>UL (panel construction) | Drive integration cross-links to NFPA 79 |
| **Control power** | General OCP/conductor rules | Ch. 15 Transformers & Power Supplies | Transformer/PSU construction | NFPA 79 + UL 508A | 24VDC architecture, secondary protection |
| **Multi-panel machines** | Panel SCCR marking required | Machine-level considerations | Each panel SCCR needed | System-level engineering | Require SCCR per panel; compute machine SCCR |

## Critical Cross-References

### SCCR (Short-Circuit Current Rating) ⚠️ CRITICAL

**Requirement**:
- NEC Article 409 **requires** SCCR marking on industrial control panels
- UL 508A Supplement SB provides the **approved calculation method**
- NFPA 79 uses SCCR concept in machinery context

**Workflow**:
1. NEC 409 → Require SCCR label
2. UL 508A SB → Compute SCCR (weakest-link method)
3. Store evidence and apply label

**Files**:
- [NEC_2023__Art409__industrial_control_panels.md](../nec/NEC_2023__Art409__industrial_control_panels.md)
- [UL508A_2022__sccr_short_circuit_current_rating.md](../ul_508a/UL508A_2022__sccr_short_circuit_current_rating.md)

### Grounding and Bonding

**Requirement**:
- NEC Article 250 → Safety grounding baseline (legally required)
- NFPA 79 Chapter 8 → Machine bonding specifics
- UL 508A Section 7 → Panel bonding workmanship

**Key Points**:
- Separate "noise grounding" from safety bonding
- Door bonding jumpers required
- PE (protective earth) continuity critical

**Files**:
- [NEC_2023__Art250__grounding_and_bonding.md](../nec/NEC_2023__Art250__grounding_and_bonding.md)
- [NFPA79_2024__Ch08__grounding_and_bonding.md](../nfpa79/NFPA79_2024__Ch08__grounding_and_bonding.md)
- [UL508A_2022__grounding_and_bonding.md](../ul_508a/UL508A_2022__grounding_and_bonding.md)

### Scope Boundary (Panel vs Machine vs Installation)

**Decision Framework**:
- **Machine behavior & safety** → NFPA 79
- **Panel construction & testing** → UL 508A
- **Installation & inspection** → NEC

**Critical Boundaries**:
- Machine supply connection point
- Panel boundary definition
- AHJ jurisdiction

**Files**:
- [NEC_2023__Art409__industrial_control_panels.md](../nec/NEC_2023__Art409__industrial_control_panels.md)
- [NEC_2023__Art670__industrial_machinery.md](../nec/NEC_2023__Art670__industrial_machinery.md)
- [NFPA79_2024__Ch01__administration.md](../nfpa79/NFPA79_2024__Ch01__administration.md)
- [UL508A_2022__scope_and_application.md](../ul_508a/UL508A_2022__scope_and_application.md)

## Conflict Resolution

When standards conflict:

1. **Legal requirement wins**: NEC is legally adopted → must comply
2. **Listing requirement**: If UL listing needed → UL 508A governs panel construction
3. **Machinery context**: NFPA 79 may add requirements beyond UL 508A for machinery panels
4. **Most restrictive**: When unclear, use most restrictive requirement
5. **Document decision**: Always document which standard was followed and why

## Use Cases

### Use Case 1: UL-Listed Control Panel (Standalone)

**Scenario**: Building control panel for motor control, US market, UL listing required

**Primary Standards**:
- UL 508A (all sections) - panel construction and listing
- NEC Article 409 - panel installation requirements
- NEC Article 250 - grounding

**Critical Items**:
- SCCR calculation (UL 508A SB)
- Spacing/clearance (UL 508A Section 4)
- Wire sizing (UL 508A Section 5)
- SCCR label (NEC 409 + UL 508A)

### Use Case 2: Industrial Machinery (US Installation)

**Scenario**: Conveyor system for US factory installation

**Primary Standards**:
- NFPA 79 (comprehensive machine standard)
- NEC Article 670 (machinery installation)
- NEC Article 430 (motors)

**Optional**:
- UL 508A if control panel requires UL listing (separate evaluation)

**Critical Items**:
- Disconnect location and labeling (NFPA 79 Ch 5)
- E-stop function (NFPA 79 Ch 9)
- Motor protection (NEC 430 + NFPA 79 Ch 12)
- Grounding (NEC 250 + NFPA 79 Ch 8)

### Use Case 3: Multi-Panel Machine

**Scenario**: Packaging line with 3 control panels

**Requirements**:
- Each panel needs SCCR (NEC 409 + UL 508A SB)
- Machine-level SCCR basis (system engineering)
- Panel interconnections documented

**Workflow**:
1. Calculate SCCR for each panel (UL 508A SB)
2. Label each panel (NEC 409)
3. Document machine SCCR basis (NFPA 79 context)
4. Store evidence per panel

## Detailed Overlap Notes

For detailed decision rules, evidence requirements, and checklists for each topic, see:

**Location**: `rag/standards_intelligence/crosswalks/overlap_notes/`

**Per-Topic Files**:
- `overlap__scope_boundary.md`
- `overlap__listing_labeling_instructions.md`
- `overlap__disconnecting_means.md`
- `overlap__overcurrent_protection.md`
- `overlap__grounding_bonding.md`
- `overlap__wiring_methods_conductors.md`
- `overlap__control_functions.md`
- `overlap__emergency_stop.md`
- `overlap__panel_construction.md`
- `overlap__sccr.md` (CRITICAL)
- `overlap__marking_documentation.md`
- `overlap__motors_drives.md`
- `overlap__control_power.md`
- `overlap__multi_panel_machines.md`

## References

This matrix is based on:
- NEC 2023 Edition (NFPA 70)
- NFPA 79-2024 Edition
- UL 508A 2022 Edition (7th Edition)

For authoritative requirements, always purchase official standards from NFPA and UL.

## Changelog

- 2026-01-15 — Initial UL 508A ↔ NEC ↔ NFPA 79 overlap matrix created
  - Topic-based routing established
  - Critical cross-references documented
  - Use cases defined
  - Status: DRAFT (ready for content development)

---

**Next Steps**: Build per-topic overlap notes with detailed decision rules, evidence requirements, and implementation checklists.
