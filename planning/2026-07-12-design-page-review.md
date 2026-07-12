## Overall assessment

The page is clean and technically credible, but it currently functions as a **small link directory**, not a complete **control-system design workflow**. The title says “Engineering Workflow,” while the URL and navigation position suggest “Design.” The page needs to explain how an engineer moves from requirements to a released, commissioned design. ([Kyaw Min Thu][1])

## Highest-priority improvements

### 1. Clarify what this page is

The URL is `/design/`, the sidebar calls it **Design**, the breadcrumb says **Engineering Workflow**, and the page heading also says **Engineering Workflow**. ([Kyaw Min Thu][1])

Choose one purpose:

- **Control System Design**
- **Engineering Design Workflow**
- **Control System Design & Architecture**

My recommendation:

> **Control System Design & Engineering Workflow**

Use that consistently in:

- Page title
- H1
- Breadcrumb
- Navigation label
- Browser metadata

The opening should also say what users will accomplish:

> Design an industrial control system from requirements and architecture through electrical drawings, software design, validation, and commissioning.

---

### 2. Add an actual end-to-end workflow

The current page jumps directly into categories such as Design & Architecture, Select & Size, Commission & Verify, and Troubleshoot. It does not show the full sequence or the output of each step. ([Kyaw Min Thu][1])

Add a workflow like this:

| Stage | Engineering activity            | Main deliverables                                    |
| ----- | ------------------------------- | ---------------------------------------------------- |
| 1     | Define process and requirements | URS, process description, operating modes            |
| 2     | Define system boundaries        | Scope diagram, interface list                        |
| 3     | Identify standards              | Standards register, compliance strategy              |
| 4     | Perform risk assessment         | Hazard analysis, PLr/SIL requirements                |
| 5     | Select architecture             | PLC, safety PLC, SCADA, networks, remote I/O         |
| 6     | Develop control philosophy      | Sequences, permissives, interlocks, alarm philosophy |
| 7     | Develop instrument design       | Instrument index, datasheets, ranges, accuracy       |
| 8     | Develop I/O design              | I/O list, channel allocation, signal types           |
| 9     | Design electrical system        | Schematics, power distribution, SCCR, protection     |
| 10    | Design networks                 | Topology, addressing, VLANs, redundancy              |
| 11    | Design software                 | Program structure, state machines, naming standards  |
| 12    | Review and verify               | Design review, calculations, traceability            |
| 13    | Build and test                  | Panel QA, simulation, FAT                            |
| 14    | Install and commission          | Loop checks, SAT, tuning, validation                 |
| 15    | Handover and maintain           | As-builts, backups, training, MOC                    |

This would make the page useful as an engineering roadmap rather than merely a collection of links.

---

### 3. Separate general controls engineering from functional safety

Your lifecycle page is heavily focused on safety engineering. It describes itself as a safety lifecycle and states that it applies where safeguarding or safety functions exist. ([Kyaw Min Thu][2])

That is useful, but the Design page currently links to it as though it were the entire machine lifecycle. ([Kyaw Min Thu][1])

You should show two related tracks:

```text
General Controls Engineering Lifecycle
    Requirements
    Process design
    Control philosophy
    Architecture
    Electrical design
    Software design
    FAT
    Commissioning
    Maintenance

Functional Safety Lifecycle
    Hazard identification
    Risk assessment
    PLr / SIL assignment
    Safety requirements specification
    Safety architecture
    Validation
    Proof testing
    Management of change
```

The functional-safety process should be shown as an overlay that intersects the general engineering lifecycle—not as a replacement for it.

---

### 4. Fix the lifecycle-stage inconsistency

The Design page describes the linked lifecycle as:

> “11-stage structured progression from concept through maintenance.” ([Kyaw Min Thu][1])

But the lifecycle page says:

> “13 stages from concept through decommissioning.” ([Kyaw Min Thu][2])

The lifecycle page also includes intermediate stages such as Safety Requirements Specification and Safety Software/Logic, making the numbering more complicated. ([Kyaw Min Thu][2])

This must be corrected. Use one numbering system throughout the website.

A cleaner structure would be:

1. Concept
2. Standards selection
3. Risk assessment
4. Safety requirements specification
5. Safety architecture
6. Detailed design
7. Documentation
8. Build
9. Installation
10. Pre-commissioning
11. Commissioning
12. Operation and maintenance
13. Management of change
14. Decommissioning

Alternatively, stop emphasizing the number and simply say:

> Structured lifecycle from concept through decommissioning.

That prevents the summary from becoming incorrect whenever stages are added.

---

### 5. Add the missing design disciplines

The page is currently strongest in electrical design, motor selection, safety, and commissioning. ([Kyaw Min Thu][1])

