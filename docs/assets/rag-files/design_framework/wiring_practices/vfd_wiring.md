<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — variable frequency drives (VFDs)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, drives, vfd, emc, grounding, motor_circuits]
  systems: [motor_control, drive_systems, control_panels]
-->

# Wiring Practices — Variable Frequency Drives

Distilled engineering knowledge behind the site guide "How to Wire a VFD."
Requirements are paraphrased at chapter/article level with references;
field practice not derivable from a standard is flagged as generally
accepted practice.

## 1. Terminal groups

A VFD presents four distinct wiring zones, each with different rules:

* **Line side (input)** — three-phase supply from the branch-circuit OCPD.
* **Load side (output)** — PWM output to the motor; the noisiest circuit in the panel.
* **Control terminals** — 24 V digital I/O, analog reference, relay outputs, safety (STO) inputs, fieldbus.
* **DC bus / brake terminals** — DC link access and braking resistor/chopper connections; stored-energy hazard.

Terminal designations, torque values, and wire-range limits are vendor-specific — always taken from the drive manual, never generalized.

## 2. Sizing and protection (NEC Art. 430 Part X, NFPA 79 Ch. 6 and Ch. 12)

* **Input conductors:** NEC 430.122 requires ampacity of at least 125% of the
  drive's **rated input current** — not the motor current. The drive input
  current governs because the drive, not the motor, is the load on the branch
  circuit.
* **FLA vs FLC discipline (NEC 430.6 principle):** branch-circuit conductor
  and OCPD sizing for motor circuits uses the NEC full-load current tables
  (Tables 430.247–430.250), while overload settings use the motor nameplate
  FLA. For a VFD circuit the drive-rated input current takes over the
  conductor-sizing role, but the FLA/FLC distinction still matters for the
  overload function and any bypass circuit.
* **Branch-circuit short-circuit/ground-fault protection:** the drive's
  listing typically specifies the permitted OCPD type and maximum rating
  (often specific fuse classes, sometimes specific breakers). Deviating from
  the listed combination can invalidate the drive's SCCR contribution and the
  panel's marked SCCR (NFPA 79 Ch. 6; UL 508A SCCR methodology).
* **Motor overload:** NEC Article 430 Part X addresses overload protection
  for adjustable-speed drive systems — a listed drive with an integral
  electronic overload typically serves as the motor overload device, so a
  separate OL relay is usually unnecessary. Verify against the current NEC
  edition and the drive listing; multi-motor (one drive, several motors)
  arrangements still need individual overloads.
* **Disconnecting means:** a disconnect within sight of the drive/controller
  location is required (NEC Art. 430 Part IX/X provisions; NFPA 79 Ch. 5).
* **Output conductors:** sized for the motor circuit per Art. 430; the drive
  manual may impose minimum/maximum cable cross-sections and lengths.

## 3. Power wiring practice

* **Segregation:** input and output power wiring routed apart; output (PWM)
  cable never bundled with input, control, or signal wiring. Generally
  accepted practice — verify for your installation.
* **Motor cable:** shielded, symmetrical VFD-rated cable (three phase
  conductors plus symmetrical ground conductors under a continuous shield)
  supports the bonding intent of NFPA 79 Ch. 8 and mitigates bearing currents
  and radiated noise (NFPA 79 Ch. 12 notes specialized VFD cabling).
* **Shield termination:** 360-degree (gland or clamp) termination at **both**
  ends of the motor cable — drive end and motor end — is the drive-vendor
  consensus. Pigtail terminations largely defeat the shield at PWM
  frequencies. Generally accepted practice — verify against the drive EMC
  installation instructions.
* **Lead length / reflected wave:** long motor leads cause voltage
  overshoot at the motor terminals (reflected-wave effect). Thresholds and
  remedies (dV/dt filter, sine filter, output reactor) are vendor- and
  voltage-class-specific — taken from the drive manual, not from a universal
  number.
* **Braking resistor:** wiring is a high-energy, PWM-switched circuit —
  short, shielded or twisted runs, routed away from control wiring; resistor
  thermal contact wired into the control/safety chain. Generally accepted
  practice plus vendor manual.

## 4. Control wiring practice

* Separate 24 V digital I/O, analog reference (screened, 0–10 V / 4–20 mA),
  and relay wiring; keep analog screens grounded per the drive manual
  (commonly drive end only for low-frequency signal screens).
* Do not mix drive I/O common with other system commons without checking the
  drive's internal reference topology (PNP/NPN, isolated vs non-isolated).
* STO wiring exists on most modern drives; its design belongs to the safety
  function (ISO 13849-1 / IEC 62061) and is covered in the safety and servo
  material, not here.

## 5. Grounding, shielding, EMC (NFPA 79 Ch. 8; IEC 60204-1)

* PE conductor terminated first, sized per NFPA 79 Table 8.2.2.3 basis
  (largest upstream OCPD) — procedure cited, values not reproduced.
* The motor-cable ground/shield provides the dedicated high-frequency return
  path back to the drive PE terminal; the building ground path alone is not
  sufficient for PWM common-mode current. Generally accepted practice.
* EMC filter (integral or external) grounded by wide, short bonds to the
  mounting plate; painted surfaces masked or scraped at bond points.
* Common-mode noise and bearing-current mitigation (insulated bearings,
  shaft-grounding rings, common-mode chokes) are generally accepted practice
  for larger machines — verify per drive and motor vendor guidance.
* Separation distances from signal/network cabling: owned by the EMC guide;
  drive output cable is the worst offender for parallel copper-Ethernet runs.

## 6. Verification highlights

* Insulation-resistance test the motor and motor cable **before** connecting
  the drive output — a megger applied through a connected drive damages the
  output stage. Generally accepted practice, universally stated by vendors.
* Capacitor discharge: NFPA 79 Ch. 7 requires stored energy discharged below
  the shock threshold within a stated time or a warning label with wait time
  — always observe the drive's marked wait time before touching terminals.
* Rotation check via low-speed bump under drive control, not by swapping
  leads under power.

## 7. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/vfd/.
