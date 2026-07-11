<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: troubleshooting — analog signal faults (4-20 mA / 0-10 V)
SOURCE_BASIS: diagnostic reasoning + generally accepted field practice (flagged)
INDEX_TAGS:
  topics: [troubleshooting, analog-io, 4-20ma, 0-10v, loop-check, grounding, emc]
  systems: [analog-input, analog-output, transmitter, plc-io]
-->

# Analog signal faults — fault-domain reasoning

The discriminating fact about an analog loop is that the *value it reports*
already narrows the fault before any meter comes out. A 4-20 mA loop is a
series current circuit with a **live zero** — 4 mA is 0% and 20 mA is 100%,
so anything below 4 mA is not a legitimate process value. A 0-10 V signal has
no such floor, which is exactly why some of its faults are harder to see. The
reasoning below sorts by the *reading*, because that is what the technician
has in hand first.

## Symptom class: reads 0 / below 4 mA (below live zero)

An under-range reading on a 4-20 mA loop means the current path is broken or
unpowered — the loop cannot even reach its zero. Candidate causes, roughly in
order of field frequency:

- **Broken wire / open connection.** The classic case the live zero was
  designed to catch. An open conductor, a backed-out terminal, or a corroded
  splice drops the loop to 0 mA. This is the built-in **broken-wire
  detection** benefit of live zero — a genuine 0% process value still reads
  4 mA, so 0 mA is unambiguous.
- **Dead loop power.** A 2-wire (loop-powered) transmitter with no supply, a
  tripped loop-power fuse, or a failed 24 V feed reads as no current. Confirm
  the supply before condemning the transmitter.
- **Transmitter fault.** A failed sensor or output stage. Distinguish from
  wiring by injecting a known mA at the card end (see below) — if the card
  reads the injection but not the transmitter, the fault is upstream.
- **Reversed polarity.** A miswired 2-wire device that will not conduct, or a
  polarity-sensitive input that reads nothing. Common on first energization.

## Symptom class: reads full-scale / over-range (pegged high)

A pinned-high reading means either too much current is flowing, or the input
is being driven past its span:

- **Short across the loop or a wetted conductor.** A short circuit, moisture
  in a junction box, or insulation breakdown can drive the input to over-range.
- **Wrong input range configured.** A card set for 0-20 mA reading a 4-20 mA
  device, or a ±10 V range reading a 0-10 V signal, mis-scales toward the rail.
- **Double-powered passive loop.** Two active ends — a self-powered (active)
  transmitter wired to a loop-powering (active) input card — push current from
  both sides. Best case it reads nonsense; worst case the input stage or the
  transmitter output is damaged. This is the **classic magic-smoke mistake**;
  confirm active/passive on *both* device manuals before energizing.

## Symptom class: reads noisy / jumpy (unstable)

A reading that will not settle is almost always coupled interference or a
ground problem, not a transmitter fault:

- **Shield grounded at both ends.** For low-frequency analog the shield is
  landed at **one end only**. A both-ends screen across any ground-potential
  difference becomes a ground-loop conductor and injects 50/60 Hz hum that
  tracks plant load.
- **VFD / motor-cable coupling.** Analog is the quietest, most sensitive
  victim class; VFD output is the noisiest source. Shared ducts or parallel
  runs couple switching noise into the loop. The fix is routing and
  separation, owned by the EMC guide.
- **Ground loop needing an isolator.** Where the loop spans two grounds at
  different potentials — long field runs, separate buildings, a device that
  insists on grounding its own end — circulating current rides the loop. A
  loop isolator or isolated input card breaks the DC path instead of fighting
  it.

## Symptom class: reads offset / wrong-but-stable

A steady but incorrect value is a configuration, budget, or calibration
problem — the loop is healthy, the interpretation is not:

- **Scaling / range configuration.** The engineering-unit scaling in the
  controller does not match the transmitter's ranged span. The current is
  right; the number on the HMI is not.
- **Loop resistance exceeding compliance.** On a long or heavily-loaded loop,
  total series resistance can exceed the supply's compliance budget. The loop
  reads correctly at low signal but **cannot reach 20 mA** — it clips near
  100%. That is a resistance-budget failure, not a transmitter fault.
- **Calibration drift.** Sensor or output-stage drift shifts zero or span.
  Confirm with a known-input injection before adjusting.

## 0-10 V-specific fault

A voltage signal shares a reference and develops a drop across conductor
resistance, so a long run behaves as an unintended **voltage divider**: the
sensed voltage at the card is lower than at the source, reading low and
load-dependent. A current loop is immune to this; it is the main reason to
prefer 4-20 mA on long runs. Verify by measuring voltage at the source versus
at the card — a difference is the divider error.

## Discriminating checks (bisect the loop)

- **Series mA reading.** Break the loop and read current in series — the
  ground truth of what is actually flowing.
- **Loop voltage.** Measure supply and terminal voltage to confirm the loop is
  powered and the transmitter has its minimum operating voltage.
- **Inject a known signal to bisect.** Inject a known mA (or V) *at the
  transmitter terminals* and again *at the card*. If the card reads the
  injection at its own terminals but not from the field, the fault is in the
  wiring or transmitter; if the card mis-reads even a local injection, the
  fault is the card or its configuration. This one move splits the loop in half.
- **Resistance.** De-energized, check conductor continuity and insulation to
  find opens, shorts, and wetted paths.

## Notes

Field-practice heuristics here are *generally accepted practice — verify for
your installation*. Vendor terminal designations, minimum operating voltage,
active/passive designation, and fault-code lists are the device manual's
authority — consult it; this note never reproduces a manufacturer's code table.
