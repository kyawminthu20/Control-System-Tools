<!-- TEMPLATE — control narrative skeleton. One numbered section per system
     or unit operation. Written for the reader who has to program, commission,
     or troubleshoot it — plain language, testable statements. -->

# Control Narrative

| Project |  | Document no. |  |
|---|---|---|---|
| System |  | Revision |  |
| Prepared by |  | Date |  |

## 1. System Overview

[Two paragraphs max: what the system does and its major equipment. Reference
P&IDs and the I/O list rather than duplicating them.]

## 2. Operating Modes

| Mode | Entered by | Behavior summary | Exited by |
|---|---|---|---|
| Off / safe |  |  |  |
| Manual |  |  |  |
| Auto |  |  |  |
| Maintenance |  |  |  |

[State what is and is not permitted in each mode, and what happens on mode
transitions — especially what keeps running and what stops.]

## 3. Sequence of Operation (per unit)

### 3.1 [Unit name] — Start Sequence

[Numbered steps. Each step: condition to advance, action taken, timeout and
what happens on timeout. Write so a commissioning engineer can test each step.]

### 3.2 [Unit name] — Normal Operation

[Control loops: what is controlled, by what, setpoint source, and behavior at
limits. Reference the alarm rationalization for alarm setpoints.]

### 3.3 [Unit name] — Stop / Shutdown Sequence

[Normal stop vs process trip vs safety trip — different paths, different
resets. State the difference explicitly.]

## 4. Interlocks

| Interlock | Cause | Effect | Reset | Bypassable? |
|---|---|---|---|---|
|  |  |  |  |  |

[Safety functions live in the SRS — reference them here, don't respecify them.]

## 5. Alarms and Operator Actions

[Reference the alarm rationalization sheet. Name the alarms that demand
immediate operator action.]

## 6. Failure Behavior

- On loss of control power:
- On loss of network / HMI:
- On instrument failure (per critical instrument):
- On restart after power loss (auto-restart policy):
