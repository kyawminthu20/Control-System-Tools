---
layout: default
title: "0–10 V Analog Signal Wiring"
description: "The voltage-signal alternative to a current loop — its shared-reference weakness, the return-conductor voltage-divider error that limits distance, single-ended vs differential inputs, and when to prefer 4–20 mA instead."
breadcrumb:
  - name: "Design"
    url: "/design/"
  - name: "Wiring & Installation"
    url: "/design/wiring/"
  - name: "0–10 V"
repo_path: "control-standards/rag/design_framework/wiring_practices/"
review:
  standard: "ISA analog signal practice; NFPA 79 / IEC 60204-1 (wiring-practice chapters)"
  edition: "NFPA 79:2024, IEC 60204-1:2016+AMD1:2021"
  status: "Review pending"
  coverage: "Voltage-signal reference dependence, distance limitation, single-ended vs differential inputs, shield policy and injection check at chapter/article level; vendor input impedance, drive capability and terminal designations deliberately excluded."
  last_reviewed: "July 2026"
related_standards:
  - name: "NFPA 79"
    url: "/standards/us-electrical/nfpa-79/"
  - name: "IEC 60204-1"
    url: "/standards/machinery/iec-60204-1/"
---

<div class="page-header">
  <span class="page-header__label">Wiring &amp; Installation</span>
  <h1>0–10 V Analog Signal Wiring</h1>
  <p>Simple, cheap, and fine over short runs — but a voltage signal leans on a shared reference, and that reference is exactly what fails first as distance and noise grow.</p>
</div>

> **Safety.** This guide is educational reference material, not a work
> instruction. Electrical work is performed de-energized and verified by
> qualified personnel under your site's LOTO procedures, following the device
> manufacturer's manual and the authority having jurisdiction.

## Overview

A 0–10 V signal transmits an analog value as a **voltage between the signal
conductor and a reference (return / common)**. The receiver measures
signal-minus-reference at its own input. That is the entire difference from a
[4–20 mA current loop]({{ '/design/wiring/analog-4-20ma/' | relative_url }}),
and it is worth stating plainly because it drives every wiring rule below:

- A **current loop is a series circuit** — the same current flows
  everywhere, so wire resistance is irrelevant and the reference is local.
- A **voltage signal is a shared-reference measurement** — source and
  receiver must agree on "zero." Any difference between the source's ground
  and the receiver's ground adds directly to the reading. **That reference
  dependence is the signal's weakness**, and it does not exist for a current
  loop.

One more consequence matters for safety: **there is no live zero.** 0 V is a
legitimate 0% reading, indistinguishable from a broken wire or a dead source.
A 0–10 V signal has **no broken-wire detection** — unlike 4–20 mA, where a
reading below 4 mA is a self-announcing fault. Never assume a 0 V reading is
safe.

This guide is the short companion to the
[4–20 mA current loop guide]({{ '/design/wiring/analog-4-20ma/' | relative_url }}),
which holds the detailed loop fundamentals. Here the focus is on where a
voltage signal differs and where it belongs. Input impedance, drive
capability, and terminal designations are vendor-specific — consult the
device manual, never a guide.

## Before You Start

- **Decide whether 0–10 V is the right signal at all.** It is appropriate
  for:
  - **Short runs** — on-board a panel, sensor to an adjacent card, a
    speed-reference pot a metre from the drive.
  - **Cost and simplicity** — where a loop-powered transmitter is overkill.
  - **Devices that only offer a voltage interface.**
  - **Prefer [4–20 mA]({{ '/design/wiring/analog-4-20ma/' | relative_url }})
    instead** for any real distance, any electrically noisy environment, or
    anywhere broken-wire detection matters. This is the headline decision —
    make it before pulling wire, not after chasing a drifting reading.
- **Know the input type.** Is the receiving input **single-ended** (all
  signals share one common) or **differential** (each signal has its own
  high/low pair)? It changes how tolerant the circuit is of a ground offset.
