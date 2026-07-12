<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: algorithms_equipment_staging
LEARNING_LEVEL: intermediate

TOPIC: Data-structure algorithms in PLC applications — FIFO queues, conveyor
shift registers, sorting at PLC scale — and the equipment-staging family:
lead-lag selection, demand-based staging, runtime equalization, sequenced
starts, failed-to-start replacement, and load shedding.

INDEX_TAGS:
  topics: ["fifo", "circular_buffer", "shift_register", "product_tracking", "bubble_sort", "index_sort", "lead_lag", "runtime_staging", "demand_staging", "hysteresis", "anti_hunting", "runtime_equalization", "start_count_balancing", "round_robin", "first_available", "priority_selection", "capacity_staging", "start_delay_sequencing", "failed_to_start", "load_shedding", "alarm_queue", "staging_function_block"]
  systems: ["plc", "pumps", "compressors", "fans", "chillers", "conveyors", "water_wastewater", "iec_61131_3"]
  standards: ["IEC 61131-3"]
-->

# PLC Algorithms & Equipment Staging

Most PLC logic is reactive: inputs in, interlocks evaluated, outputs out. But a
surprising amount of real application code is **data-structure work** — queues
that remember which product entered first, arrays that rank pumps by runtime,
buffers that hold the last hundred events. These algorithms rarely appear in
introductory PLC training, yet they are the difference between a program that
handles one pump and a program that manages a pump *station*.

This note covers the two families that come up most often: **queue and sorting
algorithms** (FIFO, shift registers, bubble sort, index ranking) and the
**equipment-staging family** (lead-lag, demand staging, runtime equalization,
sequenced starts, failed-start recovery, load shedding). All code fragments are
illustrative pseudocode with invented tag names — not platform code. Consult
your platform's documentation for the exact instructions and library blocks.

## Why data-structure algorithms appear in PLC code at all

Three recurring plant problems force them in:

1. **Order matters.** Products on a conveyor, jobs for a machine, batches for a
   reactor — something entered first and should leave first (or by priority).
   That is a queue.
2. **History matters.** Alarm sequences, recent samples, event logs — the
   controller needs a bounded memory of what happened. That is a circular
   buffer.
3. **Fairness matters.** Multiple identical pumps, fans, or compressors serve
   one duty, and running the same unit until it wears out while its twin sits
   idle is poor asset management. Choosing which unit runs next is a ranking
   and selection problem.

A rough map of algorithm to purpose:

| Algorithm | Typical purpose | Typical language fit |
|---|---|---|
| FIFO queue | Product tracking, job queues, alarm buffering | Ladder or ST |
| Circular buffer | Recent samples, event history | ST |
| Shift register | Position-indexed conveyor tracking | Ladder |
| Sorting / ranking | Order equipment by runtime, jobs by priority | ST |
| Runtime staging | Lead-lag pumps, compressors, fans | Ladder + ST |
| Round-robin | Alternate equipment on each cycle | Ladder |
| Priority queue | Serve the highest-priority request first | ST |
| Load shedding | Drop loads by priority on a demand limit | Ladder/ST |

The "language fit" column is guidance, not a rule — see the closing section on
Ladder versus Structured Text.

## FIFO queues

**First In, First Out**: the earliest value loaded is the first value unloaded.
The queue preserves arrival order, which is exactly what physical processes
usually need — the first carton onto the conveyor is the first to reach the
labeller.

Typical applications: conveyor and pallet product tracking, machine job queues,
recipe request queues, barcode buffering between a scanner and its use point,
production-order sequencing, and alarm/event buffering before a SCADA system
collects the entries.

### Generic FIFO (illustrative pseudocode — not platform code)

A FIFO needs an array, a write index, a read index, and a count:

