<!--
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Standards Applicability Matrix
**AI_READ_ACCESS: ALLOWED**
**CONTENT_CLASS: RAG_APPROVED**
**Status:** Authoritative Reference

## Purpose

Decision matrix for selecting applicable standards based on project type, jurisdiction, and requirements.

## Quick Decision Tree

```
START: What are you designing?
│
├─► Control Panel (standalone)
│   │
│   ├─► US Market + UL Listing Required
│   │   └─► USE: UL 508A + NEC Article 409 + NEC Article 250
│   │
│   ├─► US Market (no UL listing)
│   │   └─► USE: NEC Article 409 + NEC Articles 250, 310, 430
│   │
│   └─► International Market
│       └─► USE: IEC 60204-1 + ISO 13849-1 (if safety functions)
│
├─► Industrial Machinery
│   │
│   ├─► US Market Only
│   │   └─► USE: NFPA 79 + NEC Article 670 + UL 508A (if panel UL listed)
│   │
│   ├─► EU/International Market (CE marking)
│   │   └─► USE: IEC 60204-1 + ISO 13849-1 + ISO 12100
│   │
│   └─► Global (US + EU markets)
│       └─► USE: NFPA 79 + IEC 60204-1 + ISO 13849-1 + ISO 12100
│           (Design to MOST RESTRICTIVE from each)
│
├─► Safety System Design
│   │
│   ├─► US Market
│   │   └─► USE: NFPA 79 Ch 9 + applicable OSHA standards
│   │
│   └─► International Market
│       └─► USE: ISO 13849-1 (Performance Level) OR IEC 62061 (SIL)
│           + ISO 12100 (Risk Assessment)
│           + IEC 60204-1 (Electrical implementation)
│
└─► Process Industry Safety
    └─► USE: IEC 61511 + IEC 61508 (foundation)
```

## Applicability Matrix by Project Type

| Project Type | US Standards | International Standards | Safety Standards | Notes |
|--------------|--------------|------------------------|------------------|-------|
| **Standalone Control Panel** | UL 508A, NEC 409 | IEC 60204-1 Clause 11 | - | UL listing often required in US |
| **Conveyor System** | NFPA 79, NEC 670, 430 | IEC 60204-1 | ISO 13849 if guarding | Emergency stop critical |
| **Robotic Cell** | NFPA 79, UL 508A | IEC 60204-1, ISO 10218 | ISO 13849-1 (typically PLd/PLe) | High safety requirements |
| **Packaging Machine** | NFPA 79, NEC 670 | IEC 60204-1 | ISO 13849-1 | CE marking for EU |
| **CNC Machine** | NFPA 79 | IEC 60204-1 | ISO 13849-1 | Safety interlocks required |
| **Pump/HVAC Control** | NEC 430, 440, 670 | IEC 60204-1 | - (unless process critical) | May not need machinery standards |
| **Process Control** | NEC 670, NFPA 79 | IEC 60204-1, IEC 61511 | IEC 61511 (SIL) if safety critical | Process industry focus |

## Market-Based Selection

### US Market Only

**Required Standards**:
1. **NEC (NFPA 70)** - Electrical code (legally enforced)
   - Article 409: Industrial control panels
   - Article 430: Motors
   - Article 670: Industrial machinery
   - Article 250: Grounding

2. **NFPA 79** - Industrial machinery electrical design
   - Comprehensive machine electrical requirements
   - Reference for NEC Article 670

3. **UL 508A** - If panel requires UL listing
   - Insurance often requires UL listing
   - Some AHJs require UL listing

**Optional/Supporting**:
- OSHA regulations (worker safety)
- ANSI standards (component standards)

### EU/International Market (CE Marking)

**Required Standards**:
1. **IEC 60204-1** - Electrical equipment of machines
   - Electrical requirements (equivalent to NFPA 79)

2. **ISO 12100** - Risk assessment
   - Foundation for CE marking
   - Required before ISO 13849-1

3. **ISO 13849-1** OR **IEC 62061** - Safety functions
   - ISO 13849-1: Performance Levels (PLa to PLe)
   - IEC 62061: Safety Integrity Levels (SIL 1-3)
   - Choose one approach (ISO 13849-1 more common for machinery)

