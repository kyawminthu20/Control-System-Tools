---
layout: default
title: "7-Layer Industrial Machine Architecture Model"
description: "Layer-by-layer breakdown of industrial machine architecture, from the physical process to enterprise integration, with applicable standards per layer."
breadcrumb:
  - name: "Reference Models"
    url: "/tools/reference-hub/"
  - name: "Architecture"
    url: "/design/architecture/"
  - name: "Machine Architecture Model"
redirect_from:
  - /reference/architecture/machine-architecture-model/
  - /reference/architecture/machine-architecture-model/index.html
review:
  standard: "Original project reference model"
  edition: "n/a — original 7-layer model, not drawn from a published standard"
  status: "Review pending"
  coverage: "Editorial architecture model for industrial machines; a thinking tool, not a normative structure."
  last_reviewed: "April 2026"
---

<div class="page-header">
  <span class="page-header__label">Reference — Architecture</span>
  <h1>7-Layer Industrial Machine Architecture Model</h1>
  <p>Separates machine responsibilities, risks, and standards compliance so that safety, control, and enterprise integration remain manageable. Widely used in semiconductor tools, robotics cells, chemical skids, and warehouse automation.</p>
</div>

## Layer 1 — Physical Process Layer

The **actual machine and process equipment** performing work.

Typical components: hydraulic actuators, pumps and motors, valves, mechanical linkages, conveyors, chemical tanks, dosing pumps.

Applicable standards: ISO 12100, ISO 4413, ASME B31.3

Key engineering activities: mechanical design, piping design, pressure calculations, chemical compatibility.

---

## Layer 2 — Sensors & Actuators Layer

Converts the **physical process into electrical signals**.

Typical devices:
- **Sensors:** pressure transmitters, limit switches, proximity sensors, level sensors, flow meters, encoders
- **Actuators:** solenoid valves, servo drives, pumps, motor starters

Applicable standards: IEC 60947, IEC 61131-2

Key engineering activities: signal selection, wiring design, sensor redundancy, calibration.

---

## Layer 3 — Control Layer

The **primary machine control logic**.

Typical equipment: PLC controller, remote IO, motion controllers, drive controllers.

Example platforms: Allen-Bradley ControlLogix, Siemens S7-1500, Beckhoff TwinCAT.

Applicable standards: IEC 61131-3, NFPA 79, IEC 60204-1

Key engineering activities: control logic programming, sequence control, PID control, motion control.

---

## Layer 4 — Functional Safety Layer

Ensures the machine **cannot cause unacceptable harm**.

Typical components: safety PLC, safety IO modules, safety relays, STO circuits, E-stop chains, guard interlocks.

Applicable standards: ISO 13849-1, IEC 62061, IEC 61508

| Safety Function | Example |
|---|---|
| Emergency Stop | stop motion |
| Guard Interlock | disable motion |
| Hydraulic pressure safety | dump pressure |
| Chemical overflow | stop pumps |

Engineering work: safety risk analysis, PL/SIL calculations, safety logic design.

---

## Layer 5 — Human-Machine Interface Layer

Connects **operators to the machine**.

Typical components: touch HMI panels, operator stations, alarm systems, visualization screens.

Applicable standards: ISA-101, ISA-18.2

Key design rules: minimize operator error, clear alarm hierarchy, intuitive navigation.

---

## Layer 6 — Industrial Network & Edge Layer

Connects machines to **local plant systems**.

Typical systems: industrial Ethernet switches, OPC-UA servers, edge computers, data buffering systems.

Common protocols: Ethernet/IP, PROFINET, EtherCAT, OPC-UA, Modbus TCP.

Applicable standards: IEC 61784, IEC 62443

Engineering activities: network segmentation, deterministic communication, edge data buffering.

---

## Layer 7 — Enterprise / Cloud Layer

Integrates machines with **business systems**.

Typical systems: MES, data historian, predictive maintenance AI, cloud analytics.

Applicable standards: ISA-95, NIST SP 800-82

---

## Full Architecture Overview

```
Layer 7  Enterprise / Cloud
Layer 6  Industrial Network / Edge
Layer 5  HMI / Operator Interface
Layer 4  Functional Safety
Layer 3  Control (PLC / Motion)
Layer 2  Sensors & Actuators
Layer 1  Physical Machine
```

**Key principle: Higher layers cannot compromise safety layers.** Safety must remain operational even if the network fails, PLC fails, or HMI crashes.

---

## Application Mapping Example

| Layer | Example System |
|---|---|
| Physical | hydraulic clamp + chemical pumps |
| Sensors | pressure, level, flow sensors |
| Control | PLC |
| Safety | safety PLC |
| HMI | local touchscreen |
| Network | historian connection |
| Enterprise | site analytics |

---

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
Source: <code>control-standards/rag/standards_intelligence/reference_models/7-Layer Industrial Machine Architecture Model.md</code>. This is a design aid derived from the canonical RAG. Verify against applicable standards before use.
</div>