```
(* load: only when there is room *)
IF LoadRequest AND (QueueCount < QueueSize) THEN
    Queue[WriteIndex] := NewValue;
    WriteIndex := WriteIndex + 1;
    IF WriteIndex >= QueueSize THEN WriteIndex := 0; END_IF;
    QueueCount := QueueCount + 1;
END_IF;

(* unload: only when there is something to take *)
IF UnloadRequest AND (QueueCount > 0) THEN
    RemovedValue := Queue[ReadIndex];
    ReadIndex := ReadIndex + 1;
    IF ReadIndex >= QueueSize THEN ReadIndex := 0; END_IF;
    QueueCount := QueueCount - 1;
END_IF;
```

The index wrap-around turns a fixed array into a **circular buffer** — the
storage is reused endlessly without ever moving data. Guarding both operations
(full check on load, empty check on unload) is not optional polish; an
unguarded queue silently overwrites the oldest product ID or hands out stale
data, and both failures surface far downstream of the bug.

Load and unload requests should be **one-shot** (edge-triggered). A maintained
"product present" bit held true for three scans loads the same product three
times.

### Vendor instruction examples

Most platforms ship FIFO handling so you do not hand-roll the indexes — named
here purely as examples, with behaviour that differs per platform:

- **Rockwell (Logix)** — paired `FFL` (FIFO Load) and `FFU` (FIFO Unload)
  instructions operating on an array plus a CONTROL structure that tracks
  position and length.
- **Siemens (S7-1200/1500)** — FIFO/queue library blocks and application
  examples in the TIA Portal ecosystem.
- **Beckhoff (TwinCAT)** — ring-buffer function blocks in the standard PLC
  libraries.

The concepts above are portable; the instruction names, control structures, and
edge behaviours are not. Consult your platform's documentation.

## Conveyor shift-register tracking

When a conveyor has discrete positions and product advances one position per
machine cycle or encoder pulse, a **shift register** is simpler than a general
FIFO: the array index *is* the physical position.

```
Position:  0     1     2     3     4
Data:     [101] [ - ] [102] [ - ] [103]

after one shift pulse:
          [ - ] [101] [ - ] [102] [ - ]   (103 exits)
```

Every shift pulse moves each element one slot down the array; a new product ID
enters at position 0, and whatever falls off the far end is the product arriving
at the exit station. Ladder platforms provide bit-shift instructions for
single-bit tracking (Rockwell `BSL`/`BSR` are one example); for integer product
IDs the shift is a copy loop, illustrative pseudocode:

```
FOR Index := LastPosition TO 1 BY -1 DO
    TrackingArray[Index] := TrackingArray[Index - 1];
END_FOR;
TrackingArray[0] := NewProductID;
```

The shift must be edge-triggered from the encoder or cycle pulse — a maintained
trigger smears the whole array in a few scans.

### Richer records: structs in the buffer

Real tracking rarely needs just an ID. A product entry typically carries a
recipe number, a barcode, an inspection result, a reject flag, and a
destination. Define a structured type and queue the whole record
(illustrative):

```
TYPE ProductRecord :
STRUCT
    ProductID    : DINT;
    RecipeID     : INT;
    RejectFlag   : BOOL;
    Destination  : INT;
    EntryValid   : BOOL;
END_STRUCT;
END_TYPE

ProductQueue : ARRAY[0..49] OF ProductRecord;
```

Once records enter the picture, Structured Text is normally the clearer tool —
copying and inspecting structs in Ladder is possible but hard to read.

A queue is also a broader idea than FIFO: the same record array can be served
by arrival order, by a priority field, by machine availability, or by due date.
The storage pattern stays; only the selection rule changes.

## Sorting at PLC scale

Sorting means ordering data by some value: pumps by accumulated runtime, jobs
by priority, samples by magnitude. PLC arrays are small — three to perhaps a
few dozen equipment items — so algorithmic efficiency is largely irrelevant and
**bubble sort** — a short, easy-to-verify sort — is the honest workhorse
(illustrative):

