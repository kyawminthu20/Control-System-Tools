<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: ELECTRICAL_MACHINES
MODULE_ID: motor_and_vfd_equations_reference
LEARNING_LEVEL: intermediate

INDEX_TAGS:
  topics: ["equations", "torque", "power", "synchronous_speed", "slip", "vfd"]
  systems: ["motor_drive", "machine"]
-->

# Motor and VFD Equations Reference

## 0. Purpose

This module collects the most useful motor and VFD equations into one reference note for training and first-pass engineering review.

Use these as working relationships, not as a substitute for detailed manufacturer data or standards-based design methods.

## 1. Mechanical power and torque

Core relationship:

`P = T x omega`

Where:

- `P` = mechanical power
- `T` = torque
- `omega` = angular velocity

Common engineering form:

`P(kW) = T(Nm) x rpm / 9550`

Horsepower form:

`HP = T(lb-ft) x rpm / 5252`

## 2. Synchronous speed

For AC machines:

`N_s = 120 x f / poles`

Where:

- `N_s` = synchronous speed in rpm
- `f` = electrical frequency
- `poles` = number of poles

This is why changing VFD output frequency changes motor speed.

## 3. Slip

For induction motors:

`s = (N_s - N_r) / N_s`

Where:

- `N_s` = synchronous speed
- `N_r` = rotor speed

Slip is required for induction-motor torque production.

## 4. Efficiency

`eta = P_out / P_in`

Efficiency is a ratio between useful mechanical output and electrical input.

## 5. Power factor

`PF = Real Power / Apparent Power`

In simple terms, power factor indicates how effectively current is being converted into useful power.

## 6. Three-phase power reminder

For quick review:

`P(W) = sqrt(3) x V_LL(V) x I_L(A) x PF`

To convert to kilowatts: `P(kW) = P(W) / 1000`

This is a useful relationship when estimating the electrical side of a motor system.

## 7. VFD speed relationship

A VFD changes motor speed mainly by changing output frequency.

First-pass rule:

- lower output frequency -> lower synchronous speed
- higher output frequency -> higher synchronous speed until voltage and control limits are reached

## 8. Practical cautions

- Equations alone do not select a motor or drive correctly.
- Real design still depends on nameplate data, load profile, duty cycle, and manufacturer ratings.
- Do not use simplified equations as a substitute for conductor, protection, or thermal review.

## Related files

- [Motor Nameplates, Slip, and Torque](./motor_nameplates_slip_and_torque.md)
- [VFD Fundamentals](./vfd_fundamentals.md)
- [Motor Control Methods and Operating Regions](./motor_control_methods_and_operating_regions.md)
