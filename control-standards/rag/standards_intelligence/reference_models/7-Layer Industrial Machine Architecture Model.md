<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
-->

Below is the **7-Layer Industrial Machine Architecture Model** commonly used in large automation environments (semiconductor tools, robotics cells, chemical skids, warehouse automation). The layers separate **responsibilities, risks, and standards compliance** so that machine safety, control, and enterprise integration remain manageable.

---

# 7-Layer Industrial Machine Architecture Model

## Layer 1 — Physical Process Layer

This is the **actual machine and process equipment** performing work.

Typical components:

- hydraulic actuators
- pumps and motors
- valves
- mechanical linkages
- conveyors
- chemical tanks
- dosing pumps

Example for your machine:

```
Hydraulic Clamp Cylinder
Hydraulic Lift Cylinder
Chemical Pump A
Chemical Pump B
Tanks
Piping
Mechanical frame
```

Applicable standards:

- ISO 12100
- ISO 4413
- ASME B31.3

Key engineering activities:

- mechanical design
- piping design
- pressure calculations
- chemical compatibility

---

# Layer 2 — Sensors & Actuators Layer

This layer converts the **physical process into electrical signals**.

Typical devices:

Sensors

- pressure transmitters
- limit switches
- proximity sensors
- level sensors
- flow meters
- encoders

Actuators

- solenoid valves
- servo drives
- pumps
- motor starters

Applicable standards:

- IEC 60947
- IEC 61131-2

Key engineering activities:

- signal selection
- wiring design
- sensor redundancy
- calibration

---

# Layer 3 — Control Layer

This is the **primary machine control logic**.

Typical equipment:

- PLC controller
- remote IO
- motion controllers
- drive controllers

Example platforms:

- Allen-Bradley ControlLogix
- Siemens S7-1500
- Beckhoff TwinCAT

Applicable standards:

- IEC 61131-3
- NFPA 79
- IEC 60204-1

Key engineering activities:

- control logic programming
- sequence control
- PID control
- motion control

---

# Layer 4 — Functional Safety Layer

This layer ensures the machine **cannot cause unacceptable harm**.

Typical components:

- safety PLC
- safety IO modules
- safety relays
- STO circuits
- E-stop chains
- guard interlocks

Applicable standards:

- ISO 13849-1
- IEC 62061
- IEC 61508

Typical safety functions:

| Function                  | Example        |
| ------------------------- | -------------- |
| Emergency Stop            | stop motion    |
| Guard Interlock           | disable motion |
| Hydraulic pressure safety | dump pressure  |
| Chemical overflow         | stop pumps     |

Engineering work:

- safety risk analysis
- PL/SIL calculations
- safety logic design

---

# Layer 5 — Human-Machine Interface Layer

This layer connects **operators to the machine**.

Typical components:

- touch HMI panels
- operator stations
- alarm systems
- visualization screens

Applicable standards:

- ISA‑101
- ISA‑18.2

Key design rules:

- minimize operator error
- clear alarm hierarchy
- intuitive navigation

---

# Layer 6 — Industrial Network & Edge Layer

This layer connects machines to **local plant systems**.

Typical systems:

- industrial Ethernet switches
- OPC-UA servers
- edge computers
- data buffering systems

Protocols commonly used:

```
Ethernet/IP
PROFINET
EtherCAT
OPC-UA
Modbus TCP
```

Applicable standards:

- IEC 61784
- IEC 62443

Engineering activities:

- network segmentation
- deterministic communication
- edge data buffering

---

# Layer 7 — Enterprise / Cloud Layer

This layer integrates machines with **business systems**.

Typical systems:

- manufacturing execution system (MES)
- data historian
- predictive maintenance AI
- cloud analytics

Example architecture:

```
Machine
 ↓
Edge Gateway
 ↓
Historian
 ↓
MES / ERP
 ↓
Cloud analytics
```

Applicable standards:

- ISA‑95
- NIST SP 800‑82

Engineering activities:

- data modeling
- KPI monitoring
- analytics pipelines

---

# Full Architecture Overview

```
Layer 7  Enterprise / Cloud
Layer 6  Industrial Network / Edge
Layer 5  HMI / Operator Interface
Layer 4  Functional Safety
Layer 3  Control (PLC / Motion)
Layer 2  Sensors & Actuators
Layer 1  Physical Machine
```

Key principle:

```
Higher layers cannot compromise safety layers.
```

Safety must remain operational even if:

- network fails
- PLC fails
- HMI crashes

---

# How This Applies to Your Machine

Your skid machine maps directly:

| Layer      | Your System                      |
| ---------- | -------------------------------- |
| Physical   | hydraulic clamp + chemical pumps |
| Sensors    | pressure, level, flow sensors    |
| Control    | PLC                              |
| Safety     | safety PLC                       |
| HMI        | local touchscreen                |
| Network    | historian connection             |
| Enterprise | site analytics                   |

This is a **correct architecture** for industrial machines.

---

# Strategic Insight for Your Control-Standards Project

Your repository is effectively building a **standards intelligence layer** that maps onto this architecture.

Example structure you could create:

```
standards/
   layer1_process
   layer2_sensors
   layer3_control
   layer4_safety
   layer5_hmi
   layer6_network
   layer7_enterprise
```

Each layer can contain:

```
applicable standards
design rules
compliance checklists
example architectures
```

This would allow your system to automatically answer:

```
"What standards apply to this machine design?"
```

---

If you want, I can also show you the **much deeper model used by large automation companies**:

**The 12-Layer Industrial Automation Stack**

It is the model used internally by companies like:

- ASML
- Tesla manufacturing
- semiconductor equipment builders

and it will significantly improve your **standards intelligence system.**
