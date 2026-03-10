<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# Mechanical and Electrical Isolation

## Mechanical or Fluid Isolation Points

| Isolation Point                                                                     | Purpose                                                                              | Verification Method                            | Trace                                                                                                                   |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Front access door and enclosure guard                                               | Prevent operator entry to the machining zone during hazardous spindle or axis motion | Functional interlock test                      | [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] |
| Pneumatic supply shutoff and dump for tool changer, drawbar, or workholding if used | Remove stored air energy before maintenance                                          | Lockout trial and pressure-decay check         | [TO VERIFY: machine-tool-specific safety standard]                                                                      |
| Hydraulic shutoff and bleed for pallet clamp or hydraulic workholding if used       | Remove stored hydraulic pressure before maintenance                                  | Lockout trial and zero-pressure verification   | [TO VERIFY: ISO 4413]                                                                                                   |
| Coolant isolation point                                                             | Allow maintenance on coolant pump, hoses, or tank                                    | Lockout trial and leak check                   | [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]              |
| Vertical-axis maintenance support or locking method where applicable                | Prevent gravity-driven motion during brake release or service                        | Maintenance procedure review and demonstration | [TO VERIFY: machine-tool-specific safety standard]                                                                      |

## Electrical Isolation Points

| Isolation Point                             | Requirement                                                                                                                                    | Verification Method                  | Trace                                                                                                                                                                                                                       |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Main machine disconnect                     | The machine shall provide one primary disconnect that is external or otherwise accessible, clearly marked, and lockable in the `OFF` position. | Inspection and lockout trial         | [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements]                                                                                                                                 |
| Point-of-supply location                    | The disconnect shall be located at the machine point of supply and readily accessible.                                                         | Layout review and site inspection    | [LOCAL: us/nec/NEC_2023__Art670__industrial_machinery.md#1-machine-disconnecting-means]                                                                                                                                     |
| Panel door interlock and line-side guarding | Panel door access shall be interlocked or otherwise controlled, and line-side parts that remain energized shall be guarded and warned.         | Door-open test and visual inspection | [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#4-control-panel-design-rules] [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#3-panel-layout-implications]                            |
| STO path                                    | Where spindle or axis drives participate in safety functions, STO shall be the preferred torque-removal path.                                  | Drive safety test                    | [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md#2-drive-integration] |
| External source identification              | Inter-panel or auxiliary signals not removed by the local disconnect shall be identified as external sources.                                  | Label inspection                     | [LOCAL: us/nfpa79/NFPA79_2024__Ch20__system_integration.md#1-subsystem-coordination]                                                                                                                                        |

## Stored Energy Discharge Requirements

1. Stored electrical energy shall discharge below 60 V within 5 seconds after power removal, or the enclosure shall display the required wait time. [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2018__Clause06__protection_against_electric_shock.md#1-protective-measures]
2. Pneumatic or hydraulic maintenance isolation shall include a dump or bleed path and a means to verify pressure is at zero before maintenance begins. Detailed fluid-power rules are `TO VERIFY`. [TO VERIFY: ISO 4413] [TO VERIFY: machine-tool-specific safety standard]
3. Vertical-axis holding or support shall be verified before brake release or axis service if gravity motion is possible. Detailed method is `TO VERIFY`. [TO VERIFY: machine-tool-specific safety standard]
4. Where door unlocking depends on spindle stop or axis stop completion, the stop-complete logic and verification method shall be documented. Detailed method is `TO VERIFY`. [TO VERIFY: ISO 16090-1]
