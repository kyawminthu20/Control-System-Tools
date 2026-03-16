# Phase 20: Software Safety Stack Deepening — Design Spec

**Date:** 2026-03-15
**Phase:** 20
**Status:** Approved (revised after spec review)

---

## Goal

Deepen the RAG source and the `/software-stack/` site page so engineers get practical, actionable answers to three questions: "When is ladder logic safety-related?", "What must be traceable?", and "What should actually be logged?" — with vendor-specific E-stop patterns for Rockwell GuardLogix and Siemens S7-1500F.

---

## Scope

Two files change:

1. `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` — RAG source of truth, enriched with comparison table, detailed E-stop example, vendor patterns
2. `docs/software-stack/index.md` — site page mirrors the improved content

No new pages. No navigation changes. No CSS changes.

---

## Architecture

The existing page structure is preserved. Content is appended or extended in-place. Vendor-specific sections use `<details>` expandable blocks so the page remains scannable for engineers who only need the conceptual level.

---

## Tag Naming Convention

Two layers of tags exist in the E-stop example. Implementers must keep them distinct:

**Internal safety PLC tags** (used inside rung logic):
- `ESTOP_HEALTHY` — true when both E-stop channels are closed and healthy
- `FEEDBACK_OK` — true when both contactor feedbacks indicate correct state
- `RESET_VALID` — true on valid rising-edge manual reset
- `SAFETY_ENABLE` — the main safety-enable latch (true = safe to run)
- `CHANNEL_FAULT` — internal fault flag for channel discrepancy

**Standard PLC / HMI exported status tags** (read-only, derived from safety PLC status outputs):
- `ESTOP_ACTIVE` — true when E-stop is pressed (inverse of ESTOP_HEALTHY)
- `SAFETY_OK` — mirrors SAFETY_ENABLE, exported to standard PLC
- `RESET_REQUIRED` — true when a manual reset is needed before restart
- `FEEDBACK_FAULT` — true when feedback check fails (inverse of FEEDBACK_OK)
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING` — standard PLC motor control tags (not safety-owned)

The sequence of operation section uses internal safety PLC tag names where describing what happens inside the safety logic.

---

## RAG Corpus Update

File: `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`

### 1. IEC 61131-3 Edition Note

In the "PLC Language Standard vs Safety Claim Standard" section, find this exact sentence:

> Verify the applicable edition and the vendor platform actually in use. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.

Replace it with:

> The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.

### 2. Normal PLC / Safety PLC / SIS Comparison Table

Append as a new section after the "PLC Language Standard vs Safety Claim Standard" section:

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

Append as a new section after the comparison table. This is the full E-stop reference block for the RAG corpus. It includes all content from sections 3–8 below.

**3a. I/O List**

```markdown
## Worked E-Stop: I/O List

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
- `ESTOP_ACTIVE` — true when E-stop is active (inverse of internal ESTOP_HEALTHY)
- `SAFETY_OK` — mirrors internal SAFETY_ENABLE; true when safe to run
- `RESET_REQUIRED` — true when a manual reset is needed
- `FEEDBACK_FAULT` — true when contactor feedback is incorrect
- `CHANNEL_FAULT` — true when channel discrepancy is detected
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING` — standard PLC motor command and status
```

**3b. Safety logic rung intent (generic pseudocode — 7 rungs)**

The RAG section includes all 7 rungs:

```
Rung 1: ESTOP_HEALTHY := SI_ESTOP_CH1 AND SI_ESTOP_CH2
Rung 2: CHANNEL_FAULT := (SI_ESTOP_CH1 XOR SI_ESTOP_CH2) for longer than discrepancy time
Rung 3: FEEDBACK_OK   := SI_K1_FB AND SI_K2_FB
Rung 4: RESET_VALID   := RisingEdge(SI_RESET_PB) AND ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK
Rung 5: SAFETY_ENABLE := ESTOP_HEALTHY AND NOT CHANNEL_FAULT AND FEEDBACK_OK AND RESET_LATCH
Rung 6: SO_K1 := SAFETY_ENABLE; SO_K2 := SAFETY_ENABLE
Rung 7: STATUS bits := ESTOP_ACTIVE, SAFETY_OK, RESET_REQUIRED, FEEDBACK_FAULT, CHANNEL_FAULT
```

