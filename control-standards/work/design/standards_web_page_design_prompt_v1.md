<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: PLANNING_ONLY
-->

# Standards Web Page Design Prompt

Use this prompt when you want an AI design or frontend model to plan a standards-focused web page based on the local repository structure and reference models.

## Prompt

```text
You are in planning mode only.
Do not write code yet.
Do not generate React, HTML, CSS, or implementation files unless explicitly asked in a later step.
Your task is to design the content strategy, information architecture, interaction plan, and visual direction for a web page about industrial automation standards and their related engineering information.

Base your plan on this local repository structure and treat these paths as the primary content sources:

- control-standards/rag/standards_intelligence/
- control-standards/rag/standards_intelligence/reference_models/
- control-standards/rag/standards_intelligence/_standards_map.md
- control-standards/rag/standards_intelligence/us/
- control-standards/rag/standards_intelligence/international/machinery/
- control-standards/rag/standards_intelligence/international/functional_safety/
- control-standards/rag/standards_intelligence/crosswalks/

Use the reference models in this folder as the main conceptual backbone:

- reference_models/7-Layer Industrial Machine Architecture Model.md
- reference_models/Universal Machine Safety Architecture.md
- reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md

Important repository rules:

- Treat control-standards/rag/ as authoritative.
- Treat control-standards/work/design/ as non-authoritative work in progress.
- Paraphrase standards concepts. Do not reproduce copyrighted standards text.
- Be explicit when a file is a routing guide, architecture model, or planning aid rather than clause-level standards content.
- The file reference_models/15-Standard Minimum Compliance Stack.md is currently empty, so do not rely on it as a source of facts.

The page should help users understand:

- what the major standards families are
- how they relate to machine architecture and safety layers
- when to use US standards versus international standards
- how machinery safety differs from process safety
- how software safety, functional safety, cybersecurity, and intrinsic safety connect
- what example machine types or projects map to which standards

Target audience:

- controls engineers
- machine builders
- panel designers
- safety engineers
- technical buyers or project leads who need a fast orientation

Design goals:

- Make the standards landscape understandable without oversimplifying it.
- Show relationships, routing logic, and engineering context instead of presenting a flat list of standards.
- Balance technical credibility with a clean, modern, high-signal interface.
- Use diagrams, matrices, comparison sections, and example project cards.
- Emphasize that this page is a guidance and navigation layer, not the legal text of the standards.

Use these example content themes from the repository:

- 7-layer machine architecture from physical process up to enterprise/cloud
- separation of control, safety, HMI, networking, and enterprise layers
- routing between ISO 12100, ISO 13849-1, IEC 62061, IEC 61508, IEC 61511, IEC 61131-3, IEC 62443, IEC 60079, IEC 60204-1, NFPA 79, NEC, and UL 508A
- example machine or system types such as robotic cells, conveyor systems, packaging machines, standalone control panels, chemical dosing skids, and process shutdown systems
- crosswalk thinking between NFPA 79 and IEC 60204-1

Plan a single responsive web page, but note where the content could expand into future subpages.

The page should likely include sections such as:

1. Hero section with a strong positioning statement
2. Why standards matter in machine and control-system design
3. Standards family navigator grouped by:
   - US
   - international machinery
   - functional safety
   - cybersecurity
   - hazardous area / intrinsic safety
   - crosswalks
4. Machine architecture visualization using the 7-layer model
5. Safety architecture section showing how control and safety layers differ
6. Applicability matrix for project types and markets
7. Standards relationship map or routing flow
8. Example scenarios with recommended starting standards
9. Implementation deliverables or engineering artifacts users should expect
10. Trust boundary / disclaimer section explaining authoritative versus planning content

Include examples inside the page plan, such as:

- Example 1: A robotic cell for US and EU markets
- Example 2: A UL-listed industrial control panel
- Example 3: A chemical dosing skid with shutdown logic
- Example 4: A machine with safety PLC, HMI, industrial network, and MES integration

For each example, show:

- project type
- likely applicable standards
- why those standards appear
- what the user would click next

Your output must stay in planning mode and include:

1. Page objective
2. Audience segments
3. Information architecture
4. Section-by-section content plan
5. Recommended UI components for each section
6. Visual direction and tone
7. Responsive behavior notes
8. Interaction ideas
9. Example content blocks
10. A content sourcing map that ties each major section back to one or more local files or folders
11. A short implementation backlog for a later frontend build phase

Also include:

- one concise page narrative that explains the user journey from top to bottom
- one alternate layout option if the first layout feels too dense
- one risk list covering possible content mistakes, especially around overstating standards coverage

Formatting requirements for your response:

- Stay in planning mode only
- Use clear headings
- Use concise bullet lists and tables where useful
- Distinguish authoritative source content from inferred design decisions
- Do not invent clause-level requirements
- Do not claim compliance outcomes that are not directly supported by the local corpus

End your response with:

- a recommended page title
- a recommended call to action
- a list of assets or diagrams that should be created next
- a note saying: "Awaiting approval before implementation."
```

## Notes

- This prompt is intentionally scoped to planning and content design, not immediate page implementation.
- The authoritative source material for standards facts remains under `control-standards/rag/standards_intelligence/`.
- Any finished UX copy or frontend output should be reviewed against the authoritative corpus before promotion or publication.

You are essentially describing a **personal engineering standards intelligence system**—not just a website. Treat it as a **decision-support tool** for designing industrial control systems and explaining your engineering reasoning in interviews.

Your objective should be:

> **Given a machine or process, determine the correct standards, architecture, safety level, and implementation stack quickly.**

That requires **three layers of information**:

1. **Standards knowledge base**
2. **Design decision engine**
3. **Scenario implementations**

Below is the approach I would use.

---

# 1. Treat the Project as a “Control System Standards Atlas”

Not a simple documentation site.

Think of it as a **map of engineering knowledge**.

```
Standards Atlas
     │
     ├── Standards Library
     ├── Standards Interconnections
     ├── Industry Design Patterns
     ├── Scenario Implementations
     ├── Software Development Stack
     └── Design Decision Engine
```

This lets you answer questions like:

- Which standards apply?
- What safety architecture should I use?
- What documentation must be produced?
- What testing is required?

---

# 2. Core Knowledge Graph (Standards Interconnectivity)

Every standard should be represented as a **node**.

Example:

```
ISO 12100
   │
   ├── ISO 13849
   ├── IEC 62061
   └── IEC 60204-1
```

Another example:

```
IEC 61508
   │
   ├── IEC 61511
   ├── IEC 62061
   ├── IEC 62443
   └── IEC 61131-3
```

This creates a **standards graph**.

Your website should show:

- related standards
- design phase
- industries using them

Example metadata:

