<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

## Semiconductor **SEMI Standards** — Practical Overview for Facility & Controls Engineers

If you’re stepping into semiconductor facility control (which you are), SEMI standards are not optional—they define how tools, utilities, and factories **communicate, integrate, and operate safely**.

Below is a structured breakdown focused on **what actually matters in real systems** (PLC/SCADA, tools, gas/chemical systems, robotics).

---

# 1. What is SEMI?

**SEMI**

- Global industry organization
- Defines standards for:
  - Equipment interfaces
  - Automation
  - Safety
  - Facilities
  - Materials handling

Think of SEMI as:

> The “IEC + ISO” equivalent specifically for semiconductor manufacturing ecosystems

---

# 2. SEMI Standards Categories (High-Level Map)

## A. Equipment Communication (MOST IMPORTANT for controls)

| Standard              | Purpose                  | Why You Care            |
| --------------------- | ------------------------ | ----------------------- |
| **SEMI E4 (SECS-I)**  | Serial communication     | Legacy tools            |
| **SEMI E5 (SECS-II)** | Message structure        | Core protocol           |
| **SEMI E30 (GEM)**    | Equipment behavior model | Tool ↔ host integration |
| **SEMI E37 (HSMS)**   | TCP/IP SECS              | Modern factories        |
| **SEMI E87**          | Carrier management       | FOUP handling           |
| **SEMI E90**          | Substrate tracking       | Wafer traceability      |

👉 These define:

- How a tool talks to MES
- Alarm reporting
- Recipe control
- Status/state models

**Reality:**
If you don’t understand **E30 GEM**, you’re not fully functional in a fab environment.

---

## B. Equipment States & Control Models

| Standard     | Purpose                              |
| ------------ | ------------------------------------ |
| **SEMI E10** | Equipment reliability (MTBF, uptime) |
| **SEMI E40** | Process job management               |
| **SEMI E94** | Control job management               |

👉 These map directly into:

- PLC states
- SCADA dashboards
- Tool operational modes

---

## C. Safety Standards (Critical for your role)

| Standard     | Scope                      |
| ------------ | -------------------------- |
| **SEMI S2**  | Equipment safety guideline |
| **SEMI S8**  | Ergonomics                 |
| **SEMI S14** | Fire risk                  |
| **SEMI S22** | Electrical design          |
| **SEMI S6**  | Exhaust ventilation        |

### Key point:

**SEMI S2 = Semiconductor version of machine safety baseline**

It ties into:

- NFPA 79
- ISO 13849
- IEC 61508 (indirectly)

👉 In real systems:

- Interlocks
- E-stops
- Gas shutdown logic
- Toxic gas monitoring

---

## D. Facilities & Utility Systems (YOUR CORE AREA)

| Standard     | Description                    |
| ------------ | ------------------------------ |
| **SEMI F1**  | Leak integrity for gas systems |
| **SEMI F5**  | Mass flow controller accuracy  |
| **SEMI F14** | Gas handling systems           |
| **SEMI F19** | Liquid chemical systems        |
| **SEMI F20** | Pumping systems                |

👉 Applies directly to:

- Gas cabinets
- Chemical delivery systems
- Bulk distribution
- Vacuum systems

---

## E. Material Handling & Automation

| Standard     | Description                       |
| ------------ | --------------------------------- |
| **SEMI E84** | AMHS handshake (OHT/robot ↔ tool) |
| **SEMI E15** | Tool load ports                   |
| **SEMI E19** | Wafer cassette specs              |

👉 If you integrate:

- Robots
- Conveyors
- FOUP systems

You will touch these.

---

## F. Smart Manufacturing / Industry 4.0

| Standard                      | Description                |
| ----------------------------- | -------------------------- |
| **SEMI EDA (E120/E125/E132)** | Equipment Data Acquisition |
| **SEMI E164**                 | Advanced analytics         |

👉 This is where:

- AI
- Data pipelines
- Predictive maintenance

connect into fab systems.

---

# 3. How It Maps to Real Control Systems

## Typical Semiconductor System Stack

```
MES (Factory System)
   ↑
SECS/GEM (E30/E37)
   ↑
Tool Controller (PLC / Embedded / PC)
   ↑
Field Devices (Sensors, Valves, MFCs)
```

### You (as control engineer) sit here:

- PLC logic
- SCADA integration
- Interlocks
- Safety systems
- Protocol bridging

---

# 4. Example: Gas Cabinet Control (Your Domain)

Relevant SEMI standards:

