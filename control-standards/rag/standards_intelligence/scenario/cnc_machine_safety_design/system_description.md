<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
SCENARIO_ID: CNC_MACHINE_SAFETY_DESIGN
-->

# System Description

## Concept Overview

The concept machine is an enclosed CNC machining center used to remove material from a workpiece with a powered spindle and coordinated servo-axis motion. A CNC controller executes the part program, while safety logic handles emergency stop, guard interlocks, restart inhibition, and safe stopping functions independent of ordinary CNC or HMI state. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]

## ASCII Block Diagram

```text
Facility Supply
    |
    v
[Main Disconnect / LOTO]
    |
    +------------------------------------+
    | Main Control Panel                 |
    |                                    |
    | [Branch OCP]-->[Spindle Drive]-->[Spindle Motor]
    |                                    |
    | [Branch OCP]-->[X Servo Drive]-->[X Axis Motor]
    | [Branch OCP]-->[Y Servo Drive]-->[Y Axis Motor]
    | [Branch OCP]-->[Z Servo Drive]-->[Z Axis Motor / Brake]
    |                                    |
    | [Starter]----->[Coolant Pump / Lube / Chip Conveyor]
    |                                    |
    | [24 VDC PSU]-->[CNC Controller / HMI / I/O / Logger]
    |                                    |
    |                  +--> Program, status, diagnostics
    |                  +--> Read-only historian / network path
    |
    +--> Safety Logic (integrated or separate)
           ^        ^         ^         ^         ^
           |        |         |         |         |
        E-Stops  Door SW   Tool Chg   Drive     Access /
                           Guard SW   Feedback   Reset PB

Safety Outputs:
    -> Spindle STO or spindle contactor drop-out
    -> Axis STO and brake control as applicable
    -> Tool changer motion inhibit
    -> Auto-cycle inhibit and restart block
```

## Major Subsystems

| Subsystem                               | Description                                                                                                                            | Main Hazards                                                        | Design Notes                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CNC controller and HMI                  | Executes part programs, mode logic, homing, alarms, and operator interaction.                                                          | Unintended motion from incorrect commands or restart behavior.      | HMI and ordinary CNC logic shall not be the sole protective means for safety functions. [LOCAL: us/nfpa79/NFPA79_2024__Ch10__operator_interface_devices.md#2-ergonomics-and-safety] [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                     |
| Safety logic                            | Separate safety PLC, integrated safety CNC partition, or relay architecture handling E-stop, door interlock, STO, and restart inhibit. | Loss of safety due to ordinary logic failure.                       | Safety path shall remain effective regardless of standard control state. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#3-safety-vs-standard-control-separation]                                                                                                      |
| Spindle system                          | Spindle drive, motor, tool holder, and cutting tool.                                                                                   | Rotating tool contact, entanglement, tool breakage or ejection.     | Drive STO and safe stop behavior are locally supported at a high level; detailed machine-tool requirements remain `TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations] [TO VERIFY: ISO 16090-1]                                                              |
| Linear axes (`X`, `Y`, `Z`)             | Servo drives, motors, ballscrews or linear motors, feedback, and mechanical guides.                                                    | Pinch, crush, collision, vertical-axis drop.                        | Where drives participate in a safety function, certified STO or equivalent torque-removal means shall be used. Vertical-axis holding detail is `TO VERIFY`. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause14__electric_motors.md#2-drive-integration] [TO VERIFY: machine-tool-specific safety standard] |
| Enclosure and access door               | Guard enclosure, front sliding or hinged door, window, and access hardware.                                                            | Operator access to rotating tool, chips, or moving axes.            | Door interlock shall remain independent of ordinary CNC state if used as a safety function. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                                                                                             |
| Tool changer and magazine               | Automatic tool magazine, changer arm, pot carousel, and associated actuators.                                                          | Pinch, crush, entrapment, tool drop, unexpected tool change motion. | Safe sequencing and access control are required, but detailed machine-tool-specific interlock rules are `TO VERIFY`. [TO VERIFY: ISO 16090-1]                                                                                                                                                                                   |
| Workholding and optional clamp circuits | Fixture clamps, pallet clamp, pneumatic vise, or hydraulic workholding if used.                                                        | Workpiece ejection, stored pressure, part slip.                     | Workholding confirmation before cycle start is a project safety requirement; detailed normative basis is `TO VERIFY`. [TO VERIFY: machine-tool-specific safety standard]                                                                                                                                                        |
| Coolant, lubrication, and chip handling | Coolant pump, lube pump, mist extraction, chip conveyor.                                                                               | Slip, splash, maintenance contact, electrical contamination.        | Electrical supply and device environment are locally supported; fluid-system specifics remain partly `TO VERIFY`. [LOCAL: us/nfpa79/NFPA79_2024__Ch04__general_conditions_of_installation.md#0-environmental-considerations]                                                                                                    |
| Sensors and feedback                    | Door switch, E-stop contacts, drive STO feedback, home sensors, overtravel inputs, tool changer position, clamp permissives.           | False permissive, undetected fault, latent failure.                 | Safety-related sensing shall be placed in a safety-rated path where the function is safety-related. [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#3-safety-vs-standard-control-separation]                                                                                                     |
| Logger and network                      | Local event log, HMI network, optional historian connection.                                                                           | Unsafe writes, lost records, insecure access.                       | Safety path shall not depend on logger or historian availability. Cybersecurity detail is `TO VERIFY`. [LOCAL: reference_models/software_safety_and_intrinsic_safety_standards.md#Secure Development And Cybersecurity] [TO VERIFY: IEC 62443]                                                                                                   |
| Isolation devices                       | Main disconnect, panel door interlock, STO paths, pneumatic dump valves, coolant isolation points.                                     | Shock, residual voltage, trapped pressure, incomplete lockout.      | Main disconnect and residual-voltage behavior are strongly supported locally. [LOCAL: us/nfpa79/NFPA79_2024__Ch05__disconnecting_means.md#1-main-disconnect-requirements] [LOCAL: us/nfpa79/NFPA79_2024__Ch07__protection_against_electric_shock.md#1-protective-measures]                                                      |

## Baseline Safe State

On a safety demand, the baseline safe state shall be:

1. spindle torque removed and hazardous rotation brought to the allocated stop state [LOCAL: us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md#2-drive-protection-considerations]
2. axis torque removed and hazardous axis motion stopped, with vertical-axis holding means applied where required by the design. Detailed holding method is `TO VERIFY`. [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause14__electric_motors.md#2-drive-integration] [TO VERIFY: machine-tool-specific safety standard]
3. tool changer motion inhibited [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#0-control-philosophy]
4. restart blocked until manual reset and separate deliberate start action [LOCAL: us/nfpa79/NFPA79_2024__Ch09__control_circuits_and_control_functions.md#2-emergency-stop-concepts] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause03__terms_and_definitions.md#1-terms-that-affect-design-decisions]

## Operating Modes

The baseline machine should support these modes:

- `OFF / ISOLATED`
- `READY / HOMED`
- `AUTO / CYCLE`
- `JOG / SETUP`
- `MDI / PROGRAM TEST`
- `FAULT / TRIPPED`
- `MAINTENANCE`

Mode logic shall preserve stop priority over start and shall not allow restoration of power to cause automatic restart. [LOCAL: us/nfpa79/NFPA79_2024__Ch03__general_requirements.md#3-control-system-interpretation] [LOCAL: international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md#1-startstop-behavior]
