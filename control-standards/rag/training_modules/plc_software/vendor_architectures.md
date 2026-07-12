<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: PLC_SOFTWARE
MODULE_ID: vendor_architectures
LEARNING_LEVEL: intermediate-advanced

TOPIC: How the Siemens TIA Portal, Rockwell Logix, and Beckhoff TwinCAT ecosystems
implement the shared IEC 61131-3 model differently — program hierarchy, memory
model, execution model, I/O flow, and reuse mechanisms — so an engineer can
translate concepts between platforms instead of relearning from zero.

INDEX_TAGS:
  topics: ["vendor_architecture", "tia_portal", "studio_5000", "twincat", "organization_block", "instance_db", "add_on_instruction", "tag_memory_model", "rpi", "process_image", "real_time_task", "oop_extensions", "library_types", "udt", "gvl", "fifo", "cross_platform_portability"]
  systems: ["plc", "s7_1500", "controllogix", "compactlogix", "twincat_3", "ethercat", "profinet", "ethernet_ip"]
  standards: ["IEC 61131-3"]
-->

# Vendor Programming Architectures

Siemens TIA Portal, Rockwell Studio 5000 Logix Designer, and Beckhoff TwinCAT 3
all descend from the same IEC 61131-3 model: program organization units (POUs),
typed variables, and tasks that schedule execution. An engineer who understands
that shared model already understands more of each platform than the surface
differences suggest. What the platforms genuinely diverge on is **how they
schedule code, where they store state, how they expose hardware, and how they
package reusable logic**. This note maps those divergences so a concept learned
on one platform can be translated onto another rather than relearned.

Behavioural details below were checked against the vendor documents listed in
Sources, cited by publication ID. Firmware and version differences are real —
verify every behaviour against your platform's current documentation.

A rough one-line character sketch of each ecosystem, before the detail:

- **Siemens** — block-and-data architecture: behaviour lives in function
  blocks; state lives in data blocks that the engineer sees and names.
- **Rockwell** — tag-and-instruction architecture: instructions and routines
  operate directly on named tags; there is no separate data-block object.
- **Beckhoff** — software-library-and-task architecture: IEC software objects
  (with object-oriented extensions) execute in configurable real-time tasks on
  a PC-based runtime, linked symbolically to hardware.

All three support ladder and Structured Text; language availability is not the
real difference. The architecture is.

## The five divergence axes

| Axis | Question it answers |
|---|---|
| Program hierarchy | What are the containers, and who calls what? |
| Memory model | Where does state live, and how is it scoped? |
| Execution model | What triggers code to run, and on what schedule? |
| I/O flow | When do physical values enter and leave the program? |
| Reuse mechanism | What is the unit of packaged, instantiable logic? |

---

## Siemens (TIA Portal, S7-1200/1500)

### Program hierarchy: OB / FC / FB / DB

A TIA Portal project organizes user code into four block kinds:

- **OB (organization block)** — an entry point the CPU operating system calls
  when a defined event occurs. OB1 is the cyclic main program; other OBs
  handle startup, cyclic interrupts (fixed-period execution), hardware
  interrupts, and diagnostic or error events. The engineer does not call OBs;
  the operating system does. Application structure therefore starts from
  "which event should run this code," and the code is placed inside the
  corresponding OB.
- **FB (function block)** — a stateful, instantiable POU. Every call to an FB
  is bound to an **instance data block** that holds that instance's memory.
- **FC (function)** — a stateless POU for calculations and operations that do
  not need memory between calls.
- **DB (data block)** — a named block of structured data. **Global DBs** hold
  shared data the engineer defines; **instance DBs** hold FB instance state.
- **PLC data types (UDTs)** define reusable structures used inside DBs and
  block interfaces.

### Memory model: state is explicit and visible

The defining Siemens trait is that block *algorithm* and block *memory* are
related but separate objects. Calling `FB_Pump` for pump 101 means naming the
instance DB that stores pump 101's timers, counters, state word, and
statistics. Three pumps means one FB and three instance DBs — the algorithm is
shared, the state is per-instance and individually inspectable. This makes
state ownership unusually explicit: an engineer can open `DB_Pump101` and see
exactly what that instance remembers.

