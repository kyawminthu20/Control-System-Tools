<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: SPECIAL_APPLICATIONS
-->

# Voltage Drop - Fire Pump Notes

## What this file is

This is a cleaned work note derived from the fire-pump portion of the voltage-drop transcript in [check_this.md](../check_this.md).

Approximate source range:

- `19:28` to `28:22`

## Topic focus

This section discusses fire-pump conductor sizing and why fire-pump voltage-drop evaluation is not handled like ordinary branch-circuit voltage-drop work.

## Main concepts captured

### 1. Fire-pump conductor ampacity is not the hard part

- The transcript treats basic fire-pump conductor ampacity sizing as straightforward compared with the voltage-drop portion.
- The more difficult part is evaluating starting conditions.

### 2. Starting voltage matters at the controller

- The discussion references NEC `695.7` and focuses on voltage at the fire-pump controller line terminals.
- The transcript distinguishes starting-condition limits from running-condition limits.

### 3. Fire-pump starting current changes the calculation problem

- The transcript explains that motor starting current is much higher than running current.
- It also emphasizes that power factor changes significantly during starting.

### 4. Reactance and impedance matter

- The discussion says ordinary simplified voltage-drop methods are not enough for this situation.
- The working model includes:
  - AC resistance
  - reactance
  - impedance
  - starting power factor

### 5. This is presented as engineering work

- The transcript explicitly warns that fire-pump starting-voltage calculations are not something to do casually with normal field shortcuts.
- The stated recommendation is to use the proper engineering method or software/spreadsheet inputs that include reactance and power factor.

## Working takeaway

This segment should be treated as a special-application warning:

- do not treat fire-pump voltage drop like ordinary branch-circuit voltage-drop math
- starting conditions matter more than normal running assumptions
- reactance and power factor cannot be ignored

## Verification path

Verify final fire-pump design work directly against:

- NEC `695.7`
- the controller and motor manufacturer data
- the engineering method used for impedance and starting-condition analysis

## Important caution

This file is transcript-derived work material.

It is useful as a scoping note, but not sufficient by itself for fire-pump design or compliance decisions.
