<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "100"
  article_title: "Definitions"

INDEX_TAGS:
  topics: ["definitions", "terminology", "ahj", "sccr", "listed", "grounding"]
  systems: ["all"]
-->

# NEC 2023 — Article 100 — Definitions

## 0. Why definitions matter

NEC uses precise technical language. Using a term incorrectly leads to misapplied requirements. This file covers definitions most relevant to industrial control panel design and machine installation. All definitions are paraphrased — consult the NEC 2023 official text for exact language.

## 1. Authority and approval

**Authority Having Jurisdiction (AHJ):** The organization, office, or person responsible for enforcing a standard, or their designated representative. In practice: the local electrical inspector, fire marshal, or third-party inspection agency. The AHJ has final approval authority.

**Approved:** Acceptable to the AHJ.

**Listed:** Equipment, materials, or services included in a list published by a nationally recognized testing laboratory (NRTL — e.g., UL, ETL/Intertek, CSA). Listing implies evaluation against an applicable product standard. For industrial control panels, listing to UL 508A satisfies NEC Article 409 requirements.

**Labeled:** Equipment to which a label, symbol, or identifying mark has been affixed by an NRTL. Distinct from listed in some contexts; an item can be labeled but the listing scope matters.

## 2. Circuit types

**Branch Circuit:** The conductors between the last overcurrent protective device and the outlets. In a control panel context: the circuit from the branch circuit breaker to a motor starter, drive, or other load.

**Feeder:** Conductors between the service equipment (or a separately derived system) and the final branch circuit overcurrent device. In a facility: the cable from the main switchgear to a sub-panel or MCC.

**Service:** The conductors and equipment that deliver energy from the serving utility to the premises wiring system. The service ends at the service disconnecting means.

**Separately Derived System:** A premises wiring system whose power is derived from a source of electrical energy having no direct connection to supply circuit conductors other than those established by grounding. Common example: isolation transformer secondary, generator.

## 3. Grounding and bonding

**Ground:** A conducting connection, intentional or accidental, between an electrical circuit/equipment and earth, or to some conducting body that serves in place of earth.

**Grounded (Grounding):** Connected to ground or to a conductive body that extends the ground connection.

**Grounded Conductor:** A system or circuit conductor that is intentionally grounded. In US systems: the neutral conductor.

**Equipment Grounding Conductor (EGC):** The conductive path that provides a fault-current return path and ensures equipment exposed metal parts remain at ground potential. The green wire (or bare wire) in a cable assembly.

**Bonding (Bonded):** Connected to establish electrical continuity and conductivity. Bonding ensures metal parts that could become energized are at the same potential.

**Bonding Jumper:** A conductor or device ensuring required electrical conductivity between metal parts required to be electrically connected.

**Ground Fault:** An unintentional, electrically conducting connection between an ungrounded conductor and normally non-current-carrying conductors, metallic enclosures, metallic raceways, or earth.

## 4. Equipment and installations

**Controller:** A device or group of devices that serves to govern, in some predetermined manner, the electric power delivered to the apparatus to which it is connected. Broader than just a motor starter.

**Disconnecting Means:** A device or group of devices by which the conductors of a circuit can be disconnected from their source of supply.

**Industrial Control Panel (ICP):** An assembly of two or more components consisting of one of the following: (1) power circuit components only, such as motor controllers, overload relays, fused disconnect switches, and circuit breakers; (2) control circuit components only, such as push buttons, pilot lights, selector switches, timers, switches, and control relays; or (3) a combination of power and control circuit components with associated wiring, terminal blocks, pilot devices, and similar components. [See also Art. 409]

**Motor Control Center (MCC):** An assembly of one or more enclosed sections each having a common power bus and primarily containing motor control units. A specialized form of industrial control panel.

**Panelboard:** A single panel or group of panel units designed for assembly in the form of a single panel, including buses and with or without switches and OCPDs for the control of light, heat, or power circuits. Governed by Art. 408.

**Switchboard:** A large single panel, frame, or assembly of panels with switches, buses, instruments, overcurrent devices, and other equipment. Generally accessible from the rear as well as front. Governed by Art. 408.

**Switchgear:** An assembly completely enclosed on all sides and top with sheet metal. More robust than a switchboard; typically rated for higher available fault current.

**Utilization Equipment:** Equipment that uses electric energy for electronic, electromechanical, chemical, heating, lighting, or similar purposes.

## 5. Electrical properties

**Ampacity:** The maximum current a conductor can carry continuously under defined conditions without exceeding its temperature rating.

**Continuous Load:** A load where the maximum current is expected to continue for 3 hours or more. OCPDs and conductors must be sized at 125% of the continuous load.

**Overcurrent:** Current in excess of the rated current of equipment or the ampacity of a conductor. May result from overload, short circuit, or ground fault.

**Short-Circuit Current Rating (SCCR):** The prospective symmetrical fault current at a nominal voltage that the equipment can withstand. Must be marked on industrial control panels per Art. 409.110.

**Voltage to Ground:** For grounded circuits: voltage between the given conductor and the grounded conductor or point. For ungrounded circuits: voltage between the given conductor and any other conductor.

## 6. Locations and wiring environments

**Exposed (as applied to wiring methods):** On or attached to the surface, or behind panels designed to allow access.

**Concealed:** Rendered inaccessible by the structure or finish of the building.

**Wet Location:** An installation where water or other liquids may drip, splash, or flow on the wiring. Outdoor locations and locations subject to saturation with water.

**Damp Location:** A location protected from weather but subject to moderate moisture — partially protected outdoor locations, unheated spaces, cold-storage rooms.

**Dry Location:** Not normally subject to dampness or wetness.

**Raceway:** An enclosed channel of metallic or nonmetallic materials designed for holding wires, cables, or bus bars. Includes conduit, cable tray, wireway.

## 7. Change log

- 2026-03-08 — Initial draft created; focused on terms most relevant to industrial control panel design and machine installation.
