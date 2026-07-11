<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — motor starters (DOL, reversing, star-delta)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, motor_control, starters, contactors, overload, interlocks]
  systems: [motor_control, control_panels]
-->

# Wiring Practices — Motor Starters

Distilled engineering knowledge behind the site guide "Motor Starter Wiring —
DOL, Reversing, and Star-Delta." Requirements are paraphrased at
chapter/article level with references; field practice not derivable from a
standard is flagged as generally accepted practice.

## 1. What a starter is, and the three configurations

An across-the-line (electromechanical contactor) starter is the classic
alternative to a VFD: it switches the motor directly onto the line, so the
motor runs at fixed speed and takes full inrush at start. It is simpler,
cheaper, and more rugged than a drive, but gives no speed control and no soft
start. The three configurations covered here:

* **DOL (direct-on-line):** one contactor connects all three phases straight
  to the motor. Full starting inrush (typically 6–8× FLA, motor-dependent).
* **Reversing:** two contactors, one for each phase sequence; energizing
  either selects rotation direction. Requires interlocking so both can never
  close together.
* **Star-delta (wye-delta):** a reduced-voltage starter using three
  contactors (main, star, delta) plus a timer; starts the windings in star to
  cut inrush, then transitions to delta for run. For larger motors where DOL
  inrush is unacceptable to the supply or mechanics.

Terminal designations, coil voltages, contactor/overload catalog numbers,
and torque values are vendor-specific — always from the manufacturer's data,
never generalized.

## 2. Terminal groups

* **Power (line/load):** three-phase line in, motor leads out, switched
  through the contactor main poles. Star-delta and reversing route these
  through more than one contactor.
* **Control (coil circuit):** the low-power ladder circuit that energizes the
  contactor coil(s) — start/stop, seal-in, interlocks, timer, overload
  auxiliary contact. Commonly fed from a control power transformer (CPT).
* **Overload:** the thermal or electronic overload relay in series with the
  motor power leads, with its auxiliary (normally-closed) contact wired into
  the coil circuit.

## 3. Sizing and protection — the Article 430 chain

The fundamental NEC Article 430 distinction applies to a starter exactly as
to any motor circuit: **branch-circuit short-circuit/ground-fault protection
and motor overload protection are two separate devices doing two separate
jobs.**

* **Branch-circuit short-circuit/ground-fault protection (OCPD):** a fuse or
  breaker sized to protect the *wiring* against short-circuit and
  ground-fault currents. Sized separately from — and larger than — the
  overload, because it must let starting inrush pass without tripping
  (NEC Art. 430 Part IV principle). `cst motor-branch` computes the
  conventional motor-branch chain; conductor sizing follows the
  wire-sizing workflow.
* **Motor overload (running overcurrent):** the thermal or electronic
  overload relay protects the *motor* against sustained running overcurrent,
  sized to the motor nameplate FLA and service factor (NEC Art. 430 Part III
  principle). It is not sized to the breaker or the wire.
* **The distinction restated:** the OCPD protects the conductors against a
  fault; the overload protects the motor against overload. One cannot do the
  other's job — a breaker large enough to pass inrush will never protect the
  motor from a locked-rotor or overload condition, and an overload sized to
  the motor will not clear a bolted fault.
* **Contactor and overload sizing basis:** contactors are rated by
  utilization category — **AC-3** for squirrel-cage motor starting/running
  (breaking running current), **AC-4** for plugging/inching/reversing duty
  (breaking locked-rotor current), a much more severe duty. Size the
  contactor and overload to the motor FLA and the actual duty from the
  manufacturer's tables; a contactor adequate for AC-3 may be undersized for
  AC-4 reversing service. Concept-level only — consult the manufacturer
  tables for the actual ratings.
* **SCCR:** the starter *combination* (OCPD + contactor + overload) has a
  short-circuit current rating that must equal or exceed the available fault
  current at its location. The combination's SCCR is established per the
  UL 508A methodology and depends on the specific device pairing — verify the
  combination against the panel's SCCR documentation, do not assume it.
* **Reduced-voltage choice:** DOL is simplest but imposes full inrush;
  star-delta (or other reduced-voltage methods) cuts starting current for
  large motors where the supply, generator, or driven mechanics cannot
  tolerate DOL inrush. The starting-method decision is an upstream design
  choice driven by motor size, supply stiffness, and load.

## 4. Power wiring practice

* **DOL:** line to contactor main poles, load side through the overload to
  the motor. Straightforward three-phase.
* **Star-delta:** both ends of each motor winding are brought out (six leads).
  The main and star contactors energize first (windings in star ~58% of line
  voltage); after the timer, the star contactor drops out and the delta
  contactor closes (windings across full line voltage). Standard star-delta is
  **open-transition** — the motor is briefly disconnected during the changeover,
  producing a current/torque surge as it re-connects. Correct lead
  identification and contactor sequencing are essential; miswiring can short
  windings or reverse a phase.