**Supporting Standards**:
- ISO 13850: Emergency stop
- IEC 60529: IP ratings
- ISO 14119: Interlocking devices
- EN standards (EU harmonized versions of IEC/ISO)

### Global (US + International)

**Design to BOTH**:
- NFPA 79 (US) AND IEC 60204-1 (International)
- NEC Article 670 (US installation) AND ISO 13849-1 (EU safety)
- UL 508A (if US panel listing needed)

**Strategy**:
- Use **most restrictive requirement** from each standard
- Document compliance to both
- Use dual-voltage designs (480V/400V capable)
- Use dual-certified components (UL + CE)

## Standards by Technical Topic

### Grounding/Bonding
- **US**: NEC Article 250, UL 508A Section 7, NFPA 79 Ch 8
- **International**: IEC 60204-1 Clause 8

### Emergency Stop
- **US**: NFPA 79 Ch 9
- **International**: IEC 60204-1 Clause 9, ISO 13850

### Control Circuits
- **US**: NEC Article 725, NFPA 79 Ch 9
- **International**: IEC 60204-1 Clause 9

### Motor Protection
- **US**: NEC Article 430, NFPA 79 Ch 12
- **International**: IEC 60204-1 Clause 12

### Disconnects/Isolation
- **US**: NFPA 79 Ch 5
- **International**: IEC 60204-1 Clause 5

### Panel Design/Construction
- **US**: UL 508A (all sections), NEC Article 409
- **International**: IEC 60204-1 Clause 11

### Wire Sizing
- **US**: NEC Article 310, UL 508A Section 5
- **International**: IEC 60204-1 Clause 13

### Short-Circuit Protection
- **US**: UL 508A Section SB (SCCR), NEC 409.110
- **International**: IEC 60204-1 Clause 7

### Marking/Documentation
- **US**: UL 508A Section 12, NFPA 79 Ch 19, NEC Article 110
- **International**: IEC 60204-1 Clause 14

### Safety Functions (PL/SIL)
- **US**: NFPA 79 Ch 9, OSHA regulations
- **International**: ISO 13849-1 (PL), IEC 62061 (SIL)

### Software Implementation
- **Machinery**: IEC 62061 or ISO 13849-1/-2 for the safety-function route, with IEC 61131-3 for PLC language questions
- **Process**: IEC 61511 with IEC 61508-3 for safety-related software lifecycle depth
- **Cross-cutting guide**: `reference_models/software_safety_and_intrinsic_safety_standards.md`

### Secure Development
- **International**: IEC 62443-4-1 (secure development lifecycle), IEC 62443-4-2 (component requirements), IEC 62443-3-3 (system requirements)
- **Use when**: PLC or controller software is networked, remotely maintained, or productized

### Intrinsic Safety / Hazardous-Area I/O
- **US**: NEC hazardous location articles, UL 60079-11, UL 698A
- **International**: IEC 60079-11, IEC 60079-14, IEC 60079-25
- **Use when**: Sensors, barriers, isolators, or remote I/O enter classified or intrinsically safe circuits

## Certification Requirements

### US Certifications

**UL Listing** (UL 508A):
- Voluntary but often required by:
  - Insurance companies
  - Some AHJs
  - End customers
  - Liability reduction
- Covers: Industrial control panels
- Does NOT cover: Complete machines (use NFPA 79 for machine design)

**Field Evaluation**:
- If UL listing not feasible
- Third-party inspection by field evaluation service
- More expensive per unit

**NEC Compliance**:
- Legally required (adopted by jurisdictions)
- Verified by AHJ inspection
- No "certification" - just code compliance

### International Certifications

**CE Marking**:
- Legally required for EU market
- Self-certification (with technical file)
- Based on: IEC 60204-1, ISO 13849-1, ISO 12100
- No third-party testing required (but recommended)

**TÜV/Other Notified Body**:
- Optional third-party certification
- Adds credibility to CE marking
- May be required for certain machinery directives

## Special Cases

### Dual-Market Machinery (US + EU)

**Required**:
1. Design electrical to BOTH NFPA 79 AND IEC 60204-1
2. Design safety to ISO 13849-1 (covers US OSHA requirements)
3. Perform ISO 12100 risk assessment
4. If panel needs UL listing: Add UL 508A compliance

