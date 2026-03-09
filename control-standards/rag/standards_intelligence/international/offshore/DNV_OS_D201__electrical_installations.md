<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: DNV_OFFSHORE
STANDARD_ID: DNV-OS-D201
EDITION: 2023

DNV_HIERARCHY:
  document: "DNV-OS-D201"
  document_title: "Electrical Installations — Offshore and Floating Units"

INDEX_TAGS:
  topics: ["marine_grade", "power_redundancy", "hazardous_area", "emergency_power", "ESD", "fire_and_gas", "DP_class", "IEC_60092"]
  systems: ["offshore_platform", "FPSO", "ESD", "fire_and_gas", "dynamic_positioning"]
-->

# DNV-OS-D201 — Electrical Installations: Offshore and Floating Units

## 0. Why this matters for control engineers

DNV-OS-D201 is the primary DNV standard governing electrical installations on offshore platforms, FPSOs, and floating production units. For control engineers, it defines: (1) marine-grade equipment requirements that exceed onshore specifications, (2) power redundancy classes that affect UPS sizing and distribution architecture, (3) the interface between the electrical installation and the safety systems (ESD, F&G), and (4) the class society approval process that must be integrated into the engineering workflow from the outset.

Every electrical and control system installed on a DNV-classed offshore unit must be designed, documented, and approved in accordance with this offshore standard — not IEC 60204-1 or NEC alone.

## 1. Scope and applicability

DNV-OS-D201 applies to:
- Mobile offshore drilling units (MODUs)
- Floating production, storage, and offloading units (FPSOs)
- Offshore fixed and floating platforms (where DNV is the classification society)
- Semi-submersibles and jackups

For control and instrumentation engineers, the relevant sections are:
- Section 2 — Electrical power systems (redundancy, UPS, emergency power)
- Section 4 — Hazardous area electrical equipment
- Section 6 — Control and monitoring systems
- Section 7 — Safety systems (ESD, F&G interface)

## 2. Marine-grade equipment requirements

Offshore electrical and control equipment must meet environmental conditions that exceed typical onshore industrial ratings:

| Requirement | Onshore industrial | Offshore (DNV-OS-D201) |
|-------------|--------------------|------------------------|
| **Enclosure** | IP54 typical | IP56 minimum for exposed locations; IP66 for wash-down areas |
| **Vibration** | Not typically specified | Vibration tested per IEC 60068-2-6 (sinusoidal) and IEC 60068-2-64 (random) |
| **Humidity** | 85% RH typical | 95% RH, non-condensing — continuous offshore ambient |
| **Salt atmosphere** | Not required onshore | Salt mist tested per IEC 60068-2-52 for exposed equipment |
| **Cable** | PVC acceptable | Halogen-free, fire-resistant cables required throughout — LSOH (IEC 60332) |
| **Temperature** | 0–40°C typical | −20°C to +55°C ambient for topside installations; verify for specific area |

**Halogen-free cable (LSOH):** DNV-OS-D201 requires low-smoke, zero-halogen (LSOH) cables throughout the unit. PVC cables are not permitted on offshore units. This affects cable procurement, termination fittings, and cable schedule documentation.

## 3. Power system redundancy

DNV classifies offshore power systems by redundancy level. The class notation determines minimum design requirements:

| Notation | Redundancy Level | Control System Implication |
|----------|-----------------|---------------------------|
| **No notation** | Single main switchboard; no redundancy required | Basic offshore installation |
| **DP-2** | Two main power sources; no single failure shall cause loss of position | Dual bus architecture; UPS feeds each bus independently |
| **DP-3** | Three independent power sources; two fire/flood divisions | Physically segregated cable routes and switchboard rooms |

**Emergency power (Section 2.7):**
- Emergency switchboard fed from emergency generator (auto-start within 30 seconds of main power failure)
- Emergency generator capacity must cover: ESD system, F&G system, emergency lighting, HVAC for escape routes, communication systems
- UPS for ESD logic solver: battery autonomy ≥ 30 minutes at full load (verify with safety requirements specification)

**Control system power distribution:**
- Safety system (ESD, F&G logic solvers) fed from emergency bus via UPS
- Process control system may be fed from main bus via UPS (category depends on process criticality)
- Instrument buses: typically 24 VDC from regulated power supplies fed from UPS

## 4. Hazardous area electrical installations

