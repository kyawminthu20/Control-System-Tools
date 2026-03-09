<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: ABS_OFFSHORE
STANDARD_ID: ABS_OFFSHORE_ELECTRICAL
EDITION: 2023

ABS_HIERARCHY:
  document: "ABS Rules — Offshore Installations, Part 4"
  document_title: "Electrical Installations on Offshore Units"

INDEX_TAGS:
  topics: ["ABS_class", "marine_grade", "power_redundancy", "hazardous_area", "ESD", "F&G", "cable_requirements"]
  systems: ["offshore_platform", "FPSO", "MODU", "ESD", "fire_and_gas"]
-->

# ABS — Offshore Electrical Installations (Part 4)

## 0. Why this matters for control engineers

ABS (American Bureau of Shipping) is the primary US-headquartered classification society for offshore units. Where DNV is dominant in the North Sea, ABS is common for US Gulf of Mexico and US-flagged vessels. ABS Rules for Building and Classing Offshore Installations, Part 4, covers electrical systems in a structure parallel to DNV-OS-D201. Key differences from onshore standards: class approval authority, marine-grade requirements, and power redundancy classifications are all ABS-specific.

## 1. ABS class notations relevant to control engineers

ABS assigns class notations that describe the capabilities of safety-critical systems. Engineers must design to the notation specified in the contract:

| Notation | Meaning |
|----------|---------|
| **DP-2** | Dynamic positioning — two independent thrusters; loss of one not to cause loss of position |
| **DP-3** | Dynamic positioning — redundancy across fire/flood boundaries |
| **ESD** | Emergency shutdown system independently assessed by ABS |
| **AFLS** | Automatic fire and flooding detection and alarm system |
| **SPS** | Safety protection system — ESD + F&G integrated, ABS assessed |

## 2. Equipment approval: type approval vs. project-specific approval

ABS maintains a list of type-approved equipment. Using type-approved equipment streamlines class approval:

**Type-approved equipment:**
- Listed in ABS type approval database
- Certificate valid for 3–5 years (varies by equipment type)
- Accepted without individual review for standard applications

**Project-specific approval:**
- Required for novel configurations or equipment not in type approval database
- Requires submission of drawings, calculations, and test reports
- ABS plan approval takes 4–8 weeks depending on complexity

**Practical implication:** Specify only type-approved PLCs, safety relay modules, switchgear, and cable for offshore projects. Using non-approved equipment adds significant approval time and cost.

## 3. Marine electrical requirements (Part 4 key requirements)

**Cable:**
- Fire-resistant cables: must maintain circuit integrity at 750°C for 3 hours (IEC 60331) for ESD, F&G, emergency power, and fire pump circuits
- LSOH (halogen-free): required throughout — IEC 60332-3-22 or IEC 60754-1
- Minimum cable cross-section: 1.5 mm² copper for control circuits (higher mechanical robustness than onshore)
- Cable routing: ESD and F&G cables routed separately from process cables where practicable; fire-rated cables for safety functions

**Switchgear and control panels:**
- Rated for marine environment: IP56 for exposed locations, IP54 minimum for enclosed machinery spaces
- Main switchboard: draw-out or bolt-in breakers only (plug-in type not permitted)
- Control panels: natural convection preferred over forced cooling where ambient allows (fan failure offshore is harder to detect/correct)

**Earthing (grounding):**
- Insulated system (IT): offshore vessels and platforms use an insulated neutral (no earth return) — this is a critical difference from onshore TN-S systems
- First earth fault: monitored but does not trip — alarm only; a second fault causes trip
- Consequence for control engineers: earth fault monitoring must be installed on all distribution panels; nuisance trips from single earth faults indicate insulation degradation, not a safety hazard in itself

## 4. Insulated neutral system — practical implications

The IT (insulated neutral) earthing system used offshore has significant implications for control circuit design:

**What changes:**
- 24 VDC control circuits: positive and negative rails are both isolated from earth
- Earth fault on one rail: system continues operating; earth fault relay alarms
- Earth fault on both rails simultaneously: circuit fails; this is the designed protection mechanism

**What engineers must do differently:**
- Never connect control circuit 0 V to earth as a design practice (as is common onshore)
- Earth fault monitoring relay required on each isolated bus segment
- Specify earth fault monitoring on all UPS output circuits
- Document isolated earth architecture in the electrical design philosophy

## 5. Hazardous area: ABS requirements

ABS accepts IECEx, ATEX, or ABS-specific type approval for Ex equipment. On US-flagged vessels, FM or UL listed equipment is also accepted.

**Classification:** ABS accepts IEC 60079-10-1 (gas zone classification) and NFPA 497 (Division classification) — verify which system is specified in the project contract.

**Inspection:** ABS conducts Ex equipment walkdowns at commissioning and class renewal. All Ex certificates, installation records, and IS loop calculation sheets must be on file and available to the surveyor.

## 6. Emergency power requirements (Part 4, Section 3)

| System | Minimum Autonomy | Power Source |
|--------|-----------------|-------------|
| Emergency lighting | 18 hours | Emergency generator or battery |
| ESD logic solver | 30 minutes | UPS (battery) |
| F&G system | 30 minutes | UPS (battery) |
| Emergency communications | 18 hours | Dedicated battery or generator |
| Fire pump | Duration of hazard | Emergency generator (auto-start) |

**Emergency generator auto-start:** Must start and accept full load within 45 seconds of main power failure (ABS; DNV requires 30 seconds — use the more stringent value when dual classing is possible).

## 7. ABS class approval: what to submit and when

| Design Stage | Submission | ABS Review |
|-------------|-----------|-----------|
| Concept | Safety philosophy, ESD cause and effect (draft) | Approval in Principle (AiP) |
| Detailed design | Single-line diagrams, switchboard drawings, cable schedules, area classification drawing | Drawing approval (stamped drawings) |
| Equipment | Type approval certificates or test reports for major items | Plan approval update |
| FAT | Witness request | ABS surveyor attends FAT |
| Commissioning | Commissioning records, test certificates | Survey report + class notation |

**ABS plan approval fees and timelines vary** — engage ABS project manager early. Target submission at 30% detailed design to allow comment turnaround before drawings are finalized.

## 8. Change log

- 2026-03-09 — Initial draft: class notations, marine electrical requirements, IT earthing system, hazardous area, emergency power, class approval workflow.