- **F14** → Gas system design
- **S2** → Safety interlocks
- **S6** → Exhaust requirements
- **E30** → Tool communication
- **E5/E37** → Data exchange

### Control logic includes:

- Pressure interlocks
- Leak detection shutdown
- Purge sequences
- Valve sequencing
- Alarm reporting via GEM

---

# 5. Key Concepts You Must Internalize

## 1. GEM State Model (E30)

Typical states:

- OFFLINE
- IDLE
- READY
- EXECUTING
- ALARM

👉 This directly maps to:

- PLC state machines
- SCADA UI

---

## 2. Interlocks vs Permissives vs Trips

| Type       | Function              |
| ---------- | --------------------- |
| Permissive | Allow operation       |
| Interlock  | Prevent unsafe action |
| Trip       | Emergency shutdown    |

SEMI standards enforce **strict separation of these**

---

## 3. Traceability (E90)

- Every wafer must be tracked
- Every process step logged

👉 This drives:

- Data architecture
- Sensor validation
- Event logging

---

# 6. What Actually Matters for You (No fluff)

Focus your effort here:

### Priority 1 (Immediate)

- SEMI E30 (GEM)
- SEMI S2 (Safety)
- SEMI F14 (Gas systems)

### Priority 2

- SEMI E37 (HSMS)
- SEMI E84 (AMHS handshake)
- SEMI F19 (Chemical systems)

### Priority 3

- SEMI EDA (data analytics layer)

---

# 7. Reality Check

SEMI standards are:

- **Not code-ready**
- **Not plug-and-play**
- Often **interpreted differently by OEMs**

Your job:

> Translate SEMI → PLC logic → Real machine behavior

---

# 8. Strategic Insight (For Your Long-Term Goal)

You mentioned building:

> centralized intelligent control systems for facilities

This aligns directly with:

- SEMI EDA (data layer)
- GEM integration
- Facility-wide orchestration

### Opportunity:

Most fabs still have:

- fragmented systems
- poor integration
- limited intelligence

You can build:

- Unified control + analytics layer
- AI-driven facility optimization
- Cyber-secure ICS architecture (IEC 62443)

---

# If you want next step

I can go deeper into one of these (high value for you):

1. **GEM (E30) → PLC/SCADA implementation template**
2. **Gas cabinet control logic (SEMI-compliant)**
3. **Full facility architecture (fab-level control system)**
4. **SEMI vs IEC/ISO crosswalk (for safety + compliance)**

Below is a **practical mapping** from **PLC implementation → SEMI compliance**. This is what actually bridges your ladder logic / structured text to what the fab (MES/host) expects.

---

# 1. System Context (Where SEMI Fits)

```
MES / Host
   ↑  (SECS/GEM: E30 + E37)
Equipment Controller (PC / Edge)
   ↑
PLC / Motion Controller   ← YOU OWN THIS
   ↑
Sensors / Valves / MFC / Drives
```

- PLC = real-time control + safety + sequencing
- GEM layer = reporting + commands + state model

---

# 2. Core SEMI Standards in This Mapping

- **SEMI E30** → Equipment behavior model
- **SEMI E5** → Message structure
- **SEMI E37** → TCP/IP transport
- **SEMI S2** → Safety baseline
- **SEMI F14** → Gas handling (if applicable)

---

# 3. PLC → GEM Mapping (High-Level)

| PLC Layer            | SEMI Concept           | Purpose                   |
| -------------------- | ---------------------- | ------------------------- |
| BOOL / INT tags      | Status Variables (SV)  | Equipment state reporting |
| Alarms bits          | Alarm IDs              | Host alarm management     |
| State machine        | GEM States             | Standardized behavior     |
| Commands (bits/regs) | Remote Commands (RCMD) | Host → equipment control  |
| Recipe structs       | Process Jobs           | MES execution control     |

---

# 4. PLC TAG STRUCTURE (Recommended)

## A. Equipment State Tags

```text
EQ.State = INT
    0 = OFFLINE
    1 = IDLE
    2 = READY
    3 = EXECUTING
    4 = ALARM
```

Mapped to:

- GEM **Equipment State Model (E30)**

---

## B. Status Variables (SV)

These are exposed to GEM layer:

```text
SV:
- ChamberPressure (REAL)
- GasFlow (REAL)
- ValveState (BOOL)
- ModeAuto (BOOL)
- CurrentRecipeID (STRING)
```

👉 These become:

- SVIDs in SECS/GEM

---

