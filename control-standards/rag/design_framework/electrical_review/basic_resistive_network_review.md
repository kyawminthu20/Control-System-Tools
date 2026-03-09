<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Basic Resistive Network Review

## 0. When to use this review

Use this for simple DC or steady-state resistive networks where the main goal is to confirm topology, divider behavior, and power dissipation before overcomplicating the analysis.

## 1. Step 1: Identify topology

Classify the network first:

- series
- parallel
- mixed series-parallel
- divider with a load attached

If the topology is misread, the rest of the calculation will usually be wrong.

## 2. Step 2: Simplify what is obvious

- add series resistances directly
- reduce parallel resistances with the reciprocal relationship
- collapse the network in stages before solving branch values

## 3. Step 3: Check divider loading

If a divider output feeds a real load, verify whether the load materially changes the intended voltage.

Useful quick check:

- if load impedance is not much larger than the divider leg it is attached to, assume the output will shift and calculate the loaded value

## 4. Step 4: Verify power ratings

For each resistor carrying meaningful drop or current, check power with one of:

- `P = I^2 x R`
- `P = V^2 / R`
- `P = V x I`

Then confirm margin above the calculated dissipation.

## 5. Common mistakes

- assuming series when the nodes do not support series current
- assuming a no-load divider equation with a substantial attached load
- checking resistance but not wattage
- forgetting that parallel equivalent resistance is lower than the smallest branch resistance

## 6. Escalation point

If the network contains multiple interacting sources or cannot be simplified cleanly, switch to nodal, loop, Thevenin, or Norton methods.
