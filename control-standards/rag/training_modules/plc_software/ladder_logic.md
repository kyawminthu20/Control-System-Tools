<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: ladder_logic
LEARNING_LEVEL: beginner-intermediate

TOPIC: Ladder Diagram fundamentals — rungs and rails, contacts/coils/latches,
timers and counters, series-AND/parallel-OR logic, the seal-in circuit,
physical-vs-logical input meaning, I/O mapping discipline, command/status/feedback
separation, scan-order effects, one-shots, retentive data, alarm conditioning,
analog scaling, and the common design mistakes.

INDEX_TAGS:
  topics: ["ladder_diagram", "ladder_logic", "contacts_coils", "xic_xio_ote", "latch_unlatch", "seal_in", "start_stop_circuit", "timers_counters", "one_shot", "scan_order", "last_write_wins", "io_mapping", "command_feedback", "failed_to_start", "retentive_data", "alarm_hysteresis", "analog_scaling", "fail_safe_wiring"]
  systems: ["plc", "machine", "motor_control", "iec_61131_3"]
  standards: ["IEC 61131-3"]
-->

# Ladder Logic Fundamentals

Ladder Diagram (LD) is the graphical IEC 61131-3 language drawn as rungs between
two vertical power rails, deliberately shaped like the relay schematics it
replaced. Its instructions are simple; nearly everything that goes wrong in a
ladder program goes wrong in the *relationships* — evaluation order, who writes
which coil, whether an input's logical meaning matches its wiring, and whether a
command is ever confirmed by feedback. This note covers the element set and those
relationships. Language selection, program/task organization, and sequence design
are covered in the sibling modules (`languages_overview`, `program_structure`,
`state_machines`); safety application software is covered in
`safety_application_patterns`.

All ladder sketches below are illustrative ASCII renderings with invented tag
names, not platform code. Instruction mnemonics (XIC, OTE, TON…) vary by vendor —
Rockwell terms are used as examples only; consult your platform's documentation.

## 1. Rungs, rails, and evaluation order

A ladder routine is a list of horizontal **rungs** spanning a left and a right
**power rail**. Each rung is one logical statement: a chain of condition
instructions on the left resolving to a Boolean, which drives one or more output
instructions on the right.

```text
 Left rail                                      Right rail
    |                                               |
    |----[ Cond_1 ]----[ Cond_2 ]----( Output_A )---|
    |                                               |
    |----[ Cond_3 ]----------------( Output_B )-----|
```

The controller does not evaluate rungs simultaneously. Within one execution of a
routine, evaluation normally proceeds:

- **top to bottom** through the rungs, and
- **left to right** within each rung,

as one step inside the larger scan cycle (read inputs → execute logic → write
outputs → housekeeping → repeat). The scan model itself is treated in the
`program_structure` module; what matters here is that ladder logic is a
*sequential program wearing a circuit-diagram costume*. The visual metaphor of
current "flowing" through contacts is useful, but the semantics are those of
statements executed in order — which is exactly why scan-order effects (§9)
and duplicate coil writes (§10) behave the way they do.

## 2. Contacts, coils, and latches

**Normally open contact** `----[ Tag ]----` — true while the referenced Boolean
is 1 (Rockwell: XIC, "examine if closed").

**Normally closed contact** `----[/ Tag ]----` — true while the referenced
Boolean is 0 (Rockwell: XIO, "examine if open").

The crucial subtlety: these instructions examine a *bit in memory*, not a
physical contact. An NC *instruction* says nothing about the field device being
an NC *contact* — see §5.

**Output coil** `----( Tag )----` (Rockwell: OTE) writes the rung result every
scan: rung true → bit set, rung false → bit cleared. The coil follows its rung
continuously; it holds nothing.

**Set/reset (latch/unlatch)** `----(S Tag)----` / `----(R Tag)----`
(Rockwell: OTL/OTU) write the bit only when their rung is true, and only in one
direction. Once set, the bit stays set — through rung-false, and on many
platforms through a power cycle — until some rung explicitly resets it.

```text
|----[ Start_PB ]--------------------(S Motor_Request )----|   (illustrative)
|----[ Stop_PB ]---------------------(R Motor_Request )----|
```

Latch pairs are legitimate where a remembered state is genuinely needed, but
they carry recurring costs: the set and reset are usually on different rungs (or
in different routines), so the bit's life story is split across the program; a
latched bit with no reachable reset strands the machine in a state it cannot
leave; and a retained latch can wake up TRUE after a power cycle and command
something nobody asked for. For most run-command logic the seal-in pattern (§4)
is the better tool, because the holding condition and the breaking conditions
sit together on one rung. A common house rule: prefer OTE-with-seal-in; where a
latch is used, keep set and reset adjacent and account for the power-up value.

