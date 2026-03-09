<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: EQUIVALENT_CIRCUIT_METHODS
-->

# Superposition Theorem Notes

## What this file is

This is a cleaned work note derived from the superposition portion of [source_transformation_and_equivalent_methods.md](../source_transformation_and_equivalent_methods.md).

Approximate source range in the original lesson:

- `1:26:10` to `1:34:05`

## Topic focus

This segment explains how to solve a circuit with multiple independent sources by analyzing one source contribution at a time.

## Main concepts captured

### 1. Superposition separates source contributions

- The transcript frames each independent source as contributing part of the total current or voltage.
- Instead of solving the whole circuit at once, the method solves one-source cases and adds the results.

### 2. The process is procedural

- keep one independent source active
- set the other independent sources equal to zero
- solve the required current or voltage
- repeat for the next source
- add the separate contributions algebraically

### 3. Source-zeroing follows the same ideal rules used elsewhere

- voltage sources are shorted when set to zero
- current sources are opened when set to zero

### 4. Naming discipline matters

- The transcript recommends using prime notation to distinguish the separate contributions, such as first-source and second-source versions of the same variable.

### 5. The method works best when the one-source subproblems become simple

- In the example, one reduced circuit becomes a current-divider problem.
- The other becomes a simple voltage-divider problem.
- That is the key value of superposition in the lesson.

## Working takeaway

Use superposition when:

- there are multiple independent sources
- the combined circuit looks messy
- each one-source version of the circuit becomes much easier to solve

## Important caution

This file is a transcript-derived work note. The closing spoken arithmetic in the example appears internally inconsistent, so any worked numeric result from that example should be checked independently before reuse.
