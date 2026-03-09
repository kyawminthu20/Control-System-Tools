<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S2
EDITION: S2-0200 (current revision)

INDEX_TAGS:
  topics: ["equipment_safety", "electrical_safety", "lockout_tagout", "chemical_safety", "emissions", "interlocks", "grounding"]
  systems: ["semiconductor_equipment", "process_equipment", "fab_equipment"]
-->

# SEMI S2 — Environmental, Health, and Safety Guideline for Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

SEMI S2 is the primary safety standard for semiconductor manufacturing equipment (tools). It covers the complete safety envelope: electrical, mechanical, chemical, radiation, and ergonomic hazards. For control engineers designing tool electrical systems, the electrical safety, interlock, grounding, and documentation sections are directly applicable. S2 compliance is required by most semiconductor fabs as a condition of equipment purchase.

## 1. Electrical safety requirements

### Grounding and bonding
- All conductive equipment surfaces accessible during operation must be grounded
- Ground continuity must be verified before each use if reconnected
- Equipotential bonding between all isolated conductive sections

### Isolation and lockout/tagout (LOTO)
- Equipment must provide means to isolate all energy sources (electrical, pneumatic, hydraulic)
- Lockout provisions: each energy isolation point must accept a padlock
- Stored energy: capacitors must discharge to <50 V within 5 seconds of isolation; or a discharge indicator and interlock must prevent access
- Tagout-only is not acceptable for primary energy isolation in most semiconductor fabs

### Overcurrent protection
- All circuits must be protected against overcurrent
- Branch circuit protection sized per the electrical code (NEC for US fabs)
- Ground fault protection required for circuits in wet/chemical environments

### High-voltage circuits (>50 V AC or >120 V DC)
- Must be enclosed and interlocked — access triggers interlock before opening
- Interlocks must de-energize before panels open; should not be defeatable without deliberate action
- Interlock bypass provisions must be labeled, limited to trained maintenance personnel, and self-resetting or requiring deliberate re-bypass

## 2. Interlock design requirements

S2 requires a risk assessment (typically per ISO 12100 or SEMI S10) to determine required interlock performance. Key requirements:

- Safety interlocks must be independent of the process control system where a single failure could cause injury
- Interlocks must fail to a safe state (de-energize, vent, or stop)
- Interlock status must be monitored — failures must be detected
- Manual reset required after safety interlock actuation (automatic restart prohibited for personnel safety interlocks)

## 3. Chemical and gas safety

Control engineers designing gas cabinet and chemical delivery control systems must address:
- Automatic shutoff valves (normally closed) on all toxic and flammable gas lines
- Pressure switches to detect line breaks and trigger automatic shutoff
- Exhaust flow monitoring — confirm exhaust is flowing before allowing process gas flow
- Gas detector integration — concentration alarms must trigger automatic shutoff and exhaust increase

## 4. Labeling and documentation

Required on every tool:
- Electrical service requirements (voltage, phases, frequency, current)
- Equipment grounding terminal identification
- Warning labels for all hazards (chemical, electrical, laser, RF, UV)
- Emergency stop location identification
- Lockout/tagout procedure posted or attached

Required documents shipped with tool:
- Electrical diagram (schematic)
- Safety interlock list and descriptions
- Hazardous materials inventory (chemicals, gases on tool)
- Installation and utilities requirements

## 5. Relationship to other standards

| Standard | Relationship |
|----------|-------------|
| IEC 60204-1 | International equivalent for machine electrical safety — S2 fabs often require both |
| ISO 12100 | Risk assessment methodology referenced by S2 |
| NFPA 79 | US electrical requirements for the tool — S2 fabs require NEC/NFPA 79 compliance |
| SEMI S14 | Fire risk assessment companion to S2 |
| SEMI S8 | Ergonomics companion to S2 |

## 6. Change log

- 2026-03-08 — Initial draft; electrical safety, LOTO, interlocks, chemical gas safety, labeling, related standards.
