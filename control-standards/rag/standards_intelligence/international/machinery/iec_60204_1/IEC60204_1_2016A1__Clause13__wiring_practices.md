<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_60204_1
EDITION: "2016+AMD1:2021 (CSV Ed. 6.1)"

IEC_HIERARCHY:
  clause: "13"
  clause_title: "Wiring practices"

INDEX_TAGS:
  topics: ["wiring_practices", "routing", "segregation", "terminations", "ducts", "flexible_conduit"]
-->

Clause 13 of **IEC 60204-1** (2016+AMD1:2021) covers **wiring practices**: how conductors selected under Clause 12 are actually routed, supported, terminated and identified inside and on the machine.

This is the clause that most directly governs what a panel actually looks like when it is opened.

---

## 0. Scope

This clause specifies requirements for the installation of the wiring, including:

* connections and terminations;
* routing and support of conductors, in ducts, trunking and enclosures;
* segregation of circuits;
* wiring to devices on moving parts and outside enclosures;
* identification of conductors.

## 1. Connections and Terminations

* Connections must be secure, mechanically and electrically sound, and made in a way appropriate to the conductor and the terminal — a terminal is designed for a defined conductor type and number.
* **One conductor per terminal** is the general expectation; where a terminal is not designed for it, doubling up conductors is not acceptable practice.
* Terminals must be accessible for installation and maintenance, and marked in accordance with the reference designations (Clause 16) so that a conductor can be traced to the schematic.
* Soldered connections and connections subject to vibration require particular care; conductors must not be subject to undue mechanical stress at the termination.

## 2. Routing, Support and Segregation

* Conductors and cables must be routed and supported so that they are protected from mechanical damage and not subject to strain.
* Where conductors of **different circuit types** run together, they must be handled so that no circuit compromises another. This is where the standard's requirements and good EMC practice meet: power conductors and sensitive signal conductors are segregated, and screened cables are used and terminated so that the screen actually performs.
* Ducts and trunking must not be so densely filled that heat cannot escape — cable fill couples back to the current-carrying capacity assumptions made in Clause 12.
* Circuits that remain **live when the supply disconnecting device is off** (external interlock feeds, control power from another source) must be handled and identified so that a technician is not surprised by them — see also the multi-supply warning requirements.

## 3. Wiring Outside Enclosures and to Moving Parts

* Wiring outside enclosures must be protected against the environment and against mechanical damage, using appropriate cable constructions, conduit, or ducts.
* Connections to devices on **moving parts** must use cable suitable for continuous flexing and be installed so that the flexing is not concentrated at the termination — the failure mode is nearly always at the gland or the terminal, not in the middle of the run.

## 4. Identification

Conductors must be identifiable at each termination — by colour, number, or alphanumeric code — consistently with the schematics. Protective conductors carry the reserved identification (green-and-yellow), which must not be used for any other purpose.

## 5. Cross-References

* **Clause 12** — conductors and cables (selection; cable fill affects the ampacity assumed there).
* **Clause 8** — equipotential bonding; the protective bonding circuit.
* **Clause 16** — marking and reference designations (terminations must match).
* **Clause 18** — verification (continuity of the protective bonding circuit is tested here).
* US equivalent — NFPA 79 wiring-methods and wiring-practice chapters.
* Site guides — `/design/wiring/` covers the field practice of routing, segregation and EMC mitigation in depth.

## 6. Change Log

* 2026-07-12 — **Created in the Phase 45 accuracy pass.** Clause 13 previously had **no file at all**: the corpus module skipped it entirely, and the clause numbering downstream was wrong as a result. Corrected against the official IEC 60204-1:2016+AMD1:2021 contents.

## 7. Coverage Note

**Gap — depth pass pending.** This file establishes the correct clause and its principles. It has **not** been verified against the purchased text of the standard, and carries **no table values** (fill factors, bend radii, separation distances) — those are licensed content and are not stored in this corpus. Consult the published standard for any numeric limit.
