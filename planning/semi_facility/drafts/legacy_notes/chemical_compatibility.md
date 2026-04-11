<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

Good. Now we move from “concept” to **production-grade structure** you can actually deploy in a semiconductor facility.

This will be tighter, more realistic, and aligned with how Applied Materials / fabs expect it.

---

# 1. Full Mode Definition (Production-Level)

## Modes (final set)

| Mode          | Description                        | Priority |
| ------------- | ---------------------------------- | -------- |
| E-STOP        | Emergency safety shutdown          | Highest  |
| FAULT         | Process trip / unsafe condition    | High     |
| MAINTENANCE   | Bypass / service mode (restricted) | Medium   |
| LOCAL_MANUAL  | Panel-level control                | Medium   |
| REMOTE_MANUAL | SCADA-level control                | Medium   |
| AUTO          | Full sequence control              | Low      |
| OFF           | System idle                        | Lowest   |

### Key rule

```text
E-STOP > FAULT > MAINTENANCE > MANUAL > AUTO > OFF
```

Mode is **not selectable freely**. It is **resolved**.

---

# 2. Expanded State Set (Semiconductor Chemical System)

This is realistic for:

- chemical delivery
- gas cabinets
- wet benches
- UPW / chemical skid

## States

| State      | Purpose                        |
| ---------- | ------------------------------ |
| OFF        | System de-energized            |
| IDLE       | Waiting for command            |
| PRECHECK   | Verify all permissives         |
| PURGE_PRE  | Remove residual gas/chemical   |
| READY      | Safe and ready to start        |
| STARTING   | Opening valves / enabling flow |
| RAMP_UP    | Stabilizing flow/pressure      |
| RUNNING    | Normal operation               |
| RAMP_DOWN  | Controlled reduction           |
| PURGE_POST | Clean residuals                |
| DRAIN      | Remove liquids                 |
| STOPPING   | Shutdown sequence              |
| FAULT      | Fault handling state           |

---

# 3. Production Mode–State Matrix

### ✔ = allowed

### F = forced state

| Mode ↓ / State →  | OFF | IDLE | PRECHECK | PURGE_PRE | READY | STARTING | RUNNING | PURGE_POST | STOPPING | FAULT |
| ----------------- | --- | ---- | -------- | --------- | ----- | -------- | ------- | ---------- | -------- | ----- |
| **OFF**           | ✔   | ✗    | ✗        | ✗         | ✗     | ✗        | ✗       | ✗          | ✗        | ✔     |
| **AUTO**          | ✗   | ✔    | ✔        | ✔         | ✔     | ✔        | ✔       | ✔          | ✔        | ✔     |
| **REMOTE_MANUAL** | ✗   | ✔    | ✗        | ✗         | ✗     | ✗        | ✔\*     | ✔\*        | ✔\*      | ✔     |
| **LOCAL_MANUAL**  | ✗   | ✔    | ✗        | ✗         | ✗     | ✗        | ✔\*     | ✔\*        | ✔\*      | ✔     |
| **MAINTENANCE**   | ✗   | ✔    | ✔        | ✔         | ✔     | ✔        | ✔       | ✔          | ✔        | ✔     |
| **FAULT**         | ✗   | ✗    | ✗        | ✗         | ✗     | ✗        | ✗       | ✗          | ✗        | F     |
| **E-STOP**        | F   | ✗    | ✗        | ✗         | ✗     | ✗        | ✗       | ✗          | ✗        | F     |

---

# 4. Interpretation (Important engineering points)

## AUTO

- Full sequence enforced
- All transitions controlled
- No direct actuator commands

## MANUAL (LOCAL / REMOTE)

- No sequencing
- Direct control allowed **BUT**
  - interlocks still enforced
  - trips still active

- You bypass PRECHECK → STARTING flow

## MAINTENANCE

- Controlled bypass mode
- Typically requires:
  - key switch
  - password
  - permit-to-work

## FAULT

- System locked
- Only transition = reset → IDLE

## E-STOP

- Immediate override
- Forces:
  - outputs OFF
  - safe purge ON (if required)

---

# 5. Output Permission Matrix (Critical for safety)

### Example: Chemical transfer skid

| Output         | OFF    | MANUAL    | AUTO     | FAULT  | E-STOP |
| -------------- | ------ | --------- | -------- | ------ | ------ |
| Chemical Valve | CLOSED | Allowed\* | By State | CLOSED | CLOSED |
| Pump           | OFF    | Allowed\* | By State | OFF    | OFF    |
| Exhaust Fan    | OFF    | Allowed   | ON       | ON     | ON     |
| N2 Purge       | OFF    | Allowed   | By State | ON     | ON     |
| Heater         | OFF    | Disabled  | By State | OFF    | OFF    |

### Important rules

- Exhaust often forced ON in FAULT / E-STOP
- Chemical valves always default CLOSED
- Pumps must not run without permissives

