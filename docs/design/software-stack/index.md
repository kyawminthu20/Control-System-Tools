---
layout: default
title: "Software Stack and Cybersecurity"
description: "Routing guide for PLC language standards, safety-related software lifecycle, traceability, logging, cybersecurity, and intrinsic safety."
breadcrumb:
  - name: "Software Stack"
repo_path: "control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md"
related_standards:
  - name: "ISO 13849-1"
    url: "/standards/functional-safety/iso-13849-1/"
  - name: "IEC 62061"
    url: "/standards/functional-safety/iec-62061/"
  - name: "IEC 61511"
    url: "/standards/functional-safety/iec-61511/"
redirect_from:
  - /software-stack/
  - /software-stack/index.html
---

<div class="page-header">
  <span class="page-header__label">Software Stack and Cybersecurity</span>
  <h1>Software Safety, Traceability, and Cybersecurity Routing</h1>
  <p>Source: <code>rag/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md</code></p>
</div>

## Scope Boundary

This page is a **routing and implementation-boundary guide**. Key limits:

- `IEC 61131-3` is a PLC programming language standard. It does **not** by itself create a SIL or PL claim.
- SIL and PL claims apply to the full safety function chain: sensors, logic solver, software, final elements, diagnostics, and proof-test assumptions.
- Redundancy, diagnostics, sensor count, and logging depth depend on the required risk reduction and architecture.
- Detailed SIL calculations, hardware fault-tolerance tables, proof-test equations, and intrinsic-safety entity calculations are **not confirmed in this local corpus** — verify against the published standards.

---

## Quick Answers

- `Normal ladder logic does not automatically trigger safety requirements.` It is often just an implementation language under `IEC 61131-3`.
- `If the logic performs a safety function, it becomes safety-related software.` Route it through `IEC 62061` or `ISO 13849` for machinery, or `IEC 61511` plus `IEC 61508` for process safety.
- `Redundancy is not automatically required.` Use it when the target PL or SIL and the fault model demand it.
- `Traceability and logging are expected for safety-related logic, but usually event-based.` Log downloads, faults, resets, overrides, and security-relevant events, not every PLC scan.

---

## Fast Routing Table

| Question | Start With | Also Add |
|----------|-----------|---------|
| Machinery safety PLC software | IEC 62061 or ISO 13849-1 | ISO 12100, IEC 60204-1, NFPA 79 |
| Process / chemical shutdown software | IEC 61511 | IEC 61508-2/-3/-6 |
| Generic safety-related software lifecycle | IEC 61508-3 | IEC 61508-2/-6 |
| PLC programming language / code structure | **IEC 61131-3** | A safety lifecycle standard if any safety claim is made |
| Secure PLC software development | **IEC 62443-4-1** | IEC 62443-4-2, IEC 62443-3-3 |
| Redundancy, voting, sensor count | IEC 61508-2/-6, IEC 61511, IEC 62061, ISO 13849-1 | Device safety manuals |
| Cable routing and shielding | IEC 60204-1, NFPA 79, NEC, UL 508A | EMC and environmental requirements |
| Intrinsically safe loops | IEC 60079-11, IEC 60079-14, IEC 60079-25 | US hazardous-location code path if applicable |

---

## PLC Language Standard vs Safety Claim Standard

Use `IEC 61131-3` for language and software-structure questions such as:

- Ladder Diagram
- Function Block Diagram
- Structured Text
- Sequential Function Chart
- coding conventions
- project structure

The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and current vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.

**Key point:** if the code reduces risk, the language standard is only one part of the answer. Pair it with:

- `IEC 62061` or `ISO 13849-1` for machinery safety functions
- `IEC 61511` with `IEC 61508-3` for process-industry shutdown or protection logic

---

## Normal PLC vs Safety PLC vs SIS

