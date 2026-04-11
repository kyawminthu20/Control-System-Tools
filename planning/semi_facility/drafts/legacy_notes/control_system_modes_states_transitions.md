<!--
AI_READ_ACCESS: ALLOWED (with caution)
CONTENT_CLASS: WORK_IN_PROGRESS
STATUS: LEGACY_CAPTURED_NOTE
CATEGORY: SEMI_FACILITY_DRAFT_NOTE
-->

Yes. In control systems, the clean structure is usually:

# Modes → States → Transitions

You wrote **“states transactions”**. In controls, the standard term is **states and transitions**.

## 1. Basic hierarchy

### Modes

Modes define the **overall operating intent** of the system.

Examples:

- Off
- Manual
- Auto
- Maintenance
- E-Stop
- Fault / Trip
- Bypass

A **mode** answers:
**“What kind of operation is allowed right now?”**

### States

States define the **current step or condition** within that mode.

Examples in Auto mode:

- Idle
- Pre-Check
- Ready
- Start Sequence
- Running
- Shutdown Sequence
- Complete

A **state** answers:
**“What is the machine/process doing right now?”**

### Transitions

Transitions are the **logic conditions** that move the system from one state to another.

Examples:

- Operator Start PB pressed
- All permissives healthy
- Valve proven open
- Pressure > setpoint
- Timer done
- Fault detected
- Operator Stop requested

A **transition** answers:
**“Why does the system leave this state and go to the next one?”**

---

# 2. Recommended control philosophy

A solid control sequence usually looks like this:

## Mode layer

This is the top-level gate.

Example:

- If E-Stop active → force mode = E-Stop
- If critical fault active → force mode = Fault
- If operator selects Manual and safe → Manual
- If operator selects Auto and safe → Auto

Mode logic must be **dominant** over state logic.

That means:

- You do not allow Auto state progression while in Manual
- You do not allow Run sequence if fault or E-Stop is active

---

# 3. State machine structure

Inside a mode, especially **Auto**, use a state machine.

Typical state flow:

```text
OFF
  ↓
IDLE
  ↓
PRE-CHECK
  ↓
READY
  ↓
STARTING
  ↓
RUNNING
  ↓
STOPPING
  ↓
IDLE
```

Fault path:

```text
ANY STATE
  ↓
FAULT
  ↓
FAULT RESET
  ↓
IDLE
```

Emergency path:

```text
ANY STATE
  ↓
E-STOP
  ↓
MANUAL RESET / SAFE CONFIRM
  ↓
IDLE
```

---

# 4. Simple flow chart example

## Auto mode sequence for a chemical skid

```text
[Auto Selected]
      ↓
[Idle]
      ↓ Start command
[Pre-Check]
   - No E-Stop
   - No active trip
   - Tank level OK
   - Exhaust OK
   - Leak detect healthy
      ↓ all true
[Ready]
      ↓ start sequence command
[Open Exhaust / Vent]
      ↓ proof open
[Open Supply Valve]
      ↓ proof open
[Start Pump]
      ↓ run feedback
[Stabilize]
   - flow stable
   - pressure stable
      ↓ stable timer done
[Running]
      ↓ stop command
[Shutdown]
   - stop pump
   - close supply valve
   - maintain exhaust delay
      ↓ complete
[Idle]
```

Fault branch:

```text
From any step:
If leak = true
or high pressure = true
or exhaust fail = true
→ [Fault Shutdown]
```

---

# 5. What to show in the flow chart

A good controls flow chart should include these blocks:

## State block content

Each state should show:

- State name
- Outputs commanded in that state
- What conditions are being monitored
- Exit conditions

Example:

### State: START_PUMP

Outputs:

- Pump_Start = ON
- Supply_Valve = OPEN
- Exhaust = ON

Monitors:

- Pump_Run_Fbk
- Pump_Fault
- Start timeout timer

Transition:

- If Pump_Run_Fbk = TRUE → STABILIZE
- If timeout done and no feedback → FAULT
- If Stop requested → SHUTDOWN

That is much better than vague boxes.

---

# 6. Rules for good state-transition design

## Rule 1: One state active at a time

Avoid ambiguous logic.
Use a state number or enumerated state.

Example:

- 0 = Idle
- 10 = Precheck
- 20 = Ready
- 30 = Starting
- 40 = Running
- 50 = Stopping
- 90 = Fault

## Rule 2: Transitions must be explicit

Do not hide logic across many rungs without structure.

Bad:

- scattered bits everywhere

Better:

- `IF State = STARTING AND Pump_Run_Fbk THEN NextState = RUNNING`

## Rule 3: Separate permissives, interlocks, and trips

These are not the same.

### Permissive

Condition required to start.

- Tank level OK
- Utility available
- No alarm active

### Interlock

Condition required to continue operation or allow an action.

- Valve must be open before pump start
- Exhaust must be on before chemical valve opens

### Trip

Condition that forces immediate safe action.

- Leak detected
- High-high pressure
- Gas detector trip
- E-Stop

## Rule 4: Every state needs timeout handling

If expected feedback never comes, do not hang forever.

Examples:

- Valve open proof timeout
- Pump run feedback timeout
- Pressure stabilize timeout

## Rule 5: Fault handling should be global

Fault logic should override state progression.

---

# 7. Typical mode structure for industrial systems

For a semiconductor facility or chemical utility system, this is a practical mode list:

## Common modes

- **OFF** — all outputs de-energized except required safety utilities
- **LOCAL MANUAL** — maintenance/local device command
- **REMOTE MANUAL** — SCADA/operator command one output at a time
- **AUTO** — state machine sequence active
- **FAULT** — tripped state requiring reset
- **E-STOP** — emergency safe state
- **MAINTENANCE / BYPASS** — restricted service mode, tightly controlled

