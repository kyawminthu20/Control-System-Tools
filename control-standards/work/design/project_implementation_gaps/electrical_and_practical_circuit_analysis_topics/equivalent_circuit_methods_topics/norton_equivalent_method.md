<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: EQUIVALENT_CIRCUIT_METHODS
-->

# Norton Equivalent Method

## What this file is

This is a cleaned work note derived from the Norton-theorem portion of [source_transformation_and_equivalent_methods.md](../source_transformation_and_equivalent_methods.md).

Approximate source range in the original lesson:

- `1:20:47` to `1:26:09`

## Topic focus

This segment explains how to replace a black-box resistive network with one equivalent current source and one equivalent parallel resistance.

## Main concepts captured

### 1. Norton is the current-source dual of Thevenin

- The transcript presents Norton as the parallel form corresponding to the Thevenin series form.
- Both describe the same terminal behavior when constructed correctly.

### 2. The equivalent resistance is found the same way as Thevenin resistance

- remove the load resistor
- zero the independent sources
- short voltage sources
- open current sources
- find the equivalent resistance seen at the output terminals

### 3. The Norton current comes from the short-circuit condition

- remove the load resistor
- short the output terminals
- solve for the short-circuit current through that external short
- treat that current as `In`

### 4. Source transformation can simplify the current calculation

- In the transcript example, a current-source-plus-parallel-resistor block is transformed into a series voltage-source form to make the KVL easier.
- This shows the two methods working together rather than as isolated topics.

### 5. The Norton form can make parallel-load reasoning very direct

- Once `In` and `Rn` are known, the load can be reconnected.
- The transcript then finds the final load voltage by using equivalent parallel resistance and `V = I x R`.

## Working takeaway

Norton is most useful when:

- current at the output is the more natural quantity
- the load is naturally thought of as a parallel element
- a current-source view makes the remaining circuit shorter to solve

## Important caution

This file is a transcript-derived work note. As presented, the method assumes ideal independent sources and linear resistive behavior.
