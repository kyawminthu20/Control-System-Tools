<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — panel grounding and bonding
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, grounding, bonding, protective_earth, functional_earth, shielding, emc]
  systems: [industrial_control_panel, machine, drive_systems]
-->

# Wiring Practices — Panel Grounding & Bonding

Distilled engineering knowledge behind the site guide "Panel Grounding &
Bonding Practice." Requirements are paraphrased at chapter/article level;
field practice not derivable from a standard is flagged as generally
accepted practice.

## 1. The three distinct jobs

Grounding/bonding failures usually trace to conflating three functions that
share hardware but have different physics:

* **Safety fault return (bonding to source):** a low-impedance path from any
  faulted enclosure back to the source winding so the OCPD opens. NEC
  250.4(A)(5) is explicit that the earth is not this path — earth impedance
  is too high to reliably operate a breaker. The path is copper: EGC/PE
  conductors and bonding jumpers back to the source bond point.
* **Equipotential bonding (touch potential):** all simultaneously accessible
  conductive parts held at the same potential — IEC 60204-1 Clause 8 and
  NFPA 79 Ch. 8. This is about voltage *between* parts during a fault or
  induced event, independent of whether the OCPD ever trips.
* **Functional/noise grounding (FE):** a stable reference for electronics
  and a drain for shield/EMI currents. NFPA 79 Ch. 8 and IEC 60204-1 Cl. 8
  both allow FE arrangements but never at the expense of the PE function —
  FE ultimately bonds to the PE system at one point.

Grounding (earth connection) exists mainly for overvoltage/lightning
stabilization (NEC 250.4(A)(1)–(2)); bonding clears faults. The two words
are not interchangeable.

## 2. Supply-system context

* The upstream earthing arrangement (TN-S / TN-C-S / TT / IT per IEC
  terminology; solidly grounded / ungrounded / impedance-grounded per NEC)
  determines what the PE conductor is expected to do during a fault and
  whether the first fault trips anything at all. NEC 250.4(B): ungrounded
  systems still require EGCs, bonding, and an effective fault path.
* IEC 60204-1 Clause 5 requires a machine to present a single external PE
  terminal; sizing of the external protective copper conductor follows
  IEC 60204-1 Table 1 (values not reproduced here).

## 3. Sizing (procedures cited, values never reproduced)

* **NEC:** EGC sized from the rating of the upstream OCPD per Table 250.122;
  bonding jumpers per 250.102; separately derived systems (e.g., control
  transformer secondaries) bonded per 250.30 — system bonding jumper at the
  source, one point only.
* **NFPA 79:** grounding conductor sized from the largest upstream OCPD per
  Table 8.2.2.3 basis; green or green/yellow reserved exclusively for
  grounding conductors (Ch. 8, Ch. 16 color rules).
* **IEC 60204-1:** external PE conductor per Table 1 (Clause 5); protective
  bonding circuit continuity and cross-sections per Clause 8, which defers
  detailed sizing to the IEC 60364-5-54 method.

## 4. Panel PE bus practice

* Single PE bus/bar bonded to the enclosure and to the incoming PE terminal;
  every EGC lands on the bus individually — one conductor per terminal, no
  daisy-chaining, so removing one device never opens another device's fault
  path (NFPA 79 Ch. 8 principle).
* Hinges, slides, and bearing surfaces are not acceptable bonding paths
  (NFPA 79 Ch. 8; IEC 60204-1 Cl. 8). Doors and removable plates carrying
  electrical devices get a flexible bonding strap or conductor.
* Paint is an insulator: bond points scraped to bare metal, or serrated
  (star) washers / thread-forming hardware that bites through the coating —
  generally accepted practice, and the classic UL field-evaluation failure.
* Backplane-to-enclosure and enclosure-to-PE-bus bonds made with dedicated
  hardware, not relying on mounting screws through paint. Generally
  accepted practice — verify for your installation.

## 5. Functional grounding and shields

* One documented shield-landing rule per signal class. Low-frequency analog
  (4–20 mA, thermocouple, RTD): shield grounded at one end only — usually
  the panel end — to avoid circulating power-frequency current through the
  shield. VFD motor cable: shield/gland bonded 360° at **both** ends,
  because the job there is a high-frequency common-mode return, not
  low-frequency loop avoidance. Both are generally accepted practice —
  verify against device EMC instructions.
* "Isolated"/instrument ground bars are insulated from the mounting surface
  so shield/reference current takes one deliberate path — but the bar is
  still bonded to the PE system at a single point. An IG conductor is never
  floating (NEC 250.4 purposes; 250.146(D) concept at article level).
* Inter-panel and inter-building signal references: bonding two distant
  grounds through a cable shield invites circulating current; galvanic
  isolation or fiber breaks the loop. Generally accepted practice.

## 6. Verification

* IEC 60204-1 Clause 18 (Verification) requires, among its test sequence,
  verification of continuity of the protective bonding circuit with a test
  current — measured, not assumed. Fault-loop impedance verification applies
  on TN systems.
* Torque per manufacturer values, witness-marked; re-check after transport.
  Generally accepted practice.

## 7. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/grounding-bonding/.