Offshore units have extensive hazardous areas. DNV-OS-D201 Section 4 references IEC 60079 series for equipment selection and IEC 60079-14 for installation:

**Area classification on offshore units:**
- Zone 0 and Zone 1: hydrocarbon processing decks, pump rooms, compressor rooms
- Zone 2: areas adjacent to Zone 1, wellbay areas during certain operations
- Non-hazardous: control room, accommodation, auxiliary machinery room (with adequate ventilation)

**Key differences from onshore (IEC 60079-14):**
- Cable routing: LSOH cables, metallic conduit or armoured cable in Zone 1 — cable tray with armoured cable preferred
- All Ex equipment must carry valid IECEx or ATEX certificate — DNV surveyor verifies on board
- DNV performs an Ex inspection walkdown as part of class renewal — all certificates and installation records must be available on the platform

**Purged and pressurized (Ex p) enclosures:**
Offshore control rooms housing non-Ex rated panels are often maintained at positive pressure with purged/monitored air supply — classified as Ex p enclosures (IEC 60079-2). The room itself becomes the Ex p enclosure. Requires: pressure monitoring, automatic shutdown on pressure loss, alarm to operator.

## 5. Control and monitoring systems (Section 6)

DNV distinguishes three tiers of control system by their safety role:

| System Tier | Examples | DNV Requirements |
|-------------|----------|-----------------|
| **Safety systems** | ESD, F&G, HIPPS | Fail-safe, tested annually, independent of BPCS |
| **Control systems** | BPCS, DCS, SCADA | Standard industrial requirements + redundancy for critical loops |
| **Monitoring systems** | Historian, OPC, trending | No special requirements beyond marine grade |

**Independence requirement:** The ESD system must be demonstrably independent of the BPCS at the logic solver level. A single failure in the BPCS must not impair the ESD function. This is verified by DNV at FEED (front-end engineering design) stage through a functional safety assessment.

**Alarm management:** DNV requires an alarm philosophy document for all offshore process control systems. Alarm rationalisation (limiting alarm floods) is a required deliverable for class approval.

## 6. Safety systems — ESD and F&G interface

**ESD system structure (typical offshore platform):**

```
ESD Level 1 — Abandon Platform (AP)
  └─ ESD Level 2 — Emergency Shutdown (ESD): stop production, depressurize
       └─ ESD Level 3 — Process Shutdown (PSD): close wells, stop compression
            └─ ESD Level 4 — Local Shutdown: individual equipment protection
```

**DNV class notation for ESD:** Platforms may carry class notation `ESD` indicating the system has been independently assessed and meets DNV requirements. This requires:
- Cause and effect matrix reviewed and approved by DNV
- Factory acceptance test (FAT) witnessed by DNV surveyor
- Site acceptance test (SAT) on the platform
- Functional safety assessment (IEC 61511 FMEA/FTA or equivalent)

**Fire and Gas (F&G) system:**
- Gas detectors: catalytic bead or infrared, located per area classification
- Flame detectors: UV/IR combined, one-out-of-two voting typical for ESD activation
- Fire suppression: deluge (open-head sprinkler), CO₂ for enclosed machinery spaces, clean agent for control rooms
- F&G logic solver typically shares infrastructure with ESD logic solver (separate I/O modules, common hardware)

## 7. Class approval process — implications for engineering workflow

Understanding the DNV class approval timeline is essential for project planning:

| Stage | DNV Involvement | Deliverable |
|-------|----------------|-------------|
| FEED | Conceptual approval | Approval in principle (AiP) for ESD/F&G architecture |
| Detailed design | Drawing approval | Approved electrical drawings (single-line, area classification, cable schedule) |
| Procurement | Type approval check | Verify all major equipment has DNV type approval or equivalent |
| FAT | Witnessed testing | Surveyor witnesses ESD FAT, F&G FAT |
| SAT / Commissioning | On-board survey | Survey report issued; class notation confirmed |
| Annual | Audit inspection | Ex certificates current, periodic test records available |

**Engineer takeaway:** Engage DNV at FEED. Do not wait until detailed design to involve the class society — architecture changes required by DNV at detailed design stage are expensive to implement.

## 8. Change log

- 2026-03-09 — Initial draft: marine grade, power redundancy, hazardous area, ESD/F&G, class approval workflow.
