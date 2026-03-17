# Phase 20: Software Safety Stack Deepening — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deepen the RAG source file and the `/software-stack/` site page with a comparison table, expanded E-stop example (updated tag names, I/O list, Mermaid diagrams, sequence of operation, checklists), and vendor-specific patterns for Rockwell GuardLogix and Siemens S7-1500F.

**Architecture:** Two files change in sequence — RAG corpus first, then site page. No new files, no nav changes, no CSS changes. The E-stop section in both files is replaced entirely with expanded content; all other sections are extended in-place. Jekyll build verifies correct output at the end.

**Tech Stack:** Jekyll 4.2, Kramdown, Mermaid.js CDN (already integrated). Ruby 2.6 / Bundler at `~/.gem/ruby/2.6.0/bin/bundle`. Build: `cd docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build`.

**Spec:** `docs/superpowers/specs/2026-03-15-software-safety-stack-phase20-design.md`

**Source reference (read-only):** `planning/safety_software_stack.md`

---

## Chunk 1: RAG Corpus Update

### Task 1: Update RAG Corpus File

**Files:**
- Modify: `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`

**Current state of the file:**
- Line 68: old edition note (needs replacement)
- Lines 56–74: `## PLC Language Standard vs Safety Claim Standard` section
- Line 75: `## Safety-Related Software Routes` heading — comparison table goes immediately before this
- Lines 161–211: `## Worked Example - Emergency Stop Function` section with old tag names (CH_A_OK, SAFE_ENABLE, ESTOP_PRESSED, K1_FB_OFF) — replace entirely from line 161 through the last bullet of `### What should be logged` on line 211, stopping before `## Secure Development and Cybersecurity` on line 213

---

- [ ] **Step 1: Update the IEC 61131-3 edition note**

In `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`, find this exact sentence (line 68):

```
Verify the applicable edition and the vendor platform actually in use. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.
```

Replace with:

```
The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.
```

- [ ] **Step 2: Insert the comparison table**

Find this exact heading (line 75) in the RAG file:

```
## Safety-Related Software Routes
```

Insert the following block immediately before that heading. Add one blank line before the new section and one blank line between the table and the `## Safety-Related Software Routes` heading:

```
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
```

- [ ] **Step 3a: Delete the old E-stop section content**

In the RAG file, delete everything from the `## Worked Example - Emergency Stop Function` heading (line 161, adjusted for the ~12 lines inserted in step 2) through — but not including — `## Secure Development and Cybersecurity`. Use the section heading `## Secure Development and Cybersecurity` as the stop anchor, not a line number.

After deletion, `## Worked Example - Emergency Stop Function` should be gone entirely and `## Secure Development and Cybersecurity` should immediately follow the end of the `### Vendor-Specific Patterns` content you will add in steps 3b–3i.

- [ ] **Step 3b: Insert the new E-stop section opening**

At the position where the old E-stop section was, insert:

```
## Worked Example - Emergency Stop Function

An emergency stop is usually **not** implemented as ordinary PLC logic alone. For machinery, the function principles come from `ISO 13850`, the electrical realization routes through `IEC 60204-1` or `NFPA 79`, and the safety-related control system design is then governed by `ISO 13849-1/-2` or `IEC 62061`.

### Tag Naming

Two layers of tags exist in this example:

**Internal safety PLC tags** (used inside rung logic):
- `ESTOP_HEALTHY` — true when both E-stop channels are closed and healthy
- `FEEDBACK_OK` — true when both contactor feedbacks indicate the correct state
- `RESET_VALID` — true on rising edge of manual reset PB when all conditions are met
- `SAFETY_ENABLE` — the main safety-enable latch; set by RESET_VALID, cleared by E-stop or fault
- `CHANNEL_FAULT` — internal flag for channel discrepancy; also exported under the same name (see below)

**Standard PLC / HMI exported status tags** (read-only, published from safety PLC):
- `ESTOP_ACTIVE` — true when E-stop is active (inverse of ESTOP_HEALTHY)
- `SAFETY_OK` — mirrors SAFETY_ENABLE; true when safe to run
- `RESET_REQUIRED` — true when a manual reset is needed before restart
- `FEEDBACK_FAULT` — true when feedback check fails (inverse of FEEDBACK_OK)
- `CHANNEL_FAULT` — same name as the internal tag; safety PLC exports its internal CHANNEL_FAULT bit under the same name (intentional and common)
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING` — standard PLC motor command and status (not safety-owned)

