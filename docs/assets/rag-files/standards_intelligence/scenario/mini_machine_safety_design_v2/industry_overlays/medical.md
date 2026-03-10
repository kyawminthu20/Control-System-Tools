<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
INDUSTRY: medical
-->

# Medical Overlay

## What changes vs baseline

- Validation, software change control, audit trail, and electronic-record integrity requirements are usually much stricter than the baseline machine package. Those detailed rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: 21 CFR Part 11] [TO VERIFY: medical device validation standard]
- Dose accuracy, alarm escalation, user access, and batch or patient record retention may require regulated workflows beyond ordinary historian logging. [TO VERIFY: 21 CFR Part 11] [TO VERIFY: ISA-18.2]
- The local baseline remains useful for electrical safety, E-stop behavior, bonding, and documentation structure. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2. Emergency Stop Concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2. Documentation Set]

## Standards to prioritize

- Add regulated e-record and validation standards externally because they are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: 21 CFR Part 11] [TO VERIFY: medical device validation standard]
- Keep NEC, NFPA 79, and IEC 60204-1 for electrical and machinery baseline as applicable. [LOCAL: routing/standards_applicability.md#Market-Based Selection]
- Add cybersecurity and user-account controls externally if networked logging is used. [TO VERIFY: IEC 62443]

## Typical inspection or acceptance artifacts

- Software validation plan and executed test evidence. [TO VERIFY: medical device validation standard]
- Audit-trail and user-access specification. [TO VERIFY: 21 CFR Part 11]
- Calibration and dose-accuracy records for chemical pumps. [TO VERIFY: medical device validation standard]
- Turnover package with schematics, IO list, and interlock matrix. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations]