---

# 8. Example mode vs state table

| Layer      | Example                | Meaning                        |
| ---------- | ---------------------- | ------------------------------ |
| Mode       | AUTO                   | System allowed to run sequence |
| State      | PRECHECK               | Verifying permissives          |
| Transition | All permissives true   | Move to READY                  |
| State      | STARTING               | Issuing startup commands       |
| Transition | Pump run feedback true | Move to RUNNING                |
| State      | RUNNING                | Normal operation               |
| Transition | Stop request           | Move to STOPPING               |

---

# 9. PLC implementation pattern

In PLC terms, a common structure is:

## Section 1 — Input conditioning

- debounce
- scaling
- alarm limits
- feedback validation

## Section 2 — Mode manager

- determines active mode
- handles operator requests
- handles safety override

## Section 3 — State manager

- current state
- next state
- state timers
- one-shot transition commands

## Section 4 — Command/output logic

- outputs driven based on mode + state + permissives + trips

## Section 5 — Alarm/trip manager

- alarm detection
- trip latching
- reset conditions
- alarm summary to HMI/SCADA

---

# 10. Example pseudocode

```text
IF EStop THEN
    Mode := ESTOP;
ELSIF CriticalFault THEN
    Mode := FAULT;
ELSIF AutoSelected THEN
    Mode := AUTO;
ELSIF ManualSelected THEN
    Mode := MANUAL;
ELSE
    Mode := OFF;
END_IF;
```

Inside AUTO:

```text
CASE State OF

IDLE:
    IF StartCmd AND AllPermissives THEN
        State := PRECHECK;
    END_IF;

PRECHECK:
    IF NOT AllPermissives THEN
        State := FAULT;
    ELSIF PrecheckDone THEN
        State := STARTING;
    END_IF;

STARTING:
    Command_ValveOpen := TRUE;
    IF ValveOpenFbk THEN
        Command_PumpStart := TRUE;
    END_IF;

    IF PumpRunFbk THEN
        State := RUNNING;
    ELSIF StartTimeout THEN
        State := FAULT;
    END_IF;

RUNNING:
    IF StopCmd THEN
        State := STOPPING;
    ELSIF TripCondition THEN
        State := FAULT;
    END_IF;

STOPPING:
    Command_PumpStart := FALSE;
    Command_ValveOpen := FALSE;
    IF StopComplete THEN
        State := IDLE;
    END_IF;

FAULT:
    Command_PumpStart := FALSE;
    Command_ValveOpen := FALSE;
    IF ResetCmd AND FaultCleared THEN
        State := IDLE;
    END_IF;

END_CASE;
```

---

# 11. HMI/SCADA expectations

Your HMI should show:

## Mode

- Off / Manual / Auto / Fault / E-Stop

## Current state

- Idle / Starting / Running / Shutdown / Fault

## Transition blockers

- why it cannot move forward

Example:

- “Cannot start: Exhaust not proven”
- “Cannot start: Low chemical tank level”
- “Trip active: Leak detector zone 2”

This is critical. Operators need to know **why** the sequence is stuck.

---

# 12. Best flowchart symbols to use

Use these consistently:

- **Oval** → Start / End
- **Rectangle** → State or action
- **Diamond** → Transition decision
- **Parallelogram** → Inputs / outputs if needed
- **Connector** → jump to fault path or shutdown path

Recommended practice:

- One flow chart for **mode selection**
- One flow chart for **Auto sequence**
- One separate chart for **fault / shutdown sequence**

Do not cram everything into one page.

---

# 13. Semiconductor / chemical systems note

For semiconductor facility control, the sequence usually must account for:

- exhaust or scrubber prove before chemical/gas enable
- valve proof before transfer
- purge states before and after chemical or gas movement
- drain/flush/neutralization states
- leak detection trip states
- high-high level / low-low level
- utility dependencies:
  - CDA
  - N2
  - vacuum
  - DI water
  - exhaust
  - power healthy

- local cabinet safety chain
- remote E-Stop or area interlock

That means the state machine becomes more important, not less.

---

# 14. Recommended naming pattern

Use names that are obvious.

## Modes

- `MODE_OFF`
- `MODE_MANUAL`
- `MODE_AUTO`
- `MODE_FAULT`
- `MODE_ESTOP`

## States

- `ST_IDLE`
- `ST_PRECHECK`
- `ST_READY`
- `ST_STARTING`
- `ST_RUNNING`
- `ST_STOPPING`
- `ST_FAULT`

## Transition bits

- `Permissive_OK`
- `Trip_Active`
- `Valve_Open_Proven`
- `Pump_Run_Proven`
- `Reset_Allowed`

---

# 15. The engineering goal

The point of using **modes, states, and transitions** is to make the system:

- predictable
- safe
- diagnosable
- easy to document
- easy to troubleshoot
- easy to expand later

Without this structure, PLC code becomes spaghetti fast.

---

# 16. Practical template

Use this for each state:

## State Definition Template

**State Name:**
`ST_STARTING`

**Purpose:**
Bring equipment from ready to active run state.

**Commands in this state:**

- Open inlet valve
- Start exhaust
- Start pump

**Entry Conditions:**

- Auto mode active
- Start command active
- All permissives healthy

**Transition to next state:**

- Valve open proven
- Pump run feedback proven
- Stabilization timer done

**Transition to fault:**

- Any trip active
- Startup timeout
- Device fault feedback

**Transition to stop:**

- Stop request active

---

If you want, I can turn this into a **PLC/SCADA process control narrative template** or a **semiconductor chemical skid state-transition flowchart example**.

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
