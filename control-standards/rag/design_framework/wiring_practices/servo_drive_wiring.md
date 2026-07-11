<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — servo drives (power, motor, feedback, STO, brake)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, drives, servo, feedback, sto, functional_safety, holding_brake, emc, grounding, motor_circuits]
  systems: [motion_control, drive_systems, control_panels, safety_systems]
-->

# Wiring Practices — Servo Drives

Distilled engineering knowledge behind the site guide "Servo Drive Wiring —
Power, Motor, Feedback, STO, and Brake." Requirements are paraphrased at
chapter/article level with references; field practice not derivable from a
standard is flagged as generally accepted practice. This note builds on the
VFD note (`vfd_wiring.md`) and covers only what differs for a servo axis;
shared power/shielding/reflected-wave content is not re-derived here.

## 1. What makes a servo different from a VFD

A servo axis is a **closed-loop** motion system: drive + motor + real-time
position/velocity **feedback**, usually a **holding brake**, and usually an
integrated **Safe Torque Off**. A VFD is typically open-loop speed control of
an induction motor. Wiring consequences: the feedback loop is a wiring group
of its own and the circuit most likely to cause faults; servos run high
**peak** torque (several times continuous), so the motor circuit is sized on a
continuous/peak pair, not a single FLA; and drive, motor, and feedback are a
**matched set**, normally one vendor, commissioned as a unit (commutation
offset, autotune).

## 2. Terminal groups

* **Mains / DC-bus** — supply from the branch-circuit OCPD, plus DC-bus
  terminals for multi-axis bus sharing and regen/brake-resistor connection;
  stored-energy hazard.
* **Motor power** — PWM output to the servo motor; noisy, shielded, treated
  like the VFD load side.
* **Feedback** — resolver, incremental/absolute encoder, or single-cable
  digital protocol; signal-level, shielded, the core servo circuit.
* **STO / safety** — dual-channel Safe Torque Off inputs to the safety system.
* **Holding brake** — typically 24 V to a motor-mounted brake; can draw
  significant current.
* **Control / network** — enable, references, and the motion fieldbus
  (EtherCAT, PROFINET/IRT, SERCOS, etc.).

Terminal designations, torque values, wire ranges, feedback pinouts, and
cable-length limits are vendor-specific — taken from the drive and motor
manuals, never generalized.

## 3. Matched-set and cable-system decisions (upstream of wiring)

* **Drive–motor–feedback matching:** selected together; drive firmware must
  support the motor's feedback type. Confirm against the manuals before wiring
  — a mismatched feedback device will not commutate.
* **Single-cable vs two-cable:** digital-feedback families offer a
  *single-cable* solution (power + feedback in one hybrid cable to vendor
  rules) or separate power + feedback cables. Which is permitted, and the
  in-cable segregation rules, are vendor-defined.
* **Cable lengths:** maximum motor and feedback lengths are set by the
  drive/feedback system, not a universal number — feedback protocols have hard
  length limits. Consult the manual.
* **Regen / shared DC bus:** multi-axis machines commonly share a DC bus so
  one axis's regenerated energy feeds another; excess is dumped in a braking
  resistor or regen unit. Bus-sharing, fusing, and same-family rules are
  vendor-defined.

## 4. Sizing and protection (NEC Art. 430 Part X, NFPA 79 Ch. 6)

* **Mains input protection:** conductors and OCPD sized to the drive's **rated
  input current** and to the drive listing, same discipline as a VFD (NEC
  430.122; listed OCPD type/rating governs SCCR — NFPA 79 Ch. 6, UL 508A).
  `cst motor-branch` computes the conventional motor branch chain.
* **Motor-cable sizing:** size to the servo motor's **continuous** current,
  then verify the cable and terminations tolerate the **peak** current the
  drive can command — servo peak runs several times continuous. The drive
  manual states continuous/peak ratings and any min/max cross-section.
* **DC-bus / regen protection:** shared-bus links and braking-resistor
  circuits carry high energy — protect and thermally monitor per the manual;
  the resistor thermal switch wires into the control/safety chain.
* **STO is not overcurrent protection.** Safe Torque Off removes torque
  capability; it does not protect conductors and is not a substitute for
  branch-circuit or motor protection. Distinct functions.

## 5. Power wiring practice (shared with the VFD)

* Shielded servo motor-power cable, **360-degree shield termination at both
  ends** — same reasoning as the VFD motor cable (`vfd_wiring.md`): a pigtail
  defeats the shield at PWM frequencies. Reflected-wave/lead-length stress
  applies as on a VFD (vendor thresholds and remedies).
* Keep motor power away from the feedback cable. In a two-cable system route
  them apart; in a single-cable/hybrid system segregation is engineered inside
  the cable to vendor rules — follow those rules, don't improvise.
* **DC-bus link wiring** (multi-axis): short per-vendor bus bars/cables,
  correct polarity and fusing. **Regen/brake-resistor** wiring is a
  high-energy switched circuit — short, shielded/twisted, away from control
  and feedback wiring.

## 6. Feedback and safety wiring (the core servo content)

* **Feedback cable:** use the specified cable (resolver, encoder, or
  single-cable digital). Ground the feedback shield per the manual. Never
  route feedback with motor power beyond the single-cable rules — motor-cable
  coupling into feedback is the classic servo position fault.
* **STO (Safe Torque Off):** typically **dual-channel** inputs to a safety
  relay/controller as part of a rated safety function (ISO 13849-1 /
  IEC 62061). STO removes torque (a Category-0 style stop, IEC 60204-1) but is
  **not a brake** — a vertical/loaded axis can still drop — and **not galvanic
  isolation**: not a maintenance disconnect, mains LOTO still required. PL/SIL
  determination belongs to the functional-safety material and the planned
  safety-circuit guide.
* **Holding brake:** typically 24 V, **fail-safe** (spring-applied,
  electrically released), exists to *hold* a stopped axis — **not a safety
  stop** and not rated to decelerate a moving load repeatedly. Sequence
  release with enable (drive holds before brake releases, brake re-applies
  before enable drops); wrong order drops or jerks the axis. Provide coil
  suppression per the manual; brake current can be significant.

## 7. Grounding, shielding, EMC (NFPA 79 Ch. 8; IEC 60204-1)

Servo drives are aggressive EMC sources; deep treatment owned by the EMC
guide. HF grounding of drive and motor: the motor-cable shield/ground is the
dedicated high-frequency return to the drive PE; feedback shield grounded per
the manual. PE terminated first, sized per NFPA 79 Table 8.2.2.3 basis
(procedure cited, values not reproduced). Feedback corruption from motor-cable
coupling is the signature servo EMC fault — separation and shield integrity on
the feedback path are decisive.

## 8. Verification highlights

* Feedback reads position/velocity cleanly before torque is enabled;
  commutation/phasing/autotune are commissioning steps.
* STO functional test: both channels remove torque, channel mismatch detected.
* Brake sequencing test: axis holds through release/apply with no drop or jerk.
* Insulation-resistance testing follows the VFD rule — never megger through a
  connected drive.

## 9. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with
  docs/design/wiring/servo-drive/; builds on vfd_wiring.md.