Two access concepts matter for S7-1200/1500 (per the Siemens S7-1200/1500
Programming Guideline):

- **Optimized block access** — symbolic-only access; the compiler arranges
  memory for processor efficiency, not in declaration order. Recommended by
  Siemens for new work on these CPU families.
- **Standard block access** — memory laid out in declaration order and
  addressable absolutely, retained mainly for compatibility with older
  patterns and external systems that need fixed offsets.

An instance DB inherits its access mode from its FB. Which mode a project uses
affects addressing, communication partners, and some performance behaviour —
consult the programming guideline and your CPU documentation before mixing
them.

### Execution model: the OS calls OBs

The CPU firmware owns the schedule. Typical arrangement:

```
OB100  startup (runs once at CPU start)
OB1    free-running cyclic main program
OB3x   cyclic interrupt OBs (fixed periods, e.g. 10 ms / 100 ms)
OB4x   hardware interrupt OBs
OB82   diagnostic interrupt handling
```

OB1 calls the application FBs in order; time-critical control goes into a
cyclic-interrupt OB with a fixed period. Motion and PID are frequently
delegated to **technology objects** — firmware-supported objects commanded
from user code via `MC_*` and PID instructions rather than implemented as pure
user logic (see the S7-1500/S7-1500T motion control overview manual).

### I/O flow: the process image

The S7 CPU maintains a **process image**: at defined points in the cycle,
physical input values are copied into the process-image inputs and
process-image outputs are transferred to the output modules. During block
execution the program reads and writes the image, so an input value is
consistent for the whole cycle (or process-image partition) in which it was
captured. Direct peripheral access exists for cases that need fresher values,
at the cost of that consistency (see the S7-1500 cycle and response times
function manual).

### Reuse: library types and master copies

TIA Portal libraries distinguish two forms:

- **Types** — version-managed objects; instances in projects stay linked to
  the type and its version. Suited to standardization across many machines or
  projects.
- **Master copies** — plain templates; the copy is independent and can be
  freely modified. Suited to starting points rather than enforced standards.

Siemens also ships engineering libraries (for example the Library of General
Functions, containing blocks such as `LGF_FIFO`), and application examples for
common patterns.

### Hardware philosophy: engineered appliance

A TIA project is anchored to a specific, configured controller: the chosen CPU
determines memory, execution resources, and technology-object capacity, and
the station configuration (S7-1500 CPU plus ET 200 distributed I/O over
PROFINET, drives, HMI, safety) is engineered in the same tool. The strengths
that follow are tight integration and consistent diagnostics across the
Siemens device family; the corresponding constraint is that the project is
shaped around that configured hardware. PROFINET (with PROFIBUS still common
on installed systems) is the typical fieldbus in this ecosystem.

---

## Rockwell (Logix 5000: ControlLogix / CompactLogix, Studio 5000)

### Program hierarchy: task → program → routine

A Logix controller organizes code as:

```
Controller
├── Controller-scope tags
├── I/O configuration (module tree)
├── Data types (UDTs) and Add-On Instructions
└── Tasks
    └── Programs
        ├── Program-scope tags
        └── Routines (LD, ST, FBD, SFC)
```

Tasks come in three kinds: **continuous** (runs whenever nothing
higher-priority is running — the free-running background, analogous in role to
OB1), **periodic** (fixed interval, analogous in role to a cyclic-interrupt
OB), and **event** (triggered by a defined event). A task schedules one or
more programs; each program has a main routine that calls its other routines.
Rockwell publication 1756-PM005 (Logix 5000 Controllers Tasks, Programs, and
Routines) is the reference for this model.

### Memory model: tags, not addresses

Logix has no engineer-visible address-based memory map and no separate
data-block object. All data lives in **tags** — named, typed objects — at one
of two scopes:

- **Controller scope** — visible to the whole controller (and typically to
  HMI/SCADA).
- **Program scope** — private to one program; two programs can each have their
  own `CycleTimer` without collision.

A structured equipment record is built as a **UDT**: `Pump101` of type
`UDT_Pump` carries its commands, statuses, alarms, and statistics as members
of one named tag. Where Siemens separates FB from instance DB, Logix folds
"the memory" into the tag itself — the tag *is* the data object.

