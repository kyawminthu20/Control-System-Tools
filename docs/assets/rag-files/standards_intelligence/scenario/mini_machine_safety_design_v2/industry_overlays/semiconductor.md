<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: semiconductor
-->

# Semiconductor Overlay

## What changes vs baseline

- Chemical compatibility, leak containment, purge logic, and clean-material selection become higher priority than in the baseline skid; the local corpus does not contain SEMI or semiconductor chemical-handling standards, so these controls are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: SEMI standards] [TO VERIFY: chemical handling standard]
- Single-point ground and EMC discipline become more stringent because the skid will likely coexist with sensitive instrumentation and networked tooling. The local corpus supports PE and functional-ground separation only at a general level. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause08__equipotential_bonding.md#2. Noise vs. Safety Bonding] [TO VERIFY: semiconductor EMC standard]
- Documentation and interlock validation shall be deeper than baseline because tool integration often requires interface qualification and host handshake records. Local corpus supports documentation structure, but semiconductor acceptance artifacts are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations] [TO VERIFY: SEMI standards]

## Standards to prioritize

- Keep the electrical baseline: NFPA 79, IEC 60204-1, NEC, and UL 508A overlap as applicable. [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Dual-Compliance Strategy] [LOCAL: crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md#Use Cases]
- Add semiconductor-specific equipment, EHS, and interface standards; these are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: SEMI S2] [TO VERIFY: SEMI S8] [TO VERIFY: SEMI standards]
- Add functional safety and formal risk assessment standards because local modules are not populated. [LOCAL: _index.yaml#standards] [TO VERIFY: ISO 12100] [TO VERIFY: ISO 13849-1]

## Typical inspection or acceptance artifacts

- Chemical P and ID with valve lineup and spill sensors. [TO VERIFY: semiconductor chemical standard]
- Tool interface and interlock cause-and-effect matrix. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations]
- EMC bonding layout and cable segregation record. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause08__equipotential_bonding.md#2. Noise vs. Safety Bonding]
- SEMI compliance checklist or gap register. [TO VERIFY: SEMI standards]