Major control-system design topics are missing from the main page:

#### Requirements and process definition

Add:

- User Requirements Specification
- Functional Requirements Specification
- Process Description
- Control Philosophy
- Operating Modes
- Cause-and-Effect Matrix
- Sequence of Operations

#### Instrumentation design

Add:

- Instrument selection
- Measurement range
- Accuracy and uncertainty
- Response time
- Sensor technology comparison
- Instrument index
- Instrument datasheets
- Loop diagrams
- Calibration requirements

#### PLC and software design

Add:

- PLC selection
- Software architecture
- IEC 61131-3 languages
- State machines
- Equipment modules
- Function blocks
- Naming conventions
- Alarm handling
- Interlock design
- Recipe and batch controls
- Simulation and emulation
- Version control and backups

#### HMI and SCADA design

Add:

- HMI philosophy
- High-performance HMI
- Screen hierarchy
- Alarm philosophy
- Historian architecture
- User access and permissions
- Audit trails
- Redundancy
- Data retention

#### Network design

Add:

- Network topology
- Device count and loading
- IP addressing
- VLAN segmentation
- Managed-switch selection
- Redundancy
- Time synchronization
- Remote access
- Firewall placement
- Network acceptance testing

#### Cybersecurity by design

Add:

- Zones and conduits
- Asset inventory
- Secure remote access
- Least privilege
- Backup and recovery
- Patch strategy
- Logging and monitoring
- Default credential removal
- Configuration baselines

---

## Page organization I recommend

### Control System Design & Engineering Workflow

#### Start Here

A short decision section:

- Designing a new machine
- Modifying an existing machine
- Designing a process-control system
- Designing a safety-related system
- Troubleshooting an existing installation

#### 1. Requirements and Scope

Cards for:

- User Requirements Specification
- Process Description
- System Boundaries
- Control Philosophy
- Applicable Standards

#### 2. Architecture

Cards for:

- Machine Architecture
- PLC/PAC Selection
- Safety Architecture
- SCADA/HMI Architecture
- Network Architecture
- Power Architecture
- Software Architecture

#### 3. Detailed Design

Cards for:

- I/O List
- Instrument Index
- Electrical Schematics
- Panel Design
- Grounding and Bonding
- Motor and Drive Selection
- Control Loops
- Alarms and Interlocks
- Network Addressing

#### 4. Engineering Calculations

Cards for:

- Load calculation
- Wire sizing
- Short-circuit and SCCR
- Power supply sizing
- Heat-load calculation
- Network capacity
- Motor sizing
- Control-valve sizing
- Loop accuracy
- Safety response time

#### 5. Design Reviews

Cards for:

- 30% conceptual review
- 60% design review
- 90% design review
- Safety review
- Cybersecurity review
- Constructability review
- Commissioning readiness review

#### 6. Build, Test and Commission

Cards for:

- Panel inspection
- Software simulation
- FAT
- Installation verification
- Loop checks
- VFD commissioning
- Servo commissioning
- SAT
- Performance testing

#### 7. Handover and Lifecycle Support

Cards for:

- As-built documentation
- Software backups
- Training
- Spare-parts strategy
- Preventive maintenance
- Proof testing
- Management of change
- Decommissioning

---

## Add deliverable templates

Your page already links to commissioning templates, which include panel energization, drive startup, and circuit-verification material. ([Kyaw Min Thu][1])

Expand this into a complete deliverables library:

| Template                          | Format          |
| --------------------------------- | --------------- |
| User Requirements Specification   | DOCX / Markdown |
| Control Philosophy                | DOCX / Markdown |
| System Architecture Diagram       | Draw.io         |
| I/O List                          | XLSX / CSV      |
| Instrument Index                  | XLSX            |
| Motor List                        | XLSX            |
| Network Device List               | XLSX            |
| IP Address Register               | XLSX            |
| Alarm and Interlock Matrix        | XLSX            |
| Cause-and-Effect Matrix           | XLSX            |
| PLC Software Design Specification | DOCX            |
| FAT Procedure                     | DOCX / XLSX     |
| SAT Procedure                     | DOCX / XLSX     |
| Loop Check Sheet                  | XLSX            |
| Design Review Checklist           | XLSX            |
| Management of Change Form         | DOCX            |

Each design-stage card should show:

```text
Purpose
Inputs required
Engineering decisions
Deliverables
Applicable standards
Review gate
Common mistakes
Related tools
```

---

## Navigation and consistency issues

### Duplicate entries

The Design navigation shows **Motor Selection** twice: once as the section and once under Design Workflows. ([Kyaw Min Thu][1])

This may be technically correct because one is a conceptual section and the other is a workflow, but the labels should distinguish them:

