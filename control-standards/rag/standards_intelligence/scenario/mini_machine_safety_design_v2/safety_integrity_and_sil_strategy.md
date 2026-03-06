<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN_V2
-->

# Safety Integrity and SIL Strategy

## Local-corpus boundary

The local corpus supports the electrical implementation and control-behavior side of safety functions through NFPA 79, IEC 60204-1, NEC, and crosswalk files. It does not contain populated local modules for ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, or IEC 61511. This file therefore provides routing logic and documentation rules, while detailed target determination methods are marked `NOT FOUND IN LOCAL CORPUS - TO VERIFY`. [LOCAL: _index.yaml#standards] [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Integration with Other ISO/IEC Standards]

## Which integrity model applies

| Use case                                                                                                                              | Integrity model to use                                                                        | Local basis                                                                                                                                                                                                                                                               | Gap status                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Motion, guarding, E-stop, operator-access protection on a machine                                                                     | PL route via ISO 13849-1 or machine SIL route via IEC 62061                                   | Local corpus routes machinery safety functions to those standards and requires electrical implementation through IEC 60204-1 or NFPA 79. [LOCAL: _index.yaml#topic_routing] [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#Typical Safety Architecture] | Detailed methods NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061]                                        |
| Process-style prevention of loss of containment, overfill, overdosing, or independent shutdown layers in energy or petroleum contexts | SIL route via IEC 61511 on top of IEC 61508 foundation                                        | Local corpus routes process industry safety to IEC 61511 and IEC 61508. [LOCAL: routing/standards_applicability.md#Special Cases] [LOCAL: _index.yaml#regional_routing]                                                                                                           | Detailed SIS lifecycle methods NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: IEC 61511] [TO VERIFY: IEC 61508]                            |
| Dual-market machine sold as machinery, not as a formal SIS package                                                                    | Electrical behavior per NFPA 79 and IEC 60204-1, target integrity by ISO 13849-1 or IEC 62061 | Local crosswalk recommends designing to both electrical standards and pairing with machine safety standards. [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#Dual-Compliance Strategy]                                                                       | Detailed target selection method NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 12100] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] |

## Decision rules

1. The project shall classify each protective function as either a machine safety function or a process safety function before assigning architecture, validation method, and records. [LOCAL: routing/standards_applicability.md#Special Cases] [LOCAL: _index.yaml#regional_routing]
2. A machine safety function shall remain effective regardless of the state of the standard PLC or HMI and shall be implemented in a safety-rated controller or equivalent safety-related control path. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3. Safety vs. Standard Control Separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3. Safety vs. Standard Control Separation]
3. Safety-related software claims shall follow the applicable software lifecycle route, and `IEC 61131-3` alone shall not be treated as a SIL or PL claim basis. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#PLC Language Standard vs Safety Claim Standard] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Safety PLC Software And SIL]
4. Reset of an E-stop, guard interlock, or equivalent trip shall not restart the machine and shall only permit restart after a separate deliberate action. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2. Emergency Stop Concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2. Emergency Stop Concepts]
5. Each documented safety function shall identify initiators, sensors, logic solver, final elements, safe state, reset behavior, and validation tests. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1. Required Tests] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2. Documentation Set]
6. If a chemical overfill, overdose, or spill-prevention function is credited as an independent protection layer for a process-industry project, the project shall treat that function as a process safety function and complete external IEC 61511 verification. [LOCAL: routing/standards_applicability.md#Special Cases] [TO VERIFY: IEC 61511]
7. Selection of target PL or SIL, use of risk graphs, and use of LOPA are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 12100] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] [TO VERIFY: IEC 61511]

## Example safety function documentation content

Each safety function record should contain at minimum:

- unique ID
- hazard addressed
- initiating event or demand source
- sensors and diagnostics
- logic solver type
- final elements and safe state
- manual reset rule
- verification test
- candidate target PL or SIL and rationale
- proof test or periodic validation concept

The local basis for the structure above comes from the local documentation and verification expectations, not from populated local PL or SIL methodology modules. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#0. Purpose]

## Example target selection for this scenario

These are engineering starting points only. They are not normative targets because the local corpus does not contain the formal target-assignment method.

| Function                                      | Machinery route candidate                                 | Process route candidate                                                                                  | Why this is a reasonable starting point                                                                                                                                                                                                                                                                                                                                                                      | Status                                                                                                     |
| --------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Emergency stop master function                | Candidate PL d or SIL 2 [TO VERIFY]                       | Usually remains machine safety, not process SIS                                                          | E-stop is the highest-priority command and must override all modes without restart on reset. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2. Emergency Stop Concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2. Emergency Stop Concepts]                                                                 | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] |
| Guard interlock function                      | Candidate PL d or SIL 2 [TO VERIFY]                       | Usually not a process SIS                                                                                | Guard opening directly exposes personnel to motion or pressure hazards and shall remain independent of standard control logic. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3. Safety vs. Standard Control Separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3. Safety vs. Standard Control Separation] | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1]                        |
| Hydraulic overpressure protection interlock   | Candidate PL c to PL d [TO VERIFY]                        | Candidate SIL 1 [TO VERIFY] if credited for containment or pressure hazard mitigation in process service | Local electrical corpus supports trip behavior and safe-state logic, but hydraulic sizing and pressure-layer allocation are external. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1. Start/Stop Behavior] [TO VERIFY: ISO 4413] [TO VERIFY: IEC 61511]                                                                                                                    | Formal allocation NOT FOUND IN LOCAL CORPUS - TO VERIFY.                                                   |
| Chemical pump overfill or overdose prevention | Candidate PL c [TO VERIFY] if treated as machine function | Candidate SIL 1 to SIL 2 [TO VERIFY] when credited as process IPL                                        | Overfill and overdose can be ordinary machine interlocks or formal SIS functions depending on consequence severity and independence requirements. [LOCAL: routing/standards_applicability.md#Special Cases] [TO VERIFY: IEC 61511] [TO VERIFY: chemical handling standard]                                                                                                                                           | Formal allocation NOT FOUND IN LOCAL CORPUS - TO VERIFY.                                                   |

## Documentation outputs that shall exist regardless of chosen integrity model

1. Safety function register with architecture and safe-state definition shall exist. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations]
2. Cause and effect or equivalent interlock narrative shall exist for machine stop, hydraulic trip, and chemical containment trip paths. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2. Documentation Expectations]
3. Validation or verification records shall exist for continuity, insulation, functional tests, and safety-function operation. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1. Required Tests] [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#2. Final Compliance Alignment]
