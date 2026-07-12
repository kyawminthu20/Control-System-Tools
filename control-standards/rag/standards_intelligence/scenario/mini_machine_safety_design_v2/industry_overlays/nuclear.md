<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: nuclear
-->

# Nuclear Overlay

## What changes vs baseline

- Nuclear work usually drives a higher bar for QA traceability, configuration control, software validation, and component pedigree than the baseline package. These rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: nuclear QA standard]
- Separation, redundancy, seismic qualification, and records retention may exceed normal machine-control practice; these criteria are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: nuclear standard]
- The local baseline still helps for electrical workmanship, disconnects, grounding, and machine documentation, but it is not sufficient alone. [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#0. Scope and relevance to control panels] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations]

## Standards to prioritize

- Nuclear QA, software, and component qualification standards are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: nuclear QA standard] [TO VERIFY: nuclear standard]
- Keep NEC, NFPA 79, and IEC 60204-1 for general electrical and machinery structure only. [LOCAL: routing/standards_applicability.md#Market-Based Selection]
- Add formal functional safety or protection-system requirements externally as required by the project. [TO VERIFY: IEC 61508] [TO VERIFY: nuclear safety standard]

## Typical inspection or acceptance artifacts

- Configuration management and software revision log. [TO VERIFY: nuclear QA standard]
- Component pedigree and traceability dossier. [TO VERIFY: nuclear standard]
- Enhanced verification matrix with witness points. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause18__verification.md#0. Purpose]
- QA hold-point schedule. [TO VERIFY: nuclear QA standard]