- **Motor Selection Fundamentals**
- **Motor Selection Workflow**
- **Motor Selection Matrix**

The same issue appears elsewhere in the sidebar, including parent headings and child pages that use nearly identical wording, such as Ethernet Fundamentals and EtherNet/IP groupings. ([Kyaw Min Thu][1])

Use clear prefixes:

- Overview
- Fundamentals
- Design Guide
- Configuration Guide
- Commissioning Guide
- Troubleshooting Guide
- Reference Matrix

---

### Branding inconsistency

The current page uses “CS Field Guide,” while the lifecycle page is labeled “CS Standards Atlas” or “Control System Standards Atlas.” ([Kyaw Min Thu][1])

Choose one site identity. Based on the expanded content, I recommend:

> **Control Systems Engineering Field Guide**

“Standards Atlas” is too narrow now that the site includes design, communications, commissioning, manufacturers, tools, and troubleshooting.

---

## Improve each card

Current cards have a title and one-sentence description. ([Kyaw Min Thu][1])

Add metadata:

```text
Electrical Design Review

Review power distribution, conductor sizing, overcurrent
protection, SCCR, grounding, I/O wiring, and panel thermal design.

Level: Intermediate
Output: Completed design review checklist
Applies to: Machine panels, process skids, retrofit projects
Standards: NEC, NFPA 79, UL 508A, IEC 60204-1

[Open workflow] [Download checklist]
```

This helps users understand what they will receive before opening a page.

---

## Add one complete worked example

The best improvement would be a project that flows through the entire Design section.

### Example project: Pump and VFD control skid

Include:

1. Process requirements
2. P&ID
3. Operating modes
4. Motor and pump data
5. VFD selection
6. PLC and I/O selection
7. Instrument selection
8. Network architecture
9. Power architecture
10. I/O list
11. Cause-and-effect matrix
12. Electrical schematics
13. PLC software structure
14. HMI screens
15. Alarm list
16. FAT procedure
17. Commissioning procedure
18. Troubleshooting case
19. Final handover package

Then provide variants:

- Simple motor starter
- VFD-controlled pump
- Servo positioning axis
- Conveyor system
- Temperature-control skid
- Semiconductor process tool
- Building automation air handler

Your Scenario Explorer currently contains nine application scenarios, but the Design page only provides a general link to them. ([Kyaw Min Thu][1]) Tie each scenario directly to the relevant engineering workflow and deliverables.

---

## Recommended replacement introduction

# Control System Design & Engineering Workflow

Design an industrial control system from initial requirements through architecture, detailed engineering, verification, commissioning, and lifecycle support.

This section organizes the major engineering decisions, calculations, documents, and review gates required to produce a reliable and maintainable control system. It covers machine automation, process control, electrical panels, PLC and SCADA systems, industrial networks, instrumentation, motion control, and functional safety.

Use the workflow sequentially for a new project, or enter at the appropriate stage when reviewing, modifying, commissioning, or troubleshooting an existing system.

## Engineering Workflow

1. Define requirements, operating modes, and system boundaries.
2. Identify applicable standards and regulatory requirements.
3. Perform risk assessment and define required safety functions.
4. Select the control, electrical, safety, network, and software architecture.
5. Develop the control philosophy, sequences, permissives, interlocks, and alarm strategy.
6. Select and size controllers, I/O, instruments, motors, drives, power supplies, and network equipment.
7. Produce electrical schematics, I/O lists, instrument indexes, network drawings, software specifications, and test plans.
8. Review the design for safety, compliance, maintainability, cybersecurity, and commissioning readiness.
9. Build, inspect, simulate, and execute the factory acceptance test.
10. Install, commission, validate, document, and hand over the completed system.
11. Maintain configuration control through backups, proof testing, revision management, and management of change.

The most important next step is to transform this page from **nine navigation cards** into a **complete design map with stages, deliverables, review gates, and downloadable examples**.

[1]: https://kyawminthu20.github.io/Control-System-Tools/design/ "Engineering Workflow — Control Systems Engineering Field Guide"
[2]: https://kyawminthu20.github.io/Control-System-Tools/lifecycle/ "Engineering Lifecycle — Control System Standards Atlas"

====================

This should be a dedicated section under **Design → Electrical Design → Wire & Cable Identification**.

The key rule: **wire color is determined primarily by the governing standard, jurisdiction, circuit function, and facility specification—not simply by the industry.** A semiconductor fab, water plant, refinery, and packaging machine may all use different internal conventions even when they operate in the same country.

NFPA 79 applies to industrial machinery, while the NEC governs electrical installations in the United States. IEC 60204-1 applies to electrical equipment of machinery internationally, and IEC 60445 defines general conductor-identification principles. ([NFPA][1])

