<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Safety Integrity and SIL Strategy

## Local-Corpus Boundary

The local corpus supports the high-level standards-selection logic for machinery PL/SIL and process SIL, but it does not contain the detailed calculation methods, risk graphs, LOPA rules, or proof-test equations needed to finalize target integrity levels. Those detailed methods are therefore marked `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [LOCAL: _standards_map.md#market-based-selection] [LOCAL: _glossary.md#p] [LOCAL: _glossary.md#s]

## Which Integrity Model Applies

### Machinery Safety Functions

For safety functions tied to discrete machinery hazards such as emergency stop, guard interlocking, unexpected restart prevention, and hazardous motion shutdown, the machine shall use a machinery functional-safety method:

- `ISO 13849-1` for Performance Level (`PL`) allocation, or
- `IEC 62061` for machinery SIL allocation. [LOCAL: _standards_map.md#market-based-selection] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#safety-framework]

For international or CE-oriented machinery, IEC 60204-1 is the electrical implementation layer and must be paired with ISO 12100 plus ISO 13849-1 or IEC 62061. [LOCAL: international/machinery/iec_60204_1/IEC60204_OVERVIEW.md#integration-with-other-isoiec-standards] [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#dual-compliance-strategy]

### Process Safety Functions

For safety functions whose purpose is to maintain a safe process condition rather than to stop machine motion, the project shall evaluate whether the function belongs in a process-safety framework under IEC 61511 with IEC 61508 as the foundation. [LOCAL: _standards_map.md#applicability-matrix-by-project-type] [LOCAL: _standards_map.md#special-cases]

Examples include:

- chemical overfill prevention where release consequence dominates
- process pressure shutdown where downstream plant risk dominates
- shutdown functions integrated into a broader site SIS

Detailed IEC 61511 lifecycle, SRS, LOPA, and SIL-verification methods are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: IEC 61511] [TO VERIFY: IEC 61508]

## Decision Rules

1. A safety function shall be classified as a machinery safety function when the hazard is hazardous motion, access to moving equipment, or machine electrical behavior. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2-emergency-stop-concepts]
2. A safety function shall be classified as a process safety function when the primary risk is loss of containment, unsafe process state, or plant-level chemical/process consequence rather than direct machine motion. This classification logic is locally indicated but detailed criteria are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: _standards_map.md#applicability-matrix-by-project-type] [TO VERIFY: IEC 61511]
3. Safety-related software claims shall follow the applicable software lifecycle route, and `IEC 61131-3` alone shall not be treated as a SIL or PL claim basis. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#PLC Language Standard vs Safety Claim Standard] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Safety PLC Software And SIL]
4. The project shall not mix undocumented PL and process-SIL methodologies inside a single safety-function claim; if a function spans both domains, it shall be decomposed into separate, traceable subfunctions. [LOCAL: _standards_map.md#market-based-selection] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 61511]
5. Each safety function shall be documented with initiators, sensors, logic solver, final elements, safe state, restart behavior, and verification tests. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
6. Reset of any safety function shall not restart the machine; reset shall only permit a separate deliberate start action. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause03__terms_and_definitions.md#2-common-misinterpretations]

## PL vs SIL Selection Guidance

| Use Case                                                                                    | Preferred Model                            | Why                                                                                                                                                          | Local Basis                                                                              |
| ------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| E-stop, guard interlock, restart inhibit, drive STO, hydraulic motion shutdown on a machine | PL or machinery SIL                        | These are machinery safety functions connected to access and motion.                                                                                         | [LOCAL: _standards_map.md#market-based-selection]                                        |
| Chemical overfill shutdown on a stand-alone machine skid with no separate SIS               | PL or machinery SIL initially, then review | If the function primarily protects the machine and local operators, a machinery method may be sufficient pending project review. Detailed rule is TO VERIFY. | [LOCAL: _standards_map.md#applicability-matrix-by-project-type] [TO VERIFY: ISO 13849-1] |
| Chemical release prevention tied to plant SIS or process consequence                        | Process SIL                                | This is process-industry functional safety territory.                                                                                                        | [LOCAL: _standards_map.md#applicability-matrix-by-project-type]                          |
| International/CE machinery                                                                  | PL or machinery SIL plus ISO 12100         | Local corpus explicitly pairs IEC 60204-1 with ISO 12100 and ISO 13849-1 or IEC 62061.                                                                       | [LOCAL: crosswalks/overlap_matrix/nfpa79_iec60204_overlap.md#safety-framework]           |

## How To Document Safety Functions

The project safety-function record shall include:

- function identifier
- hazard addressed
- demand source / initiators
- sensing path
- logic solver
- final elements
- safe state
- reset and restart behavior
- provisional target PL/SIL where assigned
- proof-test and functional-test concept
- FAT/SAT and maintenance verification references [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests] [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]

## Example Target Selection

The table below provides provisional example targets only. Final targets are NOT FOUND IN LOCAL CORPUS – TO VERIFY and must be confirmed by a formal risk assessment and the chosen safety method.

| Safety Function                                       | Domain                                                                     | Provisional Example Target                                                                     | Rationale                                                                                                                                                                                                                                                                                                                    | Method Status                                                                                                                                          |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Emergency stop                                        | Machinery                                                                  | `PL d or SIL 2`                                                                                | Highest-priority stop that overrides all modes and shall not restart on reset. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2-emergency-stop-concepts] | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061]                                                                 |
| Guard interlock                                       | Machinery                                                                  | `PL d or SIL 2`                                                                                | Loss of guarding can expose personnel to hazardous motion. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause03__terms_and_definitions.md#0-key-definitions-for-control-engineers]                                                                                                                          | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 13849-1]                                                                                        |
| Hydraulic overpressure protection interlock           | Machinery or process, depending on consequence                             | `PL c/PL d or SIL 1`                                                                           | If the function protects personnel from line rupture or actuator over-force, treat as safety-related; if it is only equipment protection, it may remain non-safety.                                                                                                                                                          | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 61511]                                           |
| Hydraulic dump / stored-energy release on safety trip | Machinery                                                                  | `PL d or SIL 2`                                                                                | Safety demand should remove motive energy and move hydraulic system to the defined safe state.                                                                                                                                                                                                                               | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413] [TO VERIFY: IEC 62061]                                                                    |
| Chemical pump overfill / overdose prevention          | Process if release consequence dominates; otherwise machine/process hybrid | `SIL 1` provisional for process use, or `PL c/PL d` provisional for machine-contained skid use | Function classification depends on whether the machine is acting as part of a process safety instrumented function.                                                                                                                                                                                                          | NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: _standards_map.md#applicability-matrix-by-project-type] [TO VERIFY: IEC 61511] [TO VERIFY: ISO 13849-1] |

## Methods Missing From The Local Corpus

The following detailed methods are required to close the integrity strategy but are not present locally:

- ISO 12100 hazard estimation steps [TO VERIFY: ISO 12100]
- ISO 13849-1 category, MTTFd, DCavg, and PL calculation rules [TO VERIFY: ISO 13849-1]
- IEC 62061 SIL claim limits, PFHd allocation, and subsystem constraints [TO VERIFY: IEC 62061]
- IEC 61511 hazard and risk assessment, LOPA, SRS, and proof-test coverage rules [TO VERIFY: IEC 61511]

Until those items are closed, all integrity targets in this package are provisional engineering placeholders rather than release-ready compliance claims.