### Reuse: Add-On Instructions

The AOI is the Logix unit of packaged logic: parameters (Input/Output/InOut),
local tags, and logic wrapped into a custom instruction that drops into a rung
or ST expression like a built-in instruction. Each use is backed by an
instance tag holding that instance's state. AOIs also carry optional auxiliary
scans defined by the platform — logic executed on prescan, postscan, and when
the instruction's rung-condition-in is false — which exist so an AOI can
initialize and clean up the way native instructions do. Their exact semantics
are version-dependent; Rockwell publication 1756-PM010 (Add-On Instructions)
is the reference.

Logix also ships many specialized native instructions that carry their own
state in standard structures (for example `FFL`/`FFU` with a `CONTROL`
structure exposing position and status bits) — a pattern that favours online
ladder diagnostics, because the instruction's progress is visible in
standardized members.

### I/O flow: module tags updated at RPI — asynchronously

Adding an I/O module to the configuration generates **module-defined tags**
(`Local:2:I`, `Local:2:O`, `ModuleName:C`, and similar, depending on the
module profile). I/O data transfers between module and controller at the
configured **RPI (requested packet interval)** — and this transfer is
**asynchronous to program execution**. An input tag can change value between
two rungs of the same routine.

This is the classic surprise for engineers arriving from Siemens, where the
process image holds inputs stable across the cycle by default. The Logix
counterpart is a deliberate buffering pattern: copy module input tags into an
application input structure at the top of the logic (the `CPS` synchronous
copy instruction protects larger structures from mid-copy updates), run the
logic against the buffer, then copy a buffered output structure to the module
output tags. Rockwell publication 1756-PM004 (I/O and Tag Data) documents the
update model and buffering guidance.

### Hardware philosophy: modular connected controller

The Logix ecosystem is organized around a chassis-and-connection model:
controllers, local and remote I/O, drives, and other devices join the project
as configured modules with profiles, each connection carrying properties such
as its RPI. EtherNet/IP (CIP) is the typical fieldbus; produced/consumed tags
extend the same model to controller-to-controller data. The generated module
tags mean the hardware appears in the program as ready-made named structures.

---

## Beckhoff (TwinCAT 3)

### The runtime is software on a PC

TwinCAT 3 splits engineering (**XAE**, hosted inside Visual Studio) from the
real-time runtime (**XAR**), which executes on an industrial PC, embedded PC,
or compatible hardware. The runtime is not limited to PLC: PLC, motion (NC),
safety, vision, HMI, and C++ modules can execute side by side on one machine.
The Beckhoff Information System is the authoritative documentation set.

### Program hierarchy: POUs in a PLC project, tasks in the system

A TwinCAT solution has distinct layers:

- **System** — real-time settings, CPU-core assignment, and **tasks** (each
  with a cycle time and priority, optionally pinned to a dedicated core).
- **I/O** — the fieldbus configuration (typically an EtherCAT master and its
  terminals), maintained separately from the PLC code.
- **PLC project** — POUs (programs, function blocks, functions), DUTs
  (structures, enums), GVLs (global variable lists), referenced libraries, and
  the assignment of program POUs to tasks.

### Memory model and object-oriented extensions

State lives in FB instance variables, program variables, and GVLs — the plain
IEC picture, closer to Siemens' FB-instance idea than to Logix tags, but
without a separate visible data-block object: declaring `fbPump101 : FB_Pump;`
allocates the instance. `RETAIN`/`PERSISTENT` storage classes exist for data
that should survive restarts; whether values actually survive power loss
depends on the target hardware's retention mechanism — verify on your target.

The distinctive TwinCAT trait is the **object-oriented extension set** on
function blocks: methods, properties, interfaces, and FB inheritance
(`EXTENDS`/`IMPLEMENTS`). An equipment FB can expose `Start()` and `Stop()`
methods and an `Available` property, implement a shared `I_Equipment`
interface, and be extended by a variant FB — conventional software-engineering
structure applied to control logic. These are documented as extensions beyond
the base IEC 61131-3 FB model; teams can also ignore them and write plain IEC
code.

