<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — safety circuits (e-stop, safety relays, monitored reset)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, safety_circuits, estop, safety_relay, safety_plc, dual_channel, monitored_reset, edm, sto, functional_safety, stop_categories, emc, grounding]
  systems: [safety_systems, control_panels, machine_control]
-->

# Wiring Practices — Safety Circuits

Distilled engineering knowledge behind the site guide "Safety Circuit Wiring —
E-Stops, Safety Relays, and Monitored Reset." Requirements are paraphrased at
chapter/article level with references; field practice not derivable from a
standard is flagged as generally accepted practice. This note covers the
**wiring** of a safety circuit whose architecture was already fixed by a risk
assessment and safety requirements specification (SRS). It links the drive-STO
content in `servo_drive_wiring.md` and the EMC content in
`emc_noise_mitigation.md` rather than re-deriving them.

## 1. The framing that governs everything (architecture is an input)

Wiring cannot create safety performance the design did not specify. The
architecture — single vs dual channel, required PL (ISO 13849-1) or SIL/SILCL
(IEC 62061), category, reset type, diagnostic coverage — is an **output of the
risk assessment and the SRS** and an **input to the wiring**. This note assumes
that upstream work is complete. Good wiring **realizes** a specified
architecture and can **defeat** it (e.g. paralleling channels, omitting
feedback), but it cannot **upgrade** a single-channel design into a
dual-channel one. Where a required value is named here it comes from the SRS,
never from this note.

## 2. Safety functions and terminal groups covered

