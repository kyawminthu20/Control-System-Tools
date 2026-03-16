# Phase 20: Software Safety Stack Deepening — Design Spec

**Date:** 2026-03-15
**Phase:** 20
**Status:** Approved

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

## RAG Corpus Update

File: `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md`

Add the following content blocks (append after existing material or insert into appropriate sections):

### 1. IEC 61131-3 Edition Note

Replace any reference to the 2013 edition or IL deprecation with:

> The current IEC PLC programming language standard is **IEC 61131-3:2025**, published May 22, 2025. Earlier installed bases and vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.

### 2. Normal PLC / Safety PLC / SIS Comparison Table

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

### 3. Detailed E-Stop I/O List

**Safety inputs:**
- `SI_ESTOP_CH1`: E-stop channel 1, NC
- `SI_ESTOP_CH2`: E-stop channel 2, NC
- `SI_RESET_PB`: manual reset pushbutton, NO
- `SI_K1_FB`: contactor K1 feedback auxiliary contact, NC when de-energized
- `SI_K2_FB`: contactor K2 feedback auxiliary contact, NC when de-energized

**Safety outputs:**
- `SO_K1`: safety output to contactor K1 coil
- `SO_K2`: safety output to contactor K2 coil

**Standard PLC / HMI read-only status tags:**
- `ESTOP_ACTIVE`, `SAFETY_OK`, `RESET_REQUIRED`, `FEEDBACK_FAULT`, `CHANNEL_FAULT`
- `MOTOR_RUN_CMD`, `MOTOR_RUNNING`

### 4. Sequence of Operation

**Normal start:**
1. E-stop released, both NC channels closed and healthy.
2. Both contactor feedbacks indicate de-energized / ready state.
3. Operator presses Reset.
4. Safety PLC validates channels and feedback, then enables SO_K1 and SO_K2.
5. Standard PLC may now start the motor if normal run conditions are met.

**E-stop pressed:**
1. One action opens both NC channels simultaneously.
2. `ESTOP_HEALTHY` drops immediately.
3. `SAFETY_ENABLE` clears.
4. SO_K1 and SO_K2 de-energize.
5. Contactors open and remove power to the motor.
6. HMI logs E-stop event; shows reset required.

**After E-stop release:**
1. Channels may return healthy.
2. Safety outputs remain off — no auto-restart.
3. Manual reset is still required.
4. If feedback is wrong or channels disagree, reset is rejected.

**Welded contactor fault:**
1. E-stop is pressed or stop is demanded.
2. One contactor fails to open; feedback does not match expected state.
3. `FEEDBACK_OK` goes false.
4. Reset is blocked and fault is logged.

### 5. Documentation Checklist for E-Stop

- Hazard and risk assessment result, including required PLr or SIL
- Safety function statement (e.g., "Pressing E-stop removes motor torque within X ms")
- Safe state definition
- Reset philosophy: manual reset, no automatic restart
- Wiring and I/O mapping for both channels, feedbacks, and outputs
- Hardware list with safety-rated device part numbers and certifications
- Logic mapping: which safety blocks/rungs implement the function
- Verification and validation test records
- Fault tests: single-channel open, short between channels, welded contactor, feedback failure, power cycle, module fault
- Change control: version, who approved, what changed, retest evidence

### 6. Logging Checklist for E-Stop

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

### 7. Rockwell GuardLogix Vendor Pattern

**Typical safety tags:**
- `EStop_A`, `EStop_B` — E-stop dual-channel inputs
- `PB_Reset`, `PB_FaultReset` — reset pushbuttons
- `K1_FB`, `K2_FB` — contactor feedback
- `SafeIn_CombinedStatus`, `SafeOut_CombinedStatus` — Guard I/O status
- `ESTOP_E1` — ESTOP instruction backing tag
- `CROUT_M1` — CROUT instruction backing tag

**Rung structure:**

```text
Rung 1
ESTOP(ESTOP_E1, ResetType:=1, ChannelA:=EStop_A, ChannelB:=EStop_B,
      CircuitReset:=PB_Reset, FaultReset:=PB_FaultReset)

Rung 2
OSF(PB_Reset, PB_Reset_OSF)

Rung 3
CROUT(CROUT_M1, Actuate:=ESTOP_E1.O1, Feedback1:=K1_FB, Feedback2:=K2_FB,
      InputStatus:=SafeIn_CombinedStatus, OutputStatus:=SafeOut_CombinedStatus,
      Reset:=PB_Reset_OSF)

Rung 4
SO_K1 := CROUT_M1.O1
SO_K2 := CROUT_M1.O2
```

**What to log:**
- `ESTOP_E1.FP`, `ESTOP_E1.II`, `ESTOP_E1.CRHO`
- `CROUT_M1.FP`, `CROUT_M1.FaultCode`
- Safety signature / download / change events from controller audit trail

**Official references:**
- Rockwell ESTOP instruction: Studio 5000 Logix Designer safety instructions
- Rockwell CROUT instruction: Studio 5000 Logix Designer safety instructions
- GuardLogix 5580 safety status monitoring guide

### 8. Siemens S7-1500F / ET200SP Vendor Pattern

