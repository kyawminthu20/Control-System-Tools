<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# Control Architecture and Network

## Architecture Options

| Option                                      | Description                                                                                                                                                  | Best Fit                                                                      | Strengths                                                                                  | Limits                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| A. CNC controller plus separate safety PLC  | CNC controller handles program execution, interpolation, HMI, alarms, and data; separate safety PLC handles E-stop, door interlock, STO, and restart inhibit | Mixed-vendor platforms, retrofit builds, or clear safety partition preference | Strong separation and clear fault boundaries                                               | More hardware and interface complexity                                 |
| B. Integrated safety CNC or motion platform | One CNC or motion-control platform with certified safety partition and safety-rated drive network                                                            | New enclosed machining centers with multiple drive-safety functions           | Tight integration with spindle and axis drives, fewer interface points, better diagnostics | Requires disciplined safety partitioning and certified function blocks |
| C. Minimal relay safety                     | CNC controller plus hardwired E-stop and guard relays                                                                                                        | Small bench or low-complexity CNC machine                                     | Simple and deterministic for very small safety scope                                       | Not well suited to multi-axis, tool changer, or setup-mode complexity  |

The local corpus supports the core separation principle behind Options A and B: safety-related control functions shall remain effective regardless of the state of the standard CNC controller or HMI. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]

## Recommended Baseline Architecture

1. The machine should use Option B for a new enclosed machining center when the selected platform provides certified safety tasks and drive-safe interfaces; Option A remains acceptable for mixed-vendor or retrofit builds. This recommendation is an engineering inference from machine complexity and local separation guidance. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]
2. The ordinary CNC control shall own part-program execution, interpolation, homing, alarm display, recipe or parameter display, and historian tags only.
3. Safety trips shall be generated in the safety partition, safety PLC, or safety relay path rather than in ordinary user logic alone. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]
4. Safety-related software claims shall follow the applicable software lifecycle route, and `IEC 61131-3` alone shall not be treated as a SIL or PL claim basis. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#PLC Language Standard vs Safety Claim Standard]
5. Safety communication over a network, if used, shall use a safety-rated black-channel protocol or equivalent certified approach. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]

## HMI and Logging Architecture

| Layer                 | Baseline intent                                                                                               | Requirement or note                                                                                                                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Local HMI             | Cycle start, cycle stop, feed hold, reset, alarm display, mode selection, diagnostics                         | Feed hold or cycle stop should be treated as operational controls and not as substitutes for E-stop or guard safety functions. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]                         |
| Safety controls       | Physical E-stop devices and safety reset at machine locations                                                 | The HMI shall not be the sole means of emergency stop or other critical safety actions. [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]                                                                         |
| Event logger          | Record E-stop, guard trip, reset, mode change, cycle start, tool-change fault, and selected parameter changes | Detailed audit-trail and retention rules remain `TO VERIFY`. [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]                                                                                                                                              |
| Historian or MES link | Forward read-only tags to plant systems                                                                       | The local software standards guide now routes secure-development questions, but detailed gateway-hardening rules remain `TO VERIFY`. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443] |

## Network Segmentation Baseline

| Topic                          | Baseline Requirement                                                                                                                                                | Trace                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Safety network                 | Safety messages shall stay on a certified safety path and shall not depend on ordinary HMI availability.                                                            | [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]  |
| CNC control network            | CNC controller, HMI, and remote I/O should share a machine-control segment separated from plant enterprise traffic; detailed segmentation controls are `TO VERIFY`. | [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] |
| Historian uplink               | Historian transfer should be read-only or tightly controlled from machine to plant network.                                                                         | [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443]                             |
| External energy identification | Cross-panel signals not removed by the local disconnect shall be marked as external sources.                                                                        | [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination]                                                               |

## Time Sync, Audit Trail, and Program Change Records

1. The machine should use a single time source for CNC control, HMI, and logger timestamps; detailed time-sync rules remain `TO VERIFY`. [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82]
2. The logger should record at minimum: E-stop demand, door trip, reset, mode change, cycle start, cycle stop, tool-change fault, and safety fault clear. Formal alarm and audit-trail governance remains `TO VERIFY`. [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]
3. Program revision or parameter-change traceability should be retained where the project requires controlled software change records. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Implementation Deliverables] [TO VERIFY: IEC 61508-3]
