<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MATRIX_ID: NFPA79_IEC60204_OVERLAP
STANDARDS: NFPA_79_2024, IEC_60204_1_2018
JURISDICTION: US + International
-->

# NFPA 79 ↔ IEC 60204-1 Overlap Matrix

## Purpose

This matrix maps equivalent requirements between US and International machinery electrical standards:
- **NFPA 79 (2024)**: Electrical Standard for Industrial Machinery (US)
- **IEC 60204-1 (2018)**: Electrical Equipment of Machines (International/Global)

Use this matrix for:
- Dual-market machinery (US + EU sales)
- Understanding US vs International differences
- Converting designs between markets

## Legend

- **NFPA 79**: Chapter-based, US machinery standard
- **IEC 60204-1**: Clause-based, international machinery standard
- **Typical Owner**: Which standard leads when both apply
- **Equivalence**: How closely requirements align

## Topic-Based Overlap Matrix

| Topic Area | NFPA 79 Anchor | IEC 60204-1 Anchor | Equivalence | Typical Owner | Practical Notes |
|------------|----------------|---------------------|-------------|---------------|-----------------|
| **Scope boundary** | Ch. 1 Administration | Clause 1 Scope | High | Tie | Machine supply connection point definition |
| **Definitions** | Ch. 2 Definitions | Clause 3 Terms and definitions | Medium | Tie | Build shared glossary; terms differ |
| **General requirements** | Ch. 3 General requirements | Clause 4 General requirements | High | Tie | Baseline safety principles |
| **Incoming supply / Disconnect** | Ch. 5 Disconnecting Means | Clause 5 Incoming Supply | Very High | Tie | DIRECT EQUIVALENT |
| **Shock protection** | Ch. 7 Protection Against Electric Shock | Clause 6 Protection Against Electric Shock | High | IEC (internationally) | Touch-safe design, barriers |
| **Equipment protection** | Ch. 6 Overcurrent Protection | Clause 7 Protection of Equipment | High | Tie | Overcurrent, environmental protection |
| **Grounding / Bonding** | Ch. 8 Grounding and Bonding | Clause 8 Equipotential Bonding | Very High | Tie | DIRECT EQUIVALENT (terminology differs) |
| **Control circuits** | Ch. 9 Control Circuits and Control Functions | Clause 9 Control Circuits and Control Functions | Very High | Tie | DIRECT EQUIVALENT |
| **Operator interface** | Ch. 10 Operator Interface Devices | Clause 10 Operator Interface | High | Tie | HMI, pushbuttons, indicators |
| **Control equipment** | Ch. 11 Control Equipment | Clause 11 Control Equipment | High | Tie | Enclosures, panel design |
| **Motors and drives** | Ch. 12 Motors and Associated Equipment | Clause 12 Motors and Drives | High | Tie | VFDs, motor protection |
| **Accessories & lighting** | Ch. 13 Appliances/Accessories<br>Ch. 14 Lighting | Clause 13 Accessories and Lighting | Medium | IEC (combined) | IEC combines; NFPA splits |
| **Marking & documentation** | Ch. 19 Marking and Documentation | Clause 14 Marking and Documentation | High | Tie | Labeling, schematics |
| **Verification / Testing** | Ch. 20 System Integration | Clause 15 Verification | High | IEC (explicit) | IEC has dedicated verification clause |

## Direct Chapter ↔ Clause Equivalents

These are VERY HIGH equivalence mappings:

### 1. Disconnecting Means / Incoming Supply
- **NFPA 79**: Chapter 5 - Disconnecting Means
- **IEC 60204-1**: Clause 5 - Incoming Supply
- **Equivalence**: Very High (~90%)
- **Key Points**: Both require accessible disconnect, isolation capability, LOTO compatibility

**Files**:
- [NFPA79_2024__Ch05__disconnecting_means.md](../nfpa79/NFPA79_2024__Ch05__disconnecting_means.md)
- [IEC60204_1_2018__Clause05__incoming_supply.md](../iec_60204_1/IEC60204_1_2018__Clause05__incoming_supply.md)

### 2. Grounding and Bonding / Equipotential Bonding
- **NFPA 79**: Chapter 8 - Grounding and Bonding
- **IEC 60204-1**: Clause 8 - Equipotential Bonding
- **Equivalence**: Very High (~95%)
- **Key Points**: Same intent, different terminology (US: "grounding", IEC: "equipotential bonding")

**Files**:
- [NFPA79_2024__Ch08__grounding_and_bonding.md](../nfpa79/NFPA79_2024__Ch08__grounding_and_bonding.md)
- [IEC60204_1_2018__Clause08__equipotential_bonding.md](../iec_60204_1/IEC60204_1_2018__Clause08__equipotential_bonding.md)

