<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: packml_isa88_isa95
LEARNING_LEVEL: intermediate-advanced

TOPIC: The three architecture standards that organize machine behavior above the
code level — PackML (ISA-TR88.00.02) machine states, modes, and PackTags;
ISA-88 physical and procedural models; ISA-95 enterprise-integration levels —
and how they relate to, but do not replace, the PLC program itself.

INDEX_TAGS:
  topics: ["packml", "unit_modes", "state_model", "acting_states", "wait_states", "state_complete", "packtags", "oee", "isa_88", "physical_model", "procedural_model", "equipment_module", "control_module", "recipe", "phase", "isa_95", "enterprise_integration", "purdue_levels", "mes", "gamp_5", "21_cfr_part_11", "secs_gem"]
  systems: ["plc", "machine", "packaging_line", "batch_process", "mes", "erp", "line_control"]
  standards: ["ISA-TR88.00.02", "ISA-88", "ISA-95", "IEC 62264", "ISA-TR88.95.01", "OPC 30050", "GAMP 5", "FDA 21 CFR Part 11", "SEMI SECS/GEM"]
-->

# PackML, ISA-88 and ISA-95

PackML, ISA-88, and ISA-95 are not programming languages, and none of them
tells you how to write a rung or an ST statement. They standardize the layer
**above** the code: how a machine describes its operating condition to the
outside world (PackML), how equipment and procedures are decomposed and named
(ISA-88), and how the plant floor exchanges information with business systems
(ISA-95). IEC 61131-3 languages are the material the implementation is built
from; these three define the shape the implementation should take.

A useful one-line summary of the division of labor:

- **PackML** — standardized machine modes, states, and interface data
- **ISA-88** — equipment hierarchy, procedures, phases, and recipes
- **ISA-95** — manufacturing-to-enterprise information exchange

This note is a concepts-and-architecture treatment. It paraphrases the intent
of the documents; it does not reproduce their text, state-transition tables, or
tag lists. Verify details against the current published revisions of
ISA-TR88.00.02, the ISA-88 series, and the ISA-95 series (IEC 62264).

---

## 1. PackML — what it is and is not

PackML originated with OMAC (the Organization for Machine Automation and
Control) and was adopted by ISA as the technical report **ISA-TR88.00.02**,
whose current revision at the time of writing is the 2022 edition, titled
*Machine and Unit States: An Implementation Example of ISA-88.00.01*. The
title carries two important signals:

1. It is a **technical report**, not a standard proper — an implementation
   example, published for interoperability rather than compliance.
2. It is explicitly derived from **ISA-88** thinking: the machine-state model
   is ISA-88 procedural/state discipline applied to discrete automated
   machines instead of batch process cells.

PackML is also published as an OPC UA companion specification — **OPC 30050,
OPC UA for PackML** — which maps the PackML information model onto OPC UA so
that line controllers and supervisory systems can consume it in a
transport-neutral way.

PackML defines three things:

1. **Unit modes** — named operating contexts such as Production, Maintenance,
   and Manual.
2. **A machine/unit state model** — a fixed vocabulary of states (Stopped,
   Idle, Execute, Held, Suspended, Aborted and their transitional partners)
   with defined transitions between them.
3. **PackTags** — a standardized naming convention for the command, status,
   and administrative data a machine exposes.

The point of all three is the same: machines from different builders present a
**consistent operational interface**, so a line controller, OEE package, or
MES can command and observe any conforming machine the same way. Without it,
every machine on a packaging line reports "running" and "faulted" in its own
private vocabulary, and every line-integration project starts with a mapping
exercise.

## 2. The PackML state model

The state model distinguishes two kinds of states:

- **Wait states** — stable conditions the machine rests in until something
  external happens: Stopped, Idle, Execute-adjacent holds (Held, Suspended),
  Complete, Aborted. The machine sits in a wait state indefinitely.