## Recommended website content

# Industrial Wire Color Coding Guide

Wire colors help technicians identify circuit function, voltage type, grounded conductors, protective conductors, and circuits that remain energized after the main disconnect is opened.

Color alone must never be treated as proof that a conductor is safe or de-energized. Always verify the drawings, conductor labels, terminal numbers, and voltage using an approved test instrument.

## 1. Standards hierarchy

Before assigning wire colors, determine which requirements apply:

1. Local electrical code and authority having jurisdiction
2. Customer or facility engineering standard
3. Equipment standard
4. Project wire-color specification
5. Existing-site convention
6. Manufacturer recommendations

Common references include:

- NFPA 70, National Electrical Code
- NFPA 79, Electrical Standard for Industrial Machinery
- UL 508A, Industrial Control Panels
- IEC 60204-1, Electrical Equipment of Machines
- IEC 60445, Conductor and Terminal Identification
- CSA C22.1 and applicable Canadian equipment standards
- ISA documentation and instrumentation practices
- Facility-specific electrical design standards

## 2. United States industrial machinery convention

The following is a practical NFPA 79-style convention commonly used inside industrial machinery control panels.

| Circuit function                                               |                                  Recommended color | Typical examples                        |
| -------------------------------------------------------------- | -------------------------------------------------: | --------------------------------------- |
| Protective grounding conductor                                 |                              Green or green/yellow | Panel ground, motor frame ground        |
| Ungrounded AC or DC power                                      |                                              Black | Incoming power, motor feeder, VFD power |
| Ungrounded AC control                                          |                                                Red | 120 VAC relay and solenoid control      |
| Ungrounded DC control                                          |                                               Blue | 24 VDC PLC inputs and outputs           |
| Grounded AC conductor                                          |                                              White | 120 VAC neutral                         |
| Grounded DC conductor                                          |                             White with blue stripe | 0 VDC grounded common                   |
| Externally supplied or interlocked circuit remaining energized |                                             Orange | UPS source, foreign panel voltage       |
| Grounded externally supplied AC conductor                      |                           White with orange stripe | Neutral from external source            |
| Grounded externally supplied DC conductor                      | White with orange stripe or identified per drawing | External DC return                      |
| Equipment bonding jumper                                       |                              Green or green/yellow | Door bond, DIN rail bond                |

### Example machinery panel

```text
480 VAC incoming power
L1 ───────── BLACK ───── Main Disconnect
L2 ───────── BLACK ───── Main Disconnect
L3 ───────── BLACK ───── Main Disconnect
PE ───── GREEN/YELLOW ── Ground Bar

120 VAC control
L ────────── RED ─────── Relay / Contactor Coil
N ───────── WHITE ────── Neutral Terminal

24 VDC control
+24 VDC ───── BLUE ───── PLC Inputs / Outputs
0 VDC ── WHITE/BLUE ──── DC Common

External UPS circuit
UPS + ───── ORANGE ───── PLC / Network Equipment
UPS − ─ WHITE/ORANGE ─── UPS Return
```

## 3. IEC machinery convention

IEC systems reserve green/yellow for the protective conductor and light blue for the neutral conductor. IEC installations commonly identify three-phase conductors as brown, black, and grey.

| Circuit function            |                                              Common IEC color |
| --------------------------- | ------------------------------------------------------------: |
| Protective earth, PE        |                                                  Green/yellow |
| Neutral, N                  |                                                    Light blue |
| Phase L1                    |                                                         Brown |
| Phase L2                    |                                                         Black |
| Phase L3                    |                                                          Grey |
| AC control conductor        |                          Red, black, brown or project-defined |
| DC positive control         |                                  Dark blue or project-defined |
| DC negative/common          | Light blue only where permitted and not confused with neutral |
| Circuit remaining energized |                                                        Orange |
| Functional earth            |            Pink or project-defined, with clear identification |

### Example IEC machine supply

```text
L1 ───── BROWN ───── Main Disconnect
L2 ───── BLACK ───── Main Disconnect
L3 ───── GREY ────── Main Disconnect
N ── LIGHT BLUE ──── Neutral Bar
PE ─ GREEN/YELLOW ── Protective-Earth Bar
```

## 4. Building and facility power distribution

Facility wiring should follow the adopted electrical code and site standard.

### Common United States facility convention

| System                   | L1    | L2     | L3     | Neutral | Ground        |
| ------------------------ | ----- | ------ | ------ | ------- | ------------- |
| 120/208 VAC              | Black | Red    | Blue   | White   | Green or bare |
| 277/480 VAC              | Brown | Orange | Yellow | Grey    | Green or bare |
| 120/240 VAC single phase | Black | Red    | —      | White   | Green or bare |