### Typical architecture

- `E-stop PB` with two NC channels,
- `Safety PLC` or `safety relay` checks both channels, discrepancy time, shorts, and faults,
- `K1` and `K2` contactors remove power to the motor,
- `K1_FB` and `K2_FB` auxiliary contacts feed back into the safety logic,
- `Reset PB` is separate and manual,
- standard PLC or HMI reads status but does not own the safety function.

### I/O List

**Safety inputs:**
- `SI_ESTOP_CH1`: E-stop channel 1, NC
- `SI_ESTOP_CH2`: E-stop channel 2, NC
- `SI_RESET_PB`: manual reset pushbutton, NO
- `SI_K1_FB`: contactor K1 feedback auxiliary contact, NC when de-energized
- `SI_K2_FB`: contactor K2 feedback auxiliary contact, NC when de-energized

**Safety outputs:**
- `SO_K1`: safety output to contactor K1 coil
- `SO_K2`: safety output to contactor K2 coil

**Standard PLC / HMI read-only status tags (exported from safety PLC):**
- `ESTOP_ACTIVE`, `SAFETY_OK`, `RESET_REQUIRED`, `FEEDBACK_FAULT`, `CHANNEL_FAULT`
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING`
```

- [ ] **Step 3c: Insert the 7-rung pseudocode block**

Append immediately after the I/O List:

```
### Safety-ladder intent (7 rungs)
```

Then append a fenced text block with this content:

```
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_VALID
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: ESTOP_ACTIVE := NOT ESTOP_HEALTHY; SAFETY_OK := SAFETY_ENABLE;
         RESET_REQUIRED := NOT SAFETY_ENABLE; FEEDBACK_FAULT := NOT FEEDBACK_OK
```

Then append the following notes (plain text, no fence):

```
Note on Rung 2: discrepancy detection in a real safety project is typically a certified safety function block, not hand-built timer logic.

Note on Rung 5: SAFETY_ENABLE self-seals implicitly — as long as ESTOP_HEALTHY, FEEDBACK_OK, and no CHANNEL_FAULT remain true after reset, SAFETY_ENABLE stays true on the next scan without RESET_VALID. In a physical ladder implementation, an explicit OR branch (RESET_VALID OR SAFETY_ENABLE) makes the latch visible.
```

- [ ] **Step 3d: Insert the sequence of operation**

Append immediately after the rung notes:

```
### Sequence of Operation

**Normal start:**
1. E-stop released; both NC channels closed (ESTOP_HEALTHY = true; FEEDBACK_OK = true).
2. Operator presses Reset; RESET_VALID goes true for one scan.
3. SAFETY_ENABLE sets; SO_K1 and SO_K2 energize; SAFETY_OK exported to standard PLC.
4. Standard PLC may now start the motor if normal run conditions are met.

**E-stop pressed:**
1. One action opens both NC channels; ESTOP_HEALTHY drops immediately.
2. SAFETY_ENABLE clears; SO_K1 and SO_K2 de-energize.
3. Contactors open and remove power to the motor.
4. Exported status: ESTOP_ACTIVE = true, SAFETY_OK = false, RESET_REQUIRED = true.
5. HMI logs E-stop event and shows reset required.

**After E-stop release:**
1. Channels return healthy; ESTOP_HEALTHY = true.
2. Safety outputs remain off — no auto-restart; SAFETY_ENABLE remains false.
3. Manual reset is still required; RESET_REQUIRED remains true.
4. If feedback is wrong or channels still disagree, reset is rejected.

**Welded contactor fault:**
1. Stop is demanded; one contactor fails to open.
2. SI_K1_FB or SI_K2_FB does not indicate de-energized state; FEEDBACK_OK = false.
3. Exported status: FEEDBACK_FAULT = true; reset is blocked and fault is logged.
```

- [ ] **Step 3e: Insert documentation and logging checklists**

Append immediately after the sequence of operation:

```
### What must be documented

At minimum, document:

- the hazard and risk assessment result, including required PLr or SIL,
- the safety function statement (e.g., "Pressing E-stop removes motor torque within X ms"),
- safe state definition,
- reset philosophy: manual reset, no automatic restart,
- wiring and I/O mapping for both channels, feedbacks, and outputs,
- hardware list with safety-rated device part numbers and certifications,
- logic mapping showing which blocks or rungs implement the function,
- verification and validation test records,
- fault tests: single-channel open, short between channels, welded contactor, feedback failure, power cycle, module fault,
- change control: version, who approved, what changed, retest evidence.

### What should be logged

**Log these events:**
- E-stop pressed and E-stop cleared,
- reset attempted; reset accepted or rejected,
- safety fault codes (CHANNEL_FAULT, FEEDBACK_FAULT, module fault),
- safety program download, online edit, controller mode change,
- bypass, inhibit, force, or maintenance override attempts,
- user login and security-relevant events when networked (per IEC 62443-3-3, IEC 62443-4-1, IEC 62443-4-2).

**Do not log:**
- every rung state on every PLC scan,
- every internal bit transition indefinitely,
- normal non-safety sequence detail unless needed for incident analysis.
```

- [ ] **Step 3f: Insert the Rockwell GuardLogix vendor pattern**

Append immediately after the logging checklist:

```
### Vendor-Specific Patterns

#### Rockwell GuardLogix

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable Studio 5000 Logix Designer documentation for the installed platform version.

**Typical safety tags:**
- `EStop_A`, `EStop_B` — E-stop dual-channel inputs
- `PB_Reset`, `PB_FaultReset` — reset pushbuttons
- `K1_FB`, `K2_FB` — contactor feedback inputs
- `SafeIn_CombinedStatus`, `SafeOut_CombinedStatus` — Guard I/O health status
- `ESTOP_E1` — ESTOP instruction backing tag
- `CROUT_M1` — CROUT instruction backing tag

**Rung structure (pseudocode):**
```

Then append a fenced text block with this content:

```
Rung 1: ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
               CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)

Rung 2: OSF(PB_Reset, PB_Reset_OSF)

Rung 3: CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
              InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
              Reset:=PB_Reset_OSF)

Rung 4: SO_K1 := CROUT_M1.O1
         SO_K2 := CROUT_M1.O2
```

Then append (plain text):

```
**What to log:**
- `ESTOP_E1.FP` (fault present), `ESTOP_E1.II` (input invalid), `ESTOP_E1.CRHO` (cross-reset hold-off)
- `CROUT_M1.FP` (fault present), `CROUT_M1.FaultCode`
- Safety signature, download, and change events from controller audit trail

**Official references:**
- ESTOP instruction: Studio 5000 Logix Designer safety instructions reference
- CROUT instruction: Studio 5000 Logix Designer safety instructions reference
- GuardLogix 5580 and Compact GuardLogix 5380 safety reference manual
```

- [ ] **Step 3g: Insert the Siemens S7-1500F vendor pattern**

Append immediately after the Rockwell section:

```
#### Siemens S7-1500F / ET200SP

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable TIA Portal F-library and S7-1500F safety programming manual for the installed firmware and hardware version.

**Typical safety tags:**
- `fdiEstopGlobal` — F-DI dual-channel evaluated E-stop signal (discrepancy check done in F-DI module)
- `DataToSafety.Acknowledge` — standard-to-safety acknowledge crossing
- `DataFromSafety.EstopAckReq` — safety-to-standard acknowledge-request crossing
- `fdiK1Fb`, `fdiK2Fb` — contactor feedback inputs
- `qSafetyK1`, `qSafetyK2` — safety output signals to contactors
- `qSafetyK1_VS`, `qSafetyK2_VS` — F-DO value status bits

**F-program network structure (pseudocode):**
```

Then append a fenced text block with this content:

```
Network 1 — GlobalEstop : ESTOP1
  E_STOP  := fdiEstopGlobal
  ACK_NEC := TRUE
  ACK     := DataToSafety.Acknowledge

Network 2 — FbK1 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK1Fb; QBAD_FIO := qSafetyK1_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms
  Q := qSafetyK1

Network 3 — FbK2 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK2Fb; QBAD_FIO := qSafetyK2_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms
  Q := qSafetyK2

Network 4 — AckGlobal : ACK_GL
  ACK_GLOB := DataToSafety.Acknowledge
```

Then append (plain text):