```
FOR Pass := 0 TO ItemCount - 2 DO
    FOR Index := 0 TO ItemCount - 2 - Pass DO
        IF Value[Index] > Value[Index + 1] THEN
            TempValue        := Value[Index];
            Value[Index]     := Value[Index + 1];
            Value[Index + 1] := TempValue;
        END_IF;
    END_FOR;
END_FOR;
```

Two practical refinements matter more than the algorithm choice:

1. **Keep identity with the value.** Sorting a bare runtime array tells you the
   lowest runtime is 980 h but not *which pump* has it. Either sort whole
   equipment records (swap the structs), or better —
2. **Sort an index array and leave the data alone.** Initialize
   `Rank[0..N-1] := 0..N-1`, then sort `Rank[]` by comparing
   `Equipment[Rank[i]].RuntimeHr`. The result is a ranked list of equipment
   indexes — `Rank[0]` is the first choice — while every equipment record stays
   at its original, HMI-mapped, alarm-mapped address. This index-sort pattern
   is one of the most useful idioms in industrial programming:

```
IF Equipment[Rank[Index]].RuntimeHr >
   Equipment[Rank[Index + 1]].RuntimeHr THEN
    TempIndex       := Rank[Index];
    Rank[Index]     := Rank[Index + 1];
    Rank[Index + 1] := TempIndex;
END_IF;
```

Sorting in pure Ladder (compares, moves, temporary registers, indirect
addressing) is feasible but usually hard to read and harder to maintain;
Structured Text is normally the better choice here.

## The equipment-staging family

Staging is the heart of this module. The scenario: several similar units —
pumps, compressors, chillers, cooling-tower fans, boilers, generators — share
one duty, and the program must decide **how many** run and **which ones**. The
goals, common to every variant:

1. Run enough units to meet demand.
2. Balance wear (runtime and start counts) across units.
3. Skip faulted, unavailable, or in-maintenance units.
4. Respect minimum run and minimum stop times.
5. Prevent simultaneous starts (inrush).
6. Rotate the lead role so no unit is permanently first.

### Lead-lag selection by runtime

The classic rule: among the units that are available, not faulted, not in
maintenance, and past their minimum off-time, select the one with the **lowest
accumulated runtime** as the next lead. Illustrative selection scan:

```
SelectedUnit  := -1;
LowestRuntime := 3.4E38;   (* larger than any real value *)

FOR Index := 0 TO UnitCount - 1 DO
    IF Unit[Index].Available
       AND NOT Unit[Index].Faulted
       AND Unit[Index].MinOffTimeDone THEN
        IF Unit[Index].RuntimeHr < LowestRuntime THEN
            LowestRuntime := Unit[Index].RuntimeHr;
            SelectedUnit  := Index;
        END_IF;
    END_IF;
END_FOR;
```

`SelectedUnit = -1` after the loop means *no unit qualified* — that condition
deserves its own alarm, not a silent no-op. The selection typically lives in
Structured Text; the actual start commands, permissives, and feedback checks
typically live in Ladder rungs gated on the selected index.

### Demand-based staging: stage up and down on load

How many units should run is a function of demand — level, pressure, flow, or a
PID output. A constructed teaching example for three pumps (all thresholds and
times are examples, not requirements — tune per application):

```
demand > 70% for 30 s  → stage up to 2 pumps
demand > 90% for 30 s  → stage up to 3 pumps
demand < 75% for 60 s  → stage down to 2 pumps
demand < 45% for 60 s  → stage down to 1 pump
```

Two protections prevent **hunting** (rapid start/stop cycling):

- **Dead-band (hysteresis)** — the stage-down threshold sits well below the
  stage-up threshold for the same stage. If stage 2 starts above 70 % and
  stopped above 65 %, normal demand ripple would cycle the pump continuously.
- **Delays** — an on-delay before staging up and a (typically longer) off-delay
  before staging down, so momentary spikes and dips are ignored.

Minimum run time and minimum stop time per unit are the third layer of the same
protection, guarding the equipment itself rather than the stage logic.

