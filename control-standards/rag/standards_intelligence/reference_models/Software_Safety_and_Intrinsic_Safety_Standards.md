<!--
AI_READ_ACCESS: ALLOWED
CONTENT_CLASS: RAG_APPROVED
STATUS: DRAFT
-->

# Software Safety, PLC Languages, Traceability, and Intrinsic Safety Routing

## Purpose

This guide routes standards questions about PLC programming languages, safety-related software lifecycle, safety-related ladder logic, redundancy, traceability, logging, cybersecurity, wiring, and intrinsically safe field I/O.

It is a standards-selection and implementation-boundary guide. It does **not** replace the purchased standards, vendor safety manuals, hazard analyses, SIL or PL calculations, or hazardous-area installation drawings.

## Scope Boundary

- `IEC 61131-3` is a PLC programming language standard. It does **not** by itself create a SIL or PL claim.
- `SIL` and `PL` claims apply to the full safety function chain: sensors, logic solver, software, final elements, diagnostics, proof-test assumptions, and the defined safe state.
- Safety-related software requirements are driven by lifecycle standards, verification, validation, and change control, not just by the fact that the code is written in Ladder Diagram, Structured Text, or Function Block Diagram.
- Redundancy, diagnostics, and sensor count are architecture decisions tied to target risk reduction, common-cause exposure, response time, proof-test interval, and tolerated nuisance trips.
- Detailed SIL allocation rules, hardware fault-tolerance tables, proof-test equations, common-cause scoring methods, and intrinsic-safety entity or system calculations are NOT FOUND IN LOCAL CORPUS - TO VERIFY against the purchased standards.

## Quick Answers

### When does ladder logic become safety-related?

Normal machine sequencing, interlocks for production, timers, conveyors, recipes, and general automation logic do **not** automatically become safety-related just because they are written in ladder.

If the ladder logic performs a safety function such as an emergency stop, guard monitoring, safe torque off permission, burner trip, or credited shutdown, then the software becomes part of a safety-related control system and must follow the applicable lifecycle and validation requirements.

### Does safety logic always require duplicated logic or hardware?

No. The standards do not say "always use dual redundancy." They drive architecture through required risk reduction, diagnostics, fault tolerance, category or subsystem behavior, proof-test assumptions, and fault response.

### Is traceability expected for safety-related logic?

Yes. Traceability is expected when the logic is part of a safety function. In practice, that means linking the hazard or requirement to the safety function, the implemented logic, the test evidence, and the installed validated version.

### Does logging mean logging every rung on every scan?

No. Safety-related logging is usually event-based. The system normally logs downloads, edits, mode changes, faults, trips, resets, bypasses, overrides, and security-relevant events. It does **not** usually mean recording every rung transition forever.

## Fast Routing

| If the question is about... | Start with... | Add... |
| --- | --- | --- |
| Machinery safety PLC software | `IEC 62061` or `ISO 13849-1/-2` | `ISO 12100`, `IEC 60204-1`, and `NFPA 79` or `NEC` where jurisdiction applies |
| Process or chemical shutdown software | `IEC 61511` | `IEC 61508-2/-3/-6` for lifecycle and architecture depth |
| Generic safety-related software lifecycle | `IEC 61508-3` | `IEC 61508-2/-6` for subsystem architecture and diagnostics |
| PLC programming language and code structure | `IEC 61131-3` | A safety lifecycle standard if any safety claim is made |
| Secure PLC or controller software development | `IEC 62443-4-1` | `IEC 62443-4-2` and `IEC 62443-3-3` for component and system security requirements |
| Redundancy, voting, or sensor count | `IEC 61508-2/-6`, `IEC 61511`, `IEC 62061`, or `ISO 13849-1/-2` | Device safety manuals and proof-test assumptions |
| Cable routing and shielding for machinery | `IEC 60204-1`, `NFPA 79`, `NEC`, and `UL 508A` | EMC, motion, and environmental requirements |
| Intrinsically safe loops or associated apparatus | `IEC 60079-11`, `IEC 60079-14`, and `IEC 60079-25` | US hazardous-location code and listing path if the installation is in the US |

