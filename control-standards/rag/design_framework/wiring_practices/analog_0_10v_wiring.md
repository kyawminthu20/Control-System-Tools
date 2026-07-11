<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — 0-10 V analog signal
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, analog, voltage_signal, 0-10v, instrumentation, shielding, grounding, reference]
  systems: [analog_instrumentation, control_panels, plc_io]
-->

# Wiring Practices — 0-10 V Analog Signal

Distilled engineering knowledge behind the site guide "0-10 V Analog Signal
Wiring." Companion to `analog_4_20ma_wiring.md` — this note focuses on how a
voltage signal **differs** from a current loop rather than repeating loop
fundamentals. Requirements paraphrased at chapter/clause level; field
practice flagged. No standards text or tables reproduced.

## 1. A voltage signal is a shared-reference measurement

* The measurand is a **voltage between the signal conductor and a reference
  (return / common)**, not a current in a series loop. The receiver measures
  signal-minus-reference at its own input.
* This is the whole difference from 4-20 mA. A current loop is series, so
  series resistance is irrelevant and the reference is local. A voltage
  signal depends on the source and receiver **sharing the same reference**;
  any difference between "source ground" and "receiver ground" adds directly
  to the reading. That reference dependence is the signal's weakness.
* **No live zero.** 0 V is a legitimate 0% reading, indistinguishable from a
  broken wire or dead source. There is **no broken-wire detection** — a
  fundamental safety difference from 4-20 mA's 4 mA floor. Do not assume a
  0 V reading is safe.

## 2. When 0-10 V is appropriate

* Short runs — on-board a panel, sensor to adjacent card, VFD speed-reference
  potentiometer a metre away.
* Cost/simplicity where a current-loop transmitter is overkill.
* Devices that only offer a voltage output/input.
* **Prefer 4-20 mA instead** for any real distance, any electrically noisy
  environment, or anywhere broken-wire detection matters. This is the
  headline decision — see `analog_4_20ma_wiring.md`. Generally accepted
  practice.

## 3. Sizing and the distance limitation

* **Input impedance and source drive.** A voltage input is high-impedance;
  the source must drive it plus the cable, and paralleled inputs can still
  overload a weak source. Consult the manual for input impedance and drive.
* **Return-conductor voltage-divider error — the core distance limit.** The
  input measures signal-minus-return, so any current in the return develops a
  voltage across its resistance that **subtracts from the reading**. Even the
  input's own bias current, over a long thin return, causes error; shared
  returns make it far worse. Wire resistance a 4-20 mA loop ignores becomes a
  direct signal error here — this is why 0-10 V is a short-run signal.
* **No live zero** means no wiring-fault diagnosis from the signal itself;
  distance and fault-tolerance both argue for the current loop. No ampacity
  concern — the currents are tiny; the limit is voltage integrity, not heat.

## 4. The reference/return conductor is a full-status conductor

* Treat the analog **return/common as signal wiring**, not an afterthought
  scavenged onto the nearest ground. Its resistance and what else shares it
  directly set the accuracy.
* Run the return as a dedicated conductor of the same pair as the signal,
  ideally twisted with it; do not combine it with power returns or chassis
  bonding paths.

## 5. Signal wiring — the shared-ground error mechanism

* **Voltage drop in the return appears as signal error.** If the return
  carries any other load's current (shared common), that current's IR drop
  adds to or subtracts from the measured voltage — common-impedance coupling,
  the "analog reads wrong when the pump runs" mechanism. Dedicated return per
  signal.
* **Single-ended vs differential inputs.** A single-ended input references
  every signal to one common; it is cheap but fully exposed to ground-offset
  error. A **differential** input measures signal-high minus signal-low and
  rejects the common-mode difference between source and receiver grounds —
  markedly more robust for 0-10 V over any distance or between panels. Prefer
  differential where a ground offset is plausible. Generally accepted
  practice.
* **Keep runs short.** The cheapest fix for every voltage-signal problem is
  distance; past a few metres in a noisy plant, reconsider 4-20 mA.

## 6. Grounding, shielding, EMC

* **Ground-reference offset directly corrupts the signal.** Two panels (or a
  field device and a panel) at slightly different ground potentials put that
  difference straight onto a single-ended voltage reading. This is the core
  reason for the distance limit and the case for differential inputs or a
  return to 4-20 mA. A current loop is nearly immune to the same offset.
* **Shield at one end only** for low-frequency analog, same reasoning as the
  current loop — drain noise without creating a ground loop. Owned by the
  grounding/bonding note.
* Separate from power/VFD cabling (Class 1 victim vs Class 4 source); owned
  by the EMC note.

## 7. Common failure modes (field-observed)

* Long 0-10 V run — return-conductor voltage-divider error, reads low.
* Using 0-10 V where 4-20 mA belongs — noise/distance problems by design.
* Assuming a 0 V reading is safe — no broken-wire detection; a fault reads
  as a valid 0%.
* Shared return with other loads — common-impedance offset moving with load.
* Ground offset between panels — single-ended reading corrupted directly.
* Single-ended input across a ground-potential difference — the offset a
  differential input would have rejected lands on the measurement.

## 8. Verification

* Injection check at 0, 2.5, 5, 7.5, 10 V (0/25/50/75/100%); compare source,
  receiver, and displayed value; record on a loop sheet.
* Verify with the intended cable length in place — a short bench test hides
  the distance error.

## 9. Standards anchors

* **ISA analog signal practice** — voltage-signal and instrument-loop
  conventions are ISA-domain practice; cited as a category, not a clause.
* **NFPA 79** / **IEC 60204-1** — machine wiring-practice chapters
  (conductor identification, routing, separation of signal from power);
  chapter/clause-level citation only.
* Device manuals are the authority for input impedance, drive capability,
  single-ended vs differential input type, and terminal designations.

## 10. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with
  docs/design/wiring/analog-0-10v/. Companion to analog_4_20ma_wiring.md
  (that note holds the loop fundamentals; this one covers the voltage-signal
  differences).