- **Know the source's drive capability and the input impedance** — a weak
  source into several paralleled high-impedance inputs can sag. Both are
  vendor values; consult the manuals.

## Sizing & Protection

There is no ampacity concern — a voltage signal carries almost no current.
The limit is entirely **voltage integrity over distance**, and it comes from
one mechanism:

- **The return-conductor voltage-divider error.** Because the input measures
  signal-minus-return, any current in the return conductor develops a voltage
  across the conductor's resistance that **subtracts from the reading**. Even
  the input's own small bias current, flowing through a long thin return,
  creates error; a shared return makes it far worse. Wire resistance that a
  current loop simply *ignores* becomes a direct signal error here. This is
  the fundamental reason 0–10 V is a short-run signal.
- **Input impedance and source drive.** Verify the source can drive the
  input impedance plus the cable; confirm both against the device manuals.
- **No live zero, no self-diagnosis.** With no 4 mA floor, the signal itself
  gives no evidence of a wiring fault. Where distance or fault-tolerance
  matter, that alone argues for the
  [current loop]({{ '/design/wiring/analog-4-20ma/' | relative_url }}).

## Power Wiring

- **The reference/return conductor is a full-status conductor, not an
  afterthought.** On a voltage signal the return is half the measurement —
  its resistance and whatever else shares it set the accuracy directly. Run
  it as a dedicated conductor, ideally twisted with the signal, and do **not**
  scavenge it onto the nearest power return or chassis-bonding path. A return
  treated casually is a signal error waiting to appear under load.

## Control / Signal Wiring

- **Voltage drop in the return appears as signal error.** If the return
  carries any other load's current — the failure mode of a shared common —
  that current's IR drop adds to or subtracts from the measured voltage. This
  is common-impedance coupling: the classic "analog reads wrong only when the
  pump runs." Give every voltage signal its own dedicated return.
- **Single-ended vs differential inputs.** A **single-ended** input
  references every signal to one common — cheap, but fully exposed to any
  ground-offset error. A **differential** input measures signal-high minus
  signal-low and rejects the common-mode difference between the source and
  receiver grounds. For 0–10 V over any distance, or between two panels,
  prefer a differential input; it is the single most effective defence
  against reference offset. Generally accepted practice — verify for your
  installation.
- **Keep runs short.** Distance is the cheapest lever on every voltage-signal
  problem. Past a few metres in a plant environment, reconsider
  [4–20 mA]({{ '/design/wiring/analog-4-20ma/' | relative_url }}).

## Grounding, Shielding & EMC

Device-specifics here; the shield-landing theory is owned by
[panel grounding &amp; bonding]({{ '/design/wiring/grounding-bonding/' | relative_url }})
and the coupling/separation depth by the
[noise &amp; EMC mitigation guide]({{ '/design/wiring/emc-noise-mitigation/' | relative_url }}).

- **A ground-reference offset directly corrupts the signal.** Two panels — or
  a field device and a panel — sitting at slightly different ground
  potentials put that difference straight onto a single-ended voltage
  reading. This is the **core reason for the distance limit**: the farther
  apart the ends, the more likely their grounds disagree. A
  [current loop]({{ '/design/wiring/analog-4-20ma/' | relative_url }}) is
  nearly immune to the same offset, which is why it wins over distance. Where
  an offset is unavoidable, use a differential input or move to 4–20 mA.
- **Shield landed at ONE end only** for low-frequency analog — drain
  capacitively coupled noise to ground without turning the screen into a
  ground-loop conductor. Landing both ends across a ground-potential
  difference injects 50/60 Hz hum. Same reasoning as the current loop; the
  frequency argument behind the rule is owned by
  [grounding &amp; bonding]({{ '/design/wiring/grounding-bonding/' | relative_url }}).