**Typical safety tags:**
- `fdiEstopGlobal` — F-DI dual-channel evaluated E-stop signal
- `DataToSafety.Acknowledge` — standard-to-safety acknowledge crossing
- `DataFromSafety.EstopAckReq` — safety-to-standard status crossing
- `fdiK1Fb`, `fdiK2Fb` — contactor feedback inputs
- `qSafetyK1`, `qSafetyK2` — safety output signals to contactors
- `qSafetyK1_VS`, `qSafetyK2_VS` — F-DO value status bits

**F-program network structure:**

```text
Network 1 — GlobalEstop : ESTOP1
  E_STOP  := fdiEstopGlobal
  ACK_NEC := TRUE
  ACK     := DataToSafety.Acknowledge

Network 2 — FbK1 : FDBACK
  ON       := GlobalEstop.Q
  FEEDBACK := fdiK1Fb
  QBAD_FIO := qSafetyK1_VS
  ACK_NEC  := TRUE
  ACK      := DataToSafety.Acknowledge
  FDB_TIME := T#500ms
  Q        := qSafetyK1

Network 3 — FbK2 : FDBACK
  ON       := GlobalEstop.Q
  FEEDBACK := fdiK2Fb
  QBAD_FIO := qSafetyK2_VS
  ACK_NEC  := TRUE
  ACK      := DataToSafety.Acknowledge
  FDB_TIME := T#500ms
  Q        := qSafetyK2

Network 4 — AckGlobal : ACK_GL
  ACK_GLOB := DataToSafety.Acknowledge
```

**What to log:**
- `GlobalEstop.ACK_REQ`, `GlobalEstop.DIAG`
- `FbK1.ERROR`, `FbK1.ACK_REQ`, `FbK1.DIAG`
- `FbK2.ERROR`, `FbK2.ACK_REQ`, `FbK2.DIAG`
- F-I/O passivation and reintegration events
- Safety compile / download / signature / mode change events

**Official references:**
- Siemens ESTOP1 / FDBACK / ACK_GL: S7-1500F programming manual (Industry Online Support)
- Siemens feedback monitoring application example (support article 21331098)
- Siemens safety programming guideline (support article 109750255)

---

## Site Page Update (`docs/software-stack/index.md`)

### Change 1: IEC 61131-3 edition note

In the "PLC Language Standard vs Safety Claim Standard" section, replace:

> Verify the applicable edition and the actual vendor platform in use. Older materials, installed bases, and current controller ecosystems may not expose the same language set in the same way.

With:

> The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and current vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation.

### Change 2: Add Normal PLC / Safety PLC / SIS comparison table

New `## Normal PLC vs Safety PLC vs SIS` section, inserted after "PLC Language Standard vs Safety Claim Standard" and before "What Traceability and Logging Mean in Practice". Contains the comparison table from the RAG section above.

### Change 3: Expand Worked E-Stop section

Replace the existing brief "Worked E-Stop Pattern" section with a full section containing:

1. Architecture bullet list (unchanged)
2. Rung pseudocode (unchanged)
3. I/O list (from RAG section 3 above)
4. Wiring/architecture Mermaid diagram (`flowchart LR`: Field Devices → Safety PLC → Power Circuit; Standard PLC/HMI reads status only)
5. State diagram (`stateDiagram-v2`: SafeStopped → ReadyForReset → SafetyEnabled → Running → Faulted)
6. Sequence of operation (4 scenarios as compact numbered lists)
7. Documentation checklist
8. Logging checklist

### Change 4: Add vendor-specific patterns

New `### Vendor-Specific Patterns` subsection at the end of Worked E-Stop, using two `<details>` expandable blocks:
- `<summary>Rockwell GuardLogix</summary>` — tags, rung pseudocode, what to log
- `<summary>Siemens S7-1500F / ET200SP</summary>` — tags, F-program pseudocode, what to log

Both blocks include a trust-boundary note: "Instruction names and operands are vendor-specific. Verify against the applicable vendor documentation for the installed platform version."

---

## Trust Boundary

- No copyrighted standards text is reproduced
- Vendor instruction names are stated as they appear in official public documentation (referenced by document title, not reproduced in full)
- All SIL/PL claims remain explicitly deferred to the published standards
- The page retains its existing trust-boundary note

---

## Acceptance Targets

- RAG file reflects the richer content from `planning/safety_software_stack.md`
- `/software-stack/` answers "when is ladder logic safety-related?", "what must be traceable?", "what should be logged?" without requiring the user to navigate away
- The Normal PLC / Safety PLC / SIS comparison table is visible without expanding any `<details>` block
- Vendor-specific patterns are available but do not dominate the page for users who don't need them
- Jekyll build remains clean, page count unchanged (no new pages)
- All existing cross-links remain intact

---

## Files Changed

| File | Action |
|---|---|
| `control-standards/rag/standards_intelligence/reference_models/Software_Safety_and_Intrinsic_Safety_Standards.md` | Modify — append comparison table, E-stop detail, vendor patterns, edition note |
| `docs/software-stack/index.md` | Modify — add edition note, comparison table section, expanded E-stop section with Mermaid diagrams and vendor `<details>` blocks |
