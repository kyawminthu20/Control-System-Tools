<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# Verification and Validation Plan

## FAT and SAT Outline

1. Verify electrical drawings, I/O list, safety-function register, and mode table before powered testing.
2. Verify grounding, bonding, conductor identification, and panel labels before energization.
3. Perform powered functional tests for spindle, axes, tool changer, HMI, and alarms.
4. Perform safety validation tests for E-stop, door interlock, STO behavior, restart inhibition, and interlock logic.
5. Repeat critical functional and safety tests at site after installation and integration.

## Safety Validation Tests

| ID    | Test                                | Acceptance Intent                                                                                             | Citation                                                                                                                                                            |
| ----- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VV-01 | Emergency stop test                 | Each E-stop demand stops hazardous motion, inhibits restart, and requires separate deliberate restart action  | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts]                                                           |
| VV-02 | Front door interlock test in `AUTO` | Opening the enclosure door removes hazardous spindle and axis motion and blocks restart until reset and start | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                             |
| VV-03 | Power restoration test              | Restoration of power does not automatically restart spindle, axis motion, or automatic cycle                  | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior]                                                                |
| VV-04 | Spindle STO test                    | Safety demand removes spindle torque and verifies spindle-safe feedback where provided                        | [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations]                                                          |
| VV-05 | Axis STO and hold test              | Safety demand removes axis torque and verifies vertical-axis hold behavior where applicable                   | [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause14__electric_motors.md#2-drive-integration] [TO VERIFY: machine-tool-specific safety standard] |
| VV-06 | Tool change interlock test          | Tool change is inhibited when spindle-stop or axis-position permissives are not met                           | [TO VERIFY: ISO 16090-1]                                                                                                                                            |
| VV-07 | Setup-mode auto-cycle inhibit test  | Setup or jog mode blocks automatic cycle under defined setup conditions                                       | [TO VERIFY: ISO 16090-1]                                                                                                                                            |
| VV-08 | Workholding permissive test if used | Automatic cycle cannot start when clamp or workholding permissive is absent                                   | [TO VERIFY: machine-tool-specific safety standard]                                                                                                                  |
| VV-09 | Residual-voltage test               | Stored electrical energy decays below permitted threshold within required time or wait label is present       | [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures]                                                                    |
| VV-10 | Logger event integrity test         | E-stop, door trip, reset, and mode change events are captured in the logger with correct time sequence        | [TO VERIFY: ISA-18.2] [TO VERIFY: 21 CFR Part 11]                                                                                                                   |

## Documentation Deliverables Checklist

- electrical schematics and panel layout
- CNC I/O list and network list
- safety function register
- mode table and interlock narrative
- STO wiring or safe-drive interface drawings
- disconnect, LOTO, and stored-energy isolation point list
- conductor and device label schedule
- FAT results and SAT results
- maintenance instructions for electrical and stored-energy isolation
- any external `TO VERIFY` standards closure record used to finalize the build