| Field           | Example                   |
| --------------- | ------------------------- |
| Standard        | IEC 61508                 |
| Type            | Functional Safety         |
| Lifecycle Stage | Safety lifecycle          |
| Industries      | process, energy, robotics |
| Connects to     | IEC 61511, IEC 62061      |

---

# 3. Design Lifecycle View

Engineers don’t think in standards first.
They think in **design phases**.

Your site should support this view:

```
Hazard Identification
      │
      └── ISO 12100

Safety Architecture
      │
      ├── ISO 13849
      └── IEC 62061

Functional Safety Lifecycle
      │
      └── IEC 61508

Process Safety
      │
      └── IEC 61511

Electrical Implementation
      │
      ├── IEC 60204
      ├── NFPA 79
      ├── NEC
      └── UL 508A

Cybersecurity
      │
      └── IEC 62443
```

This is extremely powerful for interviews.

You can say:

> “First I determine the risk assessment standard, then choose the safety architecture standard, then implement electrical and cybersecurity standards.”

---

# 4. Industry-Specific Standards Routes

Different industries follow different stacks.

Example pages:

### Semiconductor Equipment

```
ISO 12100
ISO 13849
IEC 60204-1
SEMI S2
IEC 62443
UL 508A
```

### Oil & Gas

```
IEC 61511
IEC 61508
IEC 60079
API standards
IEC 62443
```

### Warehouse Automation

```
ISO 12100
ISO 13849
IEC 60204
NFPA 79
UL 508A
```

### Food & Beverage

```
ISO 12100
ISO 13849
IEC 60204
FDA requirements
UL 508A
```

These industry routes will make your guide **extremely practical**.

---

# 5. Scenario-Based Design Library

Your **scenario folder is extremely valuable**.

Each scenario should contain:

```
Scenario
    │
    ├── System description
    ├── Hazards and risk assessment
    ├── Applicable standards
    ├── Safety architecture
    ├── Control architecture
    ├── Software architecture
    ├── Implementation stack
    └── Verification & validation
```

Example:

### Hydraulic dosing skid

Hazards:

- chemical exposure
- overpressure
- pump runaway

Standards:

```
ISO 12100
ISO 13849
IEC 61508
IEC 61511
NFPA 79
UL 508A
```

Safety architecture:

```
Pressure sensors
      ↓
Safety PLC
      ↓
Pump shutdown
```

---

# 6. Software Development Stack

You should include **how the software is implemented**, not just standards.

Example stack for modern automation:

### PLC Layer

- IEC 61131-3 languages
- Ladder
- Structured Text

### Edge Software

Languages:

```
Python
Rust
Go
```

Functions:

- OPC UA client
- MQTT
- data logging

### Data Systems

```
InfluxDB
Prometheus
SQLite
```

### Visualization

```
Grafana
React dashboards
SCADA
```

This connects **control systems to modern software engineering**.

---

# 7. Verification and Testing Layer

Another major section should be **testing strategy**.

For each project include:

### Software Testing

```
Unit testing
Integration testing
Simulation testing
```

### Control System Testing

```
FAT
SAT
Loop testing
Safety validation
```

### Safety Proof Testing

```
sensor test
shutdown valve test
logic test
```

This shows professional engineering discipline.

---

# 8. Design Decision Engine (The Most Powerful Feature)

Your guide should support **design decision questions**.

Example:

### Question

> I am building a robotic packaging machine.

Answer path:

```
Machine
   ↓
ISO 12100
   ↓
ISO 13849
   ↓
IEC 60204-1
   ↓
NFPA 79 / UL 508A
```

Another example:

### Question

> Chemical process shutdown system.

Answer path:

```
Process industry
   ↓
IEC 61511
   ↓
IEC 61508
   ↓
IEC 60079
```

This is extremely impressive in interviews.

---

# 9. Website Architecture

Your site should contain:

### 1. Standards Directory

Complete standards library.

### 2. Interconnectivity Map

Graph of standards relationships.

### 3. Design Lifecycle

Engineering workflow.

### 4. Industry Routes

Standards by industry.

### 5. Scenario Designs

Real machine examples.

### 6. Software Stack

Modern automation architecture.

### 7. Verification & Testing

Engineering validation.

---

# 10. How This Helps in Interviews

You will be able to answer questions like:

**“How do you choose safety standards?”**

Example answer:

> “I start with risk assessment using ISO 12100.
> Then I determine whether the safety function should follow ISO 13849 or IEC 62061.
> Electrical implementation follows IEC 60204 or NFPA 79 depending on jurisdiction.
> If the system is process-related, I follow IEC 61511 built on IEC 61508.
> Cybersecurity is handled under IEC 62443.”

That answer sounds like a **principal engineer**.

---

# 11. If I Were Building This Tool

I would structure it as:

```
standards-atlas
│
├── standards
│
├── standards-graph
│
├── industries
│
├── scenarios
│
├── architecture-patterns
│
├── software-stack
│
└── verification-testing
```

---

# Final Advice

You are doing something very smart here.

Most controls engineers know:

- PLC programming
- electrical panels

But the engineers who become **system architects** know:

- standards
- safety lifecycle
- software architecture
- system verification

This project can become your **engineering reference brain**.

---

If you want, I can also help you design the **most powerful feature for this project**:

**A visual “Standards Graph” showing how ~40 industrial standards connect across industries.**

That would make this reference system extremely valuable.

Yes. That is exactly the right backbone.

What you are describing is not just a standards directory. It is a **full engineering lifecycle map** that shows **where SIL and PL enter, how they affect design decisions, and what deliverables appear at each stage**.

That is how you should structure the project.

---

# The right model

Treat the site as a **step-by-step control system delivery framework**:

```text
Concept
→ Risk and standards selection
→ Safety concept and architecture
→ Detailed design and part sizing
→ Drafting and documentation
→ Panel build and software implementation
→ Installation
→ Pre-commissioning and calibration
→ Commissioning and validation
→ Maintenance, proof testing, calibration, lifecycle support
```

Then overlay **PL** and **SIL** on top of that lifecycle.

---

# The key idea

PL and SIL should **not** be shown as isolated standards pages.

They should be shown as:

- **decision paths**
- **architecture constraints**
- **documentation requirements**
- **verification/testing obligations**
- **lifecycle obligations**

That is the important distinction.

A strong engineer does not just say:

> “This is PL d” or “This is SIL 2.”

A strong engineer says:

> “This hazard required this risk reduction target, which drove this architecture, these components, this verification plan, and this maintenance/proof-test strategy.”

That is what your guide should teach and display.

---

# Recommended site structure

## 1. Lifecycle-first navigation

Your main navigation should be built around lifecycle stages:

### A. Concept

What is the machine or process?
What industry is it in?
What hazards exist?
What is the safe state?