These phase-color combinations are widely used facility conventions, but they are not universally mandatory for every ungrounded phase conductor. Verify the facility specification.

Do not use orange for a normal 480 VAC phase inside a machine panel when orange is reserved there for conductors that remain energized after the machine disconnect is opened.

## 5. PLC and discrete control wiring

A consistent PLC convention reduces troubleshooting errors.

| Signal                    |        Recommended panel color |
| ------------------------- | -----------------------------: |
| +24 VDC distribution      |                           Blue |
| 0 VDC common              |         White with blue stripe |
| PLC digital input signal  |                           Blue |
| PLC digital output signal |                           Blue |
| 120 VAC digital input     |                            Red |
| 120 VAC digital output    |                            Red |
| Safety input channel      |         Blue with wire markers |
| Safety output channel     |         Blue with wire markers |
| External powered input    |                         Orange |
| Shield drain              | Bare, clear or project-defined |
| Protective earth          |                   Green/yellow |

Safety circuits should not rely on wire color alone. Identify each safety channel using durable markers such as:

```text
E-STOP-01-CH-A
E-STOP-01-CH-B
GATE-02-CH-A
GATE-02-CH-B
STO-DRIVE-01-A
STO-DRIVE-01-B
```

## 6. Analog instrumentation wiring

Instrumentation wiring is usually identified more reliably by cable number, pair number, polarity, and terminal designation than by conductor color.

### 4–20 mA two-wire transmitter

```text
+24 VDC
  │
  │  RED conductor
  ▼
PT-101 (+)
PT-101 (−)
  │
  │  BLACK conductor
  ▼
PLC AI+
PLC AI−
```

Recommended convention:

| Function                              |                            Typical color |
| ------------------------------------- | ---------------------------------------: |
| Transmitter positive                  |                                      Red |
| Transmitter negative                  |                                    Black |
| Analog voltage positive               |                                      Red |
| Analog common                         |                                    Black |
| Cable shield/drain                    |                            Bare or clear |
| Intrinsically safe field cable jacket |                               Light blue |
| Thermocouple conductors               | Use thermocouple extension-wire standard |
| RTD conductors                        |          Manufacturer or project-defined |

Do not assign ordinary wire colors to thermocouple extension cable. Thermocouple colors depend on thermocouple type and regional standard.

## 7. Intrinsically safe systems

Light blue cable jackets, terminals, wire duct, or identification labels are commonly used to identify intrinsically safe circuits.

Recommended visual treatment:

```text
NON-IS AREA                    IS AREA
Grey wire duct                 Light-blue wire duct
Standard terminals             Light-blue terminals
General field cable            Light-blue IS cable jacket
```

Keep intrinsically safe and non-intrinsically-safe circuits separated according to the applicable hazardous-location design standard.

Do not use light blue indiscriminately where it may be confused with an IEC neutral conductor.

## 8. VFD and motor systems

### VFD input and output

| Circuit                     |                     Recommended color |
| --------------------------- | ------------------------------------: |
| VFD input L1/L2/L3          |                                 Black |
| VFD output U/V/W            |         Black with U, V and W markers |
| DC bus positive             |                Red or project-defined |
| DC bus negative             |              Black or project-defined |
| Braking resistor conductors |            Black with BR+/BR− markers |
| Motor protective earth      |                          Green/yellow |
| Encoder power               |                                   Red |
| Encoder common              |                                 Black |
| Encoder signals             | Individually identified twisted pairs |
| Motor temperature sensor    |     Project-defined pair with markers |

### Drawing example

```text
MAIN DISCONNECT                VFD                    MOTOR

L1 ── BLACK ──────────────── R/L1
L2 ── BLACK ──────────────── S/L2
L3 ── BLACK ──────────────── T/L3

                            U/T1 ── BLACK [U] ───── U1
                            V/T2 ── BLACK [V] ───── V1
                            W/T3 ── BLACK [W] ───── W1

PE ─ GREEN/YELLOW ───────── PE ─ GREEN/YELLOW ─── MOTOR FRAME
```

VFD output conductors should be identified with permanent U, V, and W labels because all three may otherwise be the same color.

## 9. Servo and motion-control systems

Servo systems typically use manufacturer-supplied cables. Maintain the manufacturer’s pinout and cable identification.

| Servo connection         | Preferred identification           |
| ------------------------ | ---------------------------------- |
| Motor phases             | U, V, W labels                     |
| Motor protective earth   | Green/yellow                       |
| Brake positive           | BR+                                |
| Brake negative           | BR−                                |
| Encoder power            | Encoder cable pin designation      |
| Encoder data             | Manufacturer-defined twisted pairs |
| STO channel 1            | STO1+ and STO1−                    |
| STO channel 2            | STO2+ and STO2−                    |
| Absolute encoder battery | BAT+ and BAT−                      |