### Runtime accumulation

Staging by runtime requires trustworthy runtime. Accumulate while the
**confirmed running feedback** is true — never from the start command, which
counts hours a failed motor never ran. Illustrative:

```
IF Unit.RunningFeedback THEN
    Unit.RuntimeSeconds := Unit.RuntimeSeconds + TaskPeriodSeconds;
END_IF;
Unit.RuntimeHr := DINT_TO_REAL(Unit.RuntimeSeconds) / 3600.0;
```

Design considerations: make the accumulator **retentive** across power cycles;
guard against overflow; provide an authorized way to correct values after
maintenance (a replaced motor starts at zero; the pump casing does not); and
keep **lifetime** runtime and **since-maintenance** runtime as separate tags,
along with a start counter.

### Runtime equalization

Balancing works on both edges: **start the lowest-runtime available unit;
stop the highest-runtime running unit.** Over many cycles the accumulated
hours converge. The stop decision still has to respect minimum run time,
process suitability, and capacity — the highest-runtime unit is not stoppable
if it is the only one large enough for the current load.

### Start-count balancing

Runtime alone can mislead. Two pumps with near-equal hours may have wildly
different start counts, and for some equipment (compressors especially) starts
age the machine more than hours do. A weighted selection score handles both
(illustrative; weights are engineering judgment, not constants):

```
Unit[Index].SelectionScore :=
      Unit[Index].RuntimeHr * RuntimeWeight
    + DINT_TO_REAL(Unit[Index].StartCount) * StartWeight;
```

Select the lowest score. Choosing the weights is application engineering — how
much one start "costs" relative to one hour differs by equipment type.

### The simpler selection rules

- **Round-robin** — advance a lead index each cycle (1 → 2 → 3 → 1), skipping
  unavailable units. No runtime data needed; wear balance is approximate.
- **First-available** — scan from index 0 and take the first qualifying unit.
  Trivial to write, but unit 1 accumulates far more hours than unit 3.
- **Fixed lead-lag** — permanently assigned roles (Pump 1 lead, Pump 2 lag,
  Pump 3 standby). Simple and predictable; no automatic wear balancing, so
  rotation happens by manual reassignment or not at all.
- **Priority-based** — select by an operating-priority field first (normal-duty
  units before old units before rental units), then by runtime within the
  priority group. Two-key comparison in one selection loop.
- **Capacity-based** — when units differ in size (two 100-unit pumps and one
  200-unit pump), the program evaluates *combinations* against required
  capacity rather than just counting units. This edges toward optimization —
  energy cost, minimum-flow limits, start counts — and is normally Structured
  Text or a supervisory-layer job, not pure Ladder.

### The staging state machine

A robust staging controller does not switch outputs directly from demand
comparisons. It runs a state machine: determine required capacity → select the
next unit → issue the start → **wait for running feedback** → confirm the stage
→ (on stage-down) select the unit to stop → issue the stop → wait for stopped
feedback, with a fault path out of every waiting state. Sequencing through
explicit states is what prevents three pumps from being commanded in the same
scan and gives failed starts somewhere to be handled. State-machine design
itself — steps, transitions, one-shots, fault states — is covered in the
`state_machines` module of this family; the staging controller is simply a
disciplined application of it.

### Start-delay sequencing

Large motors starting together stack their inrush currents. Stagger the
starts: command unit 1, wait for its running feedback plus a spacing delay
(a few seconds to tens of seconds, sized per application and utility limits),
then command unit 2. Keying the delay from **confirmed feedback** rather than
from the previous start command means a failed start pauses the sequence
instead of piling the next unit onto a fault.

### Failed-to-start replacement

When a commanded unit produces no running feedback within a timeout:

1. Latch a failed-to-start alarm for that unit.
2. Mark it unavailable (remove it from the selection pool).
3. Re-run the selection and promote the next-ranked unit.
4. Start the replacement through the same sequenced path.