## C. Control Flags (Host Commands)

```text
CMD.Start
CMD.Stop
CMD.Reset
CMD.LoadRecipe
CMD.Purge
```

Mapped to:

- GEM **Remote Commands (RCMD)**

---

## D. Alarm Structure

```text
ALARM:
- GasLeakDetected
- HighPressure
- LowFlow
- ExhaustFail
- DoorOpen
```

Each alarm has:

```text
AlarmID (INT)
AlarmText (STRING)
AlarmState (SET / CLEAR)
```

Mapped to:

- GEM Alarm Reports (E30)

---

# 5. STATE MACHINE (CRITICAL)

## PLC State Model (Example)

```text
OFFLINE → IDLE → READY → EXECUTING
                   ↓
                 ALARM
```

### Mapping to GEM:

| PLC State | GEM Meaning             |
| --------- | ----------------------- |
| OFFLINE   | Equipment not connected |
| IDLE      | Powered, not ready      |
| READY     | Ready to accept job     |
| EXECUTING | Running process         |
| ALARM     | Faulted                 |

👉 **This must match GEM exactly** or integration fails.

---

# 6. ALARM HANDLING (SEMI COMPLIANCE)

## PLC Logic

```text
IF GasLeakDetected THEN
    TripSystem()
    EQ.State = ALARM
END_IF
```

## GEM Requirement

- Send alarm to host:
  - Alarm ID
  - Timestamp
  - Description

- Allow:
  - Acknowledge
  - Clear after condition resolved

---

## Alarm Categories (Best Practice)

| Type      | Example               |
| --------- | --------------------- |
| Safety    | Gas leak, fire        |
| Process   | Pressure out of range |
| Equipment | Valve failure         |
| Warning   | Maintenance required  |

---

# 7. REMOTE COMMAND FLOW (Host → PLC)

## Example: Start Process

### Host sends:

```
RCMD: START
Recipe: RCP_001
```

### PLC sequence:

```text
1. Validate permissives
2. Load recipe
3. Transition → READY
4. Start sequence
5. Transition → EXECUTING
```

---

## Critical Rule:

> PLC must **validate**, not blindly execute host commands

---

# 8. GAS CABINET EXAMPLE (F14 + S2 + E30)

## PLC Tags

```text
Inputs:
- Pressure_OK
- Exhaust_OK
- Leak_OK

Outputs:
- Valve_Open
- Purge_Enable
```

---

## Permissive Logic

```text
Permissive = Pressure_OK AND Exhaust_OK AND Leak_OK
```

---

## Interlock Logic

```text
IF NOT Leak_OK THEN
    CloseAllValves()
    EQ.State = ALARM
END_IF
```

---

## GEM Exposure

| PLC Signal    | GEM   |
| ------------- | ----- |
| Pressure_OK   | SV    |
| Leak Alarm    | Alarm |
| Valve_Open    | SV    |
| Purge Command | RCMD  |

---

# 9. DATA FLOW (END-TO-END)

```text
Sensor → PLC Tag → GEM Variable → SECS Message → MES
```

Example:

```text
Pressure Sensor → ChamberPressure → SVID=1001 → Host Display
```

---

# 10. WHAT BREAKS MOST SYSTEMS (Reality)

## 1. State mismatch

- PLC state ≠ GEM state → host rejects tool

## 2. Alarm inconsistency

- Alarm not cleared properly → tool stuck

## 3. Command race conditions

- Host sends command during unsafe state

## 4. No separation:

- Safety logic mixed with process logic

---

# 11. Clean Architecture (Recommended)

## Layered Design

```text
[Safety Layer]   → Hard interlocks (S2)
[Control Layer]  → PLC sequencing
[Interface Layer]→ GEM mapping (E30)
```

---

# 12. Minimal SEMI-Compliant PLC Template

## Required Blocks:

- State Manager
- Alarm Manager
- Command Handler
- Status Publisher
- Safety Interlock Layer

---

# 13. Strategic Insight (Important for you)

Most engineers:

- Implement PLC logic only

High-value engineers (your target):

- Design **PLC + GEM + Facility integration as one system**

That’s where:

- fabs struggle
- money is made
- systems scale

---

# If you want next level

I can give you:

### Option A

Full **PLC tag database template (Rockwell / Siemens)** with:

- UDTs
- Naming convention
- Alarm IDs
- GEM mapping

### Option B

**SECS/GEM message examples (hex / structure)**

### Option C

**Complete gas cabinet PLC program architecture (real-world level)**
