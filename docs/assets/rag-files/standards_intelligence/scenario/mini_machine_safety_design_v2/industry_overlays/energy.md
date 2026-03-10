<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: energy
-->

# Energy Overlay

## What changes vs baseline

- Outdoor, corrosive, or utility-yard conditions may replace the baseline indoor assumption, so enclosure selection, temperature control, and contamination control become more demanding. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0. Environmental Considerations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause07__protection_of_equipment.md#2. Environmental Protection]
- If the skid shutdown functions are credited as independent protection layers for utility or process hazards, they shall move from machine-only documentation into a process-safety route. [LOCAL: routing/standards_applicability.md#Special Cases] [TO VERIFY: IEC 61511]
- Cybersecurity, remote access control, and event retention become more important because the skid is likely to connect into plant or utility monitoring systems; detailed cybersecurity controls are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82]

## Standards to prioritize

- Electrical baseline: NFPA 79, IEC 60204-1, NEC, and UL 508A where listing is needed. [LOCAL: routing/standards_applicability.md#Market-Based Selection] [LOCAL: crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md#Use Cases]
- Process safety route for credited shutdowns: NOT FOUND IN LOCAL CORPUS - TO VERIFY. [LOCAL: _index.yaml#regional_routing] [TO VERIFY: IEC 61511] [TO VERIFY: IEC 61508]
- Cybersecurity route: NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82]

## Typical inspection or acceptance artifacts

- Site fault-current and grounding basis. [LOCAL: us/nec/NEC_2023__Art409__industrial_control_panels.md#2. Short-circuit current rating (SCCR)] [LOCAL: us/nec/NEC_2023__Art250__grounding_and_bonding.md#1. Equipment Grounding Conductors (EGC)]
- Environmental rating and heater or cooler sizing record. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#2. Enclosure Implications]
- Shutdown cause-and-effect and proof-test plan if process credit is taken. [TO VERIFY: IEC 61511]
- Remote access and network zoning record. [TO VERIFY: IEC 62443]
