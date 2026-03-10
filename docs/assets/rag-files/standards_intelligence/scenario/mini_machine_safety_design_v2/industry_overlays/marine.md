<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: marine
-->

# Marine Overlay

## What changes vs baseline

- Vessel power systems, vibration, and salt exposure may change disconnect, bonding, and enclosure assumptions from the baseline industrial floor model. Local corpus supports only general machinery electrical guidance. [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Regional Considerations] [TO VERIFY: marine standard]
- Bonding and EMC become more critical because of long cable runs and vessel interference sources. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause08__equipotential_bonding.md#2. Noise vs. Safety Bonding]
- Marine documentation, inspections, and class approvals are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: marine classification standard]

## Standards to prioritize

- IEC 60204-1 remains the closest local electrical baseline for international marine machinery, but marine class rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Overview] [TO VERIFY: marine classification standard]
- Add marine power, grounding, and environmental rules externally. [TO VERIFY: marine standard]
- Add cybersecurity guidance if bridge or ship systems are connected. [TO VERIFY: IEC 62443]

## Typical inspection or acceptance artifacts

- Vessel power-interface drawing. [TO VERIFY: marine standard]
- Bonding continuity and shield-termination inspection record. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause08__equipotential_bonding.md#2. Noise vs. Safety Bonding]
- Class-approval submittal or gap register. [TO VERIFY: marine classification standard]
- Corrosion and ingress-protection evidence. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause07__protection_of_equipment.md#2. Environmental Protection]