```
**What to log:**
- `GlobalEstop.ACK_REQ`, `GlobalEstop.DIAG`
- `FbK1.ERROR`, `FbK1.ACK_REQ`, `FbK1.DIAG`
- `FbK2.ERROR`, `FbK2.ACK_REQ`, `FbK2.DIAG`
- F-I/O passivation and reintegration events
- Safety compile, download, signature, and mode change events

**Official references:**
- ESTOP1, FDBACK, ACK_GL: S7-1500F safety programming manual (Siemens Industry Online Support)
- Feedback monitoring application example: support article 21331098
- Safety programming guideline: support article 109750255
```

- [ ] **Step 4: Verify the RAG file**

```bash
grep -n "IEC 61131-3:2025" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
grep -n "Normal PLC vs Safety PLC" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
grep -n "SI_ESTOP_CH1" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
grep -n "GuardLogix" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
grep -n "Secure Development" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
grep -n "CH_A_OK\|SAFE_ENABLE\|ESTOP_PRESSED\|K1_FB_OFF" control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
```

Expected:
- Greps 1–5: each returns at least one match
- Grep 6 (old tag names): **no match** — confirms old content was fully replaced

- [ ] **Step 5: Commit the RAG update**

```bash
git add control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md
git commit -m "feat(rag): deepen software safety stack — comparison table, expanded E-stop, vendor patterns"
```

---

## Chunk 2: Site Page Update

### Task 2: Update the Software Stack Site Page

**Files:**
- Modify: `docs/software-stack/index.md`

**Current state (187 lines):**
- Line 69: old edition note sentence
- `## PLC Language Standard vs Safety Claim Standard` section ends at line 76 with `---`
- `## What Traceability and Logging Mean in Practice` is at line 78
- `## Worked E-Stop Pattern` section starts at line 125 and ends with `---` before `## Cybersecurity and Hazardous-Area Routing`

---

- [ ] **Step 1: Update the IEC 61131-3 edition note**

Find this exact sentence in `docs/software-stack/index.md` (line 69):

```
Verify the applicable edition and the actual vendor platform in use. Older materials, installed bases, and current controller ecosystems may not expose the same language set in the same way.
```

Replace with:

```
The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and current vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.
```

- [ ] **Step 2: Insert the comparison table section**

Find this exact block in `docs/software-stack/index.md`:

```
- `IEC 61511` with `IEC 61508-3` for process-industry shutdown or protection logic

---

## What Traceability and Logging Mean in Practice
```

Replace it with:

```
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
```

- [ ] **Step 3a: Delete the old Worked E-Stop section**

In `docs/software-stack/index.md`, delete everything from the `## Worked E-Stop Pattern` heading through (and including) the closing `---` separator immediately before `## Cybersecurity and Hazardous-Area Routing`. Use `## Cybersecurity and Hazardous-Area Routing` as the stop anchor. After deletion, `## Cybersecurity and Hazardous-Area Routing` should follow immediately after the previous `---` separator.

- [ ] **Step 3b: Insert the new E-Stop section opening and rung pseudocode**

At the position where the old E-Stop section was (immediately before `## Cybersecurity and Hazardous-Area Routing`), insert:

```
## Worked E-Stop Pattern

An emergency stop is usually **not** implemented as ordinary PLC logic alone. A typical machinery architecture is:

- `E-stop PB` with two NC channels
- `Safety PLC` or `safety relay` checks channel health, discrepancy time, and faults
- `K1` and `K2` contactors remove power to the motor
- `K1_FB` and `K2_FB` auxiliary contacts feed back into the safety logic
- `Reset PB` is separate and manual
- standard PLC or HMI reads status but does not own the safety function

Simplified safety-ladder intent:
```

Then append a fenced text block (type: text) with this content:

```
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_VALID
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: export ESTOP_ACTIVE, SAFETY_OK, RESET_REQUIRED, FEEDBACK_FAULT, CHANNEL_FAULT
```

- [ ] **Step 3c: Insert the I/O list**

Append immediately after the rung pseudocode block:

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
```

- [ ] **Step 3d: Insert the wiring/architecture Mermaid diagram**

Append immediately after the I/O list:

```
### Architecture
```

Then append a Mermaid block using the existing site page wrapper pattern (`<div class="mermaid-wrap"><pre class="mermaid">` ... `</pre></div>`). The Mermaid source inside the wrapper:

```
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
```

- [ ] **Step 3e: Insert the state machine Mermaid diagram**

Append immediately after the architecture diagram:

```
### State Machine
```

Then append a Mermaid block using the same wrapper. The Mermaid source:

```
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
```

- [ ] **Step 3f: Insert sequence of operation, checklists**

Append immediately after the state machine diagram:

```
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
```

- [ ] **Step 3g: Insert the Rockwell GuardLogix `<details>` block**

Append immediately after the logging section. Add a blank line after `</summary>` so Kramdown renders the body as Markdown:

```
### Vendor-Specific Patterns

