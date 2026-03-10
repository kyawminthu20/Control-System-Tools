<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Motor Cable and Protection Review

## 0. Purpose

Use this note when reviewing motor wiring and protection decisions around drives, conductors, shielding, and starting behavior.

## 1. Cable review for VFD systems

Review:

- motor cable length
- shielding approach
- routing near control wiring
- termination quality
- any need for output reactor, dv/dt filter, or sine filter

Long motor cables can contribute to:

- reflected-wave voltage stress
- insulation stress
- motor heating

## 2. Shielding review

Shielding is important because VFD switching creates high-frequency noise.

Review whether the cable and grounding approach help reduce:

- EMI
- ground-current noise
- encoder or feedback interference

Do not rely on one universal shield rule without checking the actual drive and cable approach.

## 3. Conductor-size review

Review conductor sizing based on:

- motor current
- conductor temperature rating
- installation method
- voltage-drop concern where relevant
- protection coordination

## 4. Protection review

Motor protective-device review is different from ordinary branch-circuit thinking because motors draw high starting current.

Separate these ideas:

- short-circuit and ground-fault protection
- overload protection
- drive internal protective functions

## 5. Review questions

1. Is the conductor-size basis documented?
2. Is the motor cable suitable for the drive environment?
3. Is shielding handled intentionally?
4. Is the protective-device strategy coordinated with motor starting behavior?
5. Are long-cable effects reviewed if the drive is remote from the motor?

## Related files

- [VFD Motor Integration Review](./vfd_motor_integration_review.md)
- [VFD Commissioning Workflow](./vfd_commissioning_workflow.md)
- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