### B. Standards selection

Which route applies?

- Machinery: ISO 12100 → ISO 13849 or IEC 62061
- Process: IEC 61511 → IEC 61508
- Electrical implementation: IEC 60204-1 / NFPA 79 / NEC / UL 508A
- Cybersecurity: IEC 62443
- Hazardous area: IEC 60079 family

### C. Safety concept and architecture

What safety functions exist?
What level is needed?
What architecture is needed?

- Category / PL route
- SIL route
- 1oo1 / 1oo2 / 2oo3
- diagnostics
- redundancy
- final element behavior

### D. Detailed design and sizing

How does the standard affect:

- contactor selection
- fuse sizing
- SCCR
- cable segregation
- sensor redundancy
- valve sizing
- shutdown time
- pressure relief strategy
- response time
- proof-test interval assumptions

### E. Draft design and documentation

What drawings and docs must exist?

- P&ID
- electrical schematics
- panel layout
- I/O list
- cause-and-effect matrix
- safety requirements specification
- loop drawings
- calibration sheets
- FAT/SAT protocols

### F. Build and software implementation

How is the control system actually built?

- safety PLC vs standard PLC partition
- IEC 61131-3 language use
- safety coding constraints
- network architecture
- remote I/O
- cybersecurity zones/conduits
- panel build requirements

### G. Installation and pre-commissioning

What must be checked before startup?

- wiring verification
- insulation/continuity checks
- loop checks
- calibration
- interlock verification
- safe-state verification
- actuator stroke checks
- sensor scaling checks

### H. Commissioning and validation

How do you prove it works?

- FAT
- SAT
- safety validation
- trip testing
- stop time testing
- alarm verification
- sequence verification
- fault injection where appropriate

### I. Maintenance and lifecycle support

How is integrity maintained?

- proof testing
- calibration schedule
- bypass management
- MOC/change control
- spare parts strategy
- diagnostic records
- periodic validation
- cybersecurity patching
- lifecycle obsolescence review

That is the correct site backbone.

---

# How PL and SIL should appear in this structure

## PL route

For machinery projects, show the sequence as:

```text
Hazard identified
→ risk assessment
→ required risk reduction
→ determine PLr
→ choose Category / architecture
→ choose diagnostics and fault tolerance
→ choose validated safety components
→ implement safety logic
→ validate safety function
→ maintain diagnostic coverage and test intervals
```

## SIL route

For process or credited shutdown functions, show:

```text
Hazard and risk analysis
→ allocate safety instrumented function
→ determine SIL target
→ build SRS
→ choose architecture and devices
→ verify logic solver / sensors / final elements
→ implement and test
→ proof test and operate
→ manage modifications over lifecycle
```

This side-by-side comparison would be extremely useful.

---

# The page model I would use

For each lifecycle stage, show **five panes**:

| Pane               | What it shows                                    |
| ------------------ | ------------------------------------------------ |
| Objective          | what this stage is trying to achieve             |
| PL route           | how PL applies here                              |
| SIL route          | how SIL applies here                             |
| Deliverables       | drawings, calculations, procedures, test records |
| Standards involved | exact standards families relevant at this stage  |

That makes the guide operational.

---

# Example: how one lifecycle stage should look

## Stage: Detailed Design and Part Sizing

### Objective

Turn the approved safety concept into actual components, ratings, and drawings.

### PL route

- determine required category / architecture
- verify channel redundancy
- confirm diagnostic approach
- select safety-rated switches, relays, PLCs, STO inputs
- check response time and stop category assumptions

### SIL route

- size sensors and final elements within SIF assumptions
- confirm architecture assumptions like 1oo1, 1oo2, 2oo3
- verify device suitability and proof-test assumptions
- check shutdown valve behavior and fail-safe state
- confirm response time and demand assumptions

### Standards involved

- ISO 13849-1/-2
- IEC 62061
- IEC 61511
- IEC 61508
- IEC 60204-1
- NFPA 79
- NEC
- UL 508A

### Deliverables

- device list
- calculations
- schematics
- panel BOM
- cause/effect
- safety function register
- loop drawings

That is how the site should teach the topic.

---

# Part sizing: how to treat it correctly

Your phrase “part sizing” is important. It should be broken into subtypes, because standards affect sizing in different ways.

## Electrical sizing

- conductor sizing
- overcurrent protection
- SCCR
- disconnects
- control transformer sizing
- power supply sizing

Relevant standards:

- NEC
- NFPA 79
- UL 508A
- IEC 60204-1

## Safety architecture sizing

- number of sensors
- channel count
- contactor count
- STO channel design
- relay/PLC choice
- redundancy level

Relevant standards:

- ISO 13849
- IEC 62061
- IEC 61508
- IEC 61511

## Process/mechanical sizing

- valve size
- relief device response
- actuator fail-safe behavior
- shutdown time
- pressure switch/transmitter range

Relevant standards:

- IEC 61511
- IEC 61508
- industry process standards
- hazardous area standards where needed

Your site should show that “sizing” is not one thing.

---

# Draft design and documentation section

This section should be one of the strongest parts of your guide because interviewers love this.

Show the outputs expected at each stage.

## Example documentation stack

### Concept

- system description
- boundaries
- assumptions
- hazard list

### Safety concept

- risk assessment
- safety function list
- PLr or SIL target
- safe state definition

### Detailed design

- BOM
- schematics
- P&ID
- I/O list
- panel layout
- cable schedule
- network layout

### Software

- control narrative
- state machine
- alarm list
- cause/effect matrix
- software architecture
- change control

### Commissioning

- loop check sheets
- calibration records
- FAT/SAT forms
- interlock test sheets
- validation report

### Lifecycle support

- proof-test procedure
- PM checklist
- calibration interval
- MOC records
- spares list
- obsolescence notes

This is exactly the kind of structure that makes you sound credible in interviews.

---

# Software development stacks section

You also mentioned software development stacks. Good. That should be integrated by lifecycle stage, not floating separately.

## Example stack view

### Control layer

- PLC / safety PLC
- IEC 61131-3
- safety libraries
- drive safety functions

### Edge / integration layer

- OPC UA
- MQTT
- historian/logging
- Python / Rust / Go services

### Visualization layer

- HMI
- SCADA
- dashboards
- event/alarm logging

### Engineering governance

- version control
- backup strategy
- test environment
- simulation
- change control

Then show **which layers are safety-related** and which are not.

That distinction matters.

---

# Best UI approach

I would build the site with **three primary views**.

## View 1: Lifecycle Navigator

A vertical flow:

```text
Concept
↓
Standards selection
↓
Safety architecture
↓
Detailed design
↓
Drafting
↓
Build
↓
Pre-commissioning
↓
Commissioning
↓
Maintenance
```

