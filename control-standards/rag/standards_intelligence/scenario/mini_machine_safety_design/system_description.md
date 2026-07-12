<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: MINI_MACHINE_SAFETY_DESIGN
-->

# System Description

## Concept Overview

The concept machine is a compact process-and-utility skid that combines discrete machinery safety functions with fluid-handling duties:

- a hydraulic power unit provides motion or force to one or more guarded actuators
- chemical dosing pumps inject chemicals into a process line or receiving vessel
- a standard PLC manages sequence, permissives, HMI, and data capture
- a safety controller or equivalent safety architecture handles emergency stop, guard monitoring, and safety outputs independent of the standard PLC/HMI [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]

## ASCII Block Diagram

```text
Facility Supply
    |
    v
[Main Disconnect / LOTO]
    |
    +------------------------------+
    | Main Control Panel           |
    |                              |
    |  [Branch OCP]---->[HPU VFD/Starter]---->[Hydraulic Motor]
    |       |                                  |
    |       |                                  v
    |       |                           [Hydraulic Pump]
    |       |                                  |
    |       |                           [Filter / Relief]
    |       |                                  |
    |       |                           [Valve Manifold]
    |       |                             |         |
    |       |                             v         v
    |       |                        [Actuator] [Dump-to-Tank Valve]
    |       |
    |       +---->[Chem Pump 1 Starter]---->[Metering Pump 1]
    |       |
    |       +---->[Chem Pump 2 Starter]---->[Metering Pump 2]
    |       |
    |       +---->[24 VDC PSU]---->[PLC / Remote I/O / HMI / Logger]
    |                              |
    |                              +--> Non-safety network / historian
    |
    +--> Safety Logic (Safety PLC / relay)
           ^        ^        ^        ^        ^
           |        |        |        |        |
       E-Stops   Guards   Pressure  Leak   Tank HH / Door SW

Safety Outputs:
    -> Main control power removal / MCR
    -> VFD STO or motor contactor drop-out
    -> Hydraulic dump valve to tank
    -> Chemical pump shutdown and isolation
```

## Major Subsystems

| Subsystem                      | Description                                                                                                      | Main Hazards                                                                 | Design Notes                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hydraulic power unit           | Electric motor, pump, reservoir, relief path, filter, manifold, and dump valve.                                  | Stored pressure, hose failure, unintended motion, residual energy.           | Electrical supply, motor protection, and control behavior are covered locally; detailed hydraulic circuit safety is NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md#1-motor-protection-concepts] [TO VERIFY: ISO 4413]                                                                           |
| Hydraulic actuators and guards | Cylinders or rotary actuators performing guarded machine motion.                                                 | Pinch, crush, unexpected restart.                                            | Guarded access and stop behavior shall be enforced through safety logic independent of the standard PLC. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety]                                      |
| Chemical dosing system         | Day tanks, suction/discharge piping, dosing pumps, isolation valves, injection points, containment tray.         | Spill, overfill, exposure, wrong-dose event.                                 | Detailed chemical handling standards are NOT FOUND IN LOCAL CORPUS – TO VERIFY; the baseline package therefore requires containment, leak detection, and independent shutdown logic as project requirements. [TO VERIFY: application-specific chemical handling standard]                                                                                         |
| Sensors                        | Pressure switches/transmitters, level switches, leak sensors, guard switches, feedback contacts, overload trips. | Nuisance trips, undetected faults, false safe-state assumptions.             | Safety-related sensing shall be monitored in a safety-rated path where the function is safety-related. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                                                                                                                    |
| Final elements                 | Contactors, STO inputs, solenoid dump valves, isolation valves, pump starters, alarm horn/light.                 | Failure to de-energize, welded contacts, latent demand failure.              | Stop functions should default to de-energization to stop and should be validated during FAT/SAT. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0-control-philosophy] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause18__verification.md#1-required-tests]                                                    |
| PLC / safety controller        | Sequence logic, permissives, HMI coordination, diagnostics, safety logic.                                        | Safety function corruption by standard logic, uncontrolled restart.          | Safety and standard control shall be separated so standard PLC/HMI state cannot inhibit the safety function. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                                                                                                              |
| HMI / UI                       | Start, stop, reset, mode selection, alarm display, process values, maintenance screens.                          | Accidental actuation, unclear status, misuse of touchscreen for safety.      | HMI shall not be the sole emergency-stop means, and hazardous-motion start commands shall be guarded or recessed. [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause10__operator_interface.md#2-ergonomic-considerations]                            |
| Network and logger             | PLC communications, HMI communications, optional historian or edge logger, time source.                          | Cyber-induced unsafe state, loss of records, unsafe writes into safety path. | Safety communications may use certified black-channel protocols; cybersecurity segmentation and audit-trail rigor are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation] [TO VERIFY: IEC 62443] [TO VERIFY: NIST SP 800-82] |
| Electrical isolation devices   | Main disconnect, local drive disconnects where required, secondary OCP, guarded line-side terminals.             | Shock, arc event, incomplete de-energization.                                | Main disconnect behavior and working-space requirements are strongly covered in the local corpus. [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements] [LOCAL: us/nec/NEC_2023__Art110__requirements_for_electrical_installations.md#1-installation--listing-requirements-field-rules]                                     |
| Mechanical isolation devices   | Hydraulic block-and-bleed points, dump valves, bleed ports, chemical isolation valves.                           | Residual pressure, trapped chemicals, maintenance exposure.                  | Mechanical isolation architecture is a project requirement here because detailed normative local source content is absent. [TO VERIFY: ISO 4413] [TO VERIFY: application-specific chemical handling standard]                                                                                                                                                     |

## Baseline Safe State

On a safety demand, the baseline safe state shall be:

1. hazardous motion removed or brought to a controlled stop as allocated by the safety function [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#1-startstop-behavior] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
2. hydraulic power removed and dump path commanded to tank or equivalent depressurization state. Hydraulic implementation details are NOT FOUND IN LOCAL CORPUS – TO VERIFY. [TO VERIFY: ISO 4413]
3. chemical dosing pumps stopped and restart inhibited pending reset and operator review [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [TO VERIFY: application-specific chemical handling standard]
4. restart blocked until manual reset and separate deliberate start command [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause03__terms_and_definitions.md#1-terms-that-affect-design-decisions]

## Operating Modes

The baseline machine should support these modes:

- `OFF / ISOLATED`
- `READY`
- `AUTO`
- `MANUAL / MAINTENANCE`
- `FAULT / TRIPPED`

Mode logic shall preserve stop priority over start and shall not allow restoration of power to cause automatic restart. [LOCAL: us/nfpa79/NFPA79_2024__Ch03__general_requirements.md#3-control-system-interpretation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