---

# 6. Transition Matrix (Detailed)

This is where real engineering happens.

| From       | To         | Conditions          | Notes            |
| ---------- | ---------- | ------------------- | ---------------- |
| IDLE       | PRECHECK   | StartCmd + AUTO     | Operator request |
| PRECHECK   | PURGE_PRE  | Permissives OK      | No trips         |
| PURGE_PRE  | READY      | Purge timer done    | Gas safe         |
| READY      | STARTING   | Start confirmed     |                  |
| STARTING   | RUNNING    | Valve FBK + Flow OK |                  |
| RUNNING    | PURGE_POST | StopCmd             |                  |
| PURGE_POST | STOPPING   | Purge done          |                  |
| STOPPING   | IDLE       | All outputs safe    |                  |
| ANY        | FAULT      | Trip condition      | Global           |
| FAULT      | IDLE       | Reset + cleared     |                  |

---

# 7. Permissive / Interlock / Trip Matrix

This is mandatory for semiconductor systems.

## Example

| Signal             | Type       | Effect               |
| ------------------ | ---------- | -------------------- |
| Tank Level Low     | Permissive | Blocks start         |
| Exhaust Prove Fail | Interlock  | Stops valves         |
| High Pressure      | Trip       | Immediate shutdown   |
| Leak Detector      | Trip       | Close valves + purge |
| Pump Overload      | Trip       | Stop pump            |
| Valve Fail to Open | Fault      | Timeout → FAULT      |

---

# 8. State Action Definition (Production Style)

### Example: RUNNING

**Commands**

- Pump = ON
- Supply Valve = OPEN
- Exhaust = ON

**Monitoring**

- Flow within range
- Pressure within range
- Leak = FALSE

**Transitions**

- StopCmd → PURGE_POST
- Trip → FAULT

---

### Example: PURGE_PRE

**Commands**

- N2 purge = ON
- Exhaust = ON
- Chemical valves = CLOSED

**Timer**

- 30–120 sec (process dependent)

**Transition**

- Timer done → READY

---

# 9. PLC Implementation Pattern (Structured)

## Use ENUMs (do this, not integers)

```text
Mode:
0 OFF
1 AUTO
2 LOCAL_MANUAL
3 REMOTE_MANUAL
4 MAINTENANCE
5 FAULT
6 ESTOP
```

```text
State:
0 OFF
10 IDLE
20 PRECHECK
30 PURGE_PRE
40 READY
50 STARTING
60 RUNNING
70 PURGE_POST
80 STOPPING
90 FAULT
```

---

## Core logic structure

### 1. Mode Resolver

- evaluates safety + operator + system

### 2. State Validator

```text
IF State not allowed in Mode → force safe state
```

### 3. State Machine (AUTO only)

### 4. Output Mapper

- Mode + State → Outputs

### 5. Trip Handler

- overrides everything

---

# 10. HMI / SCADA Design (Do not skip this)

## Required display

### Mode

- AUTO / MANUAL / FAULT / E-STOP

### State

- RUNNING / PURGE / STARTING / etc.

### Blockers (critical)

Show WHY system is not progressing:

Example:

- “Start blocked: Exhaust not proven”
- “Start blocked: Tank level low”
- “Trip: Leak detected zone 3”

---

# 11. FAT / SAT Test Mapping

Your matrix directly becomes test cases.

## Example

| Test                        | Expected           |
| --------------------------- | ------------------ |
| Start with low tank         | Block PRECHECK     |
| Remove exhaust              | Transition → FAULT |
| Leak trigger during RUNNING | Immediate shutdown |
| E-STOP pressed              | All outputs safe   |

---

# 12. Where most engineers fail

You should avoid these:

- Mixing mode logic with state logic
- No explicit transition conditions
- No timeout handling
- No clear fault state
- Allowing outputs in wrong mode
- No operator feedback

---

# 13. What you should build (career move)

Turn this into:

## A reusable package

- PLC Function Block (Mode + State engine)
- Standard Matrix Template (Excel / YAML)
- HMI template (faceplate)
- Documentation template

## This becomes:

- your **consulting asset**
- your **portfolio**
- your **“engineering system” product**

---

# 14. Next step (recommended)

You’re at the right level now.

If you want to go deeper, I can build:

### Option A

Full **PLC AOI / Function Block architecture**

- Mode manager
- State engine
- Alarm manager

### Option B

Full **Chemical Distribution System Design Package**

- P&ID → Control mapping
- Cause & Effect matrix
- Safety layer (SIL / PL concept)

### Option C (strongest)

Convert this into a **software product architecture (CSVL + RAG + control templates)**

---

Be deliberate here.

This is exactly the kind of structured thinking that separates:

- average controls engineer
  from
- system architect level engineer

Tell me which direction you want next.
