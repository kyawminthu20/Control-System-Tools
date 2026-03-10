# Software Safety, Redundancy, and Intrinsic Safety Standards

**AI_READ_ACCESS: ALLOWED**
**CONTENT_CLASS: RAG_APPROVED**
**Status:** Authoritative Reference

## Purpose

This guide routes standards questions about safety PLC software, SIL or PL software implementation, redundancy and sensor architecture, PLC language standards, secure development, wiring or cable segregation, and intrinsically safe field I/O.

It is a standards-selection guide. It does **not** replace the purchased standards, vendor safety manuals, hazardous-area control drawings, or project-specific SIL or PL calculations.

## Scope Boundary

- `SIL` and `PL` claims apply to a safety function and its full chain: sensors, logic solver, software, final elements, diagnostics, and proof-test assumptions.
- `IEC 61131-3` is a PLC programming language standard. It does **not** by itself create a SIL or PL claim.
- No universal standard fixes a single sensor count or a single sensor type for every hazard. Architecture depends on target risk reduction, diagnostics, common-cause exposure, proof-test interval, nuisance-trip tolerance, and the required safe state.
- Detailed SIL allocation rules, hardware fault-tolerance tables, proof-test equations, common-cause scoring methods, and intrinsic-safety entity or system calculations are NOT FOUND IN LOCAL CORPUS - TO VERIFY against the purchased standards.

## Fast Routing

| If the question is about...                      | Start with...                                                   | Add...                                                                             |
| ------------------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Machinery safety PLC software                    | `IEC 62061` or `ISO 13849-1/-2`                                 | `ISO 12100`, `IEC 60204-1`, and `NFPA 79` or `NEC` where jurisdiction applies      |
| Process or chemical shutdown software            | `IEC 61511`                                                     | `IEC 61508-2/-3/-6` for lifecycle and architecture depth                           |
| Generic safety-related software lifecycle        | `IEC 61508-3`                                                   | `IEC 61508-2/-6` for subsystem architecture and diagnostics                        |
| PLC programming language and code structure      | `IEC 61131-3`                                                   | A safety lifecycle standard if any safety claim is made                            |
| Secure PLC or controller software development    | `IEC 62443-4-1`                                                 | `IEC 62443-4-2` and `IEC 62443-3-3` for component and system security requirements |
| Redundancy, voting, or sensor count              | `IEC 61508-2/-6`, `IEC 61511`, `IEC 62061`, or `ISO 13849-1/-2` | Device safety manuals and proof-test assumptions                                   |
| Cable routing and shielding for machinery        | `IEC 60204-1`, `NFPA 79`, `NEC`, and `UL 508A`                  | EMC, motion, and environmental requirements                                        |
| Intrinsically safe loops or associated apparatus | `IEC 60079-11`, `IEC 60079-14`, and `IEC 60079-25`              | US hazardous-location code and listing path if the installation is in the US       |

## Safety PLC Software And SIL

### Generic foundation

Use `IEC 61508-3` when the question is the safety-related software lifecycle itself: software safety requirements, design methods, verification, validation, modification control, and evidence.

Use `IEC 61508-2` and `IEC 61508-6` with it when the question moves from software alone into redundancy, diagnostics, subsystem behavior, voting logic, or proof-test assumptions.

### Machinery route

For machinery, use:

- `ISO 12100` for risk assessment,
- `ISO 13849-1/-2` for Performance Level route, or
- `IEC 62061` for machinery SIL route,
- with `IEC 60204-1` and `NFPA 79` handling the electrical implementation layer.

This means machinery projects usually do **not** start with `IEC 61511`. They start with `ISO 13849` or `IEC 62061` depending whether the project is taking the PL or machinery SIL route.

### Process route

For process skids, chemical systems, petroleum, and other credited shutdown functions, use `IEC 61511` on top of `IEC 61508`.