* **Reversing:** two contactors feed the motor with two phases swapped between
  them. If both close simultaneously the swapped phases create a direct
  **phase-to-phase short** across the line. Reversing power wiring is therefore
  only safe with interlocks (section 5).

## 5. The control circuit

* **Start/stop with seal-in (holding contact):** the fundamental ladder rung
  — a momentary start pushbutton energizes the coil; a normally-open auxiliary
  contact of that contactor wired in parallel with the start button "seals in"
  (holds) the coil after the button is released; a normally-closed stop button
  in series drops it out. Without the seal-in the motor stops the instant the
  start button is released.
* **Control voltage from a CPT:** the coil circuit is commonly fed from a
  control power transformer stepping the line down to a control voltage (e.g.
  120 V), so operators and control devices are not exposed to full line
  voltage. Control-power design is its own topic.
* **Overload auxiliary contact:** the overload relay's normally-closed
  auxiliary contact sits in series in the coil circuit, so an overload trip
  de-energizes the coil and stops the motor.
* **Reversing interlock — both electrical and mechanical:**
  - *Electrical:* each direction contactor's normally-closed auxiliary
    contact is wired in series with the *other* contactor's coil, so
    energizing one direction electrically prevents the other.
  - *Mechanical:* a physical interlock between the two contactors prevents both
    armatures closing at once even if the electrical interlock is defeated or a
    contact welds.
  Both are used together; neither alone is considered sufficient for reversing
  duty. Generally accepted practice — verify for your installation.
* **Star-delta timing:** an on-delay timer holds the star state for the
  starting interval then commands the transition to delta. The star and delta
  contactors are also interlocked against each other (they must never close
  together). Transition timing is application-specific.

## 6. Grounding, shielding, EMC

* **Motor frame grounding / equipotential bonding:** the motor frame and the
  starter enclosure are bonded to PE per NFPA 79 Ch. 8 / IEC 60204-1
  (procedure per the table basis, values not reproduced).
* **Coil suppression:** DC-operated contactor coils are inductive; a
  suppression device (diode, RC, or varistor per the coil type) across the
  coil limits the switch-off voltage spike that would otherwise stress the
  controlling contact or PLC output. AC coils commonly use RC snubbers.
  Suppression selection is device-specific — consult the manufacturer.
  Generally accepted practice.

## 7. Common mistakes

1. **Reversing starter without interlock:** if both direction contactors can
   close together, the swapped phases short line-to-line — a violent fault on
   first simultaneous energization. Both electrical and mechanical interlocks
   are required.
2. **Overload sized to the breaker/OCPD rating instead of motor FLA:** the
   overload then never protects the motor; it is set far above the motor's
   running current and a genuine overload runs the motor to failure.
3. **OCPD relied on for overload protection (or vice versa):** the two
   devices are not interchangeable. A breaker sized to pass inrush cannot
   protect against running overload; an overload cannot clear a bolted fault.
4. **No seal-in contact:** the motor runs only while the start button is
   held and stops when released — the missing holding contact.
5. **Star-delta open-transition surge misdiagnosed:** the current/torque
   spike at the star-to-delta changeover is inherent to open-transition
   starting; it is often mistaken for a fault. Closed-transition or correct
   timing addresses it where the surge is unacceptable.
6. **Contactor undersized for the utilization category/duty:** sizing a
   reversing/plugging (AC-4) application from AC-3 tables under-rates the
   contactor; contacts erode or weld under the harsher breaking duty.

## 8. Verification

* **Rotation check:** confirm motor rotation direction on a brief bump before
  coupling the load; correct by swapping two phases if wrong.
* **Overload setting/trip test:** verify the overload is set to the motor FLA
  and functions (trip test per the relay's method); confirm the auxiliary
  contact drops the coil.
* **Interlock proven:** attempt to select both directions (reversing) or both
  star and delta together and confirm the interlock prevents it.
* **Star-delta transition timing:** verify the timer interval and that the
  transition sequences correctly star → open → delta.

## 9. Standards references

* **NEC (NFPA 70) Art. 430** — motors, motor circuits, and controllers:
  Part III (overload protection), Part IV (branch-circuit short-circuit and
  ground-fault protection), Part IX (disconnecting means). Chapter/article
  level.
* **NFPA 79** — machine electrical wiring practice, protection, and
  conductor/grounding chapters (chapter-level).
* **UL 508A** — industrial control panel construction and the SCCR
  methodology for the starter combination (section-level concept).
* **IEC 60947-4-1 / utilization categories** — AC-3, AC-4 contactor duty as
  a concept (category-level reference).
