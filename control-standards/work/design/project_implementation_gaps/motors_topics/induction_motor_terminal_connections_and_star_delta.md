<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: INDUCTION_MOTOR_OVERVIEW
-->

# Induction Motor Terminal Connections and Star-Delta

## What this file is

This is a cleaned work note derived from the first embedded lesson in `motors.md` (raw source note removed from the repository).

Approximate source range:

- `8:55` to `15:27`

## Topic focus

This segment covers the six-terminal layout of a three-phase induction motor and explains the difference between delta and star (`wye`) connections.

## Main concepts captured

### 1. The terminal box exposes both ends of the three stator windings

- The transcript identifies six terminals: `U1`, `V1`, `W1`, `W2`, `U2`, and `V2`.
- Each phase winding terminates on its matching letter pair.

### 2. Delta connection closes the circuit phase-to-phase

- The transcript gives the bridge pattern as `U1-W2`, `V1-U2`, and `W1-V2`.
- In this arrangement each winding is connected directly between two phases.

### 3. Star connection ties one end of all three windings together

- The source describes joining `W2`, `U2`, and `V2` on one side.
- That common point becomes the star point or neutral point.

### 4. Delta exposes each winding to line-to-line voltage

- In the worked example the supply is `400 V` line-to-line and each winding also sees `400 V`.
- With a stated winding impedance of `20 ohms`, the transcript calculates `20 A` in each winding.
- It then states the line current is `sqrt(3)` times the winding current, giving about `34.6 A`.

### 5. Star reduces winding voltage and current

- With the same `400 V` line-to-line supply, the transcript states each winding sees about `230 V`, found by dividing by `sqrt(3)`.
- Using the same `20 ohm` winding impedance, the winding current becomes `11.5 A`.
- In the transcript's example, the line current is also `11.5 A`.

### 6. The practical comparison is lower stress in star than delta

- The lesson's main design takeaway is that star uses lower winding voltage and lower current than delta for the same line-to-line supply.
- That is why star and delta behave differently during starting or when matching a motor to a supply system.

## Working takeaway

This segment is mainly a wiring and relationship note:

- delta: winding sees line voltage
- star: winding sees line voltage divided by `sqrt(3)`
- the current relationships also differ between the two connection types

## Important caution

This file is a transcript-derived work note. Actual motor connection, starting method, and allowable supply voltage must be verified from the motor nameplate, winding data, and OEM documentation before energizing equipment.
