<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — wire sizing workflow (conductor, OCPD, overload)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, conductor_sizing, ampacity, voltage_drop, ocpd, overload, article_430, article_310]
  systems: [motor_control, control_panels, machine]
-->

# Wiring Practices — Wire Sizing Workflow

Distilled engineering knowledge behind the site guide "Wire Sizing
Walkthrough." Requirements are paraphrased at chapter/article level with
references; field practice not derivable from a standard is flagged as
generally accepted practice.

## 1. The decision chain

Conductor sizing is a sequence, not a single lookup. Each step has its own
rule and its own basis current:

1. **Load-current basis** — table FLC for motor circuits (NEC 430.6(A)
   principle), rated input current for drives (NEC 430.122), calculated or
   nameplate load for non-motor circuits.
2. **Minimum required ampacity** — apply the applicable multiplier
   (125% for motor branch conductors per NEC 430.22; 125% of continuous
   load per NEC 210.19/215.2 for general circuits).
3. **Conductor selection** — pick a size whose *corrected and adjusted*
   ampacity meets the requirement (NEC Art. 310; ambient correction via
   the 310.15(B) equation, bundle adjustment via Table 310.15(C)(1)).
4. **Termination check** — usable ampacity is capped by the termination
   temperature rating, normally 75 °C for industrial gear ≥ 100 A class
   and 60 °C or 75 °C below that (NEC 110.14(C) principle).
5. **Voltage-drop check** — informational in the NEC (210.19(A) and
   215.2(A) Informational Notes suggest 3% branch/feeder, 5% combined);
   effectively mandatory for performance on long runs and low-voltage
   circuits. Whichever of ampacity or voltage drop demands the larger
   conductor governs.
6. **OCPD** — for motor branch circuits, sized from Table 430.52(C)(1)
   multipliers on table FLC, next-standard-size-up permitted by exception;
   standard ratings enumerated in NEC 240.6(A). For non-motor circuits the
   OCPD protects the conductor directly (NEC 240.4).
7. **Overload** — motor overload protection set from **nameplate FLA**,
   not table FLC (NEC 430.32); 125% for SF ≥ 1.15 or rise ≤ 40 °C,
   115% otherwise.

## 2. FLA vs FLC discipline (NEC 430.6(A) principle)

* Conductors, branch-circuit OCPD, and disconnect sizing use the NEC
  full-load current **tables** (430.247/.248/.250) — deliberately, so the
  installation does not shrink when a replacement motor has a slightly
  different nameplate.
* Overload protection uses the **nameplate FLA**, because the overload
  protects the specific motor installed.
* Mixing these up is the most common wire-sizing error in the field.

## 3. Corrections and adjustments (NEC Art. 310)

* Table ampacities assume 30 °C ambient and ≤ 3 current-carrying
  conductors. Both assumptions fail routinely in industrial installations
  (hot mezzanines, loaded wireways).
* Ambient correction: the 310.15(B) equation scales ampacity by
  sqrt((Tc − Ta')/(Tc − Ta)) — the procedure is cited, table values are
  not reproduced here.
* Bundle adjustment: Table 310.15(C)(1) percentages by count of
  current-carrying conductors; applies to raceways and to cables bundled
  longer than the stated threshold length.
* Corrections may start from the conductor's insulation-rating column
  (often 90 °C for THHN/XHHW-2), but the final value delivered to the
  termination may not exceed the termination-rating column — the 90 °C
  column is correction headroom, not usable ampacity. NEC 110.14(C)
  principle.

## 4. Voltage drop

* NEC treats voltage drop as informational; NFPA 79 and IEC 60204-1
  address it through the general requirement that equipment operate
  correctly over the supply-tolerance band (IEC 60204-1 Cl. 4; NFPA 79
  Ch. 4 operating-condition provisions).
* K-factor estimate (VD = K × I × L × multiplier / cmil) is adequate up to
  roughly 4/0 AWG near unity power factor; larger sizes or low power
  factor warrant the NEC Chapter 9 Table 9 impedance method. Generally
  accepted practice.
* Rule of thumb: at 460 V three-phase, ampacity governs typical in-plant
  runs; voltage drop starts governing on runs of several hundred feet.
  At 120 V AC and 24 V DC, voltage drop governs almost immediately.
  Generally accepted practice — verify by calculation for each run.

## 5. OCPD selection

* Motor branch-circuit OCPD (Table 430.52(C)(1) multipliers: 250% inverse
  time breaker, 175% dual-element fuse on table FLC) protects against
  short-circuit and ground fault **only** — the overload relay handles
  sustained overcurrent. The OCPD is intentionally larger than the
  conductor ampacity; this is code-compliant for motor circuits and often
  alarms engineers seeing it for the first time.
* Next standard size up permitted when the multiplier lands between
  240.6(A) standard ratings (430.52(C)(1) Exception 1); further increases
  for starting problems are bounded by Exception 2 percentages.
* Equipment grounding conductor size follows the OCPD rating
  (Table 250.122 basis), so an OCPD change ripples into the EGC.

## 6. Scope boundaries

* **NEC (NFPA 70)** governs premises wiring up to the machine; **NFPA 79**
  governs wiring within the industrial machine's electrical equipment
  (NFPA 79 Ch. 12 conductor provisions align with but are not identical
  to Art. 310); **IEC 60204-1** is the international counterpart
  (Cl. 12 conductors, Cl. 7 protection) with different base tables and a
  design-current method.
* A US machine build typically sizes to NFPA 79/NEC and documents IEC
  60204-1 equivalence only when contractually required. Generally
  accepted practice — verify project requirements.

## 7. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/wire-sizing/.