## 3. Timers, counters, comparison, and math

**Timers** measure how long a condition persists. An on-delay timer (TON)
accumulates while its rung is true and asserts a done bit when the accumulated
time reaches the preset; rung-false typically resets it. Typical structure
members: `PRE` (preset), `ACC` (accumulated), `EN` (enabled), `TT` (timing),
`DN` (done). Off-delay (TOF) and retentive (RTO) variants differ in reset
behavior — vendor-specific, verify against your platform.

```text
|----[ Motor_Run ]----[TON Warmup_Tmr  PRE 5s]----|      (illustrative)
|----[ Warmup_Tmr.DN ]------------( Warmup_Done )-|
```

**Counters** count events: a count-up (CTU) increments each scan its rung
*transitions* false→true, and asserts `DN` when `ACC` reaches `PRE`. Because
the increment is edge-based on the rung, driving a counter from a maintained
condition without a one-shot produces one count per scan, not per event —
see §11.

**Comparison instructions** (equal, not-equal, greater, less, and the
or-equal variants) turn an analog or integer relation into a rung condition:

```text
|----[ Tank_Level >= 80.0 ]----------( High_Level )----|   (illustrative)
```

**Math and move instructions** (add, subtract, multiply, divide, compute,
move) perform arithmetic on word/real data and store results — the workhorses
for scaling (§14), totals, and setpoint handling. In LD they execute when the
rung is true, which means a math rung with no conditions executes every scan.

## 4. Series = AND, parallel = OR, and the seal-in circuit

Contacts in series must all be true — Boolean AND. Contacts in parallel
(a branch) need only one true path — Boolean OR. Combinations nest:

```text
|----[ A ]----+----[ B ]----+----( Out )----|      Out = A AND (B OR C)
|             |             |
|             +----[ C ]----+
```

The signature ladder pattern combines both: the **start/stop seal-in circuit**.

```text
|----[/ Stop_PB ]----[/ Overload ]----+----[ Start_PB ]---+----( Motor_Run )----|
|                                     |                   |
|                                     +----[ Motor_Run ]--+
```

```text
Motor_Run = NOT Stop_PB AND NOT Overload AND (Start_PB OR Motor_Run)
```

Walk it through scan by scan:

1. **Idle.** Stop healthy, overload healthy, start not pressed, `Motor_Run`
   false. Neither parallel branch is true → rung false.
2. **Start pressed.** The `Start_PB` branch conducts; the series conditions
   pass; `Motor_Run` goes true this scan.
3. **Start released.** `Start_PB` drops out — but `Motor_Run` is now true, so
   its own contact in the parallel branch keeps the rung true. The output
   "seals in" (holding contact / self-holding contact).
4. **Stop or trip.** Either series condition breaking the chain forces the rung
   false, `Motor_Run` clears, and — because the seal branch is now also false —
   the rung stays false when the stop is released. Restarting requires a fresh
   start press.

The seal-in gives memory *without* a latch instruction, and the conditions that
break it are visible on the same rung — which is why it is generally preferred
for run commands. Note also its power-loss behavior: `Motor_Run` is an ordinary
coil, so after a power cycle it is false and the motor does not restart itself;
a latch-based equivalent may not share that property. One placement rule: seal
the *request/run-level* tag, not a physical output address, so the held state
can feed the output map, alarming, and HMI status coherently.

## 5. Physical input vs logical meaning — the NC-wired stop

The most safety-relevant idea in basic ladder work: **the instruction type
examines a bit; the wiring determines what that bit means.**

Stop buttons and most protective field contacts are wired **normally closed**,
so the healthy state holds the input energized:

```text
Circuit healthy (button not pressed):  Stop_Input = TRUE
Button pressed OR wire broken:         Stop_Input = FALSE
```

The ladder then uses a *normally open instruction* on that input as a run
condition:

```text
|----[ Stop_Input ]----( Stop_Healthy_Perm )----|    (illustrative)
```

This looks backwards to newcomers — an NO instruction for an NC button — but it
is precisely the point. The NC wiring makes the circuit **fail toward safe**: a
broken wire, a lost terminal, or a dead sensor supply looks the same as a
pressed stop button, and the machine stops. If the stop were wired NO and
examined with an NC instruction, the logic would read the same in the office —
and a broken stop wire would silently disable the stop function while the
machine kept running.

