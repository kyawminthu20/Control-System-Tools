<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Motor Troubleshooting Decision Tree

## 0. Purpose

Use this as a first-pass troubleshooting note for motor and drive systems before deeper OEM diagnostics or component replacement.

This file is intentionally simple. It helps route the review, not replace the drive manual or fault-history tools.

## 1. Motor will not start

Start with the basic chain:

1. Is input power present to the drive or starter?
2. Is the device healthy, powered, and not faulted?
3. Is the start command actually present?
4. Is a permissive or safety function blocking motion?
5. Is the motor or cable open, shorted, or disconnected?
6. Is the mechanical load jammed or otherwise prevented from moving?

## 2. Overcurrent or immediate trip

Review these first:

- mechanical jam or unexpectedly high load
- acceleration time too aggressive
- incorrect motor data in the drive
- motor-cable fault or phase-to-phase issue
- wrong supply or connection arrangement
- drive hardware fault after wiring/load causes are excluded

## 3. Overheating or nuisance overload

Check whether the problem is primarily electrical or thermal:

- actual load exceeds the motor's continuous rating
- overload setting basis is wrong
- motor cooling is reduced at low speed
- ambient temperature or enclosure heat is too high
- the motor is running on the wrong voltage or connection
- repetitive starts or long acceleration time are heating the machine

## 4. Wrong speed, poor torque, or unstable running

Review:

- commanded frequency or speed reference
- control mode selection
- nameplate data entered into the drive
- slip expectations versus actual load
- low-speed torque demands beyond the chosen control method

## 5. Servo instability

If the axis oscillates or hunts, review:

- motor and encoder model match
- encoder polarity or direction errors
- mechanical resonance
- backlash or loose coupling
- tuning values that are too aggressive
- noise or intermittent feedback loss

## 6. Practical sequence

Use this order when possible:

1. Confirm the machine is safe to inspect and test.
2. Check mechanical freedom and obvious damage first.
3. Check supply, protection, and wiring next.
4. Review configuration and parameter data after hardware basics are known good.
5. Use OEM fault history and scoped measurements only after the basic chain is verified.

## Related files

- [Motor Selection Workflow](./motor_selection_workflow.md)
- [VFD Motor Integration Review](./vfd_motor_integration_review.md)
- [Drive Commissioning](../../commissioning_checklists/checklists/drive_commissioning.md)
