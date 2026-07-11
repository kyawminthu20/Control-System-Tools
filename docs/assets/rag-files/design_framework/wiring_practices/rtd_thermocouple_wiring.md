<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — RTD and thermocouple temperature sensors
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, temperature, rtd, thermocouple, analog, shielding, emc]
  systems: [instrumentation, process_control, control_panels]
-->

# Wiring Practices — RTD and Thermocouple Sensors

Distilled engineering knowledge behind the site guide "RTD & Thermocouple
Wiring." Requirements are paraphrased at category/chapter level with
references; field practice not derivable from a standard is flagged as
generally accepted practice.

## 1. Two sensor types, two wiring problems

Temperature measurement in industry is dominated by two sensor types, and
what makes their wiring special is different for each:

* **RTD (resistance temperature detector):** a precision resistor whose
  resistance varies with temperature (e.g. Pt100 = 100 Ω at 0 °C, Pt1000 =
  1000 Ω). The instrument measures **resistance**, so the resistance of the
  lead wires adds to the reading unless compensated — lead-resistance
  compensation is the whole wiring story. IEC 60751 defines the standard
  platinum RTD characteristic and tolerance classes.
* **Thermocouple (TC):** two dissimilar metals joined at a measuring junction
  that generate a small **millivolt** signal proportional to the temperature
  difference between that junction and a reference (cold) junction. Two
  consequences: the extension wire must be of the **matched thermocouple type**
  (a dissimilar metal introduces an unwanted junction and error), and the
  instrument must perform **cold-junction compensation**. IEC 60584 defines
  the TC types (J, K, T, E, N, R, S, B) and their characteristics.

Both produce low-level signals — resistance or millivolts — so **noise, not
current, is the enemy**. This drives the shielding, separation, and grounding
practice below.

## 2. Terminal groups

* **Sensor** — the RTD element or TC junction in the process.
* **Extension / lead** — the wire from the sensor head to the input; RTD lead
  wire (2, 3, or 4 conductors) or matched TC extension wire.
* **Input card / transmitter** — the RTD/TC analog input module, or a
  head/rail-mounted temperature transmitter that converts to 4–20 mA.

Terminal designations, region-specific TC color codes, and card type
selection are vendor- and standard-specific — always from the device manual
and the applicable color-code standard, never generalized.

## 3. Sizing and protection (there is no ampacity here)

These are low-level signals, not power circuits — the "sizing" concern is not
conductor ampacity but **signal integrity**:

* **RTD lead resistance** is the sizing concern: on a 2-wire RTD the lead
  resistance adds directly to the measured resistance and therefore to the
  temperature reading. Heavier gauge and shorter runs reduce the error;
  3-wire and 4-wire methods compensate it (section 5).
* **TC extension wire gauge and length:** matched extension wire has a defined
  loop resistance; long runs and the input's impedance matter for the
  millivolt signal. Where the run is long, converting to 4–20 mA at the sensor
  (a transmitter) is often the better answer.
* Because these are signal circuits, there is no overcurrent-protection sizing
  in the power sense — the design target is keeping induced noise below the
  measurement resolution.

## 4. Power wiring — the loop-powered transmitter option

* A **head- or rail-mounted temperature transmitter** can sit at the sensor
  and convert RTD resistance or TC millivolts to a **4–20 mA** loop signal.
  For long runs this is frequently the better answer: the robust 4–20 mA
  current signal shrugs off lead resistance and coupled noise that would
  corrupt a raw RTD/TC run, and the cold-junction/lead compensation is done
  locally at the transmitter. The trade is an added device to power and
  configure. The 4–20 mA loop practice (loop-resistance budget, active/passive
  matching, single-point grounding) is its own topic.

## 5. Control / signal wiring — the core

### RTD lead configurations

* **2-wire:** the lead resistance adds directly to the element resistance and
  is read as extra temperature — an uncompensated error. Acceptable only for
  short runs or low-accuracy points.
* **3-wire (the industrial standard):** a third conductor lets the instrument
  measure and subtract the lead resistance, **assuming all leads are equal**.
  The workhorse configuration — good accuracy with three conductors.
* **4-wire (true Kelvin / four-terminal sensing):** a separate pair carries a
  known excitation current and another pair senses voltage, so lead resistance
  cancels entirely regardless of lead matching. Best accuracy; used where the
  measurement must be traceable or the leads are long/unequal.