### Execution model: real-time tasks on CPU cores

The TwinCAT real-time scheduler runs configured tasks at their cycle times and
priorities on assigned cores — for example a 1 ms high-priority task carrying
EtherCAT and motion, a 10 ms machine-control task, and a 100 ms task for slow
loops and communications. PLC programs are explicitly assigned to tasks, so
execution timing is an engineering decision made in the system layer rather
than a property of the code itself.

### I/O flow: explicit linking, task-synchronized image

Hardware I/O is configured in the I/O layer, and PLC process-image variables
(declared `AT %I*` / `AT %Q*`) are **explicitly linked** to fieldbus process
data. For a task-synchronized process image, inputs update around the start of
the task cycle and outputs around its end, so the PLC code sees a consistent
image per task cycle — closer to the Siemens process-image behaviour than to
the Logix RPI model, but scoped per task. EtherCAT is the native fieldbus, and
its distributed-clock synchronization pairs naturally with the task model for
motion applications.

### Reuse: versioned libraries

The Beckhoff reuse unit is the **PLC library**: versioned packages of FBs,
functions, and DUTs referenced by projects. Beckhoff ships a broad standard
set (Tc2_Standard, Tc2_System, Tc2_Utilities, Tc2_MC2 for PLCopen motion, and
newer Tc3 libraries), and companies typically maintain their own versioned
libraries the same way. Many needs that are a native instruction on Logix are
a library FB here — for example `FB_MemRingBuffer` in Tc2_Utilities for FIFO
queues.

---

## Concept translation table

Original summary — not reproduced from any vendor document. Terms in one cell
are *role* equivalents, not exact behavioural equivalents; verify semantics
against platform documentation before relying on them.

| Concept | Siemens (TIA Portal) | Rockwell (Logix) | Beckhoff (TwinCAT 3) |
|---|---|---|---|
| Cyclic execution container | OB1 (free-running cycle) | Continuous task | Real-time task (cycle time set) |
| Fixed-period execution | Cyclic interrupt OB (OB3x) | Periodic task | Task at that cycle time |
| Event-driven execution | Hardware interrupt OB | Event task | Task triggered by event/interrupt |
| Top-level code container | OB calling FBs/FCs | Program with routines | Program POU assigned to a task |
| Stateful reusable unit | FB + instance DB | AOI + instance tag | FB (optionally with methods/interfaces) |
| Stateless routine | FC | Routine / subroutine call | FUNCTION |
| Shared global data | Global DB | Controller-scope tags | GVL |
| Module-local data | Instance DB / block interface | Program-scope tags, AOI locals | FB instance / program variables |
| Structured data type | PLC data type (UDT) | UDT | DUT (STRUCT) |
| I/O binding | Process image + hardware tags | Module-defined tags at RPI | Linked process-image variables |
| Input consistency default | Stable per cycle (process image) | Can change mid-scan (buffer it) | Stable per task cycle |
| Reuse distribution | Library types / master copies | AOI + UDT export | Versioned PLC libraries |
| Typical fieldbus | PROFINET | EtherNet/IP (CIP) | EtherCAT |

## One FIFO, three dialects

The same job queue — enqueue a job record, dequeue the oldest — lands on a
different mechanism in each ecosystem. Constructed teaching example; all
snippets illustrative, not platform code.

**Siemens** — a library or user FB over an array in a DB. The Library of
General Functions provides `LGF_FIFO`; the equivalent hand-rolled pattern is a
ring buffer with read/write indices in an instance or global DB:

```
DB_JobQueue: Buffer[0..49] of "UDT_Job", ReadIdx, WriteIdx, Count
"FB_JobQueue"(Enqueue := #NewJobReady, JobIn := #NewJob,
              Dequeue := #TakeJob,     JobOut => #NextJob);
```

**Rockwell** — the native instruction pair. `FFL` loads a tag into the FIFO
array, `FFU` unloads the oldest; both share a `CONTROL` structure whose
members (position, length, status bits) are watchable online:

```
FFL(NewJob, JobFIFO[0], JobFIFO_Ctl, 50, ?)   // on enqueue pulse
FFU(JobFIFO[0], NextJob, JobFIFO_Ctl, 50, ?)  // on dequeue pulse
```