Do not substitute conductor colors for connector pin numbers.

## 10. Building automation and HVAC controls

Building automation systems frequently use low-voltage multiconductor cable. Cable and terminal labeling is more important than individual conductor color.

### Suggested HVAC convention

| Function             |                      Suggested color |
| -------------------- | -----------------------------------: |
| 24 VAC hot           |                                  Red |
| 24 VAC common        |                        Black or blue |
| Ground               |                                Green |
| Analog input signal  |                                White |
| Analog output signal |                               Yellow |
| Digital input        |                                 Blue |
| Digital output       |                               Orange |
| RS-485 A / Data +    |                           White/blue |
| RS-485 B / Data −    |                           Blue/white |
| Cable shield         |                           Bare drain |
| Fire alarm interlock | Red cable jacket or facility-defined |

Thermostat wiring often follows conventions such as R, C, Y, G, W and O/B, but the terminal letter—not the conductor color—is authoritative.

## 11. Water and wastewater systems

A practical water-treatment panel standard may use:

| Function                           |              Suggested color |
| ---------------------------------- | ---------------------------: |
| 480 VAC motor power                |                        Black |
| 120 VAC control                    |                          Red |
| 24 VDC controls                    |                         Blue |
| 0 VDC                              |                   White/blue |
| Analog instrument positive         |                          Red |
| Analog instrument negative         |                        Black |
| Intrinsically safe instrumentation |    Light-blue identification |
| External generator or UPS power    |                       Orange |
| Ground                             |                 Green/yellow |
| Communication cable                | Manufacturer-specific jacket |

Typical equipment:

- Pumps
- Blowers
- Chemical dosing systems
- Level transmitters
- Flow transmitters
- Valve actuators
- Turbidity and chlorine analyzers

Because water plants frequently contain older equipment, drawings should document both the new convention and any legacy wire colors.

## 12. Oil, gas, chemical and refinery systems

Process plants place greater emphasis on cable classification, intrinsically safe identification, shielding, segregation and hazardous-area requirements.

| System                    | Identification method                    |
| ------------------------- | ---------------------------------------- |
| Medium-voltage power      | Cable tags and phase markers             |
| Low-voltage power         | Site phase-color standard                |
| Instrument 4–20 mA        | Pair number and polarity                 |
| Intrinsically safe signal | Light-blue identification                |
| Emergency shutdown        | Dedicated cable and terminal labels      |
| Fire and gas system       | Facility-defined red or dedicated jacket |
| Thermocouple              | Thermocouple-type color code             |
| RTD                       | Cable-core and terminal designation      |
| Communication             | Protocol and network cable label         |
| Grounding and bonding     | Green/yellow or bare conductor           |

Recommended cable labels:

```text
PT-201 / JB-04 / PAIR-07
ESD-101A / CH-A
ESD-101A / CH-B
F&G-DET-032
IS-AI-221
```

## 13. Semiconductor manufacturing facilities

Semiconductor facilities combine facility power, process tools, gas systems, life-safety systems and building automation.

Recommended system separation:

| System                            | Visual identification                    |
| --------------------------------- | ---------------------------------------- |
| Facility power                    | Facility phase-color standard            |
| Tool power                        | Tool OEM standard                        |
| 24 VDC tool control               | Blue                                     |
| Gas Life Safety                   | Dedicated cable and terminal labels      |
| Fire Life Safety                  | Red cable jacket or fire-system standard |
| Toxic gas monitoring              | Dedicated system labels                  |
| Building Management System        | BAS cable convention                     |
| Facility Monitoring System        | FMS cable convention                     |
| Emergency power or UPS            | Orange where continuously energized      |
| Intrinsically safe process signal | Light-blue identification                |
| Network fiber                     | Jacket color plus end labels             |

Do not assume all red cables belong to fire alarm systems. Confirm the site cable schedule and system drawings.

## 14. Fire alarm and life-safety systems

Fire alarm cable often uses red jackets, but this is subject to the manufacturer, listing, local code and facility specification.

Use conductor and terminal labels such as:

```text
SLC-01 IN+
SLC-01 IN−
SLC-01 OUT+
SLC-01 OUT−
NAC-02+
NAC-02−
FACP-01 AC POWER
FACP-01 BATTERY
```

Life-safety circuits must remain distinguishable from standard PLC control wiring.

## 15. Industrial communication wiring

Network cable colors are generally conventions rather than electrical-code requirements.