- **Acting states** — transitional states in which the machine is actively
  doing work to get somewhere else: Starting, Completing, Resetting, Holding,
  Unholding, Suspending, Unsuspending, Stopping, Aborting, Clearing — and
  Execute itself, which is the acting state where production work happens.

The mechanism that moves the model along is the **state-complete pattern**: an
acting state performs its defined work and then declares completion (the
internal "state complete" event), which drives the automatic transition to the
next state. External commands (Start, Stop, Hold, Unhold, Suspend, Unsuspend,
Abort, Clear, Reset) move the machine between wait states via the appropriate
acting state. Two consequences of this pattern are worth internalizing:

- Every acting state needs a **completion condition** the machine can actually
  evaluate. "Starting" is not a timer; it is "all axes homed, guards confirmed,
  vacuum up to setpoint" — whatever the machine genuinely requires before
  production may begin.
- Commands request transitions; the state model **grants** them. A Stop
  command received in Execute enters Stopping, runs the machine's controlled
  shutdown work, and only then reaches Stopped.

A simplified view of the model (the published report defines the full set of
states and the complete transition matrix — consult it for the normative
picture):

```
                 Reset             Start
   Stopped ──► Resetting ──► Idle ──► Starting ──► EXECUTE
      ▲            (SC)              (SC)             │
      │                                               ├─ production done ─► Completing ─► Complete
   Stopping ◄──────────── Stop ───────────────────────┤
      (SC)                                            ├─ Hold ─► Holding ─► Held ─► Unholding ─┐
                                                      │                                  (SC)  │
   Aborting ◄──────────── Abort (from nearly          ├─ Suspend ─► Suspending ─► Suspended    │
      │(SC)               any state)                  │             ◄─ Unsuspending ◄──────────┤
      ▼                                               │                                        │
   Aborted ──► Clear ──► Clearing ──► Stopped         ◄────────────────────────────────────────┘
```

The distinctions among the "not running" states carry real meaning for line
supervision and OEE:

- **Held** — the machine paused for an **internal** reason (operator hold, an
  internal condition needing attention). Production is interrupted by the
  machine or its operator.
- **Suspended** — the machine paused for an **external** reason: starved of
  product upstream or blocked downstream. The machine itself is healthy and
  waiting. This distinction is precisely what allows a line-level OEE system
  to attribute downtime to the right machine.
- **Stopped** — a commanded, orderly stop; the machine is powered and
  ready to be reset.
- **Aborted** — the machine went down abnormally (fault, emergency condition
  observed); a Clear is required before the normal reset path is available.

## 3. Unit modes

Modes answer a different question than states: not "what is the machine doing"
but "under what rules is it operating." The commonly implemented base modes
are:

- **Production** — normal automatic operation; the full state model applies.
- **Maintenance** — a mode for trained technicians; typically permits
  operations production forbids (jog, dry-cycle, individual actuator
  exercise) under maintenance-appropriate conditions.
- **Manual** — direct operator-driven control of parts of the machine.

The report allows machine-specific additional modes — cleaning and calibration
modes are common in practice. Each mode may use a subset of the state model
(a Manual mode may have no Suspended state, for instance), and mode changes
are normally only accepted in defined states — you do not switch from
Production to Maintenance mid-Execute. Which states permit a mode change is an
implementation decision the machine designer documents.

## 4. PackTags — the standardized data interface

PackTags are the third leg: a naming convention for the data a PackML machine
exposes, organized into three groups:

- **Command tags** — data flowing *to* the machine: mode and state commands,
  machine speed setpoint, product/recipe selection, remote interface data.
- **Status tags** — data flowing *from* the machine describing its current
  condition: current mode and state, current speed, material-flow status.
- **Administrative (Admin) tags** — accumulated and diagnostic data:
  production counts, reject counts, alarm and stop-reason information — the
  raw material of OEE and downtime-attribution reporting.

The value is uniformity: a line supervision system reads the same tag
structure from a filler, a capper, and a case packer supplied by three
different builders. The full tag list, structures, and datatypes are defined
in the technical report and the OPC 30050 companion specification — implement
from those documents (or your platform's PackML library, which typically
provides the tag structures ready-made); the list is not reproduced here.

