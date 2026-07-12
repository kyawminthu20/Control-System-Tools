<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
SCENARIO_TITLE: Mini Machine Safety Design
SOURCE_SCOPE: local standards_intelligence corpus only
-->

# Mini Machine Safety Design Scenario

## Scenario summary

This package defines a small fluid-handling machine concept that combines:

- one hydraulic power unit (HPU) with two hydraulic actuator circuits
- two chemical dosing pumps with local containment and spill sensing
- one local HMI panel plus historian or logger connection
- one electrical control panel with machine disconnect, control power, PLC, safety logic, and network equipment
- mechanical shutoff and bleed points for hydraulic and chemical circuits
- electrical isolation points for incoming power, motor drives, and service work

Intended use:

- skid-mounted machine module for dosing, clamping, lifting, positioning, or utility-fluid support
- adaptable for semiconductor, energy, petroleum, offshore, marine, nuclear, commercial, food and beverage, and medical projects through overlay files
- baseline electrical design aligned to US and international machinery practice using NFPA 79, NEC, IEC 60204-1, and local crosswalk guidance [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Dual-Compliance Strategy] [LOCAL: crosswalks/overlap_matrix/ul508a_nec_nfpa79_overlap.md#Conflict Resolution]

Primary hazard themes:

- unexpected startup or restart
- hydraulic stored energy and pressure release
- chemical overfill, spill, or exposure
- pinch, crush, and motion hazards
- electric shock, residual voltage, and arc flash exposure
- loss of control integrity across integrated panels or networks [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0. Control Philosophy] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause06__protection_against_electric_shock.md#1. Protective Measures] [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#1. Installation & listing requirements (field rules)]

Environments assumed by the baseline:

- indoor industrial
- non-classified area
- non-offshore location
- non-medical-record regulated logging

Anything beyond that baseline is pushed into the overlay files and marked `NOT FOUND IN LOCAL CORPUS - TO VERIFY` where the local corpus does not contain the governing standard content. [LOCAL: us/nfpa79/NFPA79_2024__Ch01__administration.md#1. Applicability Rules]

## How to use this package

1. Start with [system_description.md](./system_description.md) to understand the machine concept and subsystem boundaries.
2. Use [standards_applicability_matrix.md](./standards_applicability_matrix.md) to determine which standards paths are supported locally and which require external verification.
3. Build project requirements from [ul_nec_design_requirements.md](./ul_nec_design_requirements.md), [hazards_and_risk_assessment.md](./hazards_and_risk_assessment.md), [safety_functions_register.md](./safety_functions_register.md), [control_architecture_and_network.md](./control_architecture_and_network.md), and [mechanical_and_electrical_isolation.md](./mechanical_and_electrical_isolation.md).
4. Apply the relevant industry delta file in [industry_overlays/](./industry_overlays/).
5. Use [verification_and_validation_plan.md](./verification_and_validation_plan.md) and [requirements.yaml](./requirements.yaml) to drive FAT, SAT, and acceptance records.

## Traceability approach

This package uses two citation forms:

- Local source present: `[LOCAL: <relative_path_from_standards_intelligence>/<file>#<heading>]`
- Local source missing: `[TO VERIFY: <standard_name>]`

Rules used in this package:

- every standards-driven `shall` statement carries one or more trace tags
- local citations only point to content under `control-standards/rag/standards_intelligence/`
- if a topic appears in the local master index but the detailed module is not populated, the package states `NOT FOUND IN LOCAL CORPUS - TO VERIFY` and does not invent requirements [LOCAL: _index.yaml#standards] [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Integration with Other ISO/IEC Standards]

## Local corpus limits that affect this scenario

- Local, substantive guidance exists for NFPA 79, NEC, IEC 60204-1, and the crosswalk modules. [LOCAL: _index.yaml#standards] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Topic-Based Overlap Matrix]
- UL 508A is locally present mainly as module overview, index, and overlap guidance; detailed section content is largely scaffolded. [LOCAL: us/ul_508a/UL508A_OVERVIEW.md#Content Development Status] [LOCAL: us/ul_508a/_index.yaml#notes]
- Functional safety, process safety, hydraulics, cybersecurity, alarm management, e-record, and industry-specific standards are mostly absent as detailed local content and are flagged `TO VERIFY`. [LOCAL: _index.yaml#standards] [TO VERIFY: ISO 12100] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] [TO VERIFY: IEC 61508] [TO VERIFY: IEC 61511] [TO VERIFY: ISO 4413] [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] [TO VERIFY: ISA-18.2] [TO VERIFY: ISA-101] [TO VERIFY: 21 CFR Part 11]