<details>
<summary>Rockwell GuardLogix</summary>

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable Studio 5000 Logix Designer documentation for the installed platform version.

**Typical safety tags:**
- `EStop_A`, `EStop_B` — E-stop dual-channel inputs
- `PB_Reset`, `PB_FaultReset` — reset pushbuttons
- `K1_FB`, `K2_FB` — contactor feedback inputs
- `SafeIn_CombinedStatus`, `SafeOut_CombinedStatus` — Guard I/O health status
- `ESTOP_E1` — ESTOP instruction backing tag
- `CROUT_M1` — CROUT instruction backing tag

**Rung structure (pseudocode):**
```

Then append a fenced text block:

```
Rung 1: ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
               CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)

Rung 2: OSF(PB_Reset, PB_Reset_OSF)

Rung 3: CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
              InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
              Reset:=PB_Reset_OSF)

Rung 4: SO_K1 := CROUT_M1.O1
         SO_K2 := CROUT_M1.O2
```

Then append:

```
**What to log:** `ESTOP_E1.FP`, `ESTOP_E1.II`, `ESTOP_E1.CRHO` — `CROUT_M1.FP`, `CROUT_M1.FaultCode` — safety signature/download/change events

**Official references:**
- ESTOP and CROUT instructions: Studio 5000 Logix Designer safety instructions reference
- GuardLogix 5580 and Compact GuardLogix 5380 safety reference manual

</details>
```

- [ ] **Step 3h: Insert the Siemens S7-1500F `<details>` block**

Append immediately after the Rockwell `</details>`:

```
<details>
<summary>Siemens S7-1500F / ET200SP</summary>

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable TIA Portal F-library and S7-1500F safety programming manual for the installed firmware and hardware version.

**Typical safety tags:**
- `fdiEstopGlobal` — F-DI dual-channel evaluated E-stop signal
- `DataToSafety.Acknowledge` — standard-to-safety acknowledge crossing
- `fdiK1Fb`, `fdiK2Fb` — contactor feedback inputs
- `qSafetyK1`, `qSafetyK2` — safety outputs to contactors
- `qSafetyK1_VS`, `qSafetyK2_VS` — F-DO value status bits

**F-program network structure (pseudocode):**
```

Then append a fenced text block:

```
Network 1 — GlobalEstop : ESTOP1
  E_STOP := fdiEstopGlobal; ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge

Network 2 — FbK1 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK1Fb; QBAD_FIO := qSafetyK1_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms; Q := qSafetyK1

Network 3 — FbK2 : FDBACK
  ON := GlobalEstop.Q; FEEDBACK := fdiK2Fb; QBAD_FIO := qSafetyK2_VS
  ACK_NEC := TRUE; ACK := DataToSafety.Acknowledge; FDB_TIME := T#500ms; Q := qSafetyK2

Network 4 — AckGlobal : ACK_GL
  ACK_GLOB := DataToSafety.Acknowledge
```

Then append:

```
**What to log:** `GlobalEstop.ACK_REQ/DIAG` — `FbK1/FbK2.ERROR/ACK_REQ/DIAG` — F-I/O passivation/reintegration — safety compile/download/signature/mode change

**Official references:**
- ESTOP1, FDBACK, ACK_GL: S7-1500F safety programming manual (Siemens Industry Online Support)
- Feedback monitoring application: support article 21331098
- Safety programming guideline: support article 109750255

</details>

---
```

The final `---` closes the Worked E-Stop section. `## Cybersecurity and Hazardous-Area Routing` follows immediately after it.

- [ ] **Step 4: Verify the site page structure**

```bash
grep -n "IEC 61131-3:2025" docs/software-stack/index.md
grep -n "Normal PLC vs Safety PLC" docs/software-stack/index.md
grep -n "SI_ESTOP_CH1" docs/software-stack/index.md
grep -n "mermaid-wrap" docs/software-stack/index.md
grep -n "GuardLogix\|Siemens" docs/software-stack/index.md
grep -n "Cybersecurity and Hazardous" docs/software-stack/index.md
grep -n "CH_A_OK\|SAFE_ENABLE\|RESET_PB\b" docs/software-stack/index.md
```

