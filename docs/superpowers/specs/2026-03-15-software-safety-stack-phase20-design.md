# Phase 20: Software Safety Stack Deepening — Design Spec

**Date:** 2026-03-15
**Phase:** 20
**Status:** Approved (revised v3 after second spec review)

---

## Goal

Deepen the RAG source and the `/software-stack/` site page so engineers get practical, actionable answers to three questions: "When is ladder logic safety-related?", "What must be traceable?", and "What should actually be logged?" — with vendor-specific E-stop patterns for Rockwell GuardLogix and Siemens S7-1500F.

---

## Scope

Two files change:

1. `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` — RAG source of truth, enriched with comparison table, detailed E-stop example, vendor patterns
2. `docs/software-stack/index.md` — site page mirrors the improved content

No new pages. No navigation changes. No CSS changes.

**Source reference:** `planning/safety_software_stack.md` (absolute path: `/Users/kyawminthu/Dev/Control System Tools/planning/safety_software_stack.md`) — read-only reference material; do not modify this file.

---

## Architecture

The existing page structure is preserved. Content is appended or extended in-place. Vendor-specific sections use `<details>` expandable blocks so the page remains scannable for engineers who only need the conceptual level.

---

## Tag Naming Convention

Two layers of tags exist in the E-stop example. Implementers must keep them distinct and consistent throughout all new content:

**Internal safety PLC tags** (used inside rung logic):
- `ESTOP_HEALTHY` — true when both E-stop channels are closed and healthy
- `FEEDBACK_OK` — true when both contactor feedbacks indicate the correct state
- `RESET_VALID` — true on rising edge of manual reset PB when conditions are met; used as the input to the safety-enable latch
- `SAFETY_ENABLE` — the main safety-enable latch (true = safe to run); set by a valid RESET_VALID pulse, cleared by E-stop or any fault
- `CHANNEL_FAULT` — internal safety PLC flag for channel discrepancy (also exported to standard PLC under the same name — see note below)

**Standard PLC / HMI exported status tags** (read-only, published from safety PLC to standard PLC):
- `ESTOP_ACTIVE` — true when E-stop is active (inverse of ESTOP_HEALTHY)
- `SAFETY_OK` — mirrors SAFETY_ENABLE; true when safe to run
- `RESET_REQUIRED` — true when a manual reset is needed before restart
- `FEEDBACK_FAULT` — true when feedback check fails (inverse of FEEDBACK_OK)
- `CHANNEL_FAULT` — same name as the internal safety PLC flag; the safety PLC exports its internal CHANNEL_FAULT bit to the standard PLC under the same name. This is intentional and common in safety system design. An implementer should not create a second tag with a different name.
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING` — standard PLC motor command and status (not safety-owned)

**Note on RESET_VALID vs RESET_LATCH:** Rung 5 uses RESET_VALID as the enabling condition. There is no separate RESET_LATCH tag. RESET_VALID is produced by Rung 4 and acts as the one-shot reset pulse that sets SAFETY_ENABLE (which then self-seals via normal rung evaluation as long as ESTOP_HEALTHY, FEEDBACK_OK, and no CHANNEL_FAULT remain true). The latch behavior is implicit in the rung evaluation, not a separate latch coil.

---

## RAG Corpus Update

File: `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`

### 1. IEC 61131-3 Edition Note

Find this exact sentence in the "PLC Language Standard vs Safety Claim Standard" section:

> Verify the applicable edition and the vendor platform actually in use. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.

Replace it with:

> The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.

### 2. Normal PLC / Safety PLC / SIS Comparison Table

Append as a new `## Normal PLC vs Safety PLC vs SIS` section after the "PLC Language Standard vs Safety Claim Standard" section:

```markdown
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

### 3. Detailed E-Stop Section

Append as a new `## Worked E-Stop: I/O List, Logic, and Documentation` section after the comparison table:

**3a. I/O List** — use this exact content:

```markdown
## Worked E-Stop: I/O List, Logic, and Documentation

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
- `ESTOP_ACTIVE` — true when E-stop is active (inverse of ESTOP_HEALTHY)
- `SAFETY_OK` — mirrors internal SAFETY_ENABLE; true when safe to run
- `RESET_REQUIRED` — true when a manual reset is needed
- `FEEDBACK_FAULT` — true when contactor feedback is incorrect
- `CHANNEL_FAULT` — safety PLC internal flag, also exported to standard PLC under the same name
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING` — standard PLC motor command and status
```

**3b. Safety logic rung intent (generic pseudocode — 7 rungs)** — use this exact content inside a fenced code block:

```text
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_VALID
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: ESTOP_ACTIVE := NOT ESTOP_HEALTHY; SAFETY_OK := SAFETY_ENABLE;
         RESET_REQUIRED := NOT SAFETY_ENABLE; FEEDBACK_FAULT := NOT FEEDBACK_OK