```
IF StartTimeout AND NOT Unit[SelectedUnit].RunningFeedback THEN
    Unit[SelectedUnit].StartFailed := TRUE;
    Unit[SelectedUnit].Available   := FALSE;
    ReselectRequired               := TRUE;
END_IF;
```

Do not retry the same failed unit in a loop without a deliberate retry policy —
hammering a motor that will not start is how one fault becomes two.

### Load-shedding queue

The same priority-queue machinery runs in reverse for electrical demand
management. Loads carry shed priorities (nonessential HVAC first, critical
process equipment last). When demand exceeds a limit: shed the lowest-priority
group, wait a re-evaluation delay, shed the next group only if still needed.
Restoration proceeds in **reverse order** with delays between steps, so the
restored load does not immediately re-trip the limit. Structurally this is a
priority queue driving a small state machine.

### Alarm queue

An alarm buffer in the PLC is a circular buffer of event records — alarm ID,
timestamp, priority, active and acknowledged flags. It is legitimate as a
*buffer*: catching bursts and bridging communication gaps until SCADA collects
the events. It is a poor *database*: long-term storage, sorting, filtering, and
history belong in the SCADA/HMI/historian layer. The PLC detects and reports;
it should not try to be the alarm system of record.

## Ladder or Structured Text?

The general language-choice question belongs to the `languages_overview`
module; for this specific algorithm family the split is unusually clean:

- **Ladder** suits the event edges and the physical layer: load/unload
  one-shots, full/empty status, start permissives, staging delay timers,
  failed-start detection rungs, and the actual output commands — everything a
  maintenance electrician troubleshoots live.
- **Structured Text** suits the array work: sorting, ranking, weighted scores,
  circular-buffer index math, record management, and capacity combinations —
  everything with a loop in it.

A common and effective split is Ladder for commands, interlocks, and feedback;
ST for the FIFO manager, the ranking routine, and the staging selector.

## Wrap it in one function block

The key structural recommendation: put the whole staging brain in **one
reusable function block** with a clean interface, rather than scattering
selection logic across the program. Illustrative interface:

```
FB_EquipmentStaging
  inputs:  Enable, RequiredUnits (or RequiredCapacity),
           per-unit: Available[], Running[], Faulted[],
                     RuntimeHr[], StartCount[], Priority[]
  outputs: StartRequest[], StopRequest[],
           SelectedLead, ActiveUnitCount,
           AvailableUnitCount, CapacityShortfall
  inside:  availability filter → ranking → start/stop selection
           → sequencing delays → failed-start recovery
```

One block means one place to test the ranking rules, one instance per pump
station, and a program where the Ladder around it reads as plain commands and
feedback. Function-block design itself — interfaces, instance data, scope — is
the `program_structure` module's territory.

The overall pipeline every variant follows:

```
demand calculation
  → required unit count / capacity
  → availability filtering
  → ranking (runtime / score / priority)
  → start-stop selection
  → sequenced commands (staggered, feedback-verified)
  → alarm and fallback handling
```

Resist the temptation to compress that pipeline into one large rung.

## Sources

- IEC 61131-3, Programmable controllers — Part 3: Programming languages.
  https://webstore.iec.ch/en/publication/68533
- Rockwell Automation, Logix 5000 instruction reference — FIFO Load (FFL).
  https://www.rockwellautomation.com/en-us/docs/studio-5000-logix-designer/38-01/contents-ditamap/instruction-set/array--file--shift-instructions/fifo-load--ffl-.html
- Siemens Industry Online Support, Programming queues (FIFO) for S7-1200/S7-1500.
  https://support.industry.siemens.com/cs/mdm/109742272
- Siemens, Programming Guideline for S7-1200/S7-1500.
  https://support.industry.siemens.com/cs/attachments/90885040/81318674_Programming_guideline_DOC_v16_en.pdf
- Beckhoff Information System, TwinCAT 3 PLC library documentation (function
  blocks, ring buffers). https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2530279563.html
