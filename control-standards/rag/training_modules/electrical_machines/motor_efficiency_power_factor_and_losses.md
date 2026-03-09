<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: motor_efficiency_power_factor_and_losses
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["efficiency", "power_factor", "losses", "stator_copper_loss", "core_loss"]
  systems: ["motor_drive", "machine"]
-->

# Motor Efficiency, Power Factor, and Losses

## 0. Purpose

This module explains three motor concepts that are often mentioned together but should not be confused:

- efficiency
- power factor
- loss mechanisms

## 1. Efficiency

Efficiency measures how much electrical input becomes useful mechanical output.

Relationship:

`eta = P_out / P_in`

Low efficiency means more input power is being lost as heat or other internal losses.

## 2. Power factor

Power factor is the ratio of real power to apparent power.

`PF = P / S`

In practical terms:

- lower power factor means higher current is needed for the same real power
- higher current increases conductor and system burden

Induction motors commonly operate below unity power factor.

## 3. Main motor loss types

Common loss categories:

- stator copper loss
- rotor copper loss
- core loss
- mechanical loss
- stray losses

### Stator copper loss

Caused by current flowing in stator windings.

### Rotor copper loss

Important in induction motors because rotor current exists due to slip.

### Core loss

Magnetic loss in the steel, often associated with hysteresis and eddy-current effects.

### Mechanical loss

Includes bearing friction, windage, and other rotational mechanical losses.

### Stray losses

Smaller losses not always grouped neatly into the main buckets.

## 4. Why engineers should care

These concepts affect:

- heating
- current demand
- enclosure temperature
- operating cost
- motor selection quality

## 5. Practical mistakes

### Confusing efficiency and power factor

They are not the same:

- efficiency compares output power to input power
- power factor compares real power to apparent power

### Ignoring losses when current seems acceptable

A motor can overheat because of cooling or mechanical issues even when measured current is not obviously excessive.

## 6. Practical takeaway

If a motor is running hot, do not stop at current alone. Review:

- actual load
- cooling path
- ambient temperature
- friction or bearing problems
- electrical loss and operating condition

## Related files

- [Motor and VFD Equations Reference](./motor_and_vfd_equations_reference.md)
- [Motor Symptom Troubleshooting Patterns](../../design_framework/motor_systems/motor_symptom_troubleshooting_patterns.md)