## 5. PackML does not replace the machine's own sequence

This is the point most often misunderstood on first contact with PackML, and
the source of most bad implementations.

`Execute` is one state in the PackML model. Everything the machine actually
*does* to make product — clamp, index, fill, seal, inspect, release — is the
machine's own production sequence, and it runs **inside** Execute. PackML says
nothing about how that sequence works; it wraps the sequence in a
standardized coordination shell:

- PackML answers: **what overall condition is the machine in**, in a
  vocabulary the line understands?
- The machine sequence answers: **what exact operation is the machine
  performing right now?**

Architecturally that means two state machines, layered:

```
Line controller / MES
      │  PackML commands + PackTags status
      ▼
PackML mode & state manager        ← the standardized wrapper
      │  "you may run" / "hold now" / "stop now"
      ▼
Production sequence (own steps)    ← the machine's real work,
      │  step 10 wait product,       running while state = Execute
      │  step 20 clamp, step 30 …
      ▼
Equipment modules → control modules → I/O
```

The same layering applies to the other acting states: Starting runs the
machine's startup routine, Stopping its controlled-shutdown routine, Aborting
its rapid-shutdown routine. Each acting state dispatches to a procedure and
watches for its completion. The design of those inner sequences is the
step/transition/action discipline covered in the state-machines module of
this family — PackML consumes it; it does not replace it.

## 6. A PackML-style state handler in Structured Text

Structured Text suits the state-dispatch layer because the model maps directly
onto a `CASE` over an enumerated state variable. The sketch below is
**illustrative — not platform code, and not the full PackML model**; it is a
constructed teaching example showing the dispatch pattern and the
state-complete idea. Real projects normally start from a vendor or OMAC
PackML implementation library rather than hand-rolling this.

```
(* Illustrative — not platform code. Constructed teaching example. *)
CASE UnitState OF

  PACKML_IDLE:
    IF Cmd.Start AND StartConditionsOk THEN
      UnitState := PACKML_STARTING;
    END_IF;

  PACKML_STARTING:
    StartupProcedure();                      (* acting state does work *)
    IF StartupProcedure.Done THEN            (* state complete ...     *)
      UnitState := PACKML_EXECUTE;           (* ... drives transition  *)
    END_IF;

  PACKML_EXECUTE:
    ProductionSequence();                    (* the machine's own steps *)
    IF ProductionSequence.OrderDone THEN
      UnitState := PACKML_COMPLETING;
    ELSIF Cmd.Hold OR InternalHoldRequest THEN
      UnitState := PACKML_HOLDING;
    ELSIF UpstreamStarved OR DownstreamBlocked THEN
      UnitState := PACKML_SUSPENDING;
    ELSIF Cmd.Stop THEN
      UnitState := PACKML_STOPPING;
    END_IF;

  PACKML_HOLDING:
    HoldProcedure();
    IF HoldProcedure.Done THEN
      UnitState := PACKML_HELD;
    END_IF;

  PACKML_STOPPING:
    StopProcedure();
    IF StopProcedure.Done THEN
      UnitState := PACKML_STOPPED;
    END_IF;

END_CASE;

(* Abort is evaluated outside the CASE: it must win from nearly any state *)
IF Cmd.Abort AND UnitState <> PACKML_ABORTED THEN
  UnitState := PACKML_ABORTING;
END_IF;
```

Design notes on the pattern:

- The `CASE` is only the **dispatch layer**. Each acting state calls a
  separate procedure (function block or routine) that owns the real work.
  Keeping the dispatcher thin is what keeps it reviewable.
- The abort path is evaluated with priority, outside or ahead of the normal
  branch logic, because Abort must be honored from nearly every state.
- Every acting state's `Done` condition is the state-complete event. If you
  cannot state a Done condition for an acting state, the state design is not
  finished.