```

Note on Rung 2: discrepancy detection in a real safety project is typically a certified safety function block, not hand-built timer logic.

**3c. Sequence of Operation** — use this exact content:

```markdown
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

**3d. Documentation Checklist** — use this exact content:

```markdown
### Documentation Required

- Hazard and risk assessment result, including required PLr or SIL
- Safety function statement (e.g., "Pressing E-stop removes motor torque within X ms")
- Safe state definition
- Reset philosophy: manual reset, no automatic restart
- Wiring and I/O mapping for both channels, feedbacks, and outputs
- Hardware list with safety-rated device part numbers and certifications
- Logic mapping: which safety blocks or rungs implement the function
- Verification and validation test records
- Fault tests: single-channel open, short between channels, welded contactor, feedback failure, power cycle, module fault
- Change control: version, who approved, what changed, retest evidence
```

**3e. Logging Checklist** — use this exact content:

```markdown
### Logging Requirements

**Log these events:**
- E-stop pressed and E-stop cleared
- Reset attempted; reset accepted or rejected
- Safety fault codes (CHANNEL_FAULT, FEEDBACK_FAULT, module fault)
- Safety program download, online edit, controller mode change
- Bypass, inhibit, force, or maintenance override attempts
- User login and security-relevant events when networked (per IEC 62443-3-3, IEC 62443-4-1, IEC 62443-4-2)

**Do not log:**
- Every rung state on every PLC scan
- Every internal bit transition indefinitely
- Normal non-safety sequence detail unless needed for incident analysis
```

### 4. Rockwell GuardLogix Vendor Pattern

Append as a `### Rockwell GuardLogix` subsection. Use this exact Markdown (all pseudocode blocks must be wrapped in triple-backtick fences):

````markdown
### Rockwell GuardLogix

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable Studio 5000 Logix Designer documentation for the installed platform version.

**Typical safety tags:**
- `EStop_A`, `EStop_B` — E-stop dual-channel inputs
- `PB_Reset`, `PB_FaultReset` — reset pushbuttons
- `K1_FB`, `K2_FB` — contactor feedback inputs
- `SafeIn_CombinedStatus`, `SafeOut_CombinedStatus` — Guard I/O health status
- `ESTOP_E1` — ESTOP instruction backing tag
- `CROUT_M1` — CROUT instruction backing tag

**Rung structure (pseudocode):**

```text
Rung 1: ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
               CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)

Rung 2: OSF(PB_Reset, PB_Reset_OSF)

Rung 3: CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
              InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
              Reset:=PB_Reset_OSF)

Rung 4: SO_K1 := CROUT_M1.O1
         SO_K2 := CROUT_M1.O2
```

**What to log:**
- `ESTOP_E1.FP` (fault present), `ESTOP_E1.II` (input invalid), `ESTOP_E1.CRHO` (cross-reset hold-off)
- `CROUT_M1.FP` (fault present), `CROUT_M1.FaultCode`
- Safety signature, download, and change events from controller audit trail

**Official references:**
- ESTOP instruction: Studio 5000 Logix Designer safety instructions reference
- CROUT instruction: Studio 5000 Logix Designer safety instructions reference
- GuardLogix 5580 and Compact GuardLogix 5380 safety reference manual
````

### 5. Siemens S7-1500F / ET200SP Vendor Pattern

Append as a `### Siemens S7-1500F / ET200SP` subsection. Use this exact Markdown (all pseudocode blocks must be wrapped in triple-backtick fences):

````markdown
### Siemens S7-1500F / ET200SP

> **Note:** Instruction names and operands are vendor-specific. Verify against the applicable TIA Portal F-library and S7-1500F safety programming manual for the installed firmware and hardware version.

**Typical safety tags:**
- `fdiEstopGlobal` — F-DI dual-channel evaluated E-stop signal (discrepancy check done in F-DI module)
- `DataToSafety.Acknowledge` — standard-to-safety acknowledge crossing
- `DataFromSafety.EstopAckReq` — safety-to-standard acknowledge-request crossing
- `fdiK1Fb`, `fdiK2Fb` — contactor feedback inputs
- `qSafetyK1`, `qSafetyK2` — safety output signals to contactors
- `qSafetyK1_VS`, `qSafetyK2_VS` — F-DO value status bits

**F-program network structure (pseudocode):**

```text
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
````

---

## Site Page Update (`docs/software-stack/index.md`)

### Change 1: IEC 61131-3 edition note

Find this exact sentence (line 69):

> Verify the applicable edition and the actual vendor platform in use. Older materials, installed bases, and current controller ecosystems may not expose the same language set in the same way.

Replace with:

> The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and current vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.

### Change 2: Add Normal PLC / Safety PLC / SIS comparison table

Insert a new `## Normal PLC vs Safety PLC vs SIS` section between the `---` separator that follows `## PLC Language Standard vs Safety Claim Standard` and the `## What Traceability and Logging Mean in Practice` heading. Use the same table content as RAG section 2.

