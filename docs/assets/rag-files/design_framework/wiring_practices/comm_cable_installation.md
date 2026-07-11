<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — communication cable installation (routing, termination, segregation)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, communications, ethernet, rs485, profibus, shielding, emc, segregation, termination, m12]
  systems: [control_panels, networked_io, fieldbus, machine_networks]
-->

# Wiring Practices — Communication Cable Installation

Distilled engineering knowledge behind the site guide "Communication Cable
Installation in Machines & Panels." This is the installation-practice
companion to the communications physical-layer pages: it covers the physical
routing, termination, and segregation of comm cable in real machines, not
the electrical/protocol layer. Protocol theory, encoding, and the electrical
physical layer are owned by the `/communications/` pages and are not
re-derived here. Requirements are paraphrased at chapter/article level with
references; field practice not derivable from a standard is flagged as
generally accepted practice.

## 1. Scope and terminal groups

Comm cable is the machine's nervous system. In a typical machine it spans a
few media families, each with its own installation rules:

* **Industrial Ethernet** — copper (PROFINET, EtherNet/IP, Modbus TCP) on
  RJ45 or M12, and fiber for long runs or galvanic isolation.
* **RS-485 multidrop** — PROFIBUS DP, Modbus RTU; a terminated two-end bus,
  not a free topology.
* **Device-level buses** — IO-Link, sensor/actuator cordsets, typically M12.

This note covers physical installation only: cable/connector selection,
routing and segregation, termination, shielding at the panel/gland, and
verification. The electrical and protocol layers live on the
`/communications/` pages.

## 2. Media and connector selection (decided upstream)

The medium and topology come from the network design, not the panel floor.
Copper category/rating, fiber type, and RS-485 cable characteristics are
selected on the physical-layer pages; the installer implements them.

* **Copper category/rating** — match the cable rating to the protocol and
  environment (e.g. flex/robotic rating for moving cable, oil/weld-spatter
  rating on the shop floor). Vendor cordset ratings are vendor-specific —
  consult the manufacturer's datasheet. Generally accepted practice.
* **Connector system** — M12 (D-code/X-code for Ethernet, B-code for
  PROFIBUS) for on-machine, sealed, vibration-prone points; RJ45 inside the
  panel or in benign environments. The choice is an environment/ingress
  decision, not a preference.
* **Fiber** is chosen for distance beyond copper's reach, high-EMI
  environments, or where galvanic isolation between panels is wanted.

## 3. Mechanical protection — rating, bend radius, pull tension

Comm cable has no ampacity question; its "sizing and protection" is
mechanical.

* **Bend radius.** Every comm cable has a minimum bend radius (tighter for
  fiber, and a separate smaller value for flexing vs fixed installs). The
  exact figure is vendor-specific — consult the datasheet. Exceeding it
  degrades return loss on copper and can microbend or break fiber. Generally
  accepted practice.
* **Pull tension.** Data cable is far more tension-sensitive than power
  cable; over-pulling stretches pairs and permanently degrades performance.
  Use the cable's rated maximum pull force and pulling eyes/lubricant as
  appropriate. Generally accepted practice.
* **Strain relief.** Terminate to a gland or clamp that carries mechanical
  load, so the connector contacts never take the strain. Provide a service
  loop at each end.

## 4. Routing and segregation (the core)

Keeping comm cable away from power is the single highest-leverage
installation decision. NFPA 79 (wiring methods and practices chapter) and
IEC 60204-1 (wiring clause) require conductor routing and separation that
avoids interference between power and signal circuits; the machine-network
consequences are the practical reason.

* **Separate from VFD/servo motor cables and other power.** The PWM output
  of a drive is the worst offender for coupling into a data cable running
  parallel to it. Route comm cable in its own tray/duct, or use a divider or
  a separated tray level; keep clearance from power. The `/communications/`
  intermittent-I/O case study documents exactly this failure — a network
  cable sharing a tray with motor leads produced intermittent, run-dependent
  I/O faults. Generally accepted practice — verify against your EMC plan.