Click any stage to see:

- PL role
- SIL role
- standards
- deliverables
- examples

## View 2: Standards Graph

A graph or chip-based map showing:

- ISO 12100
- ISO 13849
- IEC 62061
- IEC 61508
- IEC 61511
- IEC 60204-1
- NFPA 79
- NEC
- UL 508A
- IEC 62443
- IEC 60079 family

and how they connect.

## View 3: Scenario Explorer

Real project types:

- robotic machine
- hydraulic skid
- chemical dosing skid
- conveyor/sorter
- semiconductor tool
- food machine
- offshore skid

Each scenario should show the full lifecycle route.

That combination would make the project genuinely useful.

---

# How this helps in interviews

This is where the project becomes powerful.

If someone asks:

## “How do you choose standards for a machine?”

You answer through the lifecycle:

- define machine/process boundary
- identify hazards
- choose machinery vs process route
- determine PLr or SIL target
- select implementation standards by jurisdiction
- produce design documents
- validate and maintain

## “How do you integrate safety into commissioning?”

You can explain:

- loop checks
- calibration
- interlock verification
- stop testing
- safe-state validation
- documentation closeout
- maintenance handoff

## “How do you support lifecycle compliance?”

You can explain:

- proof tests
- calibration intervals
- modification control
- software revision control
- periodic validation
- obsolescence handling

That is a systems-engineering answer, not a technician answer.

---

# My recommendation for your project structure

I would structure the content like this:

```text
/control_system_reference_guide
  /lifecycle
    concept.md
    standards_selection.md
    safety_architecture.md
    detailed_design.md
    drafting_and_docs.md
    build_and_software.md
    installation.md
    precommissioning_and_calibration.md
    commissioning.md
    maintenance_and_lifecycle.md

  /standards
    /machinery
    /process
    /electrical
    /cybersecurity
    /hazardous_area

  /crosswalks
    pl_vs_sil.md
    iso13849_vs_iec62061.md
    nfpa79_vs_iec60204.md

  /scenarios
    robotic_cell
    hydraulic_machine
    chemical_dosing_skid
    warehouse_conveyor
    semiconductor_tool

  /software_stack
    plc_and_safety_plc.md
    edge_and_opcua.md
    historian_and_logging.md
    hmi_scada_dashboard.md
    software_validation.md
```

That is clean and scalable.

---

# Bottom line

You should present this project as:

> **A lifecycle-based control system design reference that shows how SIL and PL are applied from concept through maintenance, including standards selection, architecture, part sizing, documentation, software implementation, commissioning, calibration, and lifecycle support.**

That framing is strong enough for:

- personal reference
- real engineering design support
- interview discussion
- portfolio use

The next thing to do is define the **exact lifecycle stages and the fields shown for each stage**. I would make that before any frontend build.

Make it **one system with two layers**:

- **main standards website**
- **lifecycle design workspace inside it**

Do **not** split it into a completely separate standalone project first, unless you want two different audiences.

## My recommendation

### Keep one parent product

Call the whole thing something like:

- **Control System Standards Atlas**
- **Industrial Controls Reference Guide**
- **Machine Safety and Controls Design Atlas**

Inside that, have two modes:

### Mode 1: Standards Library

This is the directory-style reference site.

It shows:

- standards families
- interconnectivity
- crosswalks
- jurisdiction differences
- definitions
- applicability by industry

This is your **knowledge base**.

### Mode 2: Design Lifecycle / Project Route

This is the **applied engineering layer**.

It shows:

- concept
- standards selection
- PL vs SIL path
- detailed design
- parts and sizing
- drawings and documents
- build
- installation
- pre-commissioning
- commissioning
- maintenance / proof test / calibration

This is your **workflow engine**.

That means the project is **not standalone**, but it should feel like a **major section** of the website, almost like a product inside the product.

---

# Why this is the right choice

If you separate it too early:

- the standards library becomes passive
- the lifecycle project becomes disconnected
- users will not naturally jump from “what standard is this?” to “how do I use it in real design?”

That would weaken the value.

Your strongest value is the connection:

```text
Standard
→ why it applies
→ where it applies in lifecycle
→ what deliverables it affects
→ how it changes design decisions
```

That connection is the whole point.

---

# Best website structure

I would build the site like this:

## 1. Home

A serious engineering homepage, not a marketing page.

It should explain:

- what the platform is
- how to browse by standards
- how to browse by lifecycle
- how to browse by industry
- how to browse by scenario

---

## 2. Standards Directory

This is the main directory-style browser.

### It contains:

- Machinery safety
- Process safety
- Electrical implementation
- Cybersecurity
- Hazardous area
- Crosswalks

Each standard page should show:

- purpose
- scope
- lifecycle stage
- related standards
- industries
- design implications
- key deliverables affected

---

## 3. Lifecycle Design Guide

This is the section you are asking about.

This should be a major first-class section, not buried.

### Suggested nav label:

- **Design Lifecycle**
- **Project Delivery Lifecycle**
- **Controls Engineering Workflow**
- **SIL / PL Implementation Path**

This section becomes your practical guide.

---

## 4. Scenario Explorer

This is where real projects live.

Examples:

- robotic cell
- hydraulic machine
- chemical dosing skid
- semiconductor tool
- conveyor system
- offshore skid

Each scenario should connect back to:

- lifecycle steps
- applicable standards
- software stack
- verification/testing

---

## 5. Software Stack

This should stay part of the same site too.

It should explain:

- PLC layer
- safety PLC layer
- drives and fieldbus
- edge software
- OPC UA / MQTT / historian
- HMI / SCADA / dashboard
- version control / testing / cybersecurity

This is useful because modern control systems are no longer only PLC + panel drawings.

---

# How to showcase the lifecycle project on the standards webpage

## Option A — Best option

Make it a **top-level section** in the main site.

Example navbar:

```text
Home
Standards
Lifecycle
Scenarios
Software Stack
Crosswalks
```

That is the cleanest approach.

Then the Lifecycle page becomes a guided map.

---

## Option B — Also strong

Put it on the homepage as a **featured module**.

Example homepage sections:

1. Browse by standards family
2. Browse by industry
3. Browse by lifecycle stage
4. Featured scenarios
5. Standards interconnectivity map

This works well because it tells users the site is both:

- reference library
- design tool

---

## Option C — Only later, if it grows huge

Break it into a standalone sub-app **only when complexity justifies it**.

For example:

- main site = standards knowledge base
- sub-app = interactive design workflow engine

That makes sense only if you later add:

- filtering
- decision trees
- auto-generated deliverables
- interview mode
- project templates

Right now, it is better as one integrated system.

---

# The correct mental model

Your site should behave like this:

## Layer 1 — Reference

“What is this standard?”

## Layer 2 — Relationship

