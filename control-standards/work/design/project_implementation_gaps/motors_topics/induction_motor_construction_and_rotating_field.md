<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: INDUCTION_MOTOR_OVERVIEW
-->

# Induction Motor Construction and Rotating Field

## What this file is

This is a cleaned work note derived from the first embedded lesson in `motors.md` (raw source note removed from the repository).

Approximate source range:

- `0:00` to `8:54`

## Topic focus

This segment explains the physical parts of a three-phase squirrel-cage induction motor and the basic electromagnetic reason the rotor turns.

## Main concepts captured

### 1. The motor is a mechanical assembly built around heat removal and shaft support

- The transcript identifies the housing, shaft, fan, cooling fins, bearings, and end shields.
- Cooling is treated as essential because excessive temperature damages winding insulation and can destroy the motor.

### 2. The stator is the stationary magnetic system

- The stator contains insulated copper windings placed in slots around the inner circumference.
- In this lesson the motor is explicitly a three-phase machine with three separate winding groups.

### 3. The rotor is a squirrel-cage structure

- The rotor uses end rings and bars to form a closed conductive cage.
- Laminated steel sheets are used to concentrate flux and reduce eddy-current losses.

### 4. Current in conductors creates magnetic fields

- The lesson walks from straight-conductor magnetic fields to coils, then to interacting fields and force on conductors.
- AC reverses current direction, so the magnetic field also changes direction and strength over time.

### 5. Three displaced stator phases create a rotating field

- The transcript explains that three coil groups spaced `120 degrees` apart and energized by different phases produce the effect of a rotating electromagnetic field.
- That rotating field induces current in the rotor bars.

### 6. Rotor current creates rotor field and torque

- Because the rotor bars are shorted by the end rings, induced voltage causes current to flow in the rotor.
- The rotor magnetic field interacts with the stator field and the rotor turns in an attempt to align with the rotating field.
- The lesson emphasizes that the rotor never fully catches the rotating field.

### 7. Skewed rotor bars help avoid magnetic locking

- The source notes that rotor bars are often skewed.
- The stated purpose is to spread the magnetic interaction across multiple bars and reduce the tendency to align and jam.

## Working takeaway

This segment gives the basic mental model for induction motors:

- the stator creates the rotating magnetic field
- the rotor receives induced current rather than direct electrical supply
- torque comes from the interaction between those two magnetic systems

## Important caution

This file is a transcript-derived work note. It is an instructional overview and does not cover nameplate limits, starting methods, insulation class, or protection requirements in enough detail for design decisions.