Note on Rung 2: in a real safety project, discrepancy detection is typically a certified safety function block, not hand-built timer logic.

**3c. Sequence of Operation**

```markdown
**Normal start:**
1. E-stop released; both NC channels closed and healthy (ESTOP_HEALTHY = true).
2. Both contactor feedbacks indicate de-energized / ready state (FEEDBACK_OK = true).
3. Operator presses Reset.
4. Safety PLC validates channels and feedback; RESET_LATCH sets; SAFETY_ENABLE goes true.
5. SO_K1 and SO_K2 energize; standard PLC may now start the motor.

**E-stop pressed:**
1. One action opens both NC channels.
2. ESTOP_HEALTHY drops immediately.
3. SAFETY_ENABLE clears; SO_K1 and SO_K2 de-energize.
4. Contactors open and remove power to the motor.
5. HMI logs E-stop event (ESTOP_ACTIVE = true, SAFETY_OK = false, RESET_REQUIRED = true).

**After E-stop release:**
1. Channels return healthy (ESTOP_HEALTHY = true).
2. Safety outputs remain off — no auto-restart.
3. Manual reset is still required; RESET_REQUIRED remains true.
4. If feedback is wrong or channels disagree, reset is rejected.

**Welded contactor fault:**
1. Stop is demanded.
2. One contactor fails to open; SI_K1_FB or SI_K2_FB does not indicate de-energized state.
3. FEEDBACK_OK goes false; FEEDBACK_FAULT = true.
4. Reset is blocked and fault is logged.
```

**3d. Documentation Checklist**

```markdown
**Documentation required for this E-stop:**
- Hazard and risk assessment result, including required PLr or SIL
- Safety function statement: "Pressing E-stop removes motor torque within X ms"
- Safe state definition
- Reset philosophy: manual reset, no automatic restart
- Wiring and I/O mapping for both channels, feedbacks, and outputs
- Hardware list with safety-rated device part numbers and certifications
- Logic mapping: which safety blocks or rungs implement the function
- Verification and validation test records
- Fault tests: single-channel open, short between channels, welded contactor, feedback failure, power cycle, module fault
- Change control: version, who approved, what changed, retest evidence
```

**3e. Logging Checklist**

```markdown
**Log these events:**
- E-stop pressed and E-stop cleared
- Reset attempted; reset accepted or rejected
- Safety fault codes (channel fault, feedback fault, module fault)
- Channel discrepancy / cross-fault
- Contactor feedback mismatch
- Safety program download, online edit, controller mode change
- Bypass, inhibit, force, or maintenance override attempts
- User login and security-relevant events when networked (per IEC 62443-3-3, IEC 62443-4-1, IEC 62443-4-2)

**Do not log:**
- Every rung state on every PLC scan
- Every internal bit transition indefinitely
- Normal non-safety sequence detail unless needed for incident analysis
```

### 4. Rockwell GuardLogix Vendor Pattern

Append as a new subsection under the E-stop section:

```markdown
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

Rung 1: ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
               CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)
Rung 2: OSF(PB_Reset, PB_Reset_OSF)
Rung 3: CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
              InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
              Reset:=PB_Reset_OSF)
Rung 4: SO_K1 := CROUT_M1.O1; SO_K2 := CROUT_M1.O2

**What to log:**
- ESTOP_E1.FP (fault present), ESTOP_E1.II (input invalid), ESTOP_E1.CRHO (cross-reset hold-off)
- CROUT_M1.FP (fault present), CROUT_M1.FaultCode
- Safety signature, download, and change events from controller audit trail

**Official references:**
- ESTOP instruction: Studio 5000 Logix Designer safety instructions reference
- CROUT instruction: Studio 5000 Logix Designer safety instructions reference
- GuardLogix 5580 and Compact GuardLogix 5380 safety reference manual
```

### 5. Siemens S7-1500F / ET200SP Vendor Pattern

Append as a new subsection:

```markdown
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

**What to log:**
- GlobalEstop.ACK_REQ, GlobalEstop.DIAG
- FbK1.ERROR, FbK1.ACK_REQ, FbK1.DIAG
- FbK2.ERROR, FbK2.ACK_REQ, FbK2.DIAG
- F-I/O passivation and reintegration events
- Safety compile, download, signature, and mode change events

**Official references:**
- ESTOP1, FDBACK, ACK_GL: S7-1500F safety programming manual (Siemens Industry Online Support)
- Feedback monitoring application example: support article 21331098
- Safety programming guideline: support article 109750255
```

