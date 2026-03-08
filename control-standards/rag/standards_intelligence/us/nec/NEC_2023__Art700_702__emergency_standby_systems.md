<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "700"
  article_title: "Emergency Systems / Legally Required Standby / Optional Standby"

INDEX_TAGS:
  topics: ["emergency_systems", "standby_power", "transfer_switch", "generator", "UPS", "safety_systems"]
  systems: ["emergency_lighting", "fire_alarm", "safety_PLC", "process_safety"]
-->

# NEC 2023 — Articles 700–702 — Emergency and Standby Systems

## 0. Why these articles matter for control engineers

Safety PLCs, emergency ventilation, fire suppression controls, and process shutdown systems often require power that remains available during a utility outage. Articles 700–702 define three tiers of backup power with different requirements for transfer time, testing, and supervision. Control engineers must identify which tier applies to their system to specify the correct power infrastructure.

## 1. Three-tier system overview

| Article | System Type | Authority Requiring It | Examples |
|---------|-------------|----------------------|---------|
| **700** | Emergency Systems | Government code (legally required) | Egress lighting, exit signs, fire alarm power, elevator recall |
| **701** | Legally Required Standby | Government code (legally required) | HVAC for occupied spaces, sewage disposal, industrial processes required by law |
| **702** | Optional Standby | Owner's choice (not legally required) | Data center UPS, production continuity, SCADA backup power |

## 2. Article 700 — Emergency Systems

**Transfer time:** Emergency systems must transfer to backup supply within **10 seconds** of normal power loss (700.12).

**Acceptable power sources (700.12):**
- Storage batteries (with automatic charger)
- Generator (10-second requirement is a challenge; most generators take 10–15s to reach rated voltage)
- UPS — satisfies 10-second requirement and provides seamless transfer
- Separate service from the utility (where the utility can guarantee independence)

**Wiring requirements:**
- Emergency wiring must be kept **entirely independent** of all other wiring. No shared conduit, enclosures, or junction boxes with normal or standby wiring.
- Exception: Transfer switches and exit fixtures where the emergency wiring terminates.

**Testing:** Emergency systems require:
- Monthly functional tests
- Annual 90-minute full-load tests
- Written records of all tests kept by the owner

**Relevance to control systems:** Fire alarm panels, emergency egress lighting, and life safety systems fall under Art. 700. Their power supplies, conduit, and panel sections must be segregated from the normal power system.

## 3. Article 701 — Legally Required Standby Systems

**Transfer time:** Within **60 seconds** of normal power loss (less stringent than Art. 700).

**Acceptable power sources:** Same as Art. 700. Generators can typically meet the 60-second requirement with proper sequencing controls.

**Wiring:** May share wiring infrastructure with normal systems in some conditions (less strict separation than Art. 700), but must be identified.

**Applications in industrial control:**
- Sewage lift station controls required by environmental permit
- Ventilation for occupied industrial spaces
- Process systems where legal or permit requirements mandate continuity

## 4. Article 702 — Optional Standby Systems

**Transfer time:** No specific requirement; owner determines acceptable outage duration.

**Applications in industrial control:**
- SCADA server power backup
- PLC rack power supply redundancy
- Continuous process systems where production loss (not safety) is the concern
- Data logging and historian systems

**Design note:** Many industrial facilities use Art. 702 UPS systems for control system power, plus Art. 700/701 for legally required systems. The UPS provides seamless transfer for control system continuity; the generator provides extended backup capacity for the UPS and for Art. 700/701 loads after UPS battery depletion.

## 5. Transfer switches

**Automatic Transfer Switch (ATS):** Senses loss of normal power and automatically transfers loads to backup supply. Required for Art. 700 and 701 systems.

**Manual Transfer Switch:** Operator-initiated transfer. Permitted only for Art. 702 (optional standby).

**Transfer switch ratings:**
- Must be rated for the connected load
- Must be rated for available fault current at the installation point
- ATS must indicate the power source currently supplying the load

**Bypass-Isolation Transfer Switch:** Allows maintenance on the ATS while loads remain powered through a bypass path. Recommended for critical industrial applications.

## 6. Safety system power — relevance to functional safety

For safety PLCs and SIL-rated safety instrumented systems:

- Power supply redundancy is often a requirement of the safety lifecycle (IEC 61511)
- The power source classification (Art. 700, 701, or 702) must match the demand of the safety function
- A SIL 2 or SIL 3 safety system requiring power during emergency shutdown may need Art. 700 or 701 power infrastructure
- UPS systems must have sufficient battery runtime to cover the required safe state duration

Coordinate the electrical power architecture (Art. 700–702) with the functional safety architecture (IEC 61511 / ISO 13849) during the design phase.

## 7. Change log

- 2026-03-08 — Initial draft; three-tier structure, transfer time requirements, safety system power coordination.