This is the correct route when the safety function is maintaining a safe process state, preventing loss of containment, or acting as a plant protection layer rather than simply stopping machine motion.

## PLC Language Standard vs Safety Claim Standard

Use `IEC 61131-3` for PLC language definitions such as:

- Structured Text,
- Ladder Diagram,
- Function Block Diagram,
- Sequential Function Chart.

Use it for language selection, coding conventions, and implementation structure. Do **not** use it alone to justify a SIL or PL claim.

If the code is part of a safety function, pair the language standard with:

- `IEC 62061` or `ISO 13849-1/-2` for machinery, or
- `IEC 61511` with `IEC 61508-3` for process-industry safety software.

## Redundancy Sensors And Architecture

The standards do not provide one universal answer such as “always use two sensors.”

Instead, they drive architecture decisions through:

- target `SIL` or `PL`,
- fault tolerance or category,
- diagnostic coverage,
- common-cause exposure,
- proof-test interval,
- response time,
- spurious-trip tolerance,
- environmental or hazardous-area constraints.

Typical architecture patterns include `1oo1`, `1oo2`, and `2oo3`, but the correct choice must be justified by the applicable lifecycle standard and the safety requirements specification.

Sensor type selection is similarly conditional. The standard normally expects the selected device to be suitable for:

- the hazard being detected,
- the response time required,
- the environmental conditions,
- the required diagnostics,
- any hazardous-area classification,
- and the claimed safety integrity or proven-in-use basis.

## Secure Development And Cybersecurity

Use `IEC 62443-4-1` when the question is secure product development for industrial automation and control components. This is the secure-development-lifecycle route for PLC or controller software products.

Use `IEC 62443-4-2` and `IEC 62443-3-3` when the question moves into technical security requirements for components and systems, including accounts, communications, hardening, and system security levels.

This cybersecurity family complements functional safety. It does not replace `IEC 61508`, `IEC 61511`, `IEC 62061`, or `ISO 13849`.

## Wiring, Cables, And Segregation

For machine or panel wiring, use:

- `IEC 60204-1`,
- `NFPA 79`,
- `NEC`,
- and `UL 508A` where listing applies.

These standards route questions about:

- conductor sizing,
- insulation rating,
- mechanical protection,
- separation between power and signal conductors,
- bonding and shielding,
- external-source marking,
- and cable support in fixed and flexing applications.

The local corpus already contains usable routing content for this layer in:

- `us/nfpa79/NFPA79_2024__Ch16__wiring_methods.md`
- `us/nec/NEC_2023__Art300__general_wiring_methods.md`
- `international/machinery/iec_60204_1/IEC60204_1_2018__Clause08__equipotential_bonding.md`
- `international/machinery/iec_60204_1/IEC60204_1_2018__Clause09__control_circuits_and_functions.md`

## Intrinsic Safety And Hazardous-Area IO

Intrinsic safety is not a generic software certification topic. It is an equipment, system, and installation discipline.

Use:

- `IEC 60079-11` for intrinsically safe apparatus,
- `IEC 60079-14` for design, selection, and erection of hazardous-area installations,
- `IEC 60079-25` for intrinsically safe electrical systems.

For US projects, also verify the listing and code path, typically through the applicable hazardous-location articles and the relevant UL standards such as `UL 60079-11`. Panel or associated-apparatus requirements may also route through `UL 698A` depending on the product and enclosure basis.

When intrinsically safe loops are used, the project normally needs:

- certified associated apparatus or isolators,
- hazardous-area and gas-group compatibility,
- temperature-class compatibility,
- loop or entity parameter checks,
- cable parameter checks,
- and controlled installation drawings.

Those detailed calculations and approval rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY.

## Implementation Deliverables

When safety-related PLC software or intrinsically safe I/O is in scope, the project should expect at least:

- a safety requirements specification,
- I/O and cause-and-effect documentation,
- software architecture showing safety and standard partitions,
- an approved list of permitted languages and function blocks,
- change control and version history,
- verification and validation records,
- proof-test procedures,
- cybersecurity design records where the controller is networked,
- and intrinsic-safety loop drawings where hazardous-area I/O is used.

## Local Corpus Status

- The local corpus already supports the electrical implementation layer through `IEC 60204-1`, `NFPA 79`, `NEC`, and `UL 508A`.
- The local corpus already supports the separation principle between standard PLC control and safety control.
- The local corpus does **not** yet contain detailed clause-level modules for `IEC 61508`, `IEC 61511`, `IEC 62061`, `ISO 13849`, `IEC 61131-3`, `IEC 62443-4-1`, or the `IEC 60079` family.
- For official purchase and current public pricing, see `STANDARDS_PURCHASE_TRACKER.md`.

You are asking a **very important question for a controls/software engineer**. Industrial software development is **not just coding**—it is governed by **functional safety, cybersecurity, lifecycle management, and verification standards**.

Since you are already working in **industrial automation, PLC systems, and safety architectures**, you should study these standards in **four layers**:

1. **Software lifecycle standards**
2. **Safety standards**
3. **Secure development standards**
4. **Testing and verification standards**

I will structure this like an **industry roadmap**.

---

# 1. Software Lifecycle Standards (Core Engineering Process)

These define **how industrial software is designed, implemented, and maintained**.

## IEC 61508-3 — Safety Software Lifecycle

This is the **foundation standard** for safety-related software.

It defines:

- Software safety requirements
- Architecture design
- Implementation rules
- Verification and validation
- Modification control
- Evidence documentation

Typical lifecycle:

```
Hazard Analysis
     ↓
Safety Requirements Specification (SRS)
     ↓
Software Architecture Design
     ↓
Implementation
     ↓
Verification
     ↓
Validation
     ↓
Deployment
     ↓
Operation and Maintenance
```

Industrial companies like:

- Siemens
- Rockwell
- ABB
- Honeywell
- Emerson

all follow **variants of this lifecycle**.

This standard is the **foundation for SIL-rated systems**.

---

# 2. Machinery and Industrial Safety Standards

The standard depends on **industry type**.

## Machinery Automation

Use:

### ISO 13849

Used for:

- robots
- conveyors
- machine tools
- packaging machines
- semiconductor tools

Defines **Performance Levels (PL)**:

| Level | Meaning          |
| ----- | ---------------- |
| PL a  | basic protection |
| PL b  | improved         |
| PL c  | moderate         |
| PL d  | high             |
| PL e  | very high        |

Example safety function:

```
Guard Door Open
      ↓
Dual channel safety input
      ↓
Safety PLC
      ↓
STO on servo drives
```

---

### IEC 62061

Similar to ISO 13849 but uses **SIL levels**.

Used heavily in:

- robotics
- factory automation
- high-risk machinery

---

## Process Industry Safety

Used in:

- chemical plants
- oil & gas
- offshore
- refineries
- nuclear

### IEC 61511

Defines:

- Safety Instrumented Systems (SIS)
- Shutdown systems
- Safety lifecycle

Example:

```
High Pressure Sensor
       ↓
Safety PLC
       ↓
Trip Valve
       ↓
Plant Shutdown
```

---

# 3. PLC Programming Standards

## IEC 61131-3

Defines **PLC programming languages**.

| Language                  | Use                   |
| ------------------------- | --------------------- |
| Ladder Diagram            | traditional PLC logic |
| Structured Text           | complex algorithms    |
| Function Block Diagram    | control systems       |
| Sequential Function Chart | process sequences     |

Important rule:

> This standard defines programming languages but **does not create safety certification by itself**.

To claim SIL/PL compliance, it must be combined with safety standards.

---

# 4. Industrial Cybersecurity Standards

Modern automation requires **secure development**.

## IEC 62443

This is the **cybersecurity framework for industrial control systems**.

Key parts:

### IEC 62443-4-1

