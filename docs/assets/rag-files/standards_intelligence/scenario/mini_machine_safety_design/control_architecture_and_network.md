<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# Control Architecture and Network

## Architecture Option A: Standard PLC + Separate Safety PLC

### Applicability

Use this option when the machine has multiple safety functions, several operator stations, or a future need to integrate plant historian, remote I/O, and industry overlays while keeping the safety path independent from the standard PLC/HMI. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]

### Baseline Structure

- standard PLC: sequence control, permissives, analog control, recipes, logging interface
- safety PLC: E-stop, guard monitoring, restart inhibit, STO/contactors, hydraulic dump path, selected chemical shutdowns
- HMI: operator commands and diagnostics only; no sole reliance for emergency stop [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]
- logger or historian: read-only subscriber to standard PLC data; shall not be able to disable or bypass the safety function. The local software standards guide now routes secure-development and software-lifecycle questions, but detailed cybersecurity hardening remains NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443]

## Architecture Option B: Integrated Safety PLC

### Applicability

Use this option when the project needs tighter diagnostics and reduced hardware count but still requires certified separation between standard and safety tasks inside the same controller family. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]

### Baseline Rules

1. The integrated controller shall use safety-rated function blocks for safety functions rather than ordinary user logic. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]
2. Safety tasks shall remain independent such that a standard logic or HMI state cannot inhibit the safety function. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]
3. The project shall document controller partitioning, safety I/O allocation, software route, and restart behavior in the safety-function register. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause14__marking_and_documentation.md#2-documentation-set] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Implementation Deliverables]

## Architecture Option C: Minimal Safety Relay System

### Applicability

Use this option only when the machine has a very small set of hardwired safety functions, no complex mode logic, and no requirement for safety networking or elaborate diagnostics. The local corpus supports this only indirectly through de-energize-to-stop and physical E-stop principles; detailed relay-architecture limits are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0-control-philosophy] [TO VERIFY: safety relay design guidance]

### Typical Scope

- E-stop chain
- one or two guard channels
- main contactor drop-out
- hydraulic dump valve command

## Architecture Comparison

| Option                                | Advantages                                                              | Constraints                                                                      | Best Fit                                              |
| ------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------- |
| A: Standard PLC + separate safety PLC | Strong separation, easier future expansion, clearer failure boundaries. | More hardware and engineering effort.                                            | Baseline recommended option for this scenario.        |
| B: Integrated safety PLC              | Compact hardware, unified diagnostics, good scalability.                | Requires disciplined separation inside one platform and validated safety blocks. | Machine families with moderate complexity.            |
| C: Safety relay minimal system        | Simple, low cost, easy for limited safety scope.                        | Poor scalability, weak diagnostics, limited network integration.                 | Small standalone skid with very few safety functions. |

## HMI and Logging Architecture

1. The HMI shall provide status, alarms, permissives, reset, and operator commands, but it shall not be the sole means of emergency stop. [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause10__operator_interface.md#2-ergonomic-considerations]
2. Start commands from HMI screens shall be deliberate and shall not bypass guard or E-stop conditions. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]
3. The logger or historian should consume status and event data from the standard controller or a demilitarized read-only interface; the local software standards guide now routes secure-development questions, while event-log integrity, audit trails, and time synchronization remain NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443] [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]

## Network Segmentation Baseline

| Topic                           | Baseline Requirement                                                                                                                                                                                                 | Citation                                                                                                                                                                                                                             |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Safety network                  | Safety-related communications, if networked, shall use a safety protocol suitable for black-channel behavior.                                                                                                        | [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]                                                                                    |
| Standard network vs safety path | Standard PLC, HMI, and logger traffic shall not inhibit or replace the safety path.                                                                                                                                  | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                                                                                              |
| External sources                | External power or signals entering a panel and not removed by the local disconnect shall be identified as external sources.                                                                                          | [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination]                                                                                                                                                 |
| Cybersecurity                   | Network zoning, remote-access controls, credential management, patching, and logging retention are NOT FOUND IN LOCAL CORPUS – TO VERIFY, but the local software guide now identifies the relevant standards family. | [LOCAL: us/nfpa79/NFPA79_2024__Ch03__general_requirements.md#0-safety-philosophy] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] |

## Time Sync, Audit Trail, and Event Logs

The following are recommended project controls, but the normative basis is not present in the local corpus:

- synchronized controller and logger clocks
- alarm and trip event sequence logging
- operator action logs for start, stop, reset, and mode changes
- tamper-evident audit trail for regulated industries

These topics are `NOT FOUND IN LOCAL CORPUS – TO VERIFY`. [TO VERIFY: ISA-18.2] [TO VERIFY: ISA-101] [TO VERIFY: 21 CFR Part 11] [TO VERIFY: IEC 62443]

## Recommended Baseline For This Scenario

Option A is the recommended baseline:

- standard PLC for process and sequencing
- separate safety PLC for all safety functions
- local physical E-stops and guard interlocks
- read-only logger on the standard network
- no write path from historian/logger to the safety controller

This best matches the local corpus emphasis on safety-path independence and on separate treatment of standard versus safety control functions. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]