| Topic | Normal PLC logic | Safety PLC logic | SIS logic |
|---|---|---|---|
| Main purpose | Machine control | Risk reduction on machinery | Process hazard reduction |
| Typical standards | IEC 61131-3:2025 | ISO 13849-1:2023, IEC 62061:2021+AMD1:2024, ISO 13850:2015, IEC 60204-1 | IEC 61511-1:2016+AMD1:2017 |
| Typical function | Sequence motors, valves, conveyors | E-stop, guard door, safety interlock | High pressure trip, burner management, reactor shutdown |
| Hardware expectation | Standard PLC I/O | Safety-rated I/O / safety relay / safety PLC | SIS logic solver, dedicated field devices |
| Redundancy | Usually not required | Used when risk target demands it | Common when SIL target demands it |
| Coding expectation | Functional correctness | Safety lifecycle, validation, controlled reset, fault response | Safety lifecycle, SRS, validation, proof testing |
| Traceability | Helpful | Expected | Expected |
| Logging | Ops/alarm history | Safety events and changes | Trips, bypasses, proof tests, demand/fault history |

---

## What Traceability and Logging Mean in Practice

For safety-related logic, traceability usually means:

- safety requirement -> safety function definition
- safety function -> I/O, logic, reset behavior, and fault response
- code version -> verification and validation results
- code change -> approval, review, and retest evidence
- installed version -> commissioning or proof-test record

Typical logged events are:

- safety downloads and online edits
- mode changes
- trips and shutdowns
- resets and reset attempts
- bypasses, inhibits, forces, and overrides
- discrepancy, feedback, and module faults
- user access and security-relevant events when the controller is networked

What usually does **not** need logging:

- every rung state on every PLC scan
- every internal bit transition forever
- normal non-safety sequence details unless needed for incident analysis

---

## Safety Route Decision

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart TD
    A[Control logic question] --> B{Does the code reduce risk?}
    B -->|No| C[IEC 61131-3 for language and structure]
    B -->|Yes| D{Application domain?}
    D -->|Machinery| E[ISO 13849-1 or IEC 62061]
    D -->|Process| F[IEC 61511]
    E --> G[IEC 60204-1 and NFPA 79 for electrical implementation]
    F --> H[IEC 61508-2/-3/-6 for lifecycle and architecture depth]
    B --> I{Networked or remotely maintained?}
    I -->|Yes| J[IEC 62443-4-1 / 4-2 / 3-3]
</pre>
</div>

---

## Worked E-Stop Pattern

An emergency stop is usually **not** implemented as ordinary PLC logic alone. A typical machinery architecture is:

- `E-stop PB` with two NC channels
- `Safety PLC` or `safety relay` checks channel health, discrepancy time, and faults
- `K1` and `K2` contactors remove power to the motor
- `K1_FB` and `K2_FB` auxiliary contacts feed back into the safety logic
- `Reset PB` is separate and manual
- standard PLC or HMI reads status but does not own the safety function

Simplified safety-ladder intent:

```text
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_VALID
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: export ESTOP_ACTIVE, SAFETY_OK, RESET_REQUIRED, FEEDBACK_FAULT, CHANNEL_FAULT
```

### I/O List

**Safety inputs:**
- `SI_ESTOP_CH1`: E-stop channel 1, NC
- `SI_ESTOP_CH2`: E-stop channel 2, NC
- `SI_RESET_PB`: manual reset pushbutton, NO
- `SI_K1_FB`: contactor K1 feedback auxiliary contact, NC when de-energized
- `SI_K2_FB`: contactor K2 feedback auxiliary contact, NC when de-energized

**Safety outputs:** `SO_K1`, `SO_K2` — safety outputs to contactors K1 and K2

**Standard PLC / HMI read-only status tags (exported from safety PLC):**
`ESTOP_ACTIVE`, `SAFETY_OK`, `RESET_REQUIRED`, `FEEDBACK_FAULT`, `CHANNEL_FAULT`

### Architecture

<div class="mermaid-wrap">
<pre class="mermaid">
flowchart LR
  subgraph Field["Field Devices"]
    EST1["E-stop CH1 (NC)"]
    EST2["E-stop CH2 (NC)"]
    RST["Reset PB (NO)"]
    K1FB["K1 Feedback (NC)"]
    K2FB["K2 Feedback (NC)"]
  end

  subgraph S["Safety PLC"]
    SI["Safety Inputs"]
    LOGIC["Safety Logic\ndual-channel check\ndiscrepancy check\nmanual reset\nfeedback monitor"]
    SO["Safety Outputs"]
  end

  subgraph P["Power Circuit"]
    K1["Contactor K1"]
    K2["Contactor K2"]
    M["Motor"]
  end

  subgraph C["Standard PLC / HMI"]
    PLC["Standard PLC"]
    HMI["HMI / Event Log"]
  end

  EST1 --> SI
  EST2 --> SI
  RST --> SI
  K1FB --> SI
  K2FB --> SI
  SI --> LOGIC
  LOGIC --> SO
  SO --> K1
  SO --> K2
  K1 --> K2 --> M
  LOGIC -. "status only" .-> PLC
  PLC -. "display / log" .-> HMI
