<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: offshore
-->

# Offshore Overlay

## What changes vs baseline

- The baseline package assumes a non-offshore environment. Local NFPA 79 content explicitly excludes fixed offshore platforms, so offshore projects require an external standards layer before design freeze. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1. Applicability Rules] [TO VERIFY: offshore standard]
- Salt fog, vibration, compact spaces, and corrosion drive enclosure, bonding, and cable-routing decisions harder than the baseline. Local corpus supports environment and bonding at a general level only. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0. Environmental Considerations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause08__equipotential_bonding.md#1. Bonding Strategy]
- Recordkeeping, inspection, and maintenance intervals are typically more formal offshore; detailed offshore lifecycle requirements are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: offshore standard]

## Standards to prioritize

- Offshore electrical and marine class rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: offshore standard] [TO VERIFY: marine classification standard]
- Keep IEC 60204-1 or NFPA 79 only for the portions still valid as machine electrical practice. [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Topic-Based Overlap Matrix]
- Add cybersecurity and remote-maintenance controls if the skid connects offshore to central systems. [TO VERIFY: IEC 62443]

## Typical inspection or acceptance artifacts

- Corrosion-protection and enclosure-material schedule. [TO VERIFY: offshore standard]
- Bonding and cable-support inspection record. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause08__equipotential_bonding.md#1. Bonding Strategy]
- Platform integration, disconnect, and shutdown interface matrix. [TO VERIFY: offshore standard]
- Maintenance and inspection interval register. [TO VERIFY: offshore standard]
