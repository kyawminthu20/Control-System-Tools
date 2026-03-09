<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Motor Symptom Troubleshooting Patterns

## 0. Purpose

Use this note after the first-pass troubleshooting tree when you already know the symptom and need a tighter list of probable causes to review.

## 1. Motor overheats but current looks normal

Possible review areas:

- blocked ventilation
- failed cooling fan
- high ambient temperature
- mechanical friction
- bearing damage

This is a reminder that heating problems are not always caused by obviously excessive current.

## 2. Excessive vibration

Possible review areas:

- shaft misalignment
- bearing wear
- rotor imbalance
- loose mounting
- coupling issues

## 3. VFD overcurrent during acceleration

Possible review areas:

- acceleration ramp too short
- load too heavy
- motor parameter mismatch
- faulty motor
- incorrect drive tuning
- mechanical binding

## 4. Motor runs but produces poor or no torque

Possible review areas:

- phase loss
- broken rotor bars
- incorrect drive configuration
- mechanical disconnect
- control mode mismatch

## 5. Noise at low speed with a VFD

Possible review areas:

- PWM switching noise
- motor resonance
- poor tuning
- low-speed operation outside the motor's comfortable range

## 6. Practical sequence

1. confirm the symptom clearly
2. separate mechanical from electrical causes
3. verify configuration and parameter basis
4. use measurements only after obvious physical causes are checked

## Related files

- [Motor Troubleshooting Decision Tree](./motor_troubleshooting_decision_tree.md)
- [Motor Efficiency, Power Factor, and Losses](../../training_modules/electrical_machines/motor_efficiency_power_factor_and_losses.md)
- [Drive Commissioning](../../commissioning_checklists/checklists/drive_commissioning.md)