</pre>
</div>

### State Machine

<div class="mermaid-wrap">
<pre class="mermaid">
stateDiagram-v2
  [*] --> SafeStopped

  SafeStopped --> ReadyForReset : CH1 healthy, CH2 healthy, feedback OK
  ReadyForReset --> SafetyEnabled : Manual reset accepted
  SafetyEnabled --> Running : Standard PLC run command
  Running --> SafeStopped : E-stop pressed
  SafetyEnabled --> SafeStopped : E-stop pressed
  Running --> Faulted : Channel fault or feedback fault
  SafetyEnabled --> Faulted : Channel fault or feedback fault
  Faulted --> ReadyForReset : Fault cleared, channels healthy
  Faulted --> SafeStopped : E-stop still active
</pre>
</div>

### Sequence of Operation

**Normal start:**
1. E-stop released; both NC channels closed; FEEDBACK_OK true.
2. Operator presses Reset; RESET_VALID true for one scan.
3. SAFETY_ENABLE sets; SO_K1 and SO_K2 energize; SAFETY_OK exported.
4. Standard PLC may now start motor.

**E-stop pressed:**
1. Both NC channels open; ESTOP_HEALTHY drops immediately.
2. SAFETY_ENABLE clears; SO_K1 and SO_K2 de-energize; contactors open.
3. Exported: ESTOP_ACTIVE = true, SAFETY_OK = false, RESET_REQUIRED = true.

**After E-stop release:**
1. Channels may return healthy — safety outputs remain off, no auto-restart.
2. Manual reset required. If feedback or channels are wrong, reset is rejected.

**Welded contactor fault:**
1. Contactor fails to open; feedback doesn't indicate de-energized state.
2. FEEDBACK_FAULT = true; reset blocked and fault logged.

### What must be documented

- Hazard and risk assessment result, including required PLr or SIL
- Safety function statement and safe state definition
- Reset philosophy: manual reset, no automatic restart
- Wiring and I/O mapping for both channels, feedbacks, and outputs
- Hardware list with safety-rated device part numbers
- Logic mapping to function blocks or rungs
- Verification and validation tests
- Fault tests: single-channel open, short, welded contactor, feedback failure, power cycle, module fault
- Change control: version, approval, changes, retest evidence

### Logging

**Log:** E-stop pressed/cleared — reset attempted/accepted/rejected — CHANNEL_FAULT, FEEDBACK_FAULT, module fault — downloads, edits, mode changes — bypass/force/inhibit attempts — security events when networked (IEC 62443-3-3, IEC 62443-4-1, IEC 62443-4-2)

**Do not log:** every rung state on every scan — every bit transition forever — normal non-safety sequence details

### Vendor-Specific Patterns

<details>
<summary>Rockwell GuardLogix</summary>
<div style="padding:0.5rem 0 0.5rem 1rem">
<blockquote><p><strong>Note:</strong> Instruction names and operands are vendor-specific. Verify against the applicable Studio 5000 Logix Designer documentation for the installed platform version.</p></blockquote>
<p><strong>Typical safety tags:</strong></p>
<ul>
<li><code>EStop_A</code>, <code>EStop_B</code> — E-stop dual-channel inputs</li>
<li><code>PB_Reset</code>, <code>PB_FaultReset</code> — reset pushbuttons</li>
<li><code>K1_FB</code>, <code>K2_FB</code> — contactor feedback inputs</li>
<li><code>SafeIn_CombinedStatus</code>, <code>SafeOut_CombinedStatus</code> — Guard I/O health status</li>
<li><code>ESTOP_E1</code> — ESTOP instruction backing tag</li>
<li><code>CROUT_M1</code> — CROUT instruction backing tag</li>
</ul>
<p><strong>Rung structure (pseudocode):</strong></p>
<pre><code>Rung 1: ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
               CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)

Rung 2: OSF(PB_Reset, PB_Reset_OSF)

