<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
-->

Below is a **Universal Machine Safety Architecture Template** used in modern industrial machinery. It is structured so the same architecture can support machines in:

- semiconductor tools
- robotics cells
- chemical dosing skids
- food processing machines
- warehouse automation
- energy / oil & gas equipment

The template aligns with:

- ISO 12100
- ISO 13849-1
- NFPA 79
- IEC 60204-1
- UL 508A
- IEC 62443

---

# Universal Machine Safety Architecture Template

## 1. System Architecture Overview

```
                ┌──────────────────────────────┐
                │        Enterprise IT         │
                │ Historian / MES / Cloud     │
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

Key principle:

**Safety system must remain functional even if the standard PLC fails.**

---

# 2. Machine Functional Layers

A well-designed machine separates **four layers**.

| Layer       | Responsibility        |
| ----------- | --------------------- |
| Enterprise  | MES, historian, cloud |
| Supervisory | SCADA / HMI           |
| Control     | PLC                   |
| Safety      | Safety PLC            |

Example hierarchy:

```
Enterprise Layer
        ↓
Supervisory Layer
        ↓
Control Layer
        ↓
Safety Layer
        ↓
Physical Machine
```

Safety layer always overrides control.

---

# 3. Safety Function Architecture

Each hazard becomes a **safety function**.

Example template:

| Safety Function    | Input           | Logic Solver | Output          | Safe State            |
| ------------------ | --------------- | ------------ | --------------- | --------------------- |
| Emergency Stop     | E-stop buttons  | Safety PLC   | contactor / STO | power removed         |
| Guard Door         | door interlock  | Safety PLC   | safety relay    | motion disabled       |
| Hydraulic Pressure | pressure switch | Safety PLC   | dump valve      | pressure released     |
| Chemical Spill     | leak sensor     | Safety PLC   | pump shutdown   | chemical flow stopped |
| Overtravel         | limit switch    | Safety PLC   | drive STO       | motion halted         |

Typical target:

```
Performance Level = PL d
Category = 3
Diagnostic Coverage > 90%
```

---

# 4. Emergency Stop Chain

Typical E-stop chain:

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

Requirements:

- dual channel wiring
- monitored contacts
- fault detection

---

# 5. Energy Isolation Design

Machines must control **all energy sources**.

| Energy Type | Isolation Method |
| ----------- | ---------------- |
| Electrical  | main disconnect  |
| Hydraulic   | dump valve       |
| Pneumatic   | exhaust valve    |
| Mechanical  | brake            |
| Chemical    | pump shutdown    |

Example safe state:

```
Motor OFF
Hydraulic pressure vented
Chemical pumps stopped
Clamp released
Motion stopped
```

---

# 6. Hydraulic Safety Template

Hydraulic systems must manage **stored energy**.

Typical safety architecture:

```
Pump Motor
     │
Hydraulic Pump
     │
Pressure Relief Valve
     │
Directional Valve
     │
Actuator (Cylinder)
     │
Pressure Sensor
```

Safety additions:

```
Safety PLC
     ↓
Hydraulic dump valve
     ↓
Tank return
```

During E-stop:

```
Dump valve opens
Pressure released
Motion stops
```

Reference standard:

- ISO 4413

---

# 7. Chemical System Safety

Chemical dosing systems require additional controls.

Typical architecture:

```
Tank
 ↓
Level sensor
 ↓
Metering pump
 ↓
Flow meter
 ↓
Injection valve
```

Safety protection:

| Hazard       | Protection        |
| ------------ | ----------------- |
| Overfill     | level switch      |
| Leak         | spill sensor      |
| Overpressure | relief valve      |
| Pump runaway | flow verification |

---

# 8. Control Panel Architecture

Panel layout typically follows:

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

Requirements from:

- UL 508A

Important considerations:

- SCCR calculation
- wire spacing
- grounding
- labeling

---

# 9. Network Segmentation

Industrial cybersecurity architecture:

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

Safety systems should **not rely on IT networks**.

Reference:

- IEC 62443

---

# 10. Required Engineering Documents

A mature machine design produces these documents.

| Document                 | Purpose               |
| ------------------------ | --------------------- |
| System Description       | machine overview      |
| Risk Assessment          | hazard identification |
| Safety Function Register | safety logic          |
| Electrical Schematics    | wiring                |
| Hydraulic Schematics     | fluid circuits        |
| P&ID                     | process flow          |
| IO List                  | PLC mapping           |
| FDS                      | control logic         |
| Test Plan                | verification          |

---

# 11. Verification & Validation

Testing must confirm safety functions work.

Typical tests:

| Test            | Method                |
| --------------- | --------------------- |
| E-stop          | press button          |
| Guard interlock | open door             |
| Hydraulic fault | simulate overpressure |
| Chemical leak   | trigger sensor        |

Expected result:

```
machine transitions to safe state
```

---

# 12. Safe Machine State Definition

The safe state should always be explicitly defined.

Example:

```
Hydraulic pump OFF
Motion drives disabled
Chemical pumps OFF
Pressure released
Clamp released
Operator safe
```

---

# 13. Reusable Machine Architecture

This template works across industries:

| Industry      | Example Machine         |
| ------------- | ----------------------- |
| Semiconductor | wafer handler           |
| Food          | mixing skid             |
| Pharma        | dosing system           |
| Energy        | chemical injection skid |
| Warehouse     | robotic cell            |

That is why this architecture is widely reused.

---

## Important observation for your project

Your **Control Standards Intelligence repository** is already moving toward something powerful:

You are essentially building a **standards-aware machine design framework**.

That is the same philosophy used internally by companies like:

- Applied Materials
- Tesla
- ASML
- Siemens

They maintain internal **machine architecture templates** like the one above.

---

If you want, I can also show you something extremely useful for your project:

**The 7-layer Industrial Machine Architecture Model**

It is a **much deeper model** used by large automation companies when designing machines and entire factories. It will significantly improve your standards intelligence system.