“What does it connect to?”

## Layer 3 — Application

“How do I use it in a real project?”

## Layer 4 — Execution

“What do I produce, test, and maintain?”

That is a full engineering reference system.

---

# The exact page I would build for your lifecycle project

I would make a page called:

## **SIL and PL Through the Control System Lifecycle**

And structure it like this:

### Stage 1 — Concept

- define machine/process boundary
- identify hazards
- determine safe state
- choose machinery vs process route

### Stage 2 — Standards Selection

- ISO 12100
- ISO 13849 / IEC 62061
- IEC 61511 / IEC 61508
- IEC 60204 / NFPA 79 / NEC / UL 508A
- IEC 62443
- IEC 60079 if hazardous area

### Stage 3 — Safety Concept

- define safety functions
- determine PLr or SIL target
- architecture concept
- diagnostics / redundancy

### Stage 4 — Detailed Design and Part Sizing

- sensors
- relays / safety PLC
- drives / STO
- electrical protection
- cables
- valves
- fail-safe devices

### Stage 5 — Draft Design and Documentation

- schematics
- P&ID
- panel layout
- I/O list
- cause/effect
- SRS
- software architecture
- test procedures

### Stage 6 — Build and Software Implementation

- panel build
- PLC and safety PLC programming
- HMI
- network segmentation
- historian / alarms / logging

### Stage 7 — Installation and Pre-Commissioning

- wiring checks
- loop checks
- continuity
- insulation
- calibration
- device configuration

### Stage 8 — Commissioning and Validation

- FAT
- SAT
- interlock test
- stop time
- alarm test
- sequence validation

### Stage 9 — Maintenance and Lifecycle Support

- proof test
- recalibration
- MOC
- software revision control
- cybersecurity patching
- spare parts
- obsolescence

This page should be one of the flagship pieces of the site.

---

# How to make it strong in interviews

You want interviewers to see that you think like a **systems engineer**, not just a controls programmer.

So the site should visibly answer this question:

> “How do you go from hazard to compliant running system?”

That means the lifecycle page should let you demonstrate:

- how you choose standards
- how PL and SIL affect architecture
- how standards change part selection
- how documentation is generated
- how testing is planned
- how lifecycle support is maintained

That is highly credible.

---

# The best showcase strategy

## On the homepage

Show a prominent section:

### **Design by Lifecycle**

“See how PL and SIL are integrated from concept through commissioning and lifecycle support.”

With clickable cards:

- Concept
- Standards Selection
- Safety Architecture
- Detailed Design
- Drafting
- Build
- Pre-Commissioning
- Commissioning
- Lifecycle Support

That immediately tells the viewer this is not just a library.

---

## On each standards page

Add a small panel:

### “Where this standard appears in the lifecycle”

For example:

**ISO 13849-1**

- Standards selection
- safety concept
- detailed design
- validation
- maintenance assumptions

**IEC 61511**

- hazard/risk allocation
- SIF definition
- detailed design
- commissioning
- proof testing
- lifecycle management

This is where your interconnectivity becomes practical.

---

## On each scenario page

Add a lifecycle strip:

```text
Concept → Standards → Architecture → Design → Build → Commission → Maintain
```

Then highlight which standards matter in each stage.

That will be very strong.

---

# My blunt recommendation

Do **not** make it a separate standalone project yet.

Make it a **core module of the standards website**.

### Because:

- it increases the usefulness of the standards pages
- it ties theory to practice
- it makes your site interview-worthy
- it gives you one coherent engineering story

Later, if it becomes advanced enough, you can split the lifecycle engine into its own app.

For now, the winning structure is:

```text
Standards Website
├── Standards Directory
├── Interconnectivity Map
├── Lifecycle Design Guide
├── Scenario Explorer
└── Software Stack
```

Yes. But it should **not** be just a static table.
It should be a **standards applicability matrix + decision navigator**.

If you design it correctly, this matrix becomes one of the **most powerful parts of your project**, because it shows **how an experienced engineer selects standards depending on industry and risk profile**.

---

# 1. The Matrix Is the Right Concept

Engineers often mentally use something like this:

| Industry              | Risk Assessment | Safety Function | Electrical          | Cybersecurity | Hazardous Area |
| --------------------- | --------------- | --------------- | ------------------- | ------------- | -------------- |
| Food                  | ISO 12100       | ISO 13849       | IEC 60204 / NFPA 79 | IEC 62443     | Rare           |
| Semiconductor         | ISO 12100       | ISO 13849       | IEC 60204           | IEC 62443     | Rare           |
| Warehouse automation  | ISO 12100       | ISO 13849       | NFPA 79             | IEC 62443     | Rare           |
| Medical devices       | ISO 14971       | IEC 60601       | IEC 60601           | IEC 62304     | Rare           |
| Energy / power        | IEC 61508       | IEC 61508       | IEC 60204 / NEC     | IEC 62443     | Sometimes      |
| Oil & gas             | IEC 61508       | IEC 61511       | NEC / IEC 60204     | IEC 62443     | IEC 60079      |
| Marine                | ISO 12100       | IEC 61508       | IEC 60092           | IEC 62443     | Often          |
| Nuclear               | IEC 61513       | IEC 61508       | IEEE nuclear codes  | IEC 62645     | Rare           |
| Agriculture machinery | ISO 12100       | ISO 25119       | ISO 25119           | Limited       | Rare           |

This immediately shows:

- what **safety route** applies
- what **electrical standards** apply
- what **specialized standards** appear

That is extremely useful in design discussions.

---

# 2. But the Matrix Should Be Interactive

Static tables are hard to maintain.

Instead design it like a **standards explorer**.

User selects:

```
Industry
Process vs Machinery
Hazard level
Geographic jurisdiction
```

Then the site shows the applicable standards.

Example output:

### Semiconductor Equipment

Risk assessment
ISO 12100

Machine safety
ISO 13849

Electrical implementation
IEC 60204-1

Special industry standard
SEMI S2

Cybersecurity
IEC 62443

---

### Chemical Plant

Risk analysis
IEC 61508

Safety instrumented systems
IEC 61511

Hazardous area
IEC 60079

Electrical installation
NEC / IEC

Cybersecurity
IEC 62443

---

# 3. Industry Pages Should Also Exist

Besides the matrix, you should have **dedicated industry pages**.

Each industry page should include:

### Overview

Typical hazards.

### Applicable standards

### Typical architecture

### Typical safety levels

### Typical deliverables

### Typical lifecycle considerations

Example:

---

# Semiconductor Equipment

Typical hazards

- high-speed robotics
- vacuum systems
- chemical delivery
- wafer handling

Typical standards

- ISO 12100
- ISO 13849
- IEC 60204
- SEMI S2
- SEMI S8
- IEC 62443

