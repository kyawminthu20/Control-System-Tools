<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: TRANSCRIPT_SEGMENT_NORMALIZED
CATEGORY: FUNDAMENTALS
-->

# EGC Sizing and Table 250.122 Notes

## What this file is

This is a cleaned work note derived from the sizing discussion in [types of equipment ground conductors.md](../types%20of%20equipment%20ground%20conductors.md).

Approximate source range:

- `5:53` to `9:56`

## Topic focus

This segment connects equipment grounding conductor sizing to fault-clearing performance and the note under Table `250.122`.

## Main concepts captured

### 1. The transcript uses a fault-current example

- A sample circuit is discussed where the equipment grounding conductor is sized from Table `250.122` based on the overcurrent device.
- The speaker then walks through an example calculation showing that the resulting fault current should be high enough to open the breaker.

### 2. Table 250.122 is treated as the baseline sizing rule

- The discussion frames Table `250.122` as the normal starting point for EGC sizing.
- The table is tied to the rating of the overcurrent device protecting the circuit.

### 3. The note under Table 250.122 matters

- The transcript specifically calls out the note that the EGC must be increased in size where necessary to comply with `250.4(A)(5)`.
- The practical point is that a table-minimum conductor is not automatically enough in every installation.

### 4. The deeper question is fault-clearing performance

- The speaker keeps returning to the idea that the path must have low enough impedance and enough current-carrying capability to trip the protective device.
- The transcript also notes that the NEC text does not hand you one simple universal clearing-time target in this context.

## Working takeaway

This segment is best read as a design caution:

- start with Table `250.122`
- then ask whether the resulting path still satisfies the effective-fault-path purpose of `250.4(A)(5)`
- long runs or unusual conditions may force a larger EGC than the table minimum

## Related repo references

- [NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md](../../../rag/standards_intelligence/us/nec/NEC_2023__Art250_4__purposes_of_grounding_and_bonding.md)
- [NEC_2023__Art250__grounding_and_bonding.md](../../../rag/standards_intelligence/us/nec/NEC_2023__Art250__grounding_and_bonding.md)

## Important caution

This note captures the teaching logic from the transcript. Final sizing should be verified against the actual NEC table, note language, and the characteristics of the protective device involved.