## PLC Language Standard vs Safety Claim Standard

Use `IEC 61131-3` for PLC language definitions and software structure questions such as:

- Ladder Diagram,
- Function Block Diagram,
- Structured Text,
- Sequential Function Chart,
- coding conventions,
- project structure,
- and language suitability for the task.

The current edition is **IEC 61131-3:2025**, published May 2025. Older installed bases and vendor platforms may implement earlier editions. Verify the edition in use against the applicable vendor platform documentation. Language availability and deprecated features can differ between older materials, current editions, and installed controller ecosystems.

If the code is part of a safety function, pair the language standard with:

- `IEC 62061` or `ISO 13849-1/-2` for machinery safety functions, or
- `IEC 61511` with `IEC 61508-3` for process-industry shutdown or protection functions.

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

## Safety-Related Software Routes

### Generic foundation

Use `IEC 61508-3` when the question is the software lifecycle itself: software safety requirements, architecture, implementation methods, verification, validation, modification control, supporting tools, and evidence.

Use `IEC 61508-2` and `IEC 61508-6` with it when the question moves from software alone into redundancy, diagnostics, subsystem behavior, voting logic, proof-test assumptions, or hardware-software interaction.

### Machinery route

For machinery, use:

- `ISO 12100` for risk assessment,
- `ISO 13849-1/-2` for the Performance Level route, or
- `IEC 62061` for the machinery SIL route,
- with `IEC 60204-1` and `NFPA 79` handling the electrical implementation layer.

Machinery projects usually do **not** start with `IEC 61511`. They start with `ISO 13849` or `IEC 62061` depending on whether the project is taking the PL or machinery SIL route.

### Process route

For process skids, chemical systems, petroleum systems, burner management, and other credited shutdown functions, use `IEC 61511` on top of `IEC 61508`.

This is the correct route when the safety function is maintaining a safe process state, preventing loss of containment, or acting as a plant protection layer rather than simply stopping machine motion.

## Traceability, Change Control, and Logging

For safety-related logic, traceability usually means:

- hazard or risk assessment result -> safety function definition,
- safety function definition -> I/O mapping, logic, reset behavior, and fault response,
- code version -> verification and validation results,
- code change -> approval, review, and retest evidence,
- installed version -> commissioning, proof test, or periodic validation record.

### Typical logged events

The system normally logs important events such as:

- safety program downloads and online edits,
- controller mode changes,
- trips and shutdowns,
- resets and reset attempts,
- bypasses, inhibits, forces, and overrides,
- channel discrepancy or module fault events,
- contactor or final-element feedback mismatch,
- user access and security-relevant events when the controller is networked.

That logging often lives in the safety PLC diagnostics, controller audit trail, HMI, historian, or SCADA layer rather than in every rung itself.

### What usually does not need logging

It usually does **not** mean:

- every rung state on every PLC scan,
- every internal bit transition forever,
- or all normal non-safety sequence activity unless it is needed for incident analysis or troubleshooting.

## Redundancy and Architecture Selection

The standards do not provide one universal answer such as "always use two sensors" or "always duplicate the ladder."

Instead, they drive architecture decisions through:

- target `SIL` or `PL`,
- category, fault tolerance, or subsystem behavior,
- diagnostic coverage,
- common-cause exposure,
- proof-test interval,
- response time,
- spurious-trip tolerance,
- environmental constraints,
- and any hazardous-area classification.

Typical architecture patterns include:

- single-channel with diagnostics,
- dual-channel inputs,
- monitored contactor feedback,
- redundant outputs,
- cross-monitoring,
- `1oo1`, `1oo2`, or `2oo3` voting,
- and separate safety CPU or safety task partitions.

