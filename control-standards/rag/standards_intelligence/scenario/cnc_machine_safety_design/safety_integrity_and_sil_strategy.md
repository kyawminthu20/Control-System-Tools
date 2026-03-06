<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# Safety Integrity and SIL Strategy

## Local-Corpus Boundary

The local corpus supports the electrical implementation and control-behavior side of CNC machine safety functions through NFPA 79, IEC 60204-1, NEC, and the local software standards guide. It does not contain populated local modules for ISO 12100, ISO 13849-1, IEC 62061, or machine-tool-specific type-C standards. Detailed target determination methods are therefore marked `TO VERIFY`. [LOCAL: _index.yaml#topic_routing] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Safety PLC Software And SIL]

## Which Integrity Model Applies

| Use case                                                                                                        | Integrity model to use                                                                  | Local basis                                                                                                                              | Gap status                                                                                              |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| E-stop, enclosure door interlock, spindle stop on access demand, axis safe stop, tool changer access protection | PL route via ISO 13849-1 or machinery SIL route via IEC 62061                           | Local corpus routes machinery safety functions to those standards and requires electrical implementation through NFPA 79 or IEC 60204-1. | Detailed methods NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] |
| Safety-related PLC or integrated safety CNC software implementation                                             | Safety software lifecycle route via IEC 61508-3 paired with the chosen machinery method | Local corpus now routes safety-related software questions through the software standards guide.                                          | Detailed lifecycle methods NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: IEC 61508-3]              |
| Machine-tool-specific safeguarding detail for machining centers                                                 | Supplemental type-C machine-tool route                                                  | CNC-specific enclosure access, tool changer, and workholding requirements are not populated locally.                                     | NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 16090-1]                                         |

## Decision Rules

1. Each protective function shall be classified as a machinery safety function before architecture and validation are assigned. [LOCAL: _standards_map.md#Applicability Matrix by Project Type]
2. Safety-related control functions shall remain effective regardless of the state of the standard CNC control or HMI. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]
3. Safety-related software claims shall follow the applicable software lifecycle route, and `IEC 61131-3` alone shall not be treated as a SIL or PL claim basis. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#PLC Language Standard vs Safety Claim Standard] [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Safety PLC Software And SIL]
4. Reset of an E-stop, guard interlock, or equivalent trip shall not restart the machine and shall only permit restart after a separate deliberate action. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#2-emergency-stop-concepts]
5. Operational controls such as cycle stop, feed hold, or ordinary CNC mode changes shall not be used as substitutes for the required safety function. Local control philosophy supports this distinction, but machine-tool-specific details remain `TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [TO VERIFY: ISO 16090-1]
6. Selection of target PL or SIL, use of risk graphs, and detailed stop-time or guard-unlocking methods are NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 12100] [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] [TO VERIFY: ISO 16090-1]

## Example Target Selection

These are engineering starting points only. They are not normative targets because the local corpus does not contain the formal target-assignment method.

| Function                                      | Candidate target                                   | Why this is a reasonable starting point                                                                                                                                                                    | Status                                                                                                     |
| --------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Emergency stop master function                | Candidate `PL d` or `SIL 2`                        | E-stop is the highest-priority command and must override all modes without restart on reset. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts]     | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1] [TO VERIFY: IEC 62061] |
| Front enclosure door interlock                | Candidate `PL d` or `SIL 2`                        | Door opening directly exposes personnel to rotating-tool and moving-axis hazards. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]  | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1]                        |
| Spindle STO or safe stop on safety demand     | Candidate `PL d` or `SIL 2`                        | Spindle torque removal is a core protective action for CNC access and emergency stop functions. [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations] | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: IEC 62061]                          |
| Axis STO or safe stop on safety demand        | Candidate `PL d` or `SIL 2`                        | Axis motion exposes pinch and crush hazards and may need coordinated drive-safe behavior. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md#2-drive-integration] | Target confirmation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 13849-1]                        |
| Tool changer access interlock                 | Candidate `PL c` to `PL d`                         | Tool changer motion can expose pinch and crush hazards; exact target depends on access and exposure conditions.                                                                                            | Formal allocation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 16090-1]                          |
| Setup-mode controlled motion with access open | Candidate `PL d` or `SIL 2` depending architecture | Reduced-hazard setup motion is highly machine-tool-specific and requires external method confirmation.                                                                                                     | Formal allocation NOT FOUND IN LOCAL CORPUS - TO VERIFY. [TO VERIFY: ISO 16090-1] [TO VERIFY: IEC 62061]   |

## Documentation Outputs That Shall Exist

1. Safety function register with initiators, sensors, logic solver, final elements, and safe-state definition shall exist. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
2. CNC mode table and interlock narrative shall exist for `AUTO`, `JOG`, `SETUP`, `FAULT`, and `MAINTENANCE` states. [LOCAL: us/nfpa79/NFPA79_2024__Ch19__marking_and_documentation.md#2-documentation-expectations]
3. Validation or verification records shall exist for continuity, insulation, stop behavior, STO operation, and restart prevention. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause15__verification.md#1-required-tests] [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#2-final-compliance-alignment]