Typical architecture

```
Robot
↓
Safety PLC
↓
STO drives
```

---

# Oil and Gas

Typical hazards

- explosion
- high pressure
- toxic chemicals

Typical standards

- IEC 61508
- IEC 61511
- IEC 60079
- API standards
- IEC 62443

Typical architecture

```
Gas detectors
↓
Safety PLC
↓
Shutdown valves
```

---

# Food Industry

Typical hazards

- sanitation
- contamination
- machine motion

Typical standards

- ISO 12100
- ISO 13849
- IEC 60204
- EHEDG / FDA
- UL 508A
- IEC 62443

---

# 4. The Matrix Should Link to Lifecycle

The industry matrix should connect to your **lifecycle design system**.

Example:

Food processing machine:

```
Concept
ISO 12100

Safety architecture
ISO 13849

Electrical design
IEC 60204 / NFPA 79

Software
IEC 61131

Cybersecurity
IEC 62443

Commissioning
FAT / SAT

Maintenance
Proof testing
```

That integration makes the guide practical.

---

# 5. Industry Standards That Should Be Included

You mentioned several industries. I would structure them like this.

### Machinery industries

- manufacturing
- warehouse automation
- robotics
- semiconductor equipment
- agriculture machinery
- food processing machinery

Core standards:

```
ISO 12100
ISO 13849
IEC 62061
IEC 60204
NFPA 79
UL 508A
```

---

### Process industries

- chemical
- oil and gas
- power generation
- pharmaceuticals

Core standards:

```
IEC 61508
IEC 61511
IEC 60079
IEC 62443
NEC
```

---

### Regulated industries

- medical devices
- nuclear
- aviation

Core standards differ significantly.

Examples:

Medical:

```
ISO 14971
IEC 60601
IEC 62304
```

Nuclear:

```
IEC 61513
IEEE nuclear standards
```

---

### Transportation industries

- marine
- rail
- aerospace ground systems

Examples:

Marine:

```
IEC 60092
IEC 61508
IMO standards
```

---

# 6. How This Should Appear on the Website

Your site should have a section:

### Industry Navigator

Grid of industries:

```
Food & Beverage
Semiconductor
Warehouse Automation
Energy & Power
Oil & Gas
Marine
Nuclear
Medical Devices
Agriculture
```

Clicking one shows:

- standards
- architecture
- lifecycle
- scenarios

---

# 7. Example Industry Matrix Page

This page would look like:

| Industry      | Risk Standard | Safety Standard | Electrical | Cybersecurity | Special    |
| ------------- | ------------- | --------------- | ---------- | ------------- | ---------- |
| Food          | ISO 12100     | ISO 13849       | IEC 60204  | IEC 62443     | FDA        |
| Semiconductor | ISO 12100     | ISO 13849       | IEC 60204  | IEC 62443     | SEMI S2    |
| Warehouse     | ISO 12100     | ISO 13849       | NFPA 79    | IEC 62443     | —          |
| Oil & Gas     | IEC 61508     | IEC 61511       | NEC        | IEC 62443     | IEC 60079  |
| Marine        | ISO 12100     | IEC 61508       | IEC 60092  | IEC 62443     | IMO        |
| Energy        | IEC 61508     | IEC 61508       | IEC        | IEC 62443     | grid codes |
| Medical       | ISO 14971     | IEC 60601       | IEC 60601  | IEC 62304     | FDA        |
| Agriculture   | ISO 12100     | ISO 25119       | ISO 25119  | limited       | —          |

Each cell links to detailed pages.

---

# 8. Why This Is Powerful in Interviews

This matrix lets you answer questions like:

**“What standards apply to a semiconductor tool?”**

You can explain the stack clearly.

**“What changes if the system is a chemical plant instead of a machine?”**

You show the shift from:

```
ISO 13849
→ IEC 61511
```

This demonstrates real understanding.

---

# 9. One Warning

Do not try to list **every standard in the world**.

Focus on **control systems and automation relevant standards**.

Keep it around **30–60 standards maximum**.

Otherwise the project becomes unmaintainable.

---

# My recommendation

Yes — include the industry matrix.

But organize the system as:

```
Standards Directory
Industry Matrix
Lifecycle Design Guide
Standards Graph
Scenario Explorer
Software Stack
```

That combination makes the project:

- practical
- educational
- credible
- impressive in interviews.

---

If you want, I can also show you the **40–50 most important automation and safety standards** that should be included in your matrix.

Here is the **directory tree I recommend** for the site.

It is designed to support:

- **standards directory**
- **industry matrix**
- **SIL / PL lifecycle guide**
- **scenario-based design examples**
- **software stack reference**
- **interconnectivity / crosswalks**
- **interview-ready engineering navigation**

---

# Recommended site directory tree

