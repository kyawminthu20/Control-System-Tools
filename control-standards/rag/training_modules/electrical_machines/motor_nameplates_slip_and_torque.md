<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: motor_nameplates_slip_and_torque
LEARNING_LEVEL: applied

INDEX_TAGS:
  topics: ["motor_nameplates", "slip", "torque", "nema_design", "enclosures"]
  systems: ["machine", "motor_branch"]
-->

# Motor Nameplates, Slip, and Torque

## 0. Purpose

This module turns common motor-training concepts into a practical review note for selection and troubleshooting.

## 1. Nameplate items that matter first

Read these before assuming anything about the motor:

- rated voltage
- full-load current
- frequency
- rated speed
- phase
- horsepower or power rating
- service factor
- insulation class
- frame size
- enclosure type

## 2. Rated speed versus synchronous speed

For induction motors, synchronous speed is the speed of the rotating magnetic field.

The common relationship is:

`synchronous speed = 120 x frequency / pole count`

The nameplate usually shows **rated speed**, which is lower than synchronous speed under normal load.

## 3. Slip in practical terms

Slip is the difference between synchronous speed and actual rotor speed.

It increases with load because the rotor must lag the field more to develop additional torque.

## 4. Torque-curve regions to recognize

- **Starting torque**: torque available at standstill
- **Pull-up torque**: the lowest torque available while accelerating
- **Breakdown torque**: the maximum torque the motor can produce without stalling
- **Rated-torque region**: the normal continuous operating area

## 5. NEMA design letters in simple terms

- **Design B** is the common general-purpose baseline.
- **Design C** is often used where higher starting torque is needed.
- **Design D** is a higher-slip option for very demanding starting duties.

Exact application still depends on the real load profile.

## 6. Enclosure type is not a side note

Common examples:

- `ODP`
- `TENV`
- `TEFC`
- `TEBC`

The enclosure affects cooling method, contamination tolerance, and environmental suitability.

## 7. Practical takeaway

The most common field mistake is treating horsepower as the whole story.

Real motor review must also consider:

- speed requirement
- load type
- starting method
- enclosure/environment
- protection settings

## Related standards

- [NEC_2023__Art430__motors_motor_circuits_and_controllers.md](../../standards_intelligence/us/nec/NEC_2023__Art430__motors_motor_circuits_and_controllers.md)
- [NFPA79_2024__Ch12__motors_and_associated_equipment.md](../../standards_intelligence/us/nfpa79/NFPA79_2024__Ch12__motors_and_associated_equipment.md)
- [IEC60204_1_2018__Clause12__motors_and_drives.md](../../standards_intelligence/international/machinery/iec_60204_1/IEC60204_1_2018__Clause12__motors_and_drives.md)