Expected:
- Greps 1–6: each returns at least one match
- Grep 7 (old tag names): **no match** — confirms old rung content was fully replaced

Also verify `<details>` blocks have blank line after `</summary>`:

```bash
grep -A 1 "</summary>" docs/software-stack/index.md
```

Expected: each `</summary>` is followed by a blank line.

- [ ] **Step 5: Run Jekyll build**

```bash
cd /Users/kyawminthu/Dev/Control\ System\ Tools/docs && ~/.gem/ruby/2.6.0/bin/bundle exec jekyll build 2>&1
```

Expected last lines:
```
done in X.XXX seconds.
Auto-regeneration: disabled. Use --watch to enable.
```

No `Error`, no `Liquid Exception`. Page count should remain 132.

**If the build fails:**
- `Liquid Exception` in `software-stack/index.md` → check front matter and any `{{` / `{%` sequences in the new content (none are expected, but verify)
- Mermaid syntax error → will not fail build (client-side rendering); fix in follow-up
- `invalid byte sequence` → remove any non-UTF-8 characters from pasted content

- [ ] **Step 6: Commit the site page update**

```bash
git add docs/software-stack/index.md
git commit -m "feat(site): deepen /software-stack/ — comparison table, expanded E-stop, Mermaid diagrams, vendor patterns"
```

---

## Chunk 3: Project State and Push

### Task 3: Update Project State and Push

**Files:**
- Modify: `project_state/project_state.md`
- Modify: `project_state/change_log.md`

---

- [ ] **Step 1: Update `project_state/project_state.md`**

Make these targeted changes:

**Change the Current Phase line** from:

```
**Current Phase:** Phase 19 COMPLETE — Engineering Workflow Navigation Refactor
```

To:

```
**Current Phase:** Phase 20 COMPLETE — Software Safety Stack Deepening
```

**Change the Next Phase line** from:

```
**Next Phase:** Phase 20 QUEUED — Software Safety, Traceability, and Cybersecurity Routing
```

To:

```
**Next Phase:** Phase 21 QUEUED — TBD
```

**Replace the Phase 20 queue entry** — find:

```
## Phase 20 Queue — Software Safety, Traceability, and Cybersecurity Routing
```

Replace the entire Phase 20 queue block (from that heading through its last bullet) with:

```
## Phase 20 Scope — Software Safety Stack Deepening — COMPLETE

**Sources:** `planning/safety_software_stack.md`, `docs/superpowers/specs/2026-03-15-software-safety-stack-phase20-design.md`

- [x] RAG corpus updated: IEC 61131-3:2025 edition note; Normal PLC vs Safety PLC vs SIS comparison table; expanded E-stop section with canonical tag names, I/O list, 7-rung pseudocode, sequence of operation, documentation checklist, logging checklist; Rockwell GuardLogix and Siemens S7-1500F vendor patterns
- [x] `/software-stack/` site page updated: edition note, comparison table section, expanded E-stop with Mermaid wiring/architecture and state machine diagrams, vendor-specific `<details>` blocks
- [x] Jekyll build: clean, 132 pages
```

- [ ] **Step 2: Add change log entry**

In `project_state/change_log.md`, add the following at the top of the change history (before any existing entries):

```
## 2026-03-15 — Phase 20: Software Safety Stack Deepening

- Updated RAG source `Software_Safety_and_Intrinsic_Safety_Standards.md`: IEC 61131-3 edition note updated to 2025; Normal PLC / Safety PLC / SIS comparison table added; E-stop section fully replaced with canonical tag names (SI_ESTOP_CH1, ESTOP_HEALTHY, SAFETY_ENABLE), 7-rung pseudocode, I/O list, sequence of operation, documentation and logging checklists; Rockwell GuardLogix and Siemens S7-1500F vendor patterns added
- Updated `/software-stack/` site page: edition note updated; comparison table section added; E-stop section replaced with expanded content including Mermaid wiring/architecture flowchart and state machine diagram; vendor patterns in `<details>` expandable blocks
- No new pages; no navigation changes; build remains clean at 132 pages
```

- [ ] **Step 3: Commit and push**

```bash
git add project_state/project_state.md project_state/change_log.md
git commit -m "chore: update project state for Phase 20 complete"
git push origin master
```

Expected: push succeeds, remote ref updated to latest commit.
