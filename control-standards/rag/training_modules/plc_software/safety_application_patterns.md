<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: safety_application_patterns
LEARNING_LEVEL: intermediate

TOPIC: Structural patterns for safety application software — safety vs standard PLC,
keeping the safety program separate and small, certified function blocks, change
control, and traceability to the SRS. Patterns and structure, NOT how to achieve a
PL/SIL.

INDEX_TAGS:
  topics: ["safety_plc", "safety_application", "certified_function_block", "estop_fb", "guard_monitoring_fb", "two_hand", "muting", "edm", "safety_lifecycle", "change_control", "srs_traceability", "safety_anti_patterns"]
  systems: ["safety_plc", "plc", "machine_safety", "iec_61131_3"]
  standards: ["ISO 13849-1", "IEC 62061", "IEC 61508", "IEC 61131-3"]
-->

# Safety Application Patterns in PLC Software

**Framing first.** Safety application software is governed by the functional-safety
standards — ISO 13849-1, IEC 62061, IEC 61508 — and it runs on a **safety-rated
controller with a certified toolchain**. This note covers the **patterns and
structure** of that software. It does **not** tell you how to achieve a required
Performance Level or Safety Integrity Level: the PL/SIL comes from the risk
assessment, the Safety Requirements Specification (SRS), and the certified function
blocks of the safety platform — not from a coding style. Nothing here substitutes
for the safety lifecycle.

## Standard PLC vs safety PLC / safety application

A standard PLC runs the machine's sequence and process logic. A **safety PLC** (or
safety controller / safety relay) is a separately certified device with redundant
internal architecture, diagnostics, and a certified programming environment. The
**safety application** is the program that runs in that certified environment.

The dividing line is a design rule, not a preference:

- The **safety application** implements the safety functions (e-stop, guard
  monitoring, two-hand control, muting, safe stop).
- The **standard logic** may *read* the safety system's status — to update the HMI,
  drive the sequence, annunciate — but it never *implements* a safety function.

Mixing the two, so a safety function depends on a rung in the standard program,
defeats the certification and is a top-tier anti-pattern.

## Keep the safety application separate and simple

The safety program should be **small, separate, and boring**. It does one thing —
evaluate the defined safety functions — and it is reviewed line by line. Complexity
is the enemy of verifiability: every added condition is something a reviewer and a
validator must reason about. In practice:

- The safety program is physically separate from the standard program (separate
  task, separate device, or the platform's safety partition).
- It contains only safety logic. Sequencing, HMI formatting, and production logic
  stay in the standard program.
- Data flows one way at the boundary: safety status out to standard logic; standard
  logic does not reach in to change safety behavior.

## The certified function-block approach

Safety platforms ship **certified function blocks** for the recognized safety
functions — an e-stop block, a guard-monitoring block, a two-hand block, a muting
block, and blocks that handle **EDM** (external device monitoring, the feedback that
proves the final contactors actually dropped out). Use them. Do **not** roll your own
safety logic out of ordinary contacts and coils: the certified block carries the
verification, the diagnostic coverage, and the fault reaction that a hand-built
equivalent does not.

These blocks map directly onto the wiring:

- Dual-channel e-stop and guard inputs wire to safety inputs; the e-stop / guard FB
  evaluates channel agreement and discrepancy timing.
- The FB's output enables the safe outputs (safety-rated outputs, redundant
  contactors, or a drive's STO).
- EDM feedback from the contactors' mirror contacts wires back to an input the FB
  monitors before it allows a reset.

The wiring side of this — dual-channel inputs, redundant outputs, STO, EDM, monitored
reset — is covered in the safety-circuit wiring guide. The function block and the
wiring are two halves of one safety function.

## Validation and change control

The safety application lives inside the **safety lifecycle**. Any change to safety
logic — however small — re-enters that lifecycle: impact analysis, modification,
re-verification, and re-validation of the affected safety functions, with the safety
program re-checksummed and the change recorded. There is no "quick edit" to a safety
program.

Two disciplines make this real:

- **Documentation and traceability to the SRS.** Every safety function in the code
  traces back to a line in the Safety Requirements Specification — inputs, outputs,
  required response time, required PL/SIL. If a function block cannot be traced to an
  SRS entry, either the SRS or the code is wrong.
- **Configuration control.** Safety program versions, checksums, and the identity of
  who verified them are recorded and controlled — a bypass added for commissioning is
  logged and, above all, removed.

## Common anti-patterns

- **Implementing a safety function in standard logic.** An e-stop that "works"
  through the standard PLC has no certified integrity and no valid PL/SIL claim.
- **Bypassing during commissioning and not removing it.** A jumpered guard or a
  forced input left in place is the classic cause of an unsafe machine passing into
  production. Every bypass is tracked and removed; the safety program is re-validated
  afterward.
- **No traceability to the SRS.** Safety code that no one can map to a specified
  requirement cannot be reviewed, validated, or maintained.
- **Home-grown safety blocks.** Re-inventing e-stop or guard logic from plain
  contacts throws away the certification the platform already provides.

## Related

- Standards: ISO 13849-1, IEC 62061, IEC 61508 (functional safety)
- Lifecycle: Safety Requirements Specification; the safety lifecycle
- Wiring: safety circuit (the wired half of every safety function)
- PLC software: state machines (the standard sequence that reads safety status)