### 3. Control Circuits and Control Functions
- **NFPA 79**: Chapter 9 - Control Circuits and Control Functions
- **IEC 60204-1**: Clause 9 - Control Circuits and Control Functions
- **Equivalence**: Very High (~90%)
- **Key Points**: E-stop behavior, start/stop logic, stop categories

**Files**:
- [NFPA79_2024__Ch09__control_circuits_and_control_functions.md](../nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md)
- [IEC60204_1_2018__Clause09__control_circuits_and_functions.md](../iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md)

### 4. Control Equipment
- **NFPA 79**: Chapter 11 - Control Equipment
- **IEC 60204-1**: Clause 11 - Control Equipment
- **Equivalence**: High (~85%)
- **Key Points**: Panel/enclosure design for machinery

**Files**:
- [NFPA79_2024__Ch11__control_equipment.md](../nfpa79/NFPA79_2024__Ch11__control_equipment.md)
- [IEC60204_1_2018__Clause11__control_equipment.md](../iec_60204_1/IEC60204_1_2018__Clause11__control_equipment.md)

### 5. Marking and Documentation
- **NFPA 79**: Chapter 19 - Marking and Documentation
- **IEC 60204-1**: Clause 14 - Marking and Documentation
- **Equivalence**: High (~80%)
- **Key Points**: Required labels, schematics, manuals (format differs)

**Files**:
- [NFPA79_2024__Ch19__marking_and_documentation.md](../nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md)
- [IEC60204_1_2018__Clause14__marking_and_documentation.md](../iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md)

## Key Differences (US vs International)

### Terminology

| Concept | NFPA 79 (US) | IEC 60204-1 (International) |
|---------|--------------|---------------------------|
| Protective connection to earth | Grounding/Bonding | Equipotential Bonding |
| Safety ground conductor | EGC (Equipment Grounding Conductor) | PE (Protective Earth) |
| Power cutoff | Disconnecting Means | Isolation / Switching Off |
| Panel/Enclosure | Control Equipment | Control Equipment |

### Voltage Standards

| Region | Common Voltages | Frequency |
|--------|----------------|-----------|
| **US (NFPA 79)** | 120V, 208V, 240V, 480V, 600V | 60 Hz |
| **International (IEC)** | 230V, 400V | 50 Hz |

### Wire Colors

| Function | NFPA 79 (US) | IEC 60204-1 |
|----------|--------------|-------------|
| **Ground (PE)** | Green or bare | Green/Yellow striped |
| **Neutral** | White or gray | Blue |
| **Phase** | Black, red, blue | Brown, black, gray (or numbered) |

### Component Certification

| Market | Certification |
|--------|---------------|
| **US** | UL, ETL, CSA listed |
| **International** | CE marked, IEC/EN certified |

### Safety Framework

**US (NFPA 79)**:
- NFPA 79 is **standalone** for machinery electrical requirements
- OSHA regulations for worker safety
- Risk assessment not explicitly required (good practice)

**International (IEC 60204-1)**:
- IEC 60204-1 is **electrical implementation layer**
- Must pair with:
  - ISO 12100 (Risk Assessment) - REQUIRED
  - ISO 13849-1 (Performance Levels) OR IEC 62061 (SIL) - for safety functions
  - ISO 13850 (Emergency Stop)

**Framework**:
```
For International/CE Marking:
ISO 12100 (Risk Assessment)
    ↓
ISO 13849-1 OR IEC 62061 (Safety Functions)
    ↓
IEC 60204-1 (Electrical Implementation)
```

## Dual-Compliance Strategy

### When Both Standards Apply

**Scenario**: Machinery sold in BOTH US and EU/International markets

**Approach**:
1. Design electrical to **BOTH** NFPA 79 AND IEC 60204-1
2. Use **most restrictive requirement** from each standard
3. Perform ISO 12100 risk assessment (required for CE, good practice for US)
4. Design safety functions to ISO 13849-1 (covers US OSHA requirements)
5. Document compliance to **both** standards

**Result**:
- Machine legal in US (NFPA 79 compliance)
- Machine legal in EU (CE marking via IEC 60204-1 + ISO 13849-1 + ISO 12100)
- Single design supports both markets

### Critical Design Decisions

**Dual-Voltage Capability**:
- Design control systems for 120V OR 230V control power
- Design power for 480V OR 400V (where applicable)
- Use dual-voltage transformers or switchable supplies

**Component Selection**:
- Use components with BOTH UL listing AND CE marking
- Verify component works at both 50Hz and 60Hz
- Check voltage ratings span both markets

**Documentation**:
- Create documentation package meeting BOTH standards
- Maintain evidence of compliance to both
- CE marking technical file (EU requirement)
- Compliance statements for US installation

## Overlap Notes

For detailed decision rules, evidence requirements, and checklists for each topic, see:

