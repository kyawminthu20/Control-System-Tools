<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Star-Delta and Supply Matching Notes

## 0. Purpose

This note captures the first-pass engineering logic for reviewing motors with multiple winding-connection options.

## 1. Core idea

Star and delta connections do not expose the winding to the same voltage.

That means the connection method must match:

- the motor winding basis
- the line voltage
- the intended starting or running scheme

## 2. Review points

- Confirm the actual motor connection data from the nameplate or terminal-diagram information.
- Do not assume that a six-terminal motor is automatically intended for field star-delta starting.
- Verify whether the supply voltage corresponds to the winding voltage in the intended connection.

## 3. Practical risks

- wrong bridge placement at the terminal box
- applying line voltage to a winding basis that does not support it
- assuming field reconnection is acceptable without OEM confirmation

## 4. When to escalate

Escalate the review when:

- the nameplate is unclear
- the motor will be used with a VFD
- the machine has high starting torque demand
- the connection change affects starting current or protection settings materially

## Related standards

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2018__Clause12__motors_and_drives.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md)