## 7. ISA-88 — physical and procedural models

ISA-88 (batch control) predates PackML and supplies the intellectual framework
PackML borrowed. Its two central models are worth knowing even if you never
build a batch plant.

**The physical model** decomposes the plant top-down:

```
Enterprise → Site → Area → Process Cell → Unit → Equipment Module → Control Module
```

The two lowest levels are the ones a PLC programmer touches daily:

- A **control module** is the smallest practically controllable device plus
  its immediate logic: a motor with its start/stop/feedback/fault handling, a
  valve with its open/close/travel-fault handling, a transmitter with its
  scaling and validation. One class, many instances.
- An **equipment module** coordinates a group of control modules to perform a
  process-oriented function: a feed conveyor (motor + photoeyes + jam
  detection), an agitation module (agitator drive + speed feedback), a
  transfer module (pump + routing valves).

**The procedural model** decomposes what the equipment is asked to do:

```
Procedure → Unit Procedure → Operation → Phase
```

A **phase** is the smallest procedural element — "add water," "heat to
setpoint," "transfer to tank" — and is the level at which recipe logic meets
equipment logic. The recipe (procedural side) sequences phases with
parameters; the equipment side implements each phase against its equipment
modules. Because the two sides are separated, the same physical unit can run
different recipes, and a recipe can be moved between compatible units —
that separation is the core economic argument of ISA-88.

**As a program-organization discipline**, the equipment-module/control-module
split applies far outside batch: the machine sequence commands equipment
modules ("feed conveyor: run", "transfer module: transfer to tank 2"), and
equipment modules command control modules. The sequence never reaches down to
individual motors and valves. That layering is the same discipline the
program-structure module of this family describes in POU terms.

## 8. ISA-88 versus PackML

The relationship, briefly:

| Aspect | PackML (ISA-TR88.00.02) | ISA-88 |
|---|---|---|
| Orientation | Discrete automated machines and lines | Batch and procedural processes |
| Core content | State model, unit modes, PackTags | Physical + procedural models, recipes |
| Execution concept | Machine state model | Procedure → operation → phase |
| Recipe handling | Basic parameter/product interface | Comprehensive recipe model |
| Typical setting | Packaging, assembly, material handling | Pharma, food, chemical, biotech |
| Relationship | An implementation example **of** ISA-88 concepts | The parent framework |

PackML took ISA-88's state and equipment discipline and packaged it for
machines that make or handle discrete product. Both leave language choice
open — any IEC 61131-3 language can implement either.

Bridging upward, **ISA-TR88.95.01** (*Using ISA-88 and ISA-95 Together*) is
ISA's guidance on making the equipment-level models (ISA-88, and by extension
PackML) mesh with the enterprise-integration models of ISA-95 — which recipe
and production information lives on which side of the boundary.

## 9. ISA-95 — enterprise integration, levels 0–4

ISA-95 (published internationally as IEC 62264) addresses the boundary between
manufacturing control and business systems. Its most widely cited artifact is the
level model:

```
Level 4  Business planning & logistics (ERP)
Level 3  Manufacturing operations management (MES/MOM)
Level 2  Supervisory control (SCADA, HMI, line/PLC coordination)
Level 1  Basic control (PLC logic, sensors/actuators interface)
Level 0  The physical process
```

Two things to be clear about:

- ISA-95 defines **information models and exchanges**, not PLC code structure.
  It standardizes what a production schedule, a production-performance
  response, material information, equipment capability, personnel capability,
  and quality/maintenance information look like when levels 3 and 4 talk to
  each other and to level 2. It says nothing about how a motor rung is
  written.
- The level model is an **information/responsibility** hierarchy, not
  necessarily a network topology — though it heavily influenced network
  segmentation practice (the "Purdue-style" zoning used in ICS security
  work).

In a machine context: PackML and ISA-88 structure behavior at levels 1–2;
ISA-95 structures what flows to and from level 3. A PackML machine's PackTags
are, in effect, a ready-made level-2-to-level-3 data contract, which is why
the two are so often deployed together on packaging lines.