Keep five things mentally distinct on every field signal, because they do not
have to match: the physical contact type; the electrical state at the input
terminal; the PLC tag value; the instruction used to examine it; and the
process meaning ("OK to run"). Naming helps enormously — a tag named
`Stop_OK` or `EStop_Healthy` reads correctly with an NO instruction, where a
tag named `Stop` invites the wrong contact type.

(Hard-stop *safety* functions have wiring and controller requirements beyond
this fail-safe convention — see §16.)

## 6. I/O mapping: touch the hardware once, at the edges

Raw hardware addresses (`Local:1:I.Data.0` and friends) should appear in
exactly two places: an **input-mapping** section at the top of the program and
an **output-mapping** section at the bottom. Everything in between works on
descriptive internal tags.

```text
Input map:     |----[ Local:1:I.Data.0 ]-------( Start_PB )----|
Logic:         |----[ Start_PB ]----[ Stop_OK ]----[/ Motor_Fault ]----( Motor_RunCmd )----|
Output map:    |----[ Motor_RunCmd ]-----------( Local:2:O.Data.0 )----|
```

Why the discipline pays:

- **Hardware changes are one-line edits.** Rewire a point or swap a module and
  only the map changes; the logic never learns.
- **Simulation and dry-testing** become possible — force or drive the internal
  tags without fighting the physical I/O image.
- **Signal conditioning has a home.** Inversion of an NC-wired input into a
  positive-logic tag (§5), debounce, and validity checks belong in the map, so
  the logic downstream sees clean, correctly-named process meaning.
- **Troubleshooting splits cleanly** into "is the field signal reaching the
  tag?" (map) and "is the logic doing the right thing with it?" (logic).

This pairs with the numbered-routine convention (input map first, output map
last, logic between) described in the `program_structure` module.

## 7. Command, status, and feedback are three different things

`Motor_RunCmd` records that the PLC *asked* the motor to run. It proves nothing
about the motor. `Motor_RunningFB` — an auxiliary contact from the starter, a
drive status word bit — records that the equipment *reports* running. A current
or speed signal can add independent confirmation.

Keeping the three separate is what makes failure detectable: a robust design
compares command against feedback and alarms on disagreement within a time
window (see the failed-to-start rung in §8). Programs that treat the command
bit as "the motor is running" — driving interlocks, sequences, or HMI status
from it — cannot see a tripped starter, an open contactor coil circuit, or a
motor that never started, and will happily sequence downstream equipment onto
a stopped machine.

## 8. A complete simple motor control (constructed teaching example)

The layered pattern for a single motor, in rung form. All tags invented.

**Permissive chain** — the conditions that must be healthy before a start is
allowed (the definitions of permissive/interlock/trip live in the interlocks
module; this is just the ladder shape):

```text
|----[ Stop_OK ]----[ EStop_Healthy ]----[ Overload_OK ]----( Motor_Perm )----|
```

**Start request** — mode-selected, from either the local button or the process
sequence:

```text
|----+--[ Manual_Mode ]--[ Start_PB ]---------------+----( Motor_Req )----|
|    |                                              |
|    +--[ Auto_Mode ]----[ Seq_Start_Request ]------+
```

**Run command** — one rung, one writer, request gated by permissive:

```text
|----[ Motor_Req ]----[ Motor_Perm ]----( Motor_RunCmd )----|
```

**Failed-to-start detection** — command present, feedback absent, for longer
than the allowed start window:

```text
|----[ Motor_RunCmd ]----[/ Motor_RunningFB ]----[TON StartFail_Tmr  PRE 5s]----|
|----[ StartFail_Tmr.DN ]---------------------( Motor_FailedToStart )-----------|
```

The timer tolerates the normal second or two between contactor pull-in and
feedback; `DN` asserting means the command has gone unanswered too long. The
alarm bit then typically drops the request and requires an operator reset
before another attempt.

Read the structure, not the tag names: *permissives → request → command →
feedback verification*, each on its own rung, each rung with one purpose, and
the command written in exactly one place. Almost every device-control pattern
is a variation of this shape.

## 9. Scan-order effects

Because rungs execute in order, *where* a rung sits changes when its readers
see its result.

```text
Rung 1: |----[ Start ]---------( Run_Request )----|
Rung 2: |----[ Run_Request ]---( Motor_Output )---|
```