---

## Site Page Update (`docs/software-stack/index.md`)

### Change 1: IEC 61131-3 edition note

Find this exact sentence (line 69):

> Verify the applicable edition and the actual vendor platform in use. Older materials, installed bases, and current controller ecosystems may not expose the same language set in the same way.

Replace with:

> The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and current vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.

### Change 2: Add Normal PLC / Safety PLC / SIS comparison table

Insert a new `## Normal PLC vs Safety PLC vs SIS` section after the existing `## PLC Language Standard vs Safety Claim Standard` section (`---` separator) and before `## What Traceability and Logging Mean in Practice`.

Section content: the same 8-row comparison table from RAG section 2 above.

### Change 3: Expand Worked E-Stop section

Replace the existing `## Worked E-Stop Pattern` section entirely. The new section contains:

**3a. Architecture bullet list** — unchanged from existing page (keep the 6-bullet list starting "E-stop PB with two NC channels …")

**3b. Simplified rung pseudocode** — keep the existing 6-rung pseudocode block as-is on the site page (Rungs 1–6 only; the site page does not need Rung 7 status-bit assignment since those are in the documentation/logging checklists). The RAG file gets all 7 rungs.

**3c. I/O list** — add the I/O list (safety inputs, safety outputs, standard PLC status tags) from RAG section 3a above.

**3d. Wiring/architecture Mermaid diagram** — insert a `flowchart LR` diagram. Use this exact source:

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

**3e. State diagram** — insert a `stateDiagram-v2` diagram. Use this exact source:

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

**3f. Sequence of operation** — the 4 scenarios from RAG section 3c (normal start, E-stop pressed, after release, welded contactor fault) as compact numbered lists.

**3g. Documentation checklist** — the bullet list from RAG section 3d.

**3h. Logging checklist** — the two-part list (log / do not log) from RAG section 3e.

### Change 4: Add vendor-specific patterns

Append a new `### Vendor-Specific Patterns` subsection at the end of the Worked E-Stop section, using two `<details>` expandable blocks:

```html
<details>
<summary>Rockwell GuardLogix</summary>

[content from RAG section 4 — tags, rung pseudocode, what to log, official references]

</details>

<details>
<summary>Siemens S7-1500F / ET200SP</summary>

[content from RAG section 5 — tags, F-program pseudocode, what to log, official references]

</details>
```

Both blocks must include the vendor trust-boundary note at the top (from RAG sections 4 and 5 respectively).

Note on Jekyll/Kramdown: add a blank line after each `</summary>` tag so Markdown inside the `<details>` block renders correctly.

---

## Trust Boundary

- No copyrighted standards text is reproduced
- Vendor instruction names are stated as they appear in official public documentation (referenced by document title, not reproduced in full)
- All SIL/PL claims remain explicitly deferred to the published standards
- The page retains its existing trust-boundary note (footer)

---

## Acceptance Targets

- RAG file updated: comparison table, full E-stop reference block (I/O, 7 rungs, sequence, doc checklist, log checklist), Rockwell and Siemens vendor patterns, edition note updated
- Site page answers "when is ladder logic safety-related?", "what must be traceable?", "what should be logged?" without navigating away
- Normal PLC / Safety PLC / SIS comparison table visible without expanding any `<details>` block
- Vendor-specific patterns behind `<details>` blocks — do not dominate the page
- Both Mermaid diagrams render correctly in Jekyll build
- Jekyll build remains clean; page count unchanged (no new pages)
- All existing cross-links remain intact
- Internal tag naming is consistent throughout site page content (internal safety PLC tags vs exported status tags do not use conflicting names for the same concept)

---

## Files Changed

| File | Action |
|---|---|
| `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` | Modify — edition note update, append comparison table, append full E-stop reference block with I/O list / sequence / checklists / vendor patterns |
| `docs/software-stack/index.md` | Modify — edition note update, add comparison table section, expand E-stop section with Mermaid diagrams and vendor `<details>` blocks |

**Source reference for implementation:** `planning/safety_software_stack.md` (absolute path: `/Users/kyawminthu/Dev/Control System Tools/planning/safety_software_stack.md`) — use as reference material, not a file to modify.
