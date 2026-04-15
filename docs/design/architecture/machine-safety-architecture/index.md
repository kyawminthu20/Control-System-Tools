---
layout: default
title: "Universal Machine Safety Architecture Template"
description: "Reusable safety system template covering E-stop chains, energy isolation, safety function design, and verification for industrial machines."
breadcrumb:
  - name: "Reference Models"
    url: "/reference/"
  - name: "Architecture"
    url: "/design/architecture/"
  - name: "Machine Safety Architecture"
redirect_from:
  - /reference/architecture/machine-safety-architecture/
  - /reference/architecture/machine-safety-architecture/index.html
---

<div class="page-header">
  <span class="page-header__label">Reference — Architecture</span>
  <h1>Universal Machine Safety Architecture Template</h1>
  <p>A reusable template applicable to semiconductor tools, robotics cells, chemical dosing skids, food processing machines, and warehouse automation. Aligns with ISO 12100, ISO 13849-1, NFPA 79, IEC 60204-1, UL 508A, and IEC 62443.</p>
</div>

## System Architecture Overview

```
                ┌──────────────────────────────┐
                │        Enterprise IT         │
                │  Historian / MES / Cloud     │
                └──────────────┬───────────────┘
                               │
                       Industrial Firewall
                               │
                     ┌─────────┴─────────┐
                     │ Industrial Switch │
                     └─────────┬─────────┘
                               │
               ┌───────────────┼────────────────┐
               │               │                │
          PLC Controller   HMI Panel      Engineering PC
               │
               │
       ┌───────┴──────────┐
       │   Safety PLC      │
       │ (SIL / PL logic)  │
       └───────┬──────────┘
               │
      ┌────────┼─────────────┐
      │        │             │
 Safety IO   Safety Relays   Safety Drives
      │        │             │
      └────────┼─────────────┘
               │
           Field Devices
      (motors, valves, pumps)
```

**Key principle: Safety system must remain functional even if the standard PLC fails.**

---

## Machine Functional Layers

| Layer | Responsibility |
|---|---|
| Enterprise | MES, historian, cloud |
| Supervisory | SCADA / HMI |
| Control | PLC |
| Safety | Safety PLC |

Safety layer always overrides control.

---

## Safety Function Architecture

Each hazard becomes a **safety function**:

| Safety Function | Input | Logic Solver | Output | Safe State |
|---|---|---|---|---|
| Emergency Stop | E-stop buttons | Safety PLC | contactor / STO | power removed |
| Guard Door | door interlock | Safety PLC | safety relay | motion disabled |
| Hydraulic Pressure | pressure switch | Safety PLC | dump valve | pressure released |
| Chemical Spill | leak sensor | Safety PLC | pump shutdown | chemical flow stopped |
| Overtravel | limit switch | Safety PLC | drive STO | motion halted |

Typical target: PL d, Category 3, Diagnostic Coverage > 90%.

---

## Emergency Stop Chain

```
E-STOP BUTTON
      ↓
Dual channel input
      ↓
Safety PLC input module
      ↓
Safety logic
      ↓
Safety contactor / STO
      ↓
Machine safe state
```

Requirements: dual channel wiring, monitored contacts, fault detection.

---

## Energy Isolation Design

| Energy Type | Isolation Method |
|---|---|
| Electrical | main disconnect |
| Hydraulic | dump valve |
| Pneumatic | exhaust valve |
| Mechanical | brake |
| Chemical | pump shutdown |

---

## Control Panel Architecture

```
┌───────────────────────────────┐
│ Main Disconnect               │
├───────────────────────────────┤
│ Branch Protection             │
├───────────────────────────────┤
│ Power Supplies                │
├───────────────────────────────┤
│ PLC + IO                      │
├───────────────────────────────┤
│ Safety PLC                    │
├───────────────────────────────┤
│ Motor Drives / Contactors     │
├───────────────────────────────┤
│ Terminal Blocks               │
└───────────────────────────────┘
```

Requirements from UL 508A: SCCR calculation, wire spacing, grounding, labeling.

---

## Network Segmentation

```
Enterprise Network
        │
        Firewall
        │
Industrial DMZ
        │
Plant Network
        │
Machine Network
        │
PLC + HMI
```

Safety systems should not rely on IT networks. Reference: IEC 62443.

---

## Required Engineering Documents

| Document | Purpose |
|---|---|
| System Description | machine overview |
| Risk Assessment | hazard identification |
| Safety Function Register | safety logic |
| Electrical Schematics | wiring |
| Hydraulic Schematics | fluid circuits |
| P&ID | process flow |
| IO List | PLC mapping |
| FDS | control logic |
| Test Plan | verification |

---

## Verification & Validation

| Test | Method |
|---|---|
| E-stop | press button |
| Guard interlock | open door |
| Hydraulic fault | simulate overpressure |
| Chemical leak | trigger sensor |

---

## Reusable Across Industries

| Industry | Example Machine |
|---|---|
| Semiconductor | wafer handler |
| Food | mixing skid |
| Pharma | dosing system |
| Energy | chemical injection skid |
| Warehouse | robotic cell |

---

<div style="margin-top:2rem; font-size:0.9rem; color:var(--color-text-muted);">
Source: <code>control-standards/rag/standards_intelligence/reference_models/Universal Machine Safety Architecture.md</code>. This is a design aid derived from the canonical RAG. Verify against applicable standards before use.
</div>