**Result**:
- Machine legal in US (NFPA 79, NEC)
- Machine legal in EU (CE marking via IEC/ISO)
- Panel UL listed if needed (UL 508A)

### Process Industry

**Safety Instrumented Systems (SIS)**:
- IEC 61511 (process industry functional safety)
- Based on IEC 61508 (generic functional safety)
- Higher rigor than ISO 13849-1
- SIL ratings for safety functions

**Control Systems**:
- Still use IEC 60204-1 for electrical design
- But safety functions per IEC 61511 (not ISO 13849-1)

### Existing Machine Retrofit

**US**:
- Must meet NEC (current edition at time of inspection)
- NFPA 79 good practice (not legally required for retrofit)
- Grandfathering may apply (check with AHJ)

**EU**:
- CE marking required if "substantial modification"
- Otherwise original certification may remain valid
- Consult notified body

## Cross-Standard Relationships

### US Standards Hierarchy
```
NEC (Legal Code)
    ↓
NEC Article 670 → References NFPA 79
NEC Article 409 → Defines industrial control panels
    ↓
UL 508A → Panel listing standard (based on NEC 409)
NFPA 79 → Machine design standard (referenced by NEC 670)
```

### International Standards Hierarchy
```
ISO 12100 (Risk Assessment)
    ↓
ISO 13849-1 OR IEC 62061 (Safety Functions)
    ↓
IEC 60204-1 (Electrical Implementation)
    ↓
Component standards (contactors, relays, etc.)
```

### US ↔ International Equivalents
```
NFPA 79 (US)  ↔  IEC 60204-1 (International)
  Ch 5        ↔  Clause 5 (Disconnects)
  Ch 8        ↔  Clause 8 (Grounding/Bonding)
  Ch 9        ↔  Clause 9 (Control Circuits)
  Ch 11       ↔  Clause 11 (Control Equipment)
  Ch 19       ↔  Clause 14 (Marking)
```

## Decision Examples

### Example 1: UL-Listed Control Panel (US Only)

**Question**: Designing standalone control panel for motor control, US market, customer requires UL listing.

**Answer**:
- **Primary**: UL 508A (all sections)
- **Supporting**: NEC Article 409 (referenced by UL 508A)
- **Required calculations**: SCCR (UL 508A Section SB), wire sizing (Section 5), spacing (Section 4)
- **Grounding**: NEC Article 250, UL 508A Section 7

### Example 2: Conveyor for US Installation

**Question**: Designing conveyor system for US factory.

**Answer**:
- **Primary**: NFPA 79 (comprehensive machine standard)
- **Code compliance**: NEC Article 670 (references NFPA 79)
- **Motors**: NEC Article 430, NFPA 79 Ch 12
- **E-stop**: NFPA 79 Ch 9
- **Panel**: UL 508A if panel requires UL listing (separate decision)

### Example 3: Robot Cell for EU (CE Marking)

**Question**: Designing robot work cell for European customer.

**Answer**:
1. **Risk assessment**: ISO 12100
2. **Safety functions**: ISO 13849-1 (likely PLd or PLe for robot cell)
3. **Electrical**: IEC 60204-1
4. **Robot-specific**: ISO 10218 (robot safety)
5. **Result**: CE marking with technical file

### Example 4: Global Packaging Machine (US + EU)

**Question**: Packaging machine sold in both US and EU markets.

**Answer**:
1. **Electrical**: Design to BOTH NFPA 79 AND IEC 60204-1 (most restrictive)
2. **Safety**: ISO 13849-1 (covers US OSHA + EU requirements)
3. **Risk assessment**: ISO 12100
4. **US installation**: Verify NEC compliance
5. **Panel**: UL 508A if US customers require UL listing
6. **Result**: Machine compliant in US (NFPA 79/NEC) and EU (CE marking)

---

## Changelog

- 2026-01-15 — Initial standards applicability matrix created
  - Decision trees for market selection
  - Topic-based standard routing
  - Cross-standard equivalents
  - Example scenarios

**Status**: Ready for use in standards selection

**Usage**: Consult this matrix when starting a new project to determine which standards apply
