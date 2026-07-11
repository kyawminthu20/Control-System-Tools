<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: troubleshooting — VFD fault categories
SOURCE_BASIS: diagnostic reasoning + generally accepted field practice (flagged)
INDEX_TAGS:
  topics: [troubleshooting, vfd, drives, faults, overvoltage, overcurrent, ground-fault]
  systems: [motion_drives, vfd, motors]
-->

# VFD Fault Categories — Diagnostic Reasoning

A variable frequency drive protects itself and the motor by tripping into a
fault state. The vendor's numeric fault code names *which* protection fired;
it does not name the *cause*. This note reasons about the fault CATEGORIES
behind those codes. Always read the actual code out of the drive against the
manufacturer's fault-code list — this note never reproduces one. The single
most useful discriminator is whether the fault correlates with a **phase of
operation** — decel, accel, steady load, warm-up, enable — not the code
number.

## Overvoltage (DC bus)

The bus rises above its trip threshold. On a low-voltage drive the bus is
regenerative: a decelerating load pumps energy back into the capacitors.

- **What it looks like** — trips on deceleration or on an overhauling load;
  a high-inertia machine that stops too fast; never trips during a gentle
  coast.
- **Discriminating check** — extend the decel ramp. If the trip moves out or
  disappears, the drive had nowhere to put the regen energy.
- **Fix direction** — lengthen decel, or add a braking resistor/chopper or
  regen unit sized for the duty. A genuinely high input supply is a separate
  cause — measure it.

## Overcurrent / output short

Instantaneous current exceeds the hardware limit. This is the drive
protecting its output stage, and it is the category most likely to mean real
damage.

- **What it looks like** — trips instantly on run or on accel; may trip the
  moment the output is enabled if a short is already present.
- **Discriminating check** — with the drive locked out and the output
  **disconnected**, insulation-test and ring out the motor and cable
  phase-to-phase and phase-to-ground. Never megger through a connected drive.
- **Fix direction** — a genuine phase-to-phase or phase-to-ground fault in
  motor or cable is repaired before re-running. If insulation is good and it
  trips only on hard accel, the ramp is too aggressive or motor data is wrong.

## Overtemperature

A heatsink, module, or internal air-temperature sensor exceeds its limit.

- **What it looks like** — trips after minutes to hours of running, worse in
  a hot cabinet or on a hot day; not tied to a specific motion event.
- **Discriminating check** — measure cabinet ambient and confirm airflow
  (filters, fans, clearance). Note the switching (carrier) frequency — a
  raised carrier frequency increases drive losses and can push a marginal
  install over the edge.
- **Fix direction** — restore cooling, derate for ambient/altitude per the
  manual, or lower carrier frequency. Derating curves are vendor-specific.

## Ground fault

The drive detects current flowing to earth on the output.

- **What it looks like** — trips on enable or on accel; may read like an
  overcurrent. Distinguished by the code and by where the leakage goes.
- **Discriminating check** — OFFLINE insulation test of motor and cable to
  ground, drive output disconnected. This is the classic
  megger-through-the-drive trap: testing with the drive still wired destroys
  the output stage.
- **Fix direction** — repair the motor or cable insulation. A long,
  poorly-shielded cable can raise capacitive earth-leakage enough to
  nuisance-trip a sensitive detector even with sound insulation — that shades
  into the EMC category below.

## Input / undervoltage

The bus is too low, or the input supply is out of tolerance.

- **What it looks like** — trips on power events, sags, or at power-up; a
  drive that will not charge its bus at all.
- **Discriminating check** — measure the three input phases under load; look
  for a lost phase, a loose input terminal, or a failed precharge (a drive
  that clicks the precharge relay but never comes ready).
- **Fix direction** — correct the supply, tighten terminations, or service
  the precharge circuit. A single lost input phase both undervolts the bus
  and overheats the remaining path — treat as urgent.

## Motor won't run — but NO fault is shown

The drive is healthy and ready but the shaft does not turn. This is not a
protection trip; it is a command or permissive gap.

- **What it looks like** — "Ready" or "Stopped", no fault, no output.
- **Discriminating check** — walk the enable chain: run/enable input, the
  active reference SOURCE (keypad vs terminal vs fieldbus — a drive commanded
  from the wrong source sits at zero), direction, and STO. On most modern
  drives an unsatisfied STO holds the output off, sometimes with only a
  status bit rather than a hard fault.
- **Fix direction** — satisfy the missing permissive; select the intended
  reference source; confirm STO is de-asserted through the safety function.

## Nuisance trips under load (EMC / coupling)

Sporadic, non-repeatable faults that appear only when the drive — or a
neighbouring drive — is loaded. The drive is reporting a real electrical
event; the cause is coupling, not the protected circuit itself.

- **What it looks like** — reads clean at commissioning (drive idle), then
  trips or corrupts signals once the plant loads up; correlated with drive
  state, not with a mechanical event.
- **Discriminating check** — scope the quiet plant, then the running plant;
  the difference is the coupling. Check shield terminations (360° both ends),
  segregation of the motor cable from control/signal runs, and PE/EMC-filter
  bonding.
- **Fix direction** — fix the installation, not the parameters: shielding,
  segregation, bonding. This is the EMC-mitigation and case-study territory.

## What to measure (always)

- **DC bus voltage** — from the readout or across marked DC terminals after
  the discharge wait; distinguishes over- from under-voltage.
- **Insulation resistance — OFFLINE, drive output disconnected** — motor and
  cable, phase-to-phase and phase-to-ground. The one non-negotiable rule.
- **Output balance** — the three output currents should be roughly equal; a
  large imbalance points at a motor/cable fault or a lost output.
- **Thermal** — cabinet ambient, airflow, heatsink; correlate with run time.

Every branch ends the same way: read the actual code against the drive's own
fault-code list, and confirm the category with a measurement before changing
anything. Generally accepted practice — verify for your installation.