**Beckhoff** — a utility-library FB over user-supplied memory.
`FB_MemRingBuffer` (Tc2_Utilities) stores and returns records FIFO-fashion via
add/remove actions against a byte buffer the application declares:

```
fbQueue : FB_MemRingBuffer;
aBuf    : ARRAY[0..4095] OF BYTE;
fbQueue.A_AddTail(pWrite := ADR(stNewJob),  cbWrite := SIZEOF(stNewJob), ...);
fbQueue.A_RemoveHead(pRead := ADR(stNextJob), cbRead := SIZEOF(stNextJob), ...);
```

One concept — a bounded oldest-first queue — as a DB-backed FB, a native
instruction with a control structure, and a library object: the
vendor-architecture story in miniature.

## One algorithm, three homes: runtime staging

Task: from a group of pumps, select the available pump with the lowest running
hours (runtime staging / lead-lag wear levelling). The ranking loop itself is
near-identical Structured Text on all three platforms; what differs is where
the algorithm and its state live. Constructed teaching example.

The shared core (illustrative — not platform code):

```
Lowest := 1.0E12;  Selected := -1;
FOR i := 0 TO PumpCount - 1 DO
    IF Pump[i].Available AND (Pump[i].RunHours < Lowest) THEN
        Lowest := Pump[i].RunHours;
        Selected := i;
    END_IF;
END_FOR;
```

- **Siemens**: the loop lives in an SCL-written `FB_Staging` called from OB1
  or a cyclic OB; the pump array passes through the block interface (InOut);
  the selection result persists in the FB's instance DB; individual `FB_Pump`
  instances receive the start request.
- **Rockwell**: the loop lives in an ST routine (or an AOI) inside a staging
  program under a periodic task; pump data is an array of UDT tags; the
  selected index is a program- or controller-scope tag consumed by ladder
  command routines.
- **Beckhoff**: the loop lives in an `FB_Staging` method executed by the
  machine-control task; pump objects can be an array of FB instances, and the
  selection can end in a method call on the chosen pump object.

Notice the design survives translation because it was structured as
*algorithm + data structure + thin platform binding*. That is the portability
lesson.

## Structuring programs to survive a platform port

Application structure that keys off functional layers rather than vendor
constructs ports well. A layering that works on all three (see the
program-structure module for the full treatment):

```
System / diagnostics → I/O mapping & validation → control modules
(motors, valves) → equipment modules → modes & states → sequences →
staging & scheduling → alarms → HMI/SCADA/MES integration
```

Vendor mapping of that structure:

| Layer | Siemens | Rockwell | Beckhoff |
|---|---|---|---|
| Execution scheduling | OBs | Tasks + programs | Real-time tasks |
| Device objects | FB + instance DB | AOI + UDT | FB instances |
| Shared machine data | Global DB | Controller tags | GVL |
| Complex algorithms | SCL blocks | ST routines / AOIs | ST FBs / methods |
| Interlock/permissive logic | LAD/FBD | Ladder | LD/FBD/ST |
| Hardware binding | Process image / HW tags | Module tags | Symbol links |

Practical portability habits:

- Keep raw I/O mapping in one thin layer; everything else works on
  application structures rather than hardware tags directly.
- Put algorithms (queues, ranking, scheduling, state machines) in Structured
  Text inside the platform's stateful reuse unit — ST is the most portable of
  the IEC languages in practice.
- Keep ladder for physical commands, permissives, and diagnostics, where its
  online readability earns its keep.
- Express machine state as an explicit state machine (see the state-machines
  module) rather than as vendor-specific latches.
- Document data ownership (which layer writes what) — the concept transfers
  even when the container (DB / tag scope / GVL) changes.

## Platform fit by project character

Neutral fit observations — none of these are exclusive, all three ecosystems
can build all of these systems, and installed base, house standards, and local
support usually weigh more than architecture:

- A Siemens-centred architecture is commonly chosen when the plant is already
  engineered around PROFINET, Siemens drives/HMI/safety, and standardized
  block libraries — the explicit FB/instance-DB separation and TIA type
  libraries suit organizations that formalize their engineering standards.