Secure product development lifecycle.

Covers:

- threat modeling
- secure coding
- patch management
- vulnerability response

### IEC 62443-4-2

Security requirements for:

- PLC
- controllers
- drives
- embedded devices

### IEC 62443-3-3

System security architecture.

---

# 5. Electrical Implementation Standards

These govern **control panels and wiring**.

## NFPA 79

Electrical standard for industrial machinery.

## NEC

National Electrical Code.

## UL 508A

Industrial control panel construction.

## IEC 60204-1

International machinery electrical safety.

These define:

- conductor sizing
- cable separation
- grounding
- protection
- panel design

These are the **physical layer standards**.

---

# 6. Hazardous Area / Intrinsic Safety

Used in:

- oil and gas
- chemical plants
- offshore rigs

Key standards:

### IEC 60079-11

Intrinsically safe equipment.

### IEC 60079-14

Installation rules.

### IEC 60079-25

Intrinsically safe systems.

Requirements include:

- certified barriers
- loop energy calculations
- cable capacitance checks
- hazardous area classification

Intrinsic safety is **hardware and installation discipline**, not just software.

---

# 7. Software Testing Standards

Industrial software testing has **three layers**.

## 1. Unit Testing

Verify code modules.

Example:

```
function calculateFlowRate()
```

Test:

```
input = 10 L/min
expected output = 600 L/hr
```

---

## 2. Integration Testing

Verify subsystem interaction.

Example:

```
PLC ↔ VFD
PLC ↔ Robot
PLC ↔ SCADA
```

---

## 3. System Validation

Example safety validation:

```
Open Guard Door
        ↓
Verify machine stops within 200 ms
```

This is called **Safety Validation Testing**.

---

# 8. Typical Deliverables in Industrial Software Projects

A compliant project will produce:

### Engineering Documents

- Safety Requirements Specification
- Functional Design Specification
- Software Architecture
- I/O list
- Cause & Effect matrix

### Software Artifacts

- PLC source code
- version control repository
- change history
- cybersecurity design records

### Verification Records

- FAT (Factory Acceptance Test)
- SAT (Site Acceptance Test)
- proof-test procedures
- safety validation report

These artifacts are required by **safety lifecycle standards**.

---

# 9. Real Industry Stack (Example)

For a semiconductor or robotics machine:

```
Risk Assessment
      │
ISO 12100
      │
ISO 13849 or IEC 62061
      │
IEC 61508-3 (software lifecycle)
      │
IEC 61131-3 (PLC programming)
      │
IEC 62443 (cybersecurity)
      │
IEC 60204 / NFPA 79 / UL508A
```

---

# 10. What the Best Automation Engineers Actually Know

Senior controls engineers usually understand:

1. **Safety architecture**
2. **Control system architecture**
3. **PLC programming standards**
4. **verification and testing**
5. **cybersecurity**
6. **documentation and lifecycle management**

Most engineers know **only PLC programming**.

The ones who understand **standards and lifecycle engineering** become:

- **Systems architects**
- **Safety engineers**
- **principal controls engineers**

---

# 11. What You Should Study (Recommended Path)

Based on your background in **automation engineering and robotics**, the best learning order is:

### Step 1

IEC 61131-3
PLC software architecture.

### Step 2

ISO 13849
Machinery safety.

### Step 3

IEC 62061
Machine SIL systems.

### Step 4

IEC 61508
Functional safety lifecycle.

### Step 5

IEC 62443
Industrial cybersecurity.

### Step 6

IEC 60204 / NFPA 79
Electrical implementation.

---

# If you want, I can also show you something extremely useful:

I can build you a **“Industrial Software Engineering Blueprint”** that explains:

- how **ASML / Tesla / Amazon Robotics machines are actually engineered**
- the **7-layer industrial machine architecture**
- the **minimum 15-standard stack used by semiconductor equipment manufacturers**

That framework will dramatically improve your **systems engineering capability**.