- **Separate from power and VFD cabling** — a voltage signal is a Class 1
  (sensitive) victim; keep it away from Class 4 power/drive cable, cross at
  right angles, and never share a duct. Separation depth is in the
  [EMC guide]({{ '/design/wiring/emc-noise-mitigation/' | relative_url }}).

## Common Mistakes

1. **Long 0–10 V runs with return-conductor error.** The return's resistance
   forms a voltage divider that subtracts from the reading; it reads low, and
   worse as the run lengthens or the return shares load. Shortening the run
   or moving to a current loop is the real fix — not a software offset.
2. **Using 0–10 V where 4–20 mA belongs.** A voltage signal specified for a
   long or noisy run designs the distance and noise problems in from day one.
   Choose the signal type deliberately; when in doubt over distance, choose
   the loop.
3. **Assuming a 0 V reading is safe.** With no live zero there is no
   broken-wire detection — a severed conductor or dead source reads as a
   valid 0%. A control decision made on "it reads zero, so it's off" can be
   acting on a fault.
4. **Shared return with other loads.** The other load's current develops an
   IR drop on the common that lands on the measurement as an offset moving
   with load. Dedicate a return to each voltage signal.
5. **Ground offset between panels.** Source and receiver referenced to
   grounds at different potentials put the difference straight onto a
   single-ended reading — a steady, load-dependent error. Bond deliberately,
   or use a differential input.
6. **Single-ended input across a ground-potential difference.** The offset
   the differential input would have rejected lands directly on the signal.
   Where the ends may not share a ground, specify a differential input from
   the start.

## Verification Checks

Loop-check before handing the point to the process (evidence-retaining sheets
in [templates]({{ '/tools/templates/' | relative_url }})):

- [ ] Signal type chosen deliberately — 0–10 V justified by short run /
      simplicity, not defaulted where 4–20 mA belongs
- [ ] Input type confirmed (single-ended vs differential) and matched to the
      ground-offset risk
- [ ] Dedicated return per signal — no shared common with power or other
      loads
- [ ] **Injection check at 0 / 2.5 / 5 / 7.5 / 10 V** (0 / 25 / 50 / 75 /
      100%); source, receiver, and displayed value agree within tolerance
- [ ] Checked **with the intended cable length in place** — a short bench
      test hides the distance error
- [ ] Shield landed at one end only; run separated from power/VFD cabling
- [ ] Terminal torques per the device manual, recorded
- [ ] Completed loop sheet filed; hand off to the
      [commissioning templates]({{ '/lifecycle/guides/commissioning-templates/' | relative_url }})
      loop-check workflow

## Standards References

- **ISA analog signal practice** — voltage-signal and instrument-loop
  conventions are ISA-domain practice; cited here as a category, not a
  specific clause.
- **NFPA 79:2024** — machine wiring-practice chapters: conductor
  identification, routing, and separation of signal from power circuits
  (chapter-level citation).
- **IEC 60204-1:2016+AMD1:2021** — wiring practices for machine electrical equipment;
  the international counterpart, cited at clause level only.
- Device manuals are the authority for input impedance, drive capability,
  single-ended vs differential input type, and terminal designations.

## Related Pages

- [4–20 mA current loop wiring]({{ '/design/wiring/analog-4-20ma/' | relative_url }}) — the detailed companion; prefer it for distance, noise, and broken-wire detection
- [PLC I/O wiring]({{ '/design/wiring/plc/' | relative_url }}) — where the analog card lives
- [Panel grounding &amp; bonding]({{ '/design/wiring/grounding-bonding/' | relative_url }}) — shield-landing policy and reference grounding
- [Noise &amp; EMC mitigation]({{ '/design/wiring/emc-noise-mitigation/' | relative_url }}) — coupling mechanisms and separation classes
- [NFPA 79 overview]({{ '/standards/us-electrical/nfpa-79/' | relative_url }})
- [IEC 60204-1 overview]({{ '/standards/machinery/iec-60204-1/' | relative_url }})