## 10. Industry notes (brief)

**Pharmaceutical.** Pharma systems layer regulatory frameworks over the same
architecture: ISA-88 organizes equipment and recipes; **GAMP 5** supplies a
risk-based lifecycle and validation approach for computerized systems
(including the category-based thinking about how much validation rigor a
software element warrants — configured products versus custom code); and
**FDA 21 CFR Part 11** governs electronic records and electronic signatures
when required records are created, stored, or transmitted electronically —
which reaches into batch reporting, audit trails, and operator authentication
on the control system. The PLC architecture itself is standard ISA-88; the
regulatory layer changes how it is specified, verified, and documented.

**Semiconductor.** Semiconductor equipment needs two distinct software
organizations: the **internal equipment control** (load/align/process/
inspect/unload sequencing — ordinary state-machine territory, implemented in
PLCs, robot controllers, or PC-based control), and the **factory host
interface**, standardized by SEMI **SECS/GEM** (and the GEM300 family for
300 mm fabs). SECS/GEM standardizes how the equipment reports states, events,
alarms, and data to the factory host and accepts remote commands and recipes —
the same "standardized outer interface, private inner sequence" pattern as
PackML, expressed in a different industry's vocabulary. SECS/GEM does not
replace the equipment's internal sequence any more than PackML does.

## 11. The safety boundary

PackML states such as Stopped or Aborted are **coordination states, not
safety functions**. A machine's safety functions — emergency stop, guard
interlocking, safe torque off — live in the safety-related parts of the
control system, designed and validated to ISO 13849-1 or IEC 62061 (IEC 61511
in the process sector), separate from the standard controller. The correct
relationship is one-directional: the safety system removes hazardous energy
and reports status; the standard controller observes that the safety function
has actuated, transitions the PackML model to Aborting/Aborted, and presents
diagnostics. The PackML layer reports the consequence; it is not the
protective mechanism.

## 12. Putting it together

A machine or line architecture that uses all three standards coherently:

```
ERP  ──────────────── ISA-95 information exchange ────────────────┐
                                                                  ▼
MES / operations management (level 3)
      │  OPC UA (e.g. OPC 30050) / industry interface
      ▼
Line control ── PackML commands & PackTags ──► Machine controller
                                                ├─ mode manager
                                                ├─ PackML state manager
                                                ├─ production sequence(s)
                                                ├─ alarm handling
                                                └─ diagnostics
                                                      │
                                          equipment modules (ISA-88 discipline)
                                                      │
                                          control modules (device classes)
                                                      │
                                          I/O, drives, instruments
```

Reading the stack bottom-up: control modules make devices trustworthy;
equipment modules make functions commandable; the production sequence makes
product; PackML makes the machine legible to the line; ISA-95 makes the line
legible to the business.

## Sources

- OMAC — PackML overview: https://www.omac.org/packml
- OPC Foundation — OPC 30050 (OPC UA for PackML), concept section: https://reference.opcfoundation.org/specs/OPC-30050/4
- ISA — ISA-88 series of standards: https://www.isa.org/standards-and-publications/isa-standards/isa-88-standards
- ISA blog — modular systems and plant programming: https://blog.isa.org/modular-systems-speed-simplify-new-industrial-plant-programming
- ISA — ISA-95 standard: https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard
- ISA — ISA-TR88.95.01 (Using ISA-88 and ISA-95 Together): https://www.isa.org/products/isa-tr88-95-01-2008-using-isa-88-and-isa-95-togeth
- SEMI — introduction to SEMI communication standards (SECS/GEM, GEM300): https://www.semi.org/en/standards-watch-2022-Sept/intro-to-semi-communication-standards
- FDA — Part 11, Electronic Records; Electronic Signatures — Scope and Application: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application
- ISO — ISO 13849-1:2023 (safety of machinery, safety-related parts of control systems): https://www.iso.org/standard/73481.html