Common safety functions realized in the panel: **emergency stop** (ISO 13850),
**guard/interlock** monitoring, and **light curtain / ESPE** trip — each fed
into a **safety relay** or **safety controller/PLC**, whose safety outputs act
on the final elements (redundant contactors, or a drive's Safe Torque Off).
Terminal groups:

* **Input devices** — e-stop NC contacts, interlock switches, ESPE OSSD
  outputs; wired as independent channels, commonly monitored by the safety
  logic's pulsed/test outputs for cross-fault detection.
* **Safety logic** — safety relay or safety PLC; performs the redundancy,
  discrepancy monitoring, and diagnostics the architecture calls for.
* **Safety outputs** — to the final elements: redundant contactors in series,
  or the drive STO inputs.
* **Feedback / EDM** — external device monitoring loop reading the
  positively-guided/mirror contacts of the contactors back into the logic.
* **Reset** — monitored (manual) or, where the risk assessment permits,
  automatic.

## 3. Dual channel as a wiring property

"Dual channel" at the wiring level means **two independent circuits** carrying
the same safety signal so that a single credible fault (a welded contact, a
short to 24 V, a broken wire) does not defeat the function and is detected.
Independence is the point: separate conductors, separate contacts, and — where
the logic supports it — separate **test/pulse sources** on each channel so a
channel-to-channel short is detected as a discrepancy. Dual-channel wiring is
necessary but not sufficient for a given PL/Cat; the achieved performance also
depends on diagnostic coverage, component reliability (MTTFd/B10d), and CCF
measures the design specifies. Generally accepted practice — verify against the
SRS and the safety-logic manual.

## 4. Device selection: safety-rated vs standard

Where the architecture requires it, devices are **safety-rated**: e-stop
actuators with **direct-opening (positively-guided) NC contacts** (IEC 60947-5-5
principle), rated interlock switches, ESPE, safety relays/controllers, and
contactors with **mirror/positively-guided** auxiliaries for EDM. A standard
relay or a pushbutton without direct-opening contacts lacks the fault behavior
the safety calculation assumes. Which parts must be safety-rated is set by the
SRS, not chosen at the panel.

## 5. Sizing and protection of the safety output circuit

* **Contact rating vs load, with backup protection.** Safety-relay/controller
  outputs have a rated making/breaking capacity and often a required **backup
  fuse** (external protection) guarding the output contacts against a load-side
  short — size the load (contactor coil inrush/seal current) to the output
  rating and fit the specified backup protection; omitting it can weld the
  output. Electromechanical and semiconductor (OSSD) outputs differ — verify
  the type against the manual.
* **Short-circuit protection of the wiring.** The safety wiring is protected
  like other control wiring (NFPA 79 Ch. 7 / IEC 60204-1); a fault must not
  both disable the function and go undetected. Coil suppression per the
  contactor manual affects drop-out time and thus stop timing.

## 6. The safety output circuit (final elements)

* **Redundant contactors in series.** The classic final element is **two
  contactors in series** on the motor/actuator supply, each driven by an
  independent safety output, so one welded contactor still leaves the load
  isolated by the other. Their **positively-guided/mirror auxiliary contacts**
  are wired into the **EDM/feedback** loop so the logic confirms both dropped
  out before allowing a reset — a welded main contact holds its mirror contact
  open and blocks reset.
* **Drive STO as the final element.** Alternatively the safety output drives a
  drive's dual-channel **Safe Torque Off** (see `servo_drive_wiring.md`). STO
  removes torque but is **not** a disconnect and **not** a brake — a loaded or
  vertical axis can still fall, and mains LOTO is still required. STO stops
  torque production; it is a stop function, not isolation (IEC 60204-1).
* Stop **category** (IEC 60204-1: 0 = immediate removal of power; 1 =
  controlled stop then removal; 2 = controlled stop, power retained) is
  specified by the design — dropping the contactors is a Cat-0 style action,
  while a Cat-1 stop sequences a drive stop before the contactors open.

## 7. Input device wiring (the core of e-stop practice)

* **Dual-channel e-stop / interlock.** Two independent NC circuits per device
  into the safety logic; the logic checks both channels agree and detects a
  discrepancy. Do **not** simply parallel two contacts — paralleling hides a
  single-contact failure (one stuck-closed path masks the other), destroying
  the fault detection the PL depends on. Series/independent channels with
  discrepancy monitoring preserve it.
* **Cross-fault detection.** The safety controller's **pulsed/test outputs**
  put distinct test patterns on each channel so a channel-to-channel short or a
  short to 24 V is detected. Using two separate test sources (one per channel)
  is what makes cross-faults visible.
* **Series-connecting multiple e-stops.** Multiple e-stops are commonly daisy-
  chained in series on each channel. This is standard, but series-connection
  **reduces achievable diagnostic coverage** (a fault-masking effect when more
  than one device is actuated / faults accumulate on a shared chain), which can
  cap the PL — the design accounts for this; verify against ISO 13849-1
  guidance and the SRS.
* **Monitored (manual) reset vs automatic reset.** With **monitored reset** the
  function does not re-enable when the e-stop is released; a **separate,
  deliberate reset action** is required, and the logic monitors the reset
  signal for a proper edge (a trailing/falling edge, so a shorted or jammed
  reset button cannot reset). Monitored reset matters because **the reset must
  not itself start the machine** — clearing the safety condition and commanding
  motion are distinct acts (IEC 60204-1 e-stop/reset principle; ISO 13850).
  Automatic reset (function re-enables on device release) is permitted only
  where the risk assessment allows it and no unexpected start-up can result.

## 8. Grounding, shielding, and earth-fault behavior

A ground fault must not defeat the function or create a dangerous state.
Safety circuits are arranged so an earth fault trips toward the safe state
rather than masking it — e.g. referencing the switched side so a fault to earth
de-energizes the load (IEC 60204-1 earth-fault/protective-bonding principle);
verify the intended behavior against the safety-logic manual and the design.
Route safety wiring away from noise (drive motor cables, switching loads) —
induced noise on OSSD/test lines can nuisance-trip or, worse, mask a
discrepancy; deep treatment owned by `emc_noise_mitigation.md`. PE terminated
per NFPA 79 Table 8.2.2.3 basis (procedure cited, values not reproduced).

## 9. Common mistakes (field-observed)

Single channel where the SRS requires dual; e-stops paralleled instead of
series/independent (loses fault detection); automatic reset where monitored
reset is required (unexpected restart); EDM/feedback loop not wired so a welded
contactor goes undetected and reset is allowed anyway; standard relay/contact
used where safety-rated/positively-guided is required; a channel bypassed
during commissioning and left jumpered; STO relied on as the e-stop stopping
means without regard to stop category, load hold, or isolation.

## 10. Verification highlights

* **Test each channel independently** — fault one channel (open it / disconnect
  it) and confirm the function still commands the safe state **and** the logic
  detects and latches the fault; repeat for the other channel.
* **Reset behavior** — confirm releasing the e-stop does not restart the
  machine and that a proper reset edge is required; confirm a held/shorted reset
  cannot reset.
* **EDM/feedback** — simulate a welded contactor (force one mirror contact) and
  confirm reset is blocked.
* Functional validation follows the machine safety validation plan and
  commissioning (ISO 13849-2 validation principle); this note covers wiring
  checks, not the full validation.

## 11. Change log

* 2026-07-11 — Initial draft (Phase 41 Wave 4); paired with
  docs/design/wiring/safety-circuit/; links servo_drive_wiring.md (STO) and
  emc_noise_mitigation.md.
