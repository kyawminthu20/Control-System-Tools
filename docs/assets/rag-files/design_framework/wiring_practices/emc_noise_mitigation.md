<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — EMC and electrical noise mitigation
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, emc, noise, shielding, separation, grounding, suppression]
  systems: [control_panels, drive_systems, analog_instrumentation, industrial_networks]
-->

# Wiring Practices — EMC and Noise Mitigation

Distilled engineering knowledge behind the site guide "Noise & EMC
Mitigation in Panels and Field Wiring." Requirements paraphrased at
chapter/clause level; field practice flagged as generally accepted.

## 1. Coupling mechanisms

Four mechanisms explain essentially all plant-floor noise problems:

* **Capacitive (electric-field) coupling** — voltage edges drive current
  into a nearby conductor through stray capacitance; grows with dV/dt,
  proximity, and parallel length. Dominant from VFD outputs.
* **Inductive (magnetic-field) coupling** — current changes induce voltage
  in a nearby loop; grows with dI/dt and enclosed loop area. Dominant from
  contactor/solenoid switching, welders, motor starting.
* **Common-impedance coupling** — two circuits share a conductor (common
  return, shared ground path); one circuit's current appears as a voltage
  in the other. The "mystery offset" mechanism.
* **Radiated coupling** — far-field pickup; matters mainly for long cable
  runs acting as antennas near strong sources (drives, radios).

Mitigation hierarchy, in cost-effectiveness order: **separate first,
suppress/shield second, filter third, fix at the receiver last.** Generally
accepted practice — engineering economics, not a standard requirement.

## 2. Separation and routing classes (NFPA 79 Ch. 13; IEC 60204-1 Cl. 13)

* NFPA 79 Chapter 13 (wiring practices) and IEC 60204-1 Clause 13 both
  address routing, ducts, and segregation of circuits of different types
  and voltage classes — chapter/clause-level citation; consult the text.
* The widely used **signal-class scheme** is generally accepted practice —
  verify for your installation:
  * Class 1 (quietest): analog, thermocouple/RTD, encoder, comms.
  * Class 2: 24 V DC discrete I/O, suppressed control circuits.
  * Class 3: 120/230 V AC control, unsuppressed coils.
  * Class 4 (noisiest): AC power, motor circuits, and above all VFD
    output and braking-resistor wiring.
* Rules of the scheme (all generally accepted practice): separate trays or
  grounded steel dividers between classes; unavoidable crossings at right
  angles; separation distance increases with parallel run length and the
  neighbor's noise class. Specific distances vary — verify against
  cable-/drive-vendor guidance and, for network cabling, the EN 50174-2 /
  TIA-569 separation tables.
* Class 1 and Class 4 never share a duct, tray section, or multi-core
  cable; VFD output shares a raceway only with other motor circuits.

## 3. Source suppression

* **Contactor and relay coils** are inductive-kick noise sources at every
  drop-out. Fit suppression *at the coil*: RC snubber or varistor for AC
  coils, flyback diode / diode+zener or varistor for DC coils. Generally
  accepted practice; vendors sell plug-on modules for the purpose.
* **Plain flyback diode caveat:** a bare diode gives the slowest coil
  decay, measurably delaying contactor drop-out. Where drop-out time
  matters — safety-related stops assessed under ISO 13849-1 / IEC 62061
  response-time budgets — use diode+zener, varistor, or RC instead, and
  verify the safety function's response time with suppression fitted.
* **Solenoid valves** (especially larger AC ones) get the same treatment;
  unsuppressed solenoids near PLC input wiring are a classic chatter source.
* **VFD input/output filtering** (reactors, EMC/dV/dt/sine filters,
  shielded motor cable) is owned by `vfd_wiring.md` — vendor-specific.

## 4. Victim hardening

* Twisted pair for every low-level signal — twisting converts field pickup
  into common-mode, which differential receivers reject (see the RS-485
  physical-layer material). Generally accepted practice.
* Prefer 4–20 mA over 0–10 V analog for any distance: loop current is
  unaffected by series resistance and far less sensitive to induced
  voltage. Generally accepted practice.
* Shielded cable for analog, encoder, and comms; the **shield landing
  policy** (both ends vs one end, by frequency regime) is owned by the
  grounding/bonding note — one-end landing is common practice for
  low-frequency analog screens, both-end 360-degree bonding for
  high-frequency (drive, network) cables.
* Ferrite sleeves: legitimate *retrofit* for common-mode noise on a
  specific cable, not a design substitute for separation and shielding.
* Signal isolators / isolated inputs break common-impedance (ground)
  loops on analog circuits spanning ground-potential differences.

## 5. Panel-level EMC practice (all generally accepted practice)

* Clean/dirty layout: drives, filters, and power switching on one side or
  zone; PLC, analog, and comms on another; wiring between zones minimized
  and crossing at right angles.
* Drive output cables leave the panel by the shortest path, glanded 360°
  at a conductive gland plate — never looped past door-mounted electronics
  or HMI cabling.
* Shield pigtails degrade sharply with frequency (a pigtail is an inductor
  in series with the shield); at PWM/network frequencies only 360-degree
  gland or clamp entries preserve shield performance.
* Bare-metal (masked or scraped) bonding of mounting plates, filter
  chassis, and gland plates; paint is an insulator at every frequency.

## 6. Standards anchors

* NFPA 79:2024 Ch. 13 — wiring practices (routing, ducts, separation);
  Ch. 8 — grounding/bonding basis. Chapter-level citations.
* IEC 60204-1 Cl. 13 — wiring practices; Cl. 4 includes EMC among the
  physical-environment considerations. Clause-level citations.
* IEC 61000 series — the EMC framework (emission/immunity levels, test
  methods) that product standards reference; cited at overview level only.
* Drive-vendor EMC installation guides — the practical authority for
  separation distances, filter selection, and shield termination;
  treated as a category, no single vendor endorsed.

## 7. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/emc-noise-mitigation/.