```text
control-system-standards-atlas/
├── README.md
├── package.json
├── tsconfig.json
├── next.config.js                         # or vite.config.ts if using Vite
├── public/
│   ├── images/
│   │   ├── standards/
│   │   ├── industries/
│   │   ├── scenarios/
│   │   └── diagrams/
│   ├── icons/
│   └── logos/
│
├── src/
│   ├── app/                              # Next.js app router style
│   │   ├── layout.tsx
│   │   ├── page.tsx                      # Home
│   │   │
│   │   ├── standards/
│   │   │   ├── page.tsx                  # Standards landing page
│   │   │   ├── machinery/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── iso-12100/
│   │   │   │   │   └── page.tsx
│   │   │   │   ├── iso-13849-1/
│   │   │   │   │   └── page.tsx
│   │   │   │   ├── iec-62061/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── iec-60204-1/
│   │   │   │       └── page.tsx
│   │   │   │
│   │   │   ├── process-safety/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── iec-61508/
│   │   │   │   │   └── page.tsx
│   │   │   │   ├── iec-61511/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── iec-60079/
│   │   │   │       └── page.tsx
│   │   │   │
│   │   │   ├── electrical/
│   │   │   │   ├── page.tsx
│   │   │   │   ├── nfpa-79/
│   │   │   │   │   └── page.tsx
│   │   │   │   ├── nec/
│   │   │   │   │   └── page.tsx
│   │   │   │   └── ul-508a/
│   │   │   │       └── page.tsx
│   │   │   │
│   │   │   ├── cybersecurity/
│   │   │   │   ├── page.tsx
│   │   │   │   └── iec-62443/
│   │   │   │       └── page.tsx
│   │   │   │
│   │   │   ├── software/
│   │   │   │   ├── page.tsx
│   │   │   │   └── iec-61131-3/
│   │   │   │       └── page.tsx
│   │   │   │
│   │   │   └── industry-specific/
│   │   │       ├── page.tsx
│   │   │       ├── semi-s2/
│   │   │       │   └── page.tsx
│   │   │       ├── medical/
│   │   │       │   └── page.tsx
│   │   │       ├── marine/
│   │   │       │   └── page.tsx
│   │   │       ├── nuclear/
│   │   │       │   └── page.tsx
│   │   │       └── agriculture/
│   │   │           └── page.tsx
│   │   │
│   │   ├── lifecycle/
│   │   │   ├── page.tsx                  # Lifecycle landing page
│   │   │   ├── concept/
│   │   │   │   └── page.tsx
│   │   │   ├── standards-selection/
│   │   │   │   └── page.tsx
│   │   │   ├── safety-concept/
│   │   │   │   └── page.tsx
│   │   │   ├── detailed-design/
│   │   │   │   └── page.tsx
│   │   │   ├── drafting-and-documentation/
│   │   │   │   └── page.tsx
│   │   │   ├── build-and-software-implementation/
│   │   │   │   └── page.tsx
│   │   │   ├── installation/
│   │   │   │   └── page.tsx
│   │   │   ├── pre-commissioning-and-calibration/
│   │   │   │   └── page.tsx
│   │   │   ├── commissioning-and-validation/
│   │   │   │   └── page.tsx
│   │   │   └── maintenance-and-lifecycle-support/
│   │   │       └── page.tsx
│   │   │
│   │   ├── industries/
│   │   │   ├── page.tsx                  # Industry landing page
│   │   │   ├── matrix/
│   │   │   │   └── page.tsx              # Industry standards matrix
│   │   │   ├── semiconductor/
│   │   │   │   └── page.tsx
│   │   │   ├── food-and-beverage/
│   │   │   │   └── page.tsx
│   │   │   ├── medical/
│   │   │   │   └── page.tsx
│   │   │   ├── warehouse-automation/
│   │   │   │   └── page.tsx
│   │   │   ├── energy-and-power/
│   │   │   │   └── page.tsx
│   │   │   ├── oil-and-gas/
│   │   │   │   └── page.tsx
│   │   │   ├── marine/
│   │   │   │   └── page.tsx
│   │   │   ├── nuclear/
│   │   │   │   └── page.tsx
│   │   │   └── agriculture/
│   │   │       └── page.tsx
│   │   │
│   │   ├── scenarios/
│   │   │   ├── page.tsx
│   │   │   ├── robotic-cell/
│   │   │   │   └── page.tsx
│   │   │   ├── conveyor-sorter/
│   │   │   │   └── page.tsx
│   │   │   ├── chemical-dosing-skid/
│   │   │   │   └── page.tsx
│   │   │   ├── hydraulic-machine/
│   │   │   │   └── page.tsx
│   │   │   ├── semiconductor-tool/
│   │   │   │   └── page.tsx
│   │   │   ├── food-processing-machine/
│   │   │   │   └── page.tsx
│   │   │   └── offshore-process-skid/
│   │   │       └── page.tsx
│   │   │
│   │   ├── software-stack/
│   │   │   ├── page.tsx
│   │   │   ├── plc-and-safety-plc/
│   │   │   │   └── page.tsx
│   │   │   ├── fieldbus-and-industrial-networks/
│   │   │   │   └── page.tsx
│   │   │   ├── opc-ua-mqtt-and-edge/
│   │   │   │   └── page.tsx
│   │   │   ├── historian-logging-and-dashboards/
│   │   │   │   └── page.tsx
│   │   │   ├── cybersecurity-architecture/
│   │   │   │   └── page.tsx
│   │   │   └── software-verification-and-version-control/
│   │   │       └── page.tsx
│   │   │
│   │   ├── crosswalks/
│   │   │   ├── page.tsx
│   │   │   ├── pl-vs-sil/
│   │   │   │   └── page.tsx
│   │   │   ├── iso-13849-vs-iec-62061/
│   │   │   │   └── page.tsx
│   │   │   ├── nfpa-79-vs-iec-60204-1/
│   │   │   │   └── page.tsx
│   │   │   ├── ul-508a-nec-nfpa-79/
│   │   │   │   └── page.tsx
│   │   │   ├── machinery-vs-process-safety/
│   │   │   │   └── page.tsx
│   │   │   └── hazardous-area-routing/
│   │   │       └── page.tsx
│   │   │
│   │   ├── interviews/
│   │   │   ├── page.tsx
│   │   │   ├── how-i-choose-standards/
│   │   │   │   └── page.tsx
│   │   │   ├── how-i-choose-sil-or-pl/
│   │   │   │   └── page.tsx
│   │   │   ├── how-i-approach-commissioning/
│   │   │   │   └── page.tsx
│   │   │   └── controls-engineer-case-studies/
│   │   │       └── page.tsx
│   │   │
│   │   └── search/
│   │       └── page.tsx
│   │
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Sidebar.tsx
│   │   │   ├── TopNav.tsx
│   │   │   ├── PageHeader.tsx
│   │   │   └── RightRail.tsx
│   │   ├── standards/
│   │   │   ├── StandardCard.tsx
│   │   │   ├── StandardNode.tsx
│   │   │   ├── RelatedStandards.tsx
│   │   │   ├── StandardsGraph.tsx
│   │   │   └── StandardsBreadcrumb.tsx
│   │   ├── lifecycle/
│   │   │   ├── LifecycleStageCard.tsx
│   │   │   ├── LifecycleFlow.tsx
│   │   │   ├── SILvsPLPanel.tsx
│   │   │   └── DeliverablesPanel.tsx
│   │   ├── industries/
│   │   │   ├── IndustryCard.tsx
│   │   │   ├── IndustryMatrix.tsx
│   │   │   └── IndustryFilters.tsx
│   │   ├── scenarios/
│   │   │   ├── ScenarioCard.tsx
│   │   │   ├── ScenarioLifecycleBar.tsx
│   │   │   └── ScenarioStandardsPanel.tsx
│   │   ├── software/
│   │   │   ├── StackLayerCard.tsx
│   │   │   └── NetworkArchitecturePanel.tsx
│   │   └── shared/
│   │       ├── Tag.tsx
│   │       ├── Badge.tsx
│   │       ├── Table.tsx
│   │       ├── Accordion.tsx
│   │       └── SearchBox.tsx
│   │
│   ├── content/
│   │   ├── standards/
│   │   │   ├── machinery/
│   │   │   │   ├── iso-12100.md
│   │   │   │   ├── iso-13849-1.md
│   │   │   │   ├── iec-62061.md
│   │   │   │   └── iec-60204-1.md
│   │   │   ├── process-safety/
│   │   │   │   ├── iec-61508.md
│   │   │   │   ├── iec-61511.md
│   │   │   │   └── iec-60079.md
│   │   │   ├── electrical/
│   │   │   │   ├── nfpa-79.md
│   │   │   │   ├── nec.md
│   │   │   │   └── ul-508a.md
│   │   │   ├── cybersecurity/
│   │   │   │   └── iec-62443.md
│   │   │   ├── software/
│   │   │   │   └── iec-61131-3.md
│   │   │   └── industry-specific/
│   │   │       ├── semi-s2.md
│   │   │       ├── medical.md
│   │   │       ├── marine.md
│   │   │       ├── nuclear.md
│   │   │       └── agriculture.md
│   │   │
│   │   ├── lifecycle/
│   │   │   ├── concept.md
│   │   │   ├── standards-selection.md
│   │   │   ├── safety-concept.md
│   │   │   ├── detailed-design.md
│   │   │   ├── drafting-and-documentation.md
│   │   │   ├── build-and-software-implementation.md
│   │   │   ├── installation.md
│   │   │   ├── pre-commissioning-and-calibration.md
│   │   │   ├── commissioning-and-validation.md
│   │   │   └── maintenance-and-lifecycle-support.md
│   │   │
│   │   ├── industries/
│   │   │   ├── semiconductor.md
│   │   │   ├── food-and-beverage.md
│   │   │   ├── medical.md
│   │   │   ├── warehouse-automation.md
│   │   │   ├── energy-and-power.md
│   │   │   ├── oil-and-gas.md
│   │   │   ├── marine.md
│   │   │   ├── nuclear.md
│   │   │   └── agriculture.md
│   │   │
│   │   ├── scenarios/
│   │   │   ├── robotic-cell.md
│   │   │   ├── conveyor-sorter.md
│   │   │   ├── chemical-dosing-skid.md
│   │   │   ├── hydraulic-machine.md
│   │   │   ├── semiconductor-tool.md
│   │   │   ├── food-processing-machine.md
│   │   │   └── offshore-process-skid.md
│   │   │
│   │   ├── software-stack/
│   │   │   ├── plc-and-safety-plc.md
│   │   │   ├── fieldbus-and-industrial-networks.md
│   │   │   ├── opc-ua-mqtt-and-edge.md
│   │   │   ├── historian-logging-and-dashboards.md
│   │   │   ├── cybersecurity-architecture.md
│   │   │   └── software-verification-and-version-control.md
│   │   │
│   │   ├── crosswalks/
│   │   │   ├── pl-vs-sil.md
│   │   │   ├── iso-13849-vs-iec-62061.md
│   │   │   ├── nfpa-79-vs-iec-60204-1.md
│   │   │   ├── ul-508a-nec-nfpa-79.md
│   │   │   ├── machinery-vs-process-safety.md
│   │   │   └── hazardous-area-routing.md
│   │   │
│   │   └── interviews/
│   │       ├── how-i-choose-standards.md
│   │       ├── how-i-choose-sil-or-pl.md
│   │       ├── how-i-approach-commissioning.md
│   │       └── controls-engineer-case-studies.md
│   │
│   ├── data/
│   │   ├── standards/
│   │   │   ├── standards-index.json
│   │   │   ├── standards-graph.json
│   │   │   ├── standards-tags.json
│   │   │   └── standards-relationships.json
│   │   ├── industries/
│   │   │   ├── industry-matrix.json
│   │   │   └── industry-tags.json
│   │   ├── lifecycle/
│   │   │   └── lifecycle-map.json
│   │   ├── scenarios/
│   │   │   └── scenarios-index.json
│   │   └── software-stack/
│   │       └── software-stack-map.json
│   │
│   ├── lib/
│   │   ├── content-loader.ts
│   │   ├── standards-graph.ts
│   │   ├── standards-router.ts
│   │   ├── industry-matrix.ts
│   │   ├── lifecycle-mapper.ts
│   │   ├── scenario-mapper.ts
│   │   └── search.ts
│   │
│   ├── styles/
│   │   ├── globals.css
│   │   └── theme.css
│   │
│   └── types/
│       ├── standard.ts
│       ├── industry.ts
│       ├── lifecycle.ts
│       ├── scenario.ts
│       └── software-stack.ts
│
├── docs/                                 # source/reference docs not directly rendered
│   ├── source-library/
│   │   ├── reference_models/
│   │   ├── us/
│   │   ├── international/
│   │   ├── crosswalks/
│   │   ├── routing/
│   │   ├── library_admin/
│   │   └── scenario/
│   │
│   ├── import-notes/
│   ├── content-governance/
│   └── citation-policy/
│
├── scripts/
│   ├── build-standards-index.ts
│   ├── build-industry-matrix.ts
│   ├── build-graph.ts
│   ├── validate-content.ts
│   └── sync-md-to-json.ts
│
└── tests/
    ├── unit/
    │   ├── standards-router.test.ts
    │   ├── industry-matrix.test.ts
    │   └── lifecycle-mapper.test.ts
    └── e2e/
        ├── homepage.spec.ts
        ├── standards.spec.ts
        ├── lifecycle.spec.ts
        └── industries.spec.ts
```