Rung 3: CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
              InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
              Reset:=PB_Reset_OSF)

Rung 4: SO_K1 := CROUT_M1.O1
         SO_K2 := CROUT_M1.O2</code></pre>
<p><strong>What to log:</strong> <code>ESTOP_E1.FP</code>, <code>ESTOP_E1.II</code>, <code>ESTOP_E1.CRHO</code> — <code>CROUT_M1.FP</code>, <code>CROUT_M1.FaultCode</code> — safety signature/download/change events</p>
<p><strong>Official references:</strong></p>
<ul>
<li>ESTOP and CROUT instructions: Studio 5000 Logix Designer safety instructions reference</li>
<li>GuardLogix 5580 and Compact GuardLogix 5380 safety reference manual</li>
</ul>
</div>
</details>

<details>
<summary>Siemens S7-1500F / ET200SP</summary>
<div style="padding:0.5rem 0 0.5rem 1rem">
<blockquote><p><strong>Note:</strong> Instruction names and operands are vendor-specific. Verify against the applicable TIA Portal F-library and S7-1500F safety programming manual for the installed firmware and hardware version.</p></blockquote>
<p><strong>Typical safety tags:</strong></p>
<ul>
<li><code>fdiEstopGlobal</code> — F-DI dual-channel evaluated E-stop signal</li>
<li><code>DataToSafety.Acknowledge</code> — standard-to-safety acknowledge crossing</li>
<li><code>fdiK1Fb</code>, <code>fdiK2Fb</code> — contactor feedback inputs</li>
<li><code>qSafetyK1</code>, <code>qSafetyK2</code> — safety outputs to contactors</li>
<li><code>qSafetyK1_VS</code>, <code>qSafetyK2_VS</code> — F-DO value status bits</li>
</ul>
<p><strong>F-program network structure (pseudocode):</strong></p>
<pre><code>Network 1 — GlobalEstop : ESTOP1
  E_STOP := fdiEstopGlobal; ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge

Network 2 — FbK1 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK1Fb; QBAD_FIO := qSafetyK1_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms; Q := qSafetyK1

Network 3 — FbK2 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK2Fb; QBAD_FIO := qSafetyK2_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms; Q := qSafetyK2

Network 4 — AckGlobal : ACK_GL
  ACK_GLOB := DataToSafety.Acknowledge</code></pre>
<p><strong>What to log:</strong> <code>GlobalEstop.ACK_REQ/DIAG</code> — <code>FbK1/FbK2.ERROR/ACK_REQ/DIAG</code> — F-I/O passivation/reintegration — safety compile/download/signature/mode change</p>
<p><strong>Official references:</strong></p>
<ul>
<li>ESTOP1, FDBACK, ACK_GL: S7-1500F safety programming manual (Siemens Industry Online Support)</li>
<li>Feedback monitoring application: support article 21331098</li>
<li>Safety programming guideline: support article 109750255</li>
</ul>
</div>
</details>

---

## Cybersecurity and Hazardous-Area Routing

### Cybersecurity

Use `IEC 62443-4-1` when the question is secure development for PLC or controller software products. Add `IEC 62443-4-2` and `IEC 62443-3-3` when the question moves into component and system security requirements.

This family complements functional safety. It does **not** replace `IEC 61508`, `IEC 61511`, `IEC 62061`, or `ISO 13849`.

### Intrinsic Safety

For sensors, barriers, and I/O in classified locations, start with:

- `IEC 60079-11` for intrinsically safe apparatus
- `IEC 60079-14` for installation design and erection
- `IEC 60079-25` for intrinsically safe electrical systems

These detailed rules are **not confirmed in the local corpus**. Verify against the published standards and the applicable US code or listing path where relevant.

---

## Related References

- [IEC 62443 detail page]({{ '/standards/cybersecurity/iec-62443/' | relative_url }})
- [7-Layer Machine Architecture Model]({{ '/design/architecture/machine-architecture-model/' | relative_url }})
- [Universal Machine Safety Architecture]({{ '/design/architecture/machine-safety-architecture/' | relative_url }})
- [Safety Wiring]({{ '/verification/safety-wiring/' | relative_url }})
- [Networked Safety PLC scenario]({{ '/implementation/scenarios/networked-safety-plc/' | relative_url }})
