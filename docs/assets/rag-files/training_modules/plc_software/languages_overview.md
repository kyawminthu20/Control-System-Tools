<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: languages_overview
LEARNING_LEVEL: foundational
TOPIC: IEC 61131-3 programming languages — the standard, the five languages, and when each fits.
SOURCE: original teaching note. IEC 61131-3 concepts paraphrased; no standard text, grammar, or formal-language tables reproduced.
INDEX_TAGS:
  topics: ["iec_61131_3", "ladder_diagram", "function_block_diagram", "structured_text", "sequential_function_chart", "instruction_list", "common_elements", "pou"]
  systems: ["plc", "programmable_controller", "control_software"]
-->

# IEC 61131-3 Programming Languages Overview

## 0. Purpose

A map of the languages you can write PLC logic in and the judgement of which to
reach for — before structuring a new program or when inheriting unfamiliar code.

## 1. What IEC 61131-3 is

IEC 61131-3 is the international standard for programmable-controller
programming languages (Part 3 of the IEC 61131 series). Before it, every vendor
had its own incompatible logic dialect; the standard defined a *common model* —
shared data types, variable and POU concepts, and a defined set of languages —
so concepts port across platforms even when the tools differ.

Two cautions that run through this whole note:

- The standard defines a model; **vendors implement partial subsets and
  supersets.** Rockwell Studio 5000, Siemens TIA Portal (with SCL for the
  ST-like language), CODESYS, and Beckhoff TwinCAT all claim IEC 61131-3
  lineage yet differ in data types, timer behaviour, and which languages ship.
  Conformance is platform-specific — **consult your platform's documentation**.
- Portability is at the level of *concepts and structure*, not copy-paste code.
  A well-structured program ports far more easily than a badly structured one,
  but rarely without edits.

## 2. The five languages

The standard defines four core languages plus one graphical structuring element (SFC), commonly counted as five.

### Ladder Diagram (LD)
Graphical, drawn as rungs between two power rails — the direct descendant of
hard-wired relay logic, with contacts and coils. Best for discrete/boolean
logic: interlocks, permissives, motor start/stop seals, combinational safety
logic. Its virtue is that a maintenance electrician can read it at 3 a.m.
without being a programmer. Weak for math, loops, and data handling.

### Function Block Diagram (FBD)
Graphical, drawn as blocks wired by signal lines — reads like a signal-flow or
P&ID sketch. Best for analog/process logic, PID loops, and assembling reusable
blocks into a data path. Encourages reuse (a block is a black box with defined
pins). Weaker for dense sequential or conditional logic, which becomes a tangle
of wires.

### Structured Text (ST)
Textual, Pascal-like high-level language. Best for algorithms: math, loops,
string/array handling, state machines, recipe and data manipulation — anything
with real conditional depth. Compact and version-control-friendly. Trade-off:
an electrician who reads ladder fluently may not read ST, so teams weigh who
maintains the code.

### Sequential Function Chart (SFC)
Graphical structuring language for *sequential* processes — **steps** (what is
active now) joined by **transitions** (the conditions that advance). Actions
attach to steps; each step's logic is written in one of the other languages.
Ideal for batch, start-up and shutdown sequences, and any "do A, then when X do
B" process; it makes the sequence visible and fits a state-machine design. Not
general-purpose — you still write the step bodies in LD/FBD/ST.

### Instruction List (IL)
Textual, low-level, assembler-like (load / store / operate on an accumulator).
Historically used for compact code. **IL was deprecated in the 3rd edition
(IEC 61131-3:2013)** and is being phased out — write new code in ST instead.
Recognise it in legacy programs; do not start new work in it.

## 3. The common elements model

Underneath all five languages sits one shared model — the reason a variable or
data type means the same thing whether you draw it or type it:

- **Data types** — elementary types (BOOL, INT, REAL, TIME, STRING, …) plus
  user-defined and structured types; exact widths vary by platform.
- **Variables** — declared with a scope and optional initial value, referenced
  by symbolic tag rather than raw memory address.
- **POUs (Program Organization Units)** — Programs, Function Blocks, and
  Functions: the containers logic lives in, independent of language. Covered in
  depth in the program-structure note.

Because the model is shared, you can mix languages: an FBD network can call an
ST function, an SFC step's action can be a ladder rung. Language choice is
per-POU (often per-action), not per-project.

## 4. Mixing languages — right tool per task

Real projects are multilingual by design. A common pattern: **SFC** for the
sequence skeleton, **LD** for interlocks and I/O-facing boolean logic, **FBD**
for the analog/PID path, **ST** for calculations and data handling. Pick per
task and stay consistent within a module — do not prove you can use all five.
Weigh who maintains the code: if night-shift electricians own first-line
support, keep their interlocks in ladder even where ST would be terser.

## 5. Choosing — quick guide

| Language | Best for | Readability | Avoid for |
|---|---|---|---|
| LD | discrete/interlock/boolean logic | high for electricians | math, loops, data handling |
| FBD | analog/process, PID, reusable blocks | high for signal-flow | dense sequential/conditional logic |
| ST | algorithms, math, loops, strings/data | high for programmers | teams with no text-code skills |
| SFC | step/sequence processes | high for sequences | continuous/combinational logic |
| IL | legacy only (deprecated 3rd ed.) | low | any new development |

## 6. Related notes

- Program structure — POUs, tasks, and scope: `program_structure.md`
- State-machine design layered onto SFC and ST; `cst` tag tooling enforces
  IEC 61131-3 identifier rules on tag names.