The correct pattern must be justified by the safety requirements and the applicable lifecycle standard.

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

### Safety-ladder intent (7 rungs)

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

Note on Rung 5: SAFETY_ENABLE self-seals implicitly — as long as ESTOP_HEALTHY, FEEDBACK_OK, and no CHANNEL_FAULT remain true after reset, SAFETY_ENABLE stays true on the next scan without RESET_VALID. In a physical ladder implementation, an explicit OR branch (RESET_VALID OR SAFETY_ENABLE) makes the latch visible.

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

## Secure Development and Cybersecurity

Use `IEC 62443-4-1` when the question is secure product development for industrial automation and control components. This is the secure-development-lifecycle route for PLC or controller software products.

Use `IEC 62443-4-2` and `IEC 62443-3-3` when the question moves into technical security requirements for components and systems, including accounts, communications, hardening, remote access, and system security levels.

This cybersecurity family complements functional safety. It does **not** replace `IEC 61508`, `IEC 61511`, `IEC 62061`, or `ISO 13849`.

## Wiring, Segregation, and Electrical Implementation

For machine or panel wiring, use:

- `IEC 60204-1`,
- `NFPA 79`,
- `NEC`,
- and `UL 508A` where listing applies.

These standards route questions about:

- conductor sizing,
- insulation rating,
- mechanical protection,
- separation between power and signal conductors,
- bonding and shielding,
- external-source marking,
- and cable support in fixed and flexing applications.

The local corpus already contains usable routing content for this layer in:

- `us/nfpa79/NFPA79_2024__Ch16__wiring_methods.md`
- `us/nec/NEC_2023__Art300__general_wiring_methods.md`
- `international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause08__equipotential_bonding.md`
- `international/machinery/iec_60204_1/IEC60204_1_2016A1__Clause09__control_circuits_and_functions.md`

## Intrinsic Safety and Hazardous-Area IO

Intrinsic safety is not a generic software certification topic. It is an equipment, system, and installation discipline.

Use:

- `IEC 60079-11` for intrinsically safe apparatus,
- `IEC 60079-14` for design, selection, and erection of hazardous-area installations,
- `IEC 60079-25` for intrinsically safe electrical systems.

For US projects, also verify the listing and code path, typically through the applicable hazardous-location articles and the relevant UL standards such as `UL 60079-11`. Panel or associated-apparatus requirements may also route through `UL 698A` depending on the product and enclosure basis.

When intrinsically safe loops are used, the project normally needs:

- certified associated apparatus or isolators,
- hazardous-area and gas-group compatibility,
- temperature-class compatibility,
- loop or entity parameter checks,
- cable parameter checks,
- and controlled installation drawings.

Those detailed calculations and approval rules are NOT FOUND IN LOCAL CORPUS - TO VERIFY.

## Minimum Implementation Deliverables

When safety-related PLC software or intrinsically safe I/O is in scope, the project should expect at least:

- a safety requirements specification,
- hazard or risk documentation that establishes the target integrity,
- I/O and cause-and-effect documentation,
- software architecture showing safety and standard partitions,
- an approved list of permitted languages and function blocks,
- change control and version history,
- verification and validation records,
- proof-test procedures,
- cybersecurity design records where the controller is networked,
- and intrinsic-safety loop drawings where hazardous-area I/O is used.

## Local Corpus Status

- The local corpus already supports the electrical implementation layer through `IEC 60204-1`, `NFPA 79`, `NEC`, and `UL 508A`.
- The local corpus already supports the separation principle between standard PLC control and safety control.
- The local corpus does **not** yet contain detailed clause-level modules for `IEC 61508`, `IEC 61511`, `IEC 62061`, `ISO 13849`, `IEC 61131-3`, `IEC 62443-4-1`, or the `IEC 60079` family.
- For official purchase and current public pricing, see `STANDARDS_PURCHASE_TRACKER.md`.