**Location**: `rag/standards_intelligence/crosswalks/overlap_notes/`

**Per-Topic Files**:
- `overlap_nfpa79_iec60204__scope_boundary.md`
- `overlap_nfpa79_iec60204__definitions.md`
- `overlap_nfpa79_iec60204__general_requirements.md`
- `overlap_nfpa79_iec60204__incoming_supply_disconnect.md`
- `overlap_nfpa79_iec60204__electric_shock_protection.md`
- `overlap_nfpa79_iec60204__equipment_protection.md`
- `overlap_nfpa79_iec60204__grounding_bonding.md`
- `overlap_nfpa79_iec60204__control_functions.md`
- `overlap_nfpa79_iec60204__operator_interface.md`
- `overlap_nfpa79_iec60204__control_equipment.md`
- `overlap_nfpa79_iec60204__motors_drives.md`
- `overlap_nfpa79_iec60204__accessories_lighting.md`
- `overlap_nfpa79_iec60204__marking_documentation.md`
- `overlap_nfpa79_iec60204__verification.md`

## Use Cases

### Use Case 1: US-Only Machinery

**Scenario**: Conveyor for US factory

**Standards**:
- Primary: NFPA 79
- Installation: NEC Article 670

**Design Choices**:
- 480V/120V (US voltages)
- 60 Hz
- UL-listed components
- NFPA 79 labeling
- English documentation

### Use Case 2: EU-Only Machinery

**Scenario**: Packaging machine for European customer

**Standards**:
- IEC 60204-1 (electrical)
- ISO 13849-1 (safety functions)
- ISO 12100 (risk assessment)

**Design Choices**:
- 400V/230V (EU voltages)
- 50 Hz
- CE-marked components
- IEC color codes
- Multilingual documentation
- CE marking with technical file

### Use Case 3: Global Machinery (US + EU)

**Scenario**: Robot cell sold worldwide

**Standards**:
- BOTH NFPA 79 AND IEC 60204-1
- ISO 13849-1 (safety)
- ISO 12100 (risk assessment)

**Design Choices**:
- Dual-voltage capable (480V/400V and 120V/230V)
- 50Hz/60Hz compatible components
- Dual-certified components (UL + CE)
- Most restrictive requirements from each standard
- Documentation meeting both standards
- Regional labeling (field-applied per market)

**Result**:
- US installation: Complies with NFPA 79 + NEC
- EU installation: CE marked per IEC 60204-1 + ISO standards
- Design once, deploy anywhere

## Regional Adaptation

### Converting US Design to International

**Electrical Changes**:
- [ ] Convert 480V → 400V (if applicable)
- [ ] Convert 120V → 230V control power
- [ ] Verify 50Hz compatibility
- [ ] Change wire colors (green → green/yellow PE, etc.)

**Component Changes**:
- [ ] Replace UL-listed with CE-marked equivalents
- [ ] Verify component voltage/frequency ratings
- [ ] Update nameplates

**Documentation Changes**:
- [ ] Add ISO 12100 risk assessment
- [ ] Add ISO 13849-1 safety function analysis
- [ ] Update schematics (IEC symbols)
- [ ] Create CE marking technical file
- [ ] Translate to local languages

**Standards Changes**:
- [ ] Verify against IEC 60204-1 (not just NFPA 79)
- [ ] Add Clause 15 verification tests
- [ ] Update marking per Clause 14

### Converting International Design to US

**Electrical Changes**:
- [ ] Convert 400V → 480V (if applicable)
- [ ] Convert 230V → 120V control power
- [ ] Verify 60Hz compatibility
- [ ] Change wire colors (green/yellow → green PE, etc.)

**Component Changes**:
- [ ] Replace CE-marked with UL-listed equivalents
- [ ] Verify component voltage/frequency ratings
- [ ] Update nameplates

**Documentation Changes**:
- [ ] Verify against NFPA 79 (not just IEC 60204-1)
- [ ] Update schematics (US symbols)
- [ ] English-only documentation (typically)
- [ ] NEC compliance statement

**Additional for US**:
- [ ] Add NEC Article 670 compliance verification
- [ ] If panel needs UL listing: Add UL 508A compliance

## References

This matrix is based on:
- NFPA 79-2024 Edition
- IEC 60204-1:2018 (6th Edition)

For authoritative requirements, always purchase official standards from NFPA and IEC.

## Changelog

- 2026-01-15 — Initial NFPA 79 ↔ IEC 60204-1 overlap matrix created
  - Direct chapter/clause equivalents mapped
  - Regional differences documented
  - Dual-compliance strategy defined
  - Conversion guidance added
  - Status: DRAFT (ready for content development)

---

**Next Steps**: Build per-topic overlap notes with US vs EU decision rules and regional adaptation checklists.