| Network or service          |               Suggested jacket color |
| --------------------------- | -----------------------------------: |
| EtherNet/IP controls        |                                 Blue |
| PROFINET                    |                                Green |
| EtherCAT                    |        Green or manufacturer-defined |
| Modbus TCP                  |                               Purple |
| SCADA network               |                                 Blue |
| Safety network              |                               Yellow |
| Enterprise network          |                                 Grey |
| Device commissioning port   |                                White |
| Fiber backbone              | Aqua, yellow or manufacturer-defined |
| Out-of-band management      |                               Purple |
| Security camera network     |                                Black |
| Building automation network |                                White |

Do not rely on network cable color to identify protocol. Every cable should have a source, destination, network and port label.

Example:

```text
ENET-PLC01-SW01-P05
PROFINET-RIO03-SW02-P12
FIBER-SW01-SW04-A
BMS-MSTP-AHU12
```

## 16. Marine and offshore systems

Marine installations should follow vessel classification requirements, flag-state regulations and applicable IEC marine standards.

Common requirements include:

- Numbered conductors
- Flame-retardant and low-smoke cable
- Circuit-specific cable tags
- Protective conductor identification
- Separation between power, control, communication and safety systems
- Marine-approved glands and terminations

Wire numbers and cable schedules are often more important than individual core color.

## 17. Railway and transportation systems

Transportation systems typically use project-specific cable standards because equipment may include:

- Traction power
- Signaling
- Train control
- Communications
- Fire and life safety
- Station controls
- Wayside equipment

Use cable tags, terminal designations and system prefixes. Do not publish a universal railway color table unless it is tied to a specific authority or standard.

## 18. Automotive machinery and vehicle wiring

Vehicle wiring and automotive manufacturing equipment are different systems.

For industrial machinery used to manufacture vehicles, follow the applicable machine-panel standard.

For vehicle harnesses:

- Use OEM wiring diagrams
- Use circuit numbers and connector pin numbers
- Preserve manufacturer stripe and tracer colors
- Do not assume red is always battery positive
- Do not assume black is always chassis ground

## 19. Legacy systems

Existing installations may use older conventions.

Examples include:

- Red, yellow and blue for three-phase power
- Blue used as a phase conductor
- Black used as DC common
- Green used as an active conductor in older equipment
- White used for non-neutral conductors
- Unmarked external power circuits

Before modifying a legacy panel:

1. Trace the conductor.
2. Measure the voltage.
3. Compare against the schematic.
4. Apply permanent wire markers.
5. Update the drawing.
6. Record the original and revised color convention.
7. Add warning labels when the old color cannot be replaced.

## 20. Recommended project wire-color schedule

Every project should include a wire-color schedule on the electrical drawing.

| Wire type             |          Color | Identification example |
| --------------------- | -------------: | ---------------------- |
| Three-phase power     |          Black | 1L1, 1L2, 1L3          |
| Motor conductors      |          Black | M101-U, M101-V, M101-W |
| 120 VAC control       |            Red | 120C-001               |
| 24 VDC positive       |           Blue | 24P-001                |
| 0 VDC common          |     White/blue | 24N-001                |
| Neutral               |          White | N-001                  |
| Protective earth      |   Green/yellow | PE-001                 |
| External live circuit |         Orange | EXT-120-001            |
| Analog positive       |            Red | PT101+                 |
| Analog negative       |          Black | PT101−                 |
| Safety input          |           Blue | EST101-A               |
| Communication         | Cable-specific | ENET-PLC01             |
| Shield drain          |           Bare | SH-PT101               |

## 21. Wire-labeling rules

Use color together with:

- Wire number
- Source terminal
- Destination terminal
- Device tag
- Signal name
- Voltage class
- Cable number
- Pair number
- Safety-channel designation

### Example terminal drawing

```text
TB1

01  +24 VDC       BLUE          24P-001
02  0 VDC         WHITE/BLUE    24N-001
03  PT-101 +      RED           PT101+
04  PT-101 −      BLACK         PT101−
05  P-101 RUN     BLUE          P101-RUN
06  P-101 FAULT   BLUE          P101-FLT
07  EXT PERMISSIVE ORANGE       EXT-PERM-01
08  PE            GREEN/YELLOW  PE-001
```

## 22. Minimum drawing notes

Place these notes on applicable electrical drawings:

1. Wire colors shall comply with the project wire-color schedule.
2. Protective conductors shall be green or green/yellow.
3. Grounded circuit conductors shall be identified according to the governing code.
4. Orange conductors identify circuits that may remain energized with the main disconnect open.
5. Every conductor shall have permanent identification at both ends.
6. Wire color shall not replace wire numbering.
7. Field wiring shall be verified before energization.
8. Existing or legacy color deviations shall be documented.
9. Thermocouple extension wire shall match the thermocouple type and applicable standard.
10. Intrinsically safe circuits shall use approved identification and segregation.