- A Logix-centred architecture is commonly chosen when maintenance
  troubleshoots primarily in online ladder, the facility standard is
  EtherNet/IP, and equipment is represented as UDT/AOI objects — direct tag
  visibility and native diagnostic-rich instructions suit that operating
  style.
- A TwinCAT-centred architecture is commonly chosen for high-speed or
  many-axis motion, EtherCAT-synchronized machinery, and teams that want
  software-engineering structure (methods, interfaces, versioned libraries,
  source control) and PC-level integration of PLC, motion, vision, and custom
  code on one runtime.

The translation skill matters more than the choice: an engineer who can say
"instance DB ≈ AOI backing tag ≈ FB instance" and "cyclic-interrupt OB ≈
periodic task ≈ 10 ms real-time task" can be productive on an unfamiliar
platform in days, not months.

## Sources

Vendor documentation consulted for the behaviours described above (verify
against the edition current for your platform):

- Siemens, *Programming Guideline for S7-1200/S7-1500* (DOC v16): https://support.industry.siemens.com/cs/attachments/90885040/81318674_Programming_guideline_DOC_v16_en.pdf
- Siemens, *S7-1500 Cycle and Response Times* function manual: https://support.industry.siemens.com/cs/attachments/59193558/s71500_cycle_and_reaction_times_function_manual_en-US_en-US.pdf
- Siemens Industry Online Support, *Programming queues (FIFO) (S7-1200, S7-1500)*: https://support.industry.siemens.com/cs/mdm/109742272?c=86842143115&lc=el-GR
- Siemens Industry Online Support, *Master copies and types* (STEP 7 Professional): https://support.industry.siemens.com/cs/mdm/109011420?c=69219625867&lc=en-id
- Siemens, *S7-1500/S7-1500T Motion Control Overview* function manual: https://support.industry.siemens.com/cs/attachments/109812056/s71500_s71500t_motion_control_overview_function_manual_en-US_en-US.pdf
- Rockwell Automation, *Logix 5000 Controllers Sequential Function Charts*, publication 1756-PM006: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm006_-en-p.pdf
- Rockwell Automation, *Logix 5000 Controllers Add-On Instructions*, publication 1756-PM010: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm010_-en-p.pdf
- Rockwell Automation, *Logix 5000 Controllers EDS AOP Guidelines for Logix Designer*, publication 1756-PM002: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm002_-en-d.pdf
- Rockwell Automation, *Logix 5000 Controllers I/O and Tag Data*, publication 1756-PM004: https://literature.rockwellautomation.com/idc/groups/literature/documents/pm/1756-pm004_-en-p.pdf
- Rockwell Automation, Studio 5000 instruction reference, *FIFO Load (FFL)*: https://www.rockwellautomation.com/en-us/docs/studio-5000-logix-designer/38-01/contents-ditamap/instruction-set/array--file--shift-instructions/fifo-load--ffl-.html
- Beckhoff Information System, *Your first TwinCAT 3 PLC project*: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2525041803.html
- Beckhoff Information System, *Object Function block*: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2530279563.html
- Beckhoff Information System, *Tasks*: https://infosys.beckhoff.com/content/1033/tc3_grundlagen/17677068555.html
- Beckhoff Information System, *TwinCAT real-time*: https://infosys.beckhoff.com/content/1033/tc3_grundlagen/6828869003.html
- Beckhoff Information System, *Object Function*: https://infosys.beckhoff.com/content/1033/tc3_plc_intro/2530284939.html
- Beckhoff Information System, *FB_MemRingBuffer* (Tc2_Utilities): https://infosys.beckhoff.com/content/1033/tcplclib_tc2_utilities/35010187.html
- Beckhoff, *TwinCAT automation software* product documentation: https://www.beckhoff.com/en-us/products/automation/twincat/

## Related

- PLC software: languages_overview (the five IEC 61131-3 languages),
  program_structure (POUs, tasks, scope — the shared model these platforms
  implement), state_machines (the portable sequence pattern),
  safety_application_patterns
- Communications: EtherCAT, PROFINET, EtherNet/IP protocol notes
- Design: machine architecture model (where the controller sits in the 7-layer
  view)
