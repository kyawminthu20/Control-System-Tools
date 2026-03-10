<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# Hazards and Risk Assessment

## Primary Hazard List

| Hazard                               | Source or Task                                                  | Typical Harm                                   | Baseline Safeguards                                                                              | Standards Route                                                                                                                                                                                                                     |
| ------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rotating spindle or tool contact     | Door open during spindle motion, maintenance near rotating tool | Laceration, entanglement, severe bodily injury | E-stop, door interlock, spindle STO or equivalent safe stop, restart inhibit                     | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations]                |
| Axis crush or pinch                  | Axis jog, auto motion, homing, setup reach-in                   | Hand or body injury                            | Guard door interlock, mode control, STO or safe stop, restart inhibit                            | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [TO VERIFY: ISO 13849-1]                                                                                                       |
| Tool changer pinch or entrapment     | Automatic tool change, magazine maintenance                     | Pinch, crush, impact                           | Tool change interlock, access guard, safe position sequencing                                    | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0-control-philosophy] [TO VERIFY: ISO 16090-1]                                                                                                       |
| Tool or workpiece ejection           | Loose tool, unclamped part, fixture failure                     | Impact injury, eye injury                      | Door closed and interlocked during cycle, workholding permissive, guarded enclosure              | [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety] [TO VERIFY: ISO 16090-1]                                                                                                                |
| Unexpected restart                   | Power restoration, reset after trip, latent logic fault         | Unplanned motion or spindle rotation           | No automatic restart, separate deliberate start after reset                                      | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md#1-startstop-behavior] |
| Electrical shock or residual voltage | Open panel, service drives after disconnect                     | Shock, burn                                    | Main disconnect, door interlock, residual-voltage discharge or wait label, grounding and bonding | [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#4-control-panel-design-rules] [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures]                                          |
| Stored pneumatic or hydraulic energy | Tool clamp, workholding, door cylinders, maintenance            | Impact, release, pinching, injection           | Lockable shutoff, dump or bleed, maintenance verification                                        | [TO VERIFY: ISO 4413] [TO VERIFY: machine-tool-specific safety standard]                                                                                                                                                            |
| Coolant slip or splash               | Door opening, maintenance, overflow                             | Slip, skin or eye irritation                   | Enclosure, drain management, controlled access, maintenance instruction                          | [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]                                                                                                                          |

## Risk Reduction Hierarchy

Apply risk reduction in this order:

1. Remove or reduce the hazard by machine design where possible.
2. Use guards, enclosure boundaries, and interlocks to prevent access to the hazard.
3. Use safety-related control functions for stop, inhibit, restart prevention, and safe state.
4. Use warnings, procedures, training, and PPE only as residual controls.

This hierarchy is consistent with the local machinery routing, but detailed risk-ranking methods remain `TO VERIFY`. [LOCAL: _standards_map.md#Market-Based Selection] [TO VERIFY: ISO 12100]

## Risk Control Mapping

| Hazard              | Safeguard                                                             | Related Standard(s)                            | Verification Method                                     |
| ------------------- | --------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------- |
| Spindle contact     | E-stop, door interlock, spindle STO, restart inhibit                  | NFPA 79, IEC 60204-1, ISO 13849-1 or IEC 62061 | Functional stop test, door-open test, power-cycle test  |
| Axis motion crush   | Guard interlock, axis STO, mode control, restart inhibit              | NFPA 79, IEC 60204-1, ISO 13849-1 or IEC 62061 | Functional test in AUTO and JOG                         |
| Tool changer motion | Tool change safe-position interlock, access guard                     | NFPA 79, machine-tool-specific type-C standard | Simulated tool-change test and access-door test         |
| Workpiece ejection  | Clamp or workholding permissive, enclosure closed                     | Machine-tool-specific type-C standard          | Simulated permissive loss and cycle-start inhibit test  |
| Electrical shock    | Main disconnect, door interlock, residual-voltage protection, bonding | NFPA 79, NEC, IEC 60204-1                      | Disconnect test, residual-voltage test, continuity test |
| Stored fluid energy | Lockable shutoff and bleed, pressure verification                     | ISO 4413 and machine-tool-specific standard    | Maintenance isolation and pressure-decay test           |

## Concise Risk Assessment Template

For each hazardous task, document:

- task or machine state
- hazard source
- who is exposed
- existing safeguards
- required safety function or interlock
- safe state after demand
- reset and restart behavior
- verification test
- residual risk note
- `TO VERIFY` items if the local corpus does not close the method

## Local-Corpus Boundary

The local corpus supports the electrical and control-behavior side of CNC machine risk reduction through NFPA 79, NEC, and IEC 60204-1. Detailed machine-tool-specific hazard analysis for tooling, workholding, tool changing, and door unlocking remains `TO VERIFY`. [LOCAL: _standards_map.md#Applicability Matrix by Project Type] [TO VERIFY: ISO 16090-1]