## Recommended drawings to add

Create these as separate, readable illustrations rather than one oversized infographic:

1. **NFPA 79 machinery-panel color diagram**
2. **IEC three-phase and control-panel color diagram**
3. **PLC 24 VDC input/output wiring diagram**
4. **120 VAC control-circuit diagram**
5. **4–20 mA transmitter hookup**
6. **Intrinsically safe versus non-IS wiring**
7. **VFD input, output and motor-ground diagram**
8. **Servo power, brake, encoder and STO diagram**
9. **HVAC/BMS controller wiring**
10. **Semiconductor facility system-color map**
11. **Industrial Ethernet cable-identification example**
12. **Legacy-panel warning and conversion example**

Use separate pages for **code requirements** and **recommended engineering conventions**. Do not present the common U.S. 120/208 V or 277/480 V phase-color sets as universally mandatory. The NEC chiefly protects reserved conductor identities such as grounded and equipment-grounding conductors, while facility phase conventions can vary. NFPA 79 specifically addresses industrial machinery, including conductors inside machine electrical equipment. ([NFPA][2])

The current IEC references should be shown as **IEC 60445:2021 with Amendment 1:2026** and **IEC 60204-1:2016+A1:2021**. ([IEC Webstore][3])

[1]: https://www.nfpa.org/product/nfpa-79-standard/p0079code?utm_source=chatgpt.com "NFPA 79, Electrical Standard for Industrial Machinery"
[2]: https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70?utm_source=chatgpt.com "NFPA 70 (NEC) Code Development"
[3]: https://webstore.iec.ch/en/publication/66124?utm_source=chatgpt.com "IEC 60204-1:2016/AMD1:2021"

==========================

---

# Phase 46.1 Triage Record (2026-07-12)

This document is the **fourth external review** (of the `/design/` page). It was
not part of the `temp/` intake batch and had not been triaged. It is also the
upstream source of the wire-colour-coding and design-package assets published in
Phase 46 — those were built from its downstream artifacts.

## Fixed immediately (Phase 46.1) — all three verified against the repo first

| Claim | Verdict | Fix |
|---|---|---|
| Lifecycle stage count is inconsistent: `/design/` says "11 stages", `/lifecycle/` says "13 stages" | **CONFIRMED, and worse than reported.** The lifecycle index actually publishes **14** stages. Neither number was right. | Adopted the review's own better suggestion: **dropped the count entirely** rather than restating a number that keeps rotting. All four assertions (homepage, `/design/`, `/lifecycle/` description + heading) now read "from concept through operation and management of change". |
| — | **Found while fixing it:** the site claimed the lifecycle runs "through **decommissioning**". **There is no decommissioning stage page.** | Endpoint claim corrected, and an explicit **coverage-gap note** added to `/lifecycle/` — the functional-safety standards (IEC 61508/61511/62061) *do* define a lifecycle through decommissioning, so the gap is stated rather than papered over. |
| Sidebar shows "Motor Selection" twice | **CONFIRMED** (navigation.yml:133 and :145) | Disambiguated to **Motor Selection Fundamentals** (the section) and **Motor Selection Workflow** (the workflow). |
| Branding inconsistency — "Standards Atlas" vs "Field Guide" | **CONFIRMED on live pages.** The standards-finder page rendered a card titled "Standards Atlas"; the nav read "About this Atlas". (The Phase 45 review flagged the same leak on the NEC page; that pass fixed status labels but missed the branding.) | Card → **"Standards Library"**; nav → **"About this Field Guide"**. Site identity is now *Control Systems Engineering Field Guide* throughout. |

## Recorded, not yet scheduled — the `/design/` restructure

The review's larger proposal: restructure `/design/` from a link directory into an
end-to-end design workflow; separate general controls engineering from functional
safety; add the missing design disciplines; and carry one worked example
(pump & VFD skid) through the whole thing.

**Partially landed already.** The worked pump/VFD example it asks for *is* the
design-package poster published in Phase 46 on `/tools/templates/`. The remaining
work is the `/design/` page restructure itself.

**Not scheduled.** It is a genuine content phase and should be scoped on its own,
sequenced against Phases 47–49. It also overlaps the third review's rejected
"three-level page architecture" proposal — evaluate them together, not separately.

## Note on the wire-colour source text

Sections 1–22 of this review contain the full wire-colour-coding source text from
which the Phase 46 assets were generated, including several sections the published
gallery does **not** cover (water/wastewater, oil & gas, fire alarm & life safety,
marine/offshore, railway, automotive, project wire-colour schedule, wire-labeling
rules, minimum drawing notes). Those are a candidate expansion of the gallery if
the owner wants it — but they are text, not diagrams, and would need original
diagrams drawn before publication.
