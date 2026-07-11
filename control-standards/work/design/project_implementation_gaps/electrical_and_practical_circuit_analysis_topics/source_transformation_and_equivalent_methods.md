<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: EQUIVALENT_CIRCUIT_METHODS
-->

# Source Transformation and Equivalent Methods

## What this file is

This is a cleaned work note derived from the final analysis-method section of `electrical and practical circuit analysis.md` (raw source note removed from the repository).

Approximate source range:

- `1:09:31` to `1:34:05`

## Topic focus

This segment groups several higher-level simplification tools: source transformation, Thevenin equivalents, Norton equivalents, and superposition.

## Main concepts captured

### 1. Source transformation converts between equivalent source forms

- A voltage source in series with a resistance can be converted into a current source in parallel with the same resistance.
- The reverse conversion also works.
- The purpose is not to change the circuit behavior seen at the terminals, but to make later analysis easier.

### 2. Thevenin equivalents reduce a network to one source and one resistance

The transcript's procedure is:

- remove the load
- zero the independent sources to find `Rth`
- find the open-circuit terminal voltage to get `Vth`
- reconnect the load and solve the simplified circuit

### 3. Norton equivalents are the current-source dual of Thevenin

The procedure parallels Thevenin:

- remove the load
- zero the independent sources to get `Rn`
- short the output terminals and solve for short-circuit current to get `In`
- reconnect the load and solve the simplified network

### 4. Superposition isolates one source at a time

- Each independent source is considered alone while the others are set to zero.
- The desired current or voltage contribution is solved for each single-source case.
- The separate contributions are then added algebraically.

### 5. The real skill is choosing the fastest reduction path

- The speaker repeatedly emphasizes that the methods are individually manageable.
- The harder part is deciding which method or combination of methods makes the problem shortest and cleanest.

## Working takeaway

These methods are best treated as simplification tools, not just textbook theorems:

- use source transformation to clean up awkward source-resistor blocks
- use Thevenin or Norton when a load sits on the edge of a larger network
- use superposition when multiple independent sources make direct analysis messy

## Important caution

This file is a transcript-derived work note. The closing superposition example appears to contain an internal arithmetic or sign inconsistency in the spoken result, so any worked values from that segment should be verified independently before reuse.
