<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — 4-20 mA current loop
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, analog, current_loop, 4-20ma, instrumentation, shielding, grounding, isolation]
  systems: [analog_instrumentation, control_panels, plc_io]
-->

# Wiring Practices — 4-20 mA Current Loop

Distilled engineering knowledge behind the site guide "4-20 mA Current Loop
Wiring." Requirements paraphrased at chapter/article level; field practice
flagged as generally accepted. No standards text or tables reproduced.

## 1. Why current wins for industrial analog

* The measurand is **current**, not voltage. In a series loop the same
  current flows everywhere, so series resistance (wire, terminals, barrier)
  does not change the reading — the fundamental advantage over a voltage
  signal, which depends on a shared reference.
* **Live zero.** 4 mA is 0% of span, 20 mA is 100%. A true zero (broken wire,
  dead transmitter, lost power) reads below 4 mA, distinguishable from a
  legitimate 0% — broken-wire / open-loop detection, and why 4 mA rather than
  0 mA is the floor.
* The low-impedance loop shunts capacitively coupled noise far better than a
  high-impedance voltage node. Generally accepted practice.

## 2. The loop as a series circuit — three terminal roles

Every loop, whatever the transmitter, has three functional roles spread over
one to three devices: the **transmitter** (modulates the loop current; needs
a minimum terminal voltage), the **loop power source** (DC supply, commonly
nominal 24 V DC), and the **receiver / input** (a **sense resistor**, commonly
250 ohm but card-dependent, across which the input reads the current as a
voltage). The defining wiring question is which device owns each role — set by
transmitter type.

## 3. Transmitter types (the defining distinction)

* **2-wire (loop-powered)** — draws operating power from the same two wires
  that carry the signal; loop supply and sense resistor are external (panel
  end). Simplest wiring; its minimum operating voltage sets a hard limit on
  the loop-resistance budget.
* **3-wire** — separate power supply (+ and common), signal returned on a
  third conductor referenced to that common. Local power, more drive.
* **4-wire** — fully separate power input and an isolated 4-20 mA output
  pair; highest drive, power and signal independent.
* **Active vs passive** applies to both transmitter output and input card:
  *active* **sources** loop power; *passive* does not and needs the loop
  energized by the other end. The wiring must have **exactly one** power
  source. An active card with an active (self-powered) transmitter
  double-powers the loop — the classic magic-smoke fault. Consult both
  manuals for the designation.

## 4. Loop budget — supply voltage vs total burden

The loop supply must exceed the sum of every voltage drop around the loop at
20 mA (worst case):

  V_supply >= V_transmitter(min) + I x (R_sense + R_wire + R_barrier + ...)

* **Transmitter minimum voltage** — vendor value; consult the manual.
* **Sense resistor** — e.g., 250 ohm drops 5 V at 20 mA. Barriers,
  isolators, and extra HART reads add further burden.
* **Wire resistance** — 2 x one-way run resistance; grows with distance,
  shrinks with gauge. Same conductor-resistance concept behind
  `cst voltage-drop`; use it to keep a long run inside the budget.
* The transmitter's usable range from its supply is its **compliance
  voltage** budget. Too much loop resistance and the loop cannot reach
  20 mA — it reads correctly low but **clips** near 100%; undersized wire on
  a long run is the usual cause.
* Fuse / current-limit the loop supply per device and panel practice;
  generally accepted practice — verify for your installation.

## 5. Signal path and HART coexistence

* The signal *is* the loop current; on a 2-wire device there is no separate
  signal conductor. Series-wire the sense element into the loop.
* **HART** rides the same two wires as a small AC signal on the 4-20 mA DC —
  it coexists without disturbing the analog value, provided the loop has
  adequate resistance (commonly the 250 ohm sense resistor) for the modem.
  Overview-level mention; HART configuration is out of scope.

## 6. Grounding, shielding, isolation

* **Ground the loop at one point only** (commonly supply-negative / panel
  end) to prevent circulating ground-loop current; multiple grounds create a
  loop through the shield or return. Generally accepted practice.
* **Shield landed at one end only** for low-frequency analog — drains
  capacitively coupled noise without becoming a ground-loop conductor. This
  is the opposite of the both-ends 360-degree rule for high-frequency
  VFD/motor cable; a frequency question, not a contradiction (owned by the
  grounding/bonding note). Both-ends across a ground-potential difference
  injects 50/60 Hz hum.
* **Isolators earn their place** where the loop spans a ground-potential
  difference — long runs, separate buildings, or a device that grounds its
  own end. A loop isolator or isolated input breaks the DC path so two
  grounds cannot fight. Generally accepted practice.
* **Separate analog from power/VFD cabling** — analog is a Class 1 (quietest)
  victim, VFD output Class 4. Separation/right-angle rules owned by the EMC
  note; network-side tables in the copper-Ethernet material.

## 7. Common failure modes (field-observed)

* Double-powering a passive loop (two active ends) — overcurrent, damage.
* Loop resistance exceeds compliance — reads correct low, clips near 100%.
* Shield grounded both ends — steady hum/ripple tracking plant load.
* Analog common shared with digital/high-current returns — common-impedance
  offset moving with load.
* No isolator across a ground-potential difference — circulating current.
* Active/passive mismatch — no reading, or double-power damage.

## 8. Verification

* Loop calibration / injection at 4, 8, 12, 16, 20 mA (0/25/50/75/100%);
  compare source, receiver, and displayed value; record on a loop sheet.
* Milliamp injection confirms the receiver independently of the transmitter.
* Retain the completed loop sheet; the toolkit generates one per I/O point
  (`cst loop-sheets`).

## 9. Standards anchors

* **ISA analog signal practice** — the 4-20 mA transmission convention and
  instrument-loop conventions are ISA-domain practice; cited as a category,
  not a clause.
* **NFPA 79** / **IEC 60204-1** — machine wiring-practice chapters
  (conductor identification, routing, separation of signal from power);
  chapter/clause-level citation only.
* Device manuals are the authority for terminal designations, minimum
  operating voltage, active/passive designation, and torque.

## 10. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with
  docs/design/wiring/analog-4-20ma/. Companion to analog_0_10v_wiring.md
  (this is the detailed loop note; the 0-10 V note references it).