---

# Why this structure is right

## 1. It separates **rendered content** from **source library**

You need both:

- `src/content/` = website-ready content
- `docs/source-library/` = raw/reference source repository

That prevents the frontend from becoming messy.

## 2. It supports your **main user journeys**

The top-level sections are exactly what you said you want:

- `standards`
- `lifecycle`
- `industries`
- `scenarios`
- `software-stack`
- `crosswalks`
- `interviews`

## 3. It is good for both **learning and interview use**

The `interviews/` section is not fluff. It is smart.
It lets you convert your research into:

- how you choose standards
- how you decide PL vs SIL
- how you explain commissioning and lifecycle support

That makes the project portfolio-ready.

---

# Simpler version if you want to start lean

If you want an MVP first, use this:

```text
control-system-standards-atlas/
├── src/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── standards/
│   │   ├── lifecycle/
│   │   ├── industries/
│   │   ├── scenarios/
│   │   ├── software-stack/
│   │   └── crosswalks/
│   ├── components/
│   ├── content/
│   │   ├── standards/
│   │   ├── lifecycle/
│   │   ├── industries/
│   │   ├── scenarios/
│   │   ├── software-stack/
│   │   └── crosswalks/
│   ├── data/
│   │   ├── standards-graph.json
│   │   └── industry-matrix.json
│   └── lib/
│
├── docs/
│   └── source-library/
│
└── scripts/
```

That is enough to start building without overengineering.

---

# My blunt recommendation

Start with these **6 sections only**:

1. `standards`
2. `lifecycle`
3. `industries`
4. `scenarios`
5. `software-stack`
6. `crosswalks`

Add `interviews` later.

That will keep the project under control.

If you want, I can turn this into a **real folder structure matched to Next.js + MDX** with sample files for the first 10 pages.
