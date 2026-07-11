<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — incremental encoder feedback
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, encoder, feedback, quadrature, differential_signaling, line_driver, shielding, grounding, emc]
  systems: [motion_feedback, plc_hsc, counters, control_panels]
-->

# Wiring Practices — Encoder Feedback

Distilled engineering knowledge behind the site guide "Encoder Wiring —
Differential vs Single-Ended, Signals, and Shielding." Requirements
paraphrased at chapter/article level; field practice flagged as generally
accepted. No standards text or tables reproduced.

Scope: general-purpose incremental encoders landing on counters, PLC
high-speed-counter (HSC) inputs, and dedicated encoder input cards. Servo /
drive feedback wiring (resolver, absolute serial feedback, drive-matched
cable) is owned by the servo-drive note and is only cross-referenced here.

## 1. What an encoder is, and the terminal groups

An encoder converts shaft angle into electrical pulses (incremental) or a
coded word (absolute); the control system derives **position and velocity**
from them. Whatever the type, the landing splits into three terminal groups:
**power** (a +V/0 V pair, commonly 5 V or 24 V DC); **signal channels** — the
quadrature pair **A** and **B** plus the index/marker **Z** (one pulse per
rev), each a complementary pair (A/A‑not, B/B‑not, Z/Z‑not) on a differential
device; and **shield/ground**. Commutation channels (U/V/W) appear on
motor-feedback encoders — servo-drive note owns those.

**Incremental vs absolute** is a real distinction but mostly a *protocol* one
(incremental = counted pulses needing a home/reference; absolute = a coded
position, often on a serial channel such as SSI / BiSS / EnDat). This note is
about **wiring practice** for the electrical channels, not the protocol.

## 2. The defining decision — output/interface type

The single decision that drives everything is the encoder's **output type**,
which must match the receiving input card:

* **Differential (RS‑422 / line‑driver)** — each channel is a complementary
  pair driven by a line driver; the receiver reads the difference. Highest
  noise immunity and the only sound choice for long or electrically noisy
  runs. Category anchor is the RS‑422/RS‑423 line-driver convention.
* **Single-ended** — one wire per channel, referenced to 0 V. Sub-types:
  **push-pull / HTL** (typically 24 V logic, more robust than TTL),
  **open-collector** (needs a pull-up; the input or an external resistor
  supplies it), and **TTL / 5 V**. Single-ended is cheaper and fine for
  short, quiet runs but loses noise margin and distance fast.
* **The receiver must match the driver.** A TTL (5 V) signal into a 24 V HTL
  input under-drives it; a 24 V HTL output into a 5 V TTL input over-drives /
  damages it. Open-collector needs a defined pull-up. Confirm driver and
  input electrical type on **both** device manuals before wiring.

Supply voltage (5 V vs 24 V) and PPR/resolution are the other two upstream
facts — see sections 3 and 4.

## 3. Supply, voltage drop, and length vs PPR

Encoder current is small, so supply wiring is a **voltage-integrity**
question, not an ampacity one — no conductor-ampacity table applies.

* **5 V drop over a long cable is a real failure.** The +V/0 V pair has
  resistance; at 5 V a fraction of a volt of drop browns out the encoder and
  its line driver, and counts degrade or stop. 24 V devices have far more
  headroom. The relevant arithmetic is conductor voltage drop over the run
  (concept behind `cst voltage-drop`); never invent a resistance-per-length
  value, take it from wire tables.
* Some line-driver encoders offer **remote sense** (a separate sense pair to
  compensate for cable drop) — consult the manual; use it on long 5 V runs.
* **Fuse / current-limit the supply** per device and panel practice —
  generally accepted practice, verify for your installation.
* **Length vs PPR/frequency.** Output frequency = PPR × RPM / 60 (×4 counts
  after quadrature decode). **Max usable cable length falls as frequency
  rises and as supply drops** — a run fine at low PPR fails when a higher-count
  encoder is fitted or the speed is raised. Verify length against the
  encoder's frequency-vs-length curve and the input card's max count
  frequency (datasheet values). `cst encoder` handles the counts/units/RPM
  scaling math; this note is about the wiring, not the kinematics.

## 4. Signal wiring — the core

