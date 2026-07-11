<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: program_structure
LEARNING_LEVEL: foundational
TOPIC: Structuring PLC programs under IEC 61131-3 — POUs, variable scope, tasks/execution, modular design.
SOURCE: original teaching note. IEC 61131-3 concepts paraphrased; no standard text, grammar, or formal-language tables reproduced.
INDEX_TAGS:
  topics: ["pou", "program", "function_block", "function", "variable_scope", "global_variables", "tasks", "scan_cycle", "reusability", "instance_vs_type", "naming_conventions", "tag_database"]
  systems: ["plc", "programmable_controller", "control_software"]
-->

# Structuring PLC Programs — POUs, Tasks, and Scope

## 0. Purpose

How to organise the *containers* of PLC logic so a program stays maintainable
through commissioning and years of modification — structure, scope, execution.
Language choice is a separate note.

## 1. The POU model

IEC 61131-3 organises logic into **Program Organization Units (POUs)**. Three
kinds, distinguished mainly by whether they carry memory:

- **Function** — stateless; the same inputs always give the same output, with
  no memory between calls. Use for pure calculations (scaling, unit conversion).
- **Function Block (FB)** — stateful and *instantiated*. The FB is a **type**
  (the definition); each place you use it is an **instance** with private memory
  that persists across scans. A timer, a PID controller, a motor-starter block —
  each instance remembers its own state. The FB is the unit of reuse.
- **Program** — the top-level organising POU. It wires FB instances and logic
  together and is assigned to a task. Think "one machine section per program."

```
Program  (assigned to a task)
  └─ calls Function Block instances  (each has private memory)
        └─ which may call Functions   (stateless helpers)
```

The type/instance distinction is the crux: define an FB once (`MotorStarter`),
instantiate it many times (`Conveyor1`, `Conveyor2`), fix a bug in the type and
every instance inherits the fix. Copy-pasted logic does not give you that.

## 2. Variable scope

Every variable is declared in a scope. Common scopes (names vary by platform):

- **Input (VAR_INPUT)** — passed in to a POU; read-only inside it.
- **Output (VAR_OUTPUT)** — computed inside, readable by the caller.
- **In-out (VAR_IN_OUT)** — passed by reference; the POU reads and writes it.
- **Local (VAR)** — private to the POU (for an FB, per-instance, retained).
- **Temp (VAR_TEMP)** — scratch, valid only within one execution.
- **Global (VAR_GLOBAL)** — visible project-wide (the trap; see below).

**Globals are a maintenance trap.** A global can be written from anywhere, so a
wrong value has no bounded list of suspects — the whole program is in scope.
They defeat reuse (an FB that reaches out to a global is no longer
self-contained) and hide data flow. Prefer passing data through inputs/outputs
so a POU's dependencies show at its interface. Reserve globals for genuinely
system-wide state (e.g. plant-wide E-stop status), kept short and documented.

## 3. Tasks and execution

A **task** decides when and how often a program runs. The standard's model:

- **Cyclic / periodic** — run every N milliseconds; the workhorse for control.
- **Event / interrupt** — run in response to an event or condition.
- **Priority** — higher-priority tasks pre-empt lower ones, so time-critical
  logic runs fast and high-priority while housekeeping runs slower.

Underneath sits the **scan cycle**: read inputs → execute logic → update
outputs, repeated. Scan time is the loop period; logic must finish within the task interval or the task overruns.

**Standard model vs vendor reality.** The task/priority concepts are defined by
IEC 61131-3, but the number of tasks, their scheduling, watchdog behaviour, and
I/O update timing are platform-specific — Rockwell continuous/periodic/event
tasks, Siemens OBs, CODESYS tasks, and TwinCAT tasks all differ. **Consult your
platform's documentation**; never assume one vendor's timing model on another.

## 4. Modular, reusable design

- **The FB is the unit of reuse.** A well-made block has a clean interface
  (clear inputs/outputs, no reach-out to globals) and one responsibility — one
  valve, one starter, one loop. Build a library of proven blocks.
- **Instance vs type, again.** Reuse the *type*; give each *instance* its own
  name and I/O mapping — duplicating logic multiplies every future bug fix.
- **One machine section per program.** Map software structure to the physical
  machine — infeed, main, outfeed, utilities — so a commissioning engineer finds
  a jammed conveyor's logic without a site map.

## 5. Naming conventions and the tag database

Consistent naming makes a large program navigable. IEC 61131-3 constrains
**identifiers** (letters, digits, underscores; no leading digit; no spaces or
reserved words — details vary by platform). On top of that, adopt a project
convention: area/function prefixes, instance names matching the P&ID or
electrical tag, and a documented I/O pattern.

The **tag database** is the single source of truth for symbolic names, data
types, and I/O addresses. Keeping it clean — no duplicate tags, no address
conflicts, valid identifiers — pays back at every modification. The `cst`
toolkit validates I/O lists for duplicate tags and address conflicts and
generates tag databases under IEC 61131-3 identifier rules (engineering-toolkit).

## 6. Structuring for maintainability and commissioning

- Clear, one-to-one **I/O mapping** documented alongside the program; each
  program self-contained enough to be tested in isolation at commissioning.
- Faults and diagnostics surfaced per module, not buried in globals.
- Sequential logic given explicit structure — see the state-machine note, which
  layers a finite-state design onto SFC/ST rather than sprawling boolean flags.

## 7. Related notes

- Languages overview — the five IEC 61131-3 languages: `languages_overview.md`
- State-machine design for structured sequential logic; `cst` tag tooling for
  I/O validation and IEC 61131-3 identifier rules.