Here rung 2 sees the value rung 1 just wrote — same scan. Reverse the order and
`Motor_Output` reacts one scan late, because rung 1 (now the reader) executed
before the writer. One scan is usually milliseconds and often harmless; it
stops being harmless when the delayed bit is a one-shot (the edge can be
consumed before the reader runs), when several cross-ordered rungs accumulate
multi-scan delays, or when logic in different routines executes in an order
nobody chose deliberately.

The defense is direction: organize routines and rungs so data flows *downhill*
— inputs mapped first, then permissives/interlocks, then sequence, then device
commands, then output mapping — so producers execute before their consumers and
same-scan visibility is the norm rather than an accident.

## 10. Multiple writes to the same coil

An OTE coil writes its bit every scan — true *or false*. Put the same coil on
two rungs and the later rung's result silently overwrites the earlier one every
scan ("last write wins"):

```text
Rung 1: |----[ Auto_Start ]-----( Motor_RunCmd )----|   <- result discarded
Rung 2: |----[ Manual_Start ]---( Motor_RunCmd )----|   <- this one decides
```

With `Auto_Start` true and `Manual_Start` false, the motor never runs — rung 1
sets the bit, rung 2 immediately clears it. Nothing flags this; the first rung
simply stops mattering, and online monitoring shows a rung that is "true" while
its output is off — a genuinely confusing symptom. This is a defect, not a
style preference: it makes behavior depend on rung position, and it breaks the
troubleshooting assumption that the rung above a coil explains the coil.

The fix is to merge the conditions into one rung (parallel branches into a
request tag) and keep **one primary write location per command output**:

```text
|----+--[ Auto_Start ]----+----( Motor_Request )----|
|    |                    |
|    +--[ Manual_Start ]--+
|----[ Motor_Request ]----[ Motor_Perm ]----( Motor_RunCmd )----|
```

(Latch/unlatch pairs intentionally write one bit from two rungs — that is their
design. The rule targets unintentional duplicate OTE-style writes.)

## 11. One-shot (edge) operation

A one-shot (ONS / rising-edge detect) is true for exactly one scan when its
input transitions false→true. It converts a *level* into an *event*.

Why it matters: a part sensor that stays true for 500 ms in front of a 10 ms
scan is true for ~50 consecutive scans. Logic that reacts to the level reacts
50 times.

```text
|----[ Part_Sensor ]----[ONS Part_OS]----[CTU Part_Count]----|   (illustrative)
```

One-shots are required wherever an action must happen once per occurrence:
counting parts, toggling a bit from a single button (press = flip, not
flip-every-scan), issuing commands to devices that expect a pulse, triggering
data logging or totalization, acknowledging alarms, and firing state
transitions (covered in `state_machines`). The symptom of a missing one-shot
is typically some flavor of "it happened N times when it should have happened
once."

## 12. Retentive vs non-retentive values

A **non-retentive** value returns to its initial state after a power cycle or
program download; a **retentive** value survives. Which behavior a given tag,
timer, or data area has is a configuration and platform question — check, do
not assume.

Retentive storage is right for data whose loss would be a defect: production
totals, runtime hours, recipe selections, calibration constants. It is
dangerous for command and sequence state: a retained run request or sequence
step means the machine can wake from a power cycle already "mid-cycle,"
possibly with product, axes, and operators in positions the retained state no
longer describes. A startup/first-scan routine should validate retained values
before anything trusts them — range-check the numbers, and force sequence
state and commands to a known safe default.

## 13. Alarm conditioning: delay and hysteresis

A bare comparison (`Temp > 80.0 → alarm`) makes a poor alarm. Real signals
carry noise and ride near thresholds, so an unconditioned alarm chatters —
on/off repeatedly — training operators to ignore it. Two conditioning tools:

- **On-delay (debounce):** the condition must persist for a set time before
  the alarm asserts, so a one-scan spike or a transient excursion does not
  alarm. An off-delay can similarly hold an alarm long enough to be seen.
- **Hysteresis (deadband):** assert above one value, clear below a lower one —
  e.g. in at 80 °C, out at 77 °C — so a signal hovering at the threshold cannot
  cycle the alarm.

```text
|----[ Temp > 80.0 ]----[TON AlmDly_Tmr  PRE 3s]----|          (illustrative)
|----[ AlmDly_Tmr.DN ]----------------(S HighTemp_Alm )----|
|----[ Temp < 77.0 ]----[ HighTemp_Ack ]----(R HighTemp_Alm )--|
```

A complete alarm typically also carries acknowledgment (a deliberate operator
action, distinct from the condition clearing), timestamping, and HMI
presentation — alarm-system design beyond the rung level is its own topic.