* **Cross power at right angles.** Where a comm cable must cross power
  wiring, cross at 90 degrees to minimize the coupling length. Generally
  accepted practice.
* **Separation grows with parallel run length.** The longer the parallel
  run, the more separation (or a physical barrier) is needed; a short
  crossing is far less of a problem than a long parallel haul. The specific
  separation classes and distances are owned by the EMC mitigation guide.
* **Never bundle comm with motor/drive output cable** in the same clamp or
  tie. Generally accepted practice.

## 5. Termination and connectors

* **Field-terminated RJ45 vs pre-made cordsets.** Pre-made, tested cordsets
  are preferred wherever there is vibration or motion; a field-crimped RJ45
  in a vibrating machine is a classic intermittent-fault source. Field
  termination is acceptable in benign, static panel locations by trained
  hands with the right tooling. Generally accepted practice.
* **M12 torque.** M12 connectors are torqued to the connector maker's spec
  to achieve the sealing and contact rating — consult the manual; do not
  hand-tighten by feel. Generally accepted practice.
* **360-degree shield termination.** Land the cable shield in a full-
  circumference gland or EMC clamp at the panel entry or connector, not a
  pigtail — a pigtail is a significant impedance at network frequencies.
  Generally accepted practice.
* **RS-485/PROFIBUS bus termination.** A multidrop RS-485 bus is terminated
  at its two physical ends only (PROFIBUS uses the connector's switchable
  terminator; Modbus RTU uses the characteristic-impedance resistor).
  Missing, doubled, or mid-bus termination causes reflections and
  intermittent comms. The termination values and topology rules are owned by
  the RS-485 physical-layer page.
* **Service loops.** Leave slack at each end for re-termination and strain
  relief.

## 6. Grounding, shielding, and EMC

The deep treatment is owned by the EMC mitigation and grounding/bonding
guides; only comm-specifics here.

* **Shield/drain policy is per-medium.** Industrial Ethernet shields are
  commonly bonded at both ends through the connector/gland (the shielding
  system is designed for it); low-frequency signal screens are sometimes
  single-end grounded to avoid loops. Follow the physical-layer page and the
  device manual for the specific medium — do not apply one rule universally.
  Generally accepted practice.
* **Panel entry glands.** Bond the shield to the enclosure at the point of
  entry with an EMC gland; mask/scrape paint at the bond point.
* **Fiber for galvanic isolation.** Where ground-potential differences
  between panels are a concern, fiber removes the copper path entirely and
  is the clean fix.

## 7. Common mistakes

1. **Comm cable in the same tray as VFD motor cable** — parallel coupling
   from the drive output; intermittent, run-dependent network faults.
2. **Field-crimped RJ45 in a vibrating machine** — contacts work loose;
   link errors that come and go with machine motion.
3. **Exceeded bend radius** — degraded return loss on copper, microbending
   or breakage on fiber; marginal links that fail intermittently.
4. **Missing or incorrect bus termination** — reflections on an RS-485/
   PROFIBUS segment; garbled or dropped frames.
5. **Shield not landed at the gland** — the shield is continuous but not
   bonded to the enclosure; EMC performance lost.
6. **Daisy-chaining where a star was designed** — an installer chains
   devices the network design intended as a star through a switch, changing
   the topology and its fault behavior.

## 8. Verification

* Baseline packet capture at commissioning (the `/communications/`
  Wireshark methodology page) so a healthy baseline exists to compare
  against later; error counters read at the managed switch.
* Continuity/wiremap test for copper; DOM (digital optical monitoring) power
  levels for fiber.
* Physical inspection of glands, torque, bend radius, service loops, and
  segregation against the routing plan.

## 9. Standards references

* **NFPA 79** — wiring methods and practices chapter (conductor routing,
  separation of power and signal, identification), at chapter level.
* **IEC 60204-1** — wiring clause (conductor routing and practices for
  machine electrical equipment), at clause level.
* Physical-layer/protocol requirements: the `/communications/` pages.