* **Differential rejects common-mode noise.** Each channel is a twisted pair
  carrying complementary signals (A and A‑not). Noise couples roughly
  **equally** into both conductors of a tight pair, shifting them together;
  the receiver reads only the difference, so equal noise cancels. This is the
  same balanced-signaling idea as RS‑485 — the RS‑485 physical-layer material
  owns the full explanation.
* **Twist by channel complement, not at random.** A must be paired with
  A‑not, B with B‑not, Z with Z‑not — the pairing is what makes common-mode
  rejection work. Pairing A with B (a common field error) destroys it and can
  cross-couple the two channels.
* **Single-ended has no such rejection** — its margin is the logic swing
  against a shared 0 V; use it only on short, quiet runs.
* **Terminate fast/long differential lines.** A long line-driver run at high
  edge rate reflects off an unterminated end; terminate across each receiver
  pair (commonly ~120 Ω, matching the cable) where length/frequency warrant.
  Short slow runs may not need it. Same reasoning as RS‑485 termination.
* **Quadrature and index.** A and B are 90° out of phase; lead/lag gives
  **direction**, ×4 edges give resolution; Z is one pulse per rev for homing.
  Land unused complementary inputs per the card manual. Terminal
  designations, logic thresholds, and pull-up values are vendor-specific —
  consult the device manual.

## 5. Grounding, shielding, EMC

* **Shield landed at ONE end only** for the low-level encoder signal
  (commonly the **controller / panel** end) — it drains coupled noise without
  becoming a conductor between two grounds. This is deliberately the
  **opposite** of the both-ends 360° rule for high-frequency VFD/servo motor
  cable; the frequency reasoning is owned by the grounding/bonding note.
  Both-ends on a signal cable across a ground-potential difference injects
  50/60 Hz hum and can corrupt counts.
* **Keep the encoder cable away from VFD / servo motor power.** The classic
  fault is **counts jumping or drifting only when the motor runs / under
  load** — the drive's PWM output couples into the feedback cable. Separate
  routes, cross at right angles, never share a duct with motor cable.
  Separation classes are owned by the EMC note; the servo-drive note covers
  the motor-cable side.
* Maintain shield continuity through junction boxes; do not land the shield
  on a signal conductor.

## 6. Common failure modes (field-observed)

* Single-ended encoder on a long / noisy run where differential was needed —
  intermittent or unstable counts.
* Wrong twisted-pair grouping (A paired with B instead of A/A‑not) — lost
  common-mode rejection, cross-talk.
* 5 V supply drop over a long cable — encoder/line-driver brownout, counts
  degrade or stop.
* Encoder cable in the same tray/duct as VFD or servo motor cable — counts
  jump under motor load.
* Shield landed at both ends on the low-level signal — ground loop, hum,
  count corruption.
* TTL into an HTL input (under-drives) or HTL into a TTL input (over-drives /
  damages) — no counts or a dead input.
* Missing termination on a fast/long differential line — reflections, miscounts.

## 7. Verification

* Scope the differential pairs (A–A‑not, B–B‑not) for clean, fast edges and
  adequate amplitude **at the receiver end** — same practice as reading an
  RS‑485 bus with a scope.
* **Count-per-rev:** one shaft revolution equals the expected counts (PPR ×
  decode factor); `cst encoder` gives the expected scaling.
* **Direction / quadrature:** A leads/lags B in the expected sense and count
  direction matches machine direction; Z observed once per rev where used.
* **Run the machine and watch for count jumps under motor load** — the tell
  for coupling from drive/motor cable.
* Shield landed at one end only; supply voltage measured **at the encoder**
  (not just the panel) on long 5 V runs.

## 8. Standards anchors

* **RS‑422 / RS‑423 line-driver** convention — cited as a category for the
  differential encoder output type, not a specific clause.
* **NFPA 79** / **IEC 60204-1** — machine wiring-practice chapters (conductor
  identification, routing, separation of signal from power, shielding of
  sensitive circuits); chapter/clause-level citation only.
* Device manuals are the authority for terminal designations, output
  electrical type, supply and remote-sense wiring, logic thresholds, and
  termination values.

## 9. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with
  docs/design/wiring/encoder/. Differential-signaling explanation deferred to
  the RS‑485 physical-layer material; motor-feedback / drive-matched encoder
  wiring deferred to the servo-drive note.