## 14. Analog scaling in the ladder context

An analog input arrives as raw counts (for example 0–32767 across the module's
range) representing a transmitter span (for example 4–20 mA = 0–100 psi).
Linear interpolation converts raw to engineering units:

```text
EU = (Raw - RawMin) × (EUMax - EUMin) / (RawMax - RawMin) + EUMin
```

In ladder this is typically a compute/CPT rung, a chain of MUL/DIV/ADD, or a
vendor scaling instruction, executed unconditionally in the input-mapping
section so the rest of the program only ever sees engineering units. The raw
endpoint values depend on the module and its configuration — read them from
the hardware configuration, do not guess. (An ST rendering of the same
interpolation appears in the `languages_overview` module; the algorithm is
identical in any language.)

Scaling is only half the job. The mapping section should also qualify the
signal: under-range and over-range (which for 4–20 mA signals can indicate an
open or shorted loop), channel fault status from the module, and a stale/frozen
value check where the protocol allows. A scaled value with no validity bit
invites the program to control from a broken sensor.

## 15. Rung structure habits

- One rung, one purpose — a rung that computes a permissive should not also
  time an alarm and command a valve.
- Break big conditions into named intermediate tags (`Motor_Perm`,
  `Pump_Trip`) rather than one heroic rung; the intermediate names are
  self-documenting and watchable online.
- Order rungs in the data-flow direction (§9).
- Comment the *why* on rungs whose logic is not self-evident — especially any
  place where physical wiring sense is inverted (§5).

## 16. Ladder logic and safety functions

Standard ladder logic in a standard PLC is not, by itself, adequate protection
for hazardous machinery. Emergency stops, guard monitoring, light curtains and
similar functions normally require safety-rated hardware and architecture —
safety controller or relay, safety-rated I/O, dual channels with discrepancy
monitoring, monitored manual reset — designed to the applicable performance
level or SIL. The standard program may *read* safety status for sequencing and
display, but it does not implement, bypass, or substitute for the safety
function. See the `safety_application_patterns` module and the safety-circuit
wiring guide.

## 17. Common ladder design mistakes

1. **HMI-only interlocking.** Disabling or hiding an HMI button is treated as
   the interlock. Failure mode: the action still fires from another screen,
   a script, or a communications write. Root cause: enforcing a rule in the
   presentation layer instead of in the PLC logic, which is the only layer
   every command path passes through.
2. **Writing one coil from multiple rungs.** Failure mode: outputs that ignore
   a rung that is visibly true; behavior changes when rungs are reordered.
   Root cause: last-write-wins semantics of the OTE-style coil (§10).
3. **Treating command as feedback.** Failure mode: sequences advance and
   interlocks satisfy against equipment that never actually started. Root
   cause: no separate feedback signal, or feedback ignored because "the
   command bit is on" (§7).
4. **Counting without a one-shot.** Failure mode: counts inflated by orders of
   magnitude. Root cause: a level-driven counter increments every scan the
   condition holds, not once per event (§11).
5. **Latches without a dependable reset.** Failure mode: machine stuck in a
   state no operator action can leave, or a latched command reappearing after
   power-up. Root cause: set and reset logic separated and incompletely
   thought through; retention over power cycles not considered (§2, §12).
6. **Ignoring first-scan and power-cycle behavior.** Failure mode: unexpected
   motion or spurious alarms at power-up. Root cause: retained data, timer
   presets, and sequence state assumed to initialize themselves (§12).
7. **Monolithic rungs.** Failure mode: a fault takes hours to trace because
   one rung mixes modes, timers, and commands. Root cause: no
   one-rung-one-purpose discipline; missing intermediate tags (§15).
8. **Raw I/O addresses scattered through the logic.** Failure mode: a module
   swap or rewire becomes a program-wide edit; simulation impossible. Root
   cause: no mapping layer at the edges (§6).
9. **Undefined abnormal behavior.** Failure mode: nobody can say what the
   machine does on comms loss, sensor failure, e-stop, or controller restart —
   until it happens. Root cause: only the sunny-day sequence was designed;
   abnormal states were left to whatever the logic happens to do.

## Related

- `languages_overview` — the five IEC 61131-3 languages and when LD fits
- `program_structure` — tasks, programs, routines, tags, naming, the scan model
- `state_machines` — sequence design; where MOV-to-state rungs belong
- `safety_application_patterns` — safety controller separation
- Fundamentals: interlocks/permissives/trips definitions; safety-circuit wiring