### Thermocouple wiring

* **Matched extension wire is mandatory.** The extension wire must be of the
  **same thermocouple type** as the sensor (Type K extension for a Type K
  sensor, etc.). Running plain **copper** wire from a thermocouple creates a
  second, unintended junction at the transition and injects error — the single
  most common thermocouple mistake.
* **Observe polarity.** TC polarity matters (the two legs are different
  metals), and the **color codes differ by region** (IEC vs ANSI/other codes
  assign different colors, and in several codes the negative leg is the
  distinguishing color). Consult the applicable color-code standard and the
  device manual — do not assume a color means the same thing everywhere.
* **Cold-junction compensation** happens at the **card or transmitter**, where
  the reference-junction temperature is measured and corrected. It is a
  property of the instrument, not the field wiring — but it only works if the
  matched extension wire carries the signal unbroken to that point.
* **Keep low-level signal cable away from power and VFD cabling** — the
  millivolt/low-resistance signal is highly susceptible to coupled noise.

## 6. Grounding, shielding, EMC

* **Shielded cable, shield grounded at ONE end only** for these low-frequency,
  low-level signals — the shield drains capacitively coupled noise without
  becoming a conductor between two grounds. Grounding a shield at both ends
  across any ground-potential difference carries 50/60 Hz hum into the signal.
  This is the same single-end policy as other low-frequency analog signals;
  the frequency reasoning is owned by the grounding/bonding and EMC material.
* **Grounded vs ungrounded TC junction:** a *grounded* junction (bonded to the
  sheath) responds faster but ties the signal to the process ground — a
  potential ground-loop source; an *ungrounded* (isolated) junction is slower
  but electrically floating, preferred where ground loops or isolation matter.
  Selection is application-specific.
* **Ground loops corrupt millivolt signals:** two ground references at
  different potentials drive circulating current that appears as an offset or
  noise on the tiny TC/RTD signal. Single-point grounding, ungrounded
  junctions, or isolated inputs break the loop.
* **Separation from power / VFD cable** — routing RTD/TC cable in the same
  tray as VFD motor cable couples PWM noise into the measurement; keep them
  segregated (separation classes owned by the EMC material). Generally
  accepted practice — verify for your installation.

## 7. Common mistakes

1. **Copper extension wire on a thermocouple** instead of matched TC wire —
   creates an unintended junction and a temperature error that tracks the
   transition-point temperature.
2. **Thermocouple polarity reversed** — the reading moves the wrong way or
   reads a large offset; compounded by region-varying color codes.
3. **2-wire RTD on a long run** — lead resistance adds directly to the
   reading, a steady positive temperature error that grows with cable length.
4. **RTD/TC cable in the tray with VFD motor cable** — PWM noise couples into
   the low-level signal; the reading is noisy only while the drive runs.
5. **Shield grounded at both ends** — the screen becomes a ground-loop
   conductor and injects 50/60 Hz hum into the millivolt signal.
6. **Mixing TC types, or the wrong card type** — a Type J sensor on a Type K
   card (or mismatched extension) applies the wrong characteristic and reads
   a systematic error.

## 8. Verification

* **Signal injection:** inject a known resistance (RTD decade box) or millivolt
  value (TC source) at the field terminals and confirm the input reads the
  corresponding temperature — verifies the card independently of the sensor.
  Record on the loop sheet.
* **Known-temperature check:** compare the reading against a reference
  thermometer at a known/ambient temperature, or an ice-point/bath reference.
* **Lead-resistance check (RTD):** verify lead resistance is within the
  configuration's tolerance (especially before trusting a 2- or 3-wire point).
* **Type/polarity confirmation:** confirm sensor type matches the card
  configuration and TC polarity is correct before closing out the point.

## 9. Standards references

* **IEC 60751** — industrial platinum RTDs: standard characteristic (Pt100
  etc.) and tolerance classes (category-level reference).
* **IEC 60584** — thermocouples: TC types (J, K, T, E, N, R, S, B),
  reference tables, and tolerances; region color codes referenced to the
  applicable part (category-level reference).
* **NFPA 79 / IEC 60204-1** — machine electrical wiring-practice chapters:
  conductor identification, routing, and separation of low-level signal from
  power (chapter-level).
* Device manuals and the applicable TC color-code standard are the authority
  for terminal designations, color codes, and card configuration.
