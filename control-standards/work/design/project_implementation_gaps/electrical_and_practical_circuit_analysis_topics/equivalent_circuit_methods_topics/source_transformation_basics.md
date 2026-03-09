<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: EQUIVALENT_CIRCUIT_METHODS
-->

# Source Transformation Basics

## What this file is

This is a cleaned work note derived from the source-transformation portion of [source_transformation_and_equivalent_methods.md](../source_transformation_and_equivalent_methods.md).

Approximate source range in the original lesson:

- `1:09:31` to `1:11:39`

## Topic focus

This segment introduces the idea that a voltage-source form and a current-source form can describe the same external behavior.

## Main concepts captured

### 1. Two common equivalent source forms are introduced

- A Thevenin-style form is a voltage source in series with a resistor.
- A Norton-style form is a current source in parallel with a resistor.

### 2. Source transformation converts between those forms

- The resistor value stays the same in the conversion.
- The conversion is based on Ohm's law.

### 3. The core conversion relationships are simple

- `V = I x R` gives the equivalent voltage when starting from the current-source form.
- `I = V / R` gives the equivalent current when starting from the voltage-source form.

### 4. The point is simplification, not changing behavior

- The transcript emphasizes that the transformed source should behave identically at its terminals.
- The benefit is that one form may be easier to analyze in the surrounding circuit than the other.

## Working takeaway

Use source transformation when a source-resistor pair looks awkward in its current form:

- convert series voltage-source forms into parallel current-source forms when branch current thinking is easier
- convert parallel current-source forms into series voltage-source forms when loop or divider thinking is easier

## Important caution

This file is a transcript-derived work note. The method assumes ideal independent sources and a valid source-resistor pairing viewed from the same two terminals.