### Change 3: Expand Worked E-Stop section

Replace the **entire** existing `## Worked E-Stop Pattern` section (from the `## Worked E-Stop Pattern` heading through the closing `---` separator) with the following content:

**3a. Architecture bullet list** — keep the existing 6-bullet list unchanged:
```
- `E-stop PB` with two NC channels
- `Safety PLC` or `safety relay` checks channel health, discrepancy time, and faults
- `K1` and `K2` contactors remove power to the motor
- `K1_FB` and `K2_FB` auxiliary contacts feed back into the safety logic
- `Reset PB` is separate and manual
- standard PLC or HMI reads status but does not own the safety function
```

**3b. Updated rung pseudocode** — replace the existing 6-rung block with the 7-rung block using canonical tag names. The existing rungs use legacy names (CH_A_OK, SAFE_ENABLE, etc.) that differ from the new I/O list and sequence of operation. Update them to match the canonical names from the Tag Naming Convention. Use this exact content in a fenced code block:

```text
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_VALID
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: export ESTOP_ACTIVE, SAFETY_OK, RESET_REQUIRED, FEEDBACK_FAULT, CHANNEL_FAULT
```

**3c. I/O list** — add after the rung pseudocode. Use the I/O list from RAG section 3a.

**3d. Wiring/architecture Mermaid diagram** — add after the I/O list. Wrap in `<div class="mermaid-wrap"><pre class="mermaid">` tags (matching the existing page's Mermaid wrapper pattern). Use this exact Mermaid source:

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

**3e. State diagram** — add after the wiring diagram. Use the same Mermaid wrapper. Use this exact Mermaid source:

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

**3f. Sequence of operation** — add after the state diagram. Use the 4 scenarios from RAG section 3c.

**3g. Documentation checklist** — add after sequence. Use the content from RAG section 3d.

**3h. Logging checklist** — add after documentation checklist. Use the content from RAG section 3e.

### Change 4: Add vendor-specific patterns

Append a new `### Vendor-Specific Patterns` subsection at the end of the Worked E-Stop section, before the closing `---` separator. Use this exact HTML/Markdown structure:

```html
### Vendor-Specific Patterns

<details>
<summary>Rockwell GuardLogix</summary>

[copy exact content of RAG section 4, including the trust-boundary note, tag list, rung pseudocode in triple-backtick fences, logging list, and official references]

</details>

<details>
<summary>Siemens S7-1500F / ET200SP</summary>

[copy exact content of RAG section 5, including the trust-boundary note, tag list, F-program pseudocode in triple-backtick fences, logging list, and official references]

</details>
```

**Jekyll/Kramdown note:** Add a blank line after each `</summary>` tag so the Markdown body inside the `<details>` block renders correctly (Kramdown requires a blank line before Markdown content inside HTML blocks).

---

## Trust Boundary

- No copyrighted standards text is reproduced
- Vendor instruction names are stated as they appear in official public documentation (referenced by document title, not reproduced in full)
- All SIL/PL claims remain explicitly deferred to the published standards
- The page retains its existing trust-boundary note (footer include)

---

## Acceptance Targets

- RAG file updated: edition note, comparison table, full E-stop reference block (7-rung pseudocode with canonical tag names, I/O list, sequence with both internal and exported tag layers labeled, documentation checklist, logging checklist), Rockwell and Siemens vendor patterns with code-fenced pseudocode
- Site page: edition note updated; comparison table visible without expanding any `<details>` block; rung pseudocode uses canonical tag names consistent with the I/O list and sequence of operation; both Mermaid diagrams render correctly; vendor patterns behind `<details>` blocks
- Jekyll build clean; page count unchanged (no new pages)
- All existing cross-links remain intact
- Internal tag naming consistent throughout: ESTOP_HEALTHY / FEEDBACK_OK / RESET_VALID / SAFETY_ENABLE used for safety PLC internal signals; ESTOP_ACTIVE / SAFETY_OK / RESET_REQUIRED / FEEDBACK_FAULT used for exported HMI status signals; CHANNEL_FAULT used in both layers under the same name (intentional, documented)

---

## Files Changed

| File | Action |
|---|---|
| `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` | Modify — edition note update; append comparison table; append E-stop section (7 rungs, I/O list, sequence, doc checklist, log checklist, vendor patterns) |
| `docs/software-stack/index.md` | Modify — edition note update; insert comparison table section; replace E-stop section (updated rungs with canonical tags, I/O list, Mermaid diagrams, sequence, checklists, vendor `<details>` blocks) |
