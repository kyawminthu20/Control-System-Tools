<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: state_machines
LEARNING_LEVEL: intermediate

TOPIC: Designing PLC sequences as explicit state machines — the step/transition/action
model, and implementing it in SFC, Structured Text CASE, or latched Ladder.

INDEX_TAGS:
  topics: ["state_machine", "fsm", "sfc", "sequential_function_chart", "case_statement", "step_transition", "one_shot", "entry_exit_actions", "fault_state", "reset_recovery", "interlocks_over_sequence"]
  systems: ["plc", "machine", "sequence_control", "iec_61131_3"]
  standards: ["IEC 61131-3"]
-->

# State Machines in PLC Programs

A machine sequence is a state machine whether or not the programmer admits it.
The choice is between making the state **explicit** — one variable that names the
current step — or leaving it **implicit**, scattered across dozens of coils and
timers that together imply where the machine is. Explicit wins for every reason
that matters on a running plant: deterministic, debuggable, and one place for the
operator and commissioning engineer to read the machine's state.

This note describes the step/transition/action model and three ways to implement
it. It is a design-pattern discussion, not a reproduction of the IEC 61131-3
language definitions; consult your platform's documentation for exact syntax.

## Why explicit beats ad-hoc logic

Ad-hoc sequence logic — "start the pump when these six bits are true, unless this
timer, but not if that latch" — has no single source of truth for where the
machine is. Two rungs can silently disagree, and the failure mode is the machine
that stops "somewhere" nobody can name, because there is no step to name. An
explicit state machine fixes the machine to exactly one named state at a time:

- **Deterministic** — one and only one state is active each scan; a transition is
  the only way state changes, so behavior is reproducible.
- **Debuggable** — the current-state variable is a single tag to watch, trend, or
  put on the HMI. A stall is "stuck in HOMING waiting for the home switch," not a
  hunt through the logic.
- **Operator/commissioning benefit** — the HMI shows the state name; the
  commissioning engineer steps the machine through its cycle one transition at a
  time.

## The step/transition/action model

Three parts:

- **States (steps)** — the named, mutually exclusive situations the machine can be
  in (IDLE, HOMING, READY, RUNNING, STOPPING…).
- **Transitions** — guarded moves from one state to the next. A transition fires
  only when its guard condition is true (home complete, start pressed, cycle done).
  Guards are what keep the machine from skipping steps.
- **Actions** — what runs because of the state: continuous actions while in a state,
  plus **entry** and **exit** actions that run once as the state is entered or left.

A simple machine cycle:

```
IDLE --(start & permissives)--> HOMING --(homed)--> READY
READY --(cycle start)--> RUNNING --(stop req / cycle done)--> STOPPING --> IDLE
any state --(fault)--> FAULT --(cause cleared & reset)--> IDLE
```

## Three ways to implement it

**SFC (Sequential Function Chart)** — the native IEC 61131-3 language for
sequences. Steps and transitions are first-class graphical elements, with step
actions and transition conditions built in. It is the most direct expression of
the model when the sequence is genuinely linear or branching, and the graphic
doubles as documentation. Availability and execution details are vendor-specific.

**CASE on a state variable (Structured Text)** — the common, portable pattern. A
single enumerated `State` variable is switched in a `CASE`; each branch holds that
state's actions and evaluates its transition guards, writing the next state. It
ports cleanly across platforms and is easy to code-review. Illustrative only:

```
CASE State OF
  IDLE:    IF StartCmd AND Permissives THEN State := HOMING; END_IF;
  HOMING:  Home();  IF HomeDone THEN State := READY; END_IF;
  READY:   IF CycleStart THEN State := RUNNING; END_IF;
  RUNNING: RunCycle(); IF CycleDone OR StopReq THEN State := STOPPING; END_IF;
  STOPPING: IF Stopped THEN State := IDLE; END_IF;
  FAULT:   IF ResetPulse AND FaultCleared THEN State := IDLE; END_IF;
END_CASE;
```

**Step-latching in Ladder** — where LD is the house language, each step is a latched
bit; the transition rung seals in the next step and unlatches the current one, so
exactly one step bit is on. Readable to a maintenance electrician, but it takes
discipline to keep genuinely one-hot.

## Entry/exit actions and one-shots

Entry actions run once when a state is entered (start a timer, command a setpoint,
reset a counter); exit actions run once when it is left (stop the motor, clear a
request). They must be **one-shot** — edge-triggered on the transition — not
re-executed every scan the state is active. Re-issuing a "start" command every scan
is a classic bug: the action fights itself, or a downstream one-shot never sees an
edge. Detect the transition, act once.

## Interlocks and permissives layered OVER the machine

Interlocks and permissives sit **on top of** the state machine, not buried inside
individual transitions. A permissive must be true to allow a state to proceed; an
interlock forces a safe state regardless of where the sequence thinks it is.
Keeping them in a separated layer keeps the sequence readable and the protective
logic auditable — see the interlocks and permissives fundamentals. Machine-actuated
**safety** functions are not sequence logic at all: they live in the wired safety
circuit and the safety application.

## Fault states and recovery

A fault is a transition that can fire from many states into a single FAULT state,
which commands the safe outputs and holds. Recovery is deliberate: the operator
clears the cause, then a **reset** (a monitored edge, never a maintained bit) returns
the machine to IDLE — usually via re-homing, because after a fault the machine's
physical position is unknown. Never let a fault silently self-clear back into the
running sequence.

## Related

- Fundamentals: machine state model, interlocks & permissives, control fundamentals
- PLC software: program structure, safety application patterns
- Wiring: safety circuit (the safety function is wired, not sequenced)
