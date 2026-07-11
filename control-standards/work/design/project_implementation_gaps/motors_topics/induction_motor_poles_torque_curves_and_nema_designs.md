<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: INDUCTION_MOTOR_TRAINING_REFERENCE
-->

# Induction Motor Poles, Torque Curves, and NEMA Designs

## What this file is

This is a cleaned work note derived from the fourth embedded lesson in `motors.md` (raw source note removed from the repository).

Approximate source range:

- `13:12` to `21:58`

## Topic focus

This segment explains how pole count affects synchronous speed, how speed-torque curves are read, and how NEMA design letters describe induction-motor behavior.

## Main concepts captured

### 1. Pole count changes synchronous speed

- The transcript uses the standard synchronous-speed relationship `120 x f / p`.
- More poles reduce synchronous speed for the same supply frequency.
- Inference from the examples: the lesson presents added pole count as one way to obtain a motor suited for slower, higher-torque duty.

### 2. The training distinguishes several torque regions on the speed-torque curve

The named regions are:

- starting torque
- pull-up torque
- breakdown torque
- rated-torque operating region

### 3. Breakdown torque is the maximum torque point

- The transcript states that breakdown torque is the greatest torque the motor can produce.
- If the motor is pushed beyond that point, speed falls sharply and stalling risk rises.

### 4. Load increase drives current increase and more slip

- The lesson explicitly connects increasing load with increased current draw and higher developed torque up to the breakdown region.
- It also notes that overload protection is needed because sustained overload can overheat the stator.

### 5. NEMA designs describe characteristic starting and slip behavior

The segment summarizes:

- `Design A`: low slip, no mandated starting-current limit, efficient general-duty behavior
- `Design B`: most common general-purpose design with limited starting current
- `Design C`: high breakaway-torque applications such as conveyors and positive-displacement pumps
- `Design D`: very high locked-rotor-torque, higher-slip applications such as cranes, hoists, and stamping presses

## Working takeaway

This segment is a selection-oriented note:

- pole count influences speed
- torque curves show how the motor behaves during acceleration and overload
- NEMA design letters help match motor behavior to load type

## Important caution

This file is a transcript-derived work note. Actual motor selection still depends on the full nameplate, driven-load profile, starting method, ambient conditions, and control approach.
