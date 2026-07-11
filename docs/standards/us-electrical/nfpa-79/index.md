---
layout: default
title: "NFPA 79 — Electrical Standard for Industrial Machinery"
description: "NFPA 79:2024 — scope, per-chapter depth, worked example, common mistakes, practical checklist, and lifecycle application."
breadcrumb:
  - name: "Standards"
    url: "/standards/"
  - name: "US Electrical"
    url: "/standards/us-electrical/"
  - name: "NFPA 79"
repo_path: "control-standards/rag/standards_intelligence/us/nfpa79/"
related_standards:
  - name: "IEC 60204-1 (International equivalent)"
    url: "/standards/machinery/iec-60204-1/"
  - name: "NEC (NFPA 70)"
    url: "/standards/us-electrical/nec/"
  - name: "UL 508A"
    url: "/standards/us-electrical/ul-508a/"
crosswalk_refs:
  - name: "NFPA 79 ↔ IEC 60204-1 Overlap"
    url: "/tools/crosswalks/nfpa79-iec60204/"
lifecycle_stage:
  - name: "Detailed Design"
    slug: "detailed-design/"
  - name: "Build"
    slug: "build/"
  - name: "Installation"
    slug: "installation/"
review:
  standard: "NFPA 79"
  edition: "2024"
  status: "Reviewed"
  coverage: "All 20 chapters at chapter level; worked example and common mistakes"
  last_reviewed: "May 2026"
---

<div class="page-header">
  <span class="page-header__label">US Electrical Standards · NFPA 79</span>
  <h1>NFPA 79:2024 — Electrical Standard for Industrial Machinery</h1>
</div>

## Quick Start

- **Scope cutoff.** NFPA 79 covers a machine's electrical and electronic equipment up to **600 V nominal**, starting at the supply-conductor connection point. Above that voltage or upstream of that point, you are in NEC territory.
- **NEC handoff.** NEC Article 670 references NFPA 79 for industrial-machinery design but governs the **site installation** (feeder, raceway runs, building disconnect, available-fault-current verification). NEC Article 409 governs UL-listed industrial control panels at the site.
- **NFPA 79 vs. IEC 60204-1.** Choose NFPA 79 for US/North-American markets; choose [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) for CE-marked machines under the Machinery Directive. Wire-color rules, voltage scope, and Technical Construction File requirements differ — pick the destination market early; a clean swap mid-design is rare.
- **Where Chapter 9 stops.** NFPA 79 specifies stop-category architecture (0/1/2) and E-stop device requirements, but the **safety-function reliability metrics** (Performance Level, SIL) come from [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) or [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}). A Cat-1 controlled stop on PLd / SIL 2 dual-channel architecture is a typical pairing.
- **UL 508A overlay.** When the machine ships with a UL-listed control panel, [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) governs panel construction (component selection, spacing, SCCR documentation per Supplement SB4). NFPA 79 governs the electrical design; the two interlock rather than overlap.

---

## Standard Overview

| Field | Value |
|-------|-------|
| **Standard ID** | NFPA 79 |
| **Edition** | 2024 |
| **Publisher** | National Fire Protection Association (NFPA) |
| **Jurisdiction** | United States |
| **Scope** | Electrical/electronic equipment for industrial machines |
| **Repository** | `control-standards/rag/standards_intelligence/us/nfpa79/` — 20 chapters |
| **Status in Corpus** | Complete |

**Purpose.** NFPA 79 covers the electrical and electronic equipment, apparatus, and wiring of industrial machinery operating at a nominal voltage not exceeding 600 V. It applies to the point of connection of the supply conductor(s) to the machine and covers all electrical equipment after that point.

---

## Chapter Reference

The chapters below are the most-consulted by machine builders. Chapters in **bold** are covered in depth in the next section.

| Chapter | Title | IEC 60204-1 equivalent |
|---------|-------|------------------------|
| **4**  | **General Conditions of Installation** | Cl 4 |
| **5**  | **Disconnecting Means** | Cl 5 |
| **6**  | **Overcurrent Protection** | Cl 7 |
| **7**  | **Protection Against Electric Shock** | Cl 6 |
| **8**  | **Grounding and Bonding** | Cl 8 |
| **9**  | **Control Circuits and Control Functions** | Cl 9, 10 |
| 10 | Operator Interface and Control Devices | Cl 10 |
| 11 | Control Equipment | Cl 11 |
| 12 | Motors and Associated Equipment | Cl 12 |
| **15** | **Transformers and Power Supplies** | Cl 9.1 |
| **16** | **Wiring Methods** | Cl 13 |
| 17 | Cables and Flexible Cords | Cl 13 |
| 18 | Terminal Blocks, Connectors, and Wiring Devices | Cl 13.1.3 |
| **19** | **Marking and Documentation** | Cl 16, 17 |

---

## Per-Chapter Depth

### Chapter 4 — General Conditions of Installation

The installation conditions chapter sets baseline expectations for ambient environment, working space, and enclosure protection. Standard equipment is rated for altitudes up to **1000 m (3300 ft)** without derating; above that, convection cooling weakens and the dielectric strength of air drops, so component ratings shift. Operating handles for disconnects and primary controls should sit between **0.6 m and 1.9 m** above floor for ergonomic access. Working space around control panels follows NEC 110.26 (typically 3 ft of clear depth in front). Enclosures containing live parts at 50 V or above require a tool or key to open, or the door must be interlocked with the main disconnect so power is removed before access.

### Chapter 5 — Disconnecting Means

Every machine has a single main disconnect — a listed motor-circuit switch, a listed molded-case circuit breaker, or a listed molded-case switch. The handle is mechanically linked to the device, located outside the enclosure, and clearly marks **ON (I)** and **OFF (O)**. It must be **padlockable in the OFF position only** — never in ON — and the lockout mechanism must be a permanent part of the switch (a removable hasp does not qualify). Handle height has a hard ceiling: the centre of the grip in its highest position must not exceed **2.0 m (6 ft 7 in.)** above floor. The enclosure door is mechanically or electrically interlocked with the disconnect so the door cannot open while power is ON, and power cannot be turned ON while the door is open, except via a keyed defeater for qualified work. Line-side terminals (where supply enters the cabinet) remain live with the disconnect OFF and must be guarded — a "WARNING: LIVE TERMINALS" label is required.

### Chapter 6 — Overcurrent Protection

Branch-circuit OCPDs are the first line of defence for the machine's internal wiring. They must be **listed branch-circuit-rated** breakers or fuses; supplemental protectors (the small "mini" breakers used for component-level protection) are **not permitted** as branch-circuit OCP. The 2024 edition requires the machine's **Short-Circuit Current Rating (SCCR)** to be calculated, documented, and labelled — and the available fault current at the install site (governed by NEC Article 670) must be at or below the machine SCCR. Branch-circuit OCP and machine SCCR are separate analyses: OCP protects conductors against overload and short circuit; SCCR is the highest fault current the panel can safely interrupt without component failure. Component combinations matter — a VFD rated 100 kA SCCR only with Class J fuses gives a different machine SCCR if you swap to a thermal-magnetic breaker. OCPDs **must not** be placed in the grounded (neutral/common) conductor; opening it could leave the rest of the system live.

### Chapter 7 — Protection Against Electric Shock

The shock-hazard threshold is **30 V rms (42.4 V peak) AC, or 60 V DC** under dry conditions; above that, specific protective measures are required. Live conductors must be insulated with jackets that can only be removed by destruction, or enclosed behind barriers rated **IP2X or IPXXB** (finger-safe). Stored-energy components (VFD DC-bus capacitors, large filters) must discharge to below **60 V within 5 seconds** after power removal, or carry a label stating the required wait time. Control circuits at PELV/SELV (typically 24 V DC) reduce shock risk significantly — PELV requires one side of the secondary bonded to PE so a ground fault trips the protection rather than energising the frame. Cabinets that cannot be fully de-energised by the main disconnect (external interlock feeds, control power from another source) must carry the standard "more than one disconnect may be required" warning.

### Chapter 8 — Grounding and Bonding

NFPA 79 strictly distinguishes the **grounded conductor** (neutral or common — current-carrying) from the **grounding conductor** (Protective Earth — fault-current path). Every machine has a single primary **PE terminal**, marked with the ground symbol or the letters "PE", to which all internal grounding conductors terminate. The protective bonding circuit must be continuous and cannot rely on hinges, slides, or bearings — moving panels (swing arms, control stations on cabinet doors) need flexible braided copper bonding jumpers anchored at both ends. Grounding conductor colour is **green or green with one or more yellow stripes**; using these colours for any other purpose is a code violation. PE conductor sizing follows the largest upstream OCPD per **Table 8.2.2.3**, not the load current. Common field-evaluation failures: bolting a ground lug to a painted surface (paint insulates — scrape to bare metal or use star-washers that bite through finish), undersizing the conductor, and daisy-chaining grounds device-to-device (each device should have a direct path back to the PE bus). Functional Earth (FE, often pink or pink-with-white) is for EMI/RFI shielding and must still ultimately bond to PE — safety ground is never sacrificed to solve a noise problem.

### Chapter 9 — Control Circuits and Control Functions

Control circuits are designed for **predictability and fail-safe operation**: any single failure (broken wire, welded contact, software crash) should not result in a hazardous condition. Most circuits stop on opening (de-energise-to-stop). NFPA 79 defines three stop categories:

- **Category 0** — immediate, uncontrolled removal of power.
- **Category 1** — controlled stop with power available to actuators, then power removal once stopped.
- **Category 2** — controlled stop with power maintained (not suitable for emergency stops).

E-stop devices are red mushroom-head pushbuttons on a yellow background, self-latching (they stay pressed until manually twisted or pulled out). The E-stop function overrides all other operating modes. **Resetting** the E-stop must not restart the machine — reset only permits a deliberate restart via the start function. Software-implemented safety must run on a **safety-rated controller** (PL or SIL rated) using validated safety blocks; rungs in a standard PLC do not satisfy the integrity requirement for safety-related functions. The system should monitor for control-circuit cross-faults — for example, a 24 V wire shorted to another 24 V wire that would mask an open guard.

### Chapter 15 — Transformers and Power Supplies

Control transformers must have **separate primary and secondary windings** — autotransformers (shared winding) are not permitted for control circuits because they do not provide isolation from the line. DC power supplies (typically SMPS today) must be short-circuit protected; many cases additionally require **Class 2** rating, particularly when feeding limited-energy sensors or networks. Transformer sizing must account for the **magnetising inrush** of all solenoids and contactors that can energise simultaneously — a transformer that meets steady-state load but not inrush will sag, causing safety relays to chatter and PLC CPUs to reboot. Every transformer needs overcurrent protection on the secondary; primary protection is required too, with sizing that accommodates magnetising inrush. Secondary grounding is a design choice with safety consequences: a grounded common is the default — a wire-to-earth fault then trips the OCPD; ungrounded "floating" secondaries require a ground-fault detection scheme.

### Chapter 16 — Wiring Methods

Wiring practices govern the physical craftsmanship of the electrical system. Conductors must be supported so termination strain is not transmitted to terminal blocks (slotted plastic duct inside the panel; conduit or cable tray on the machine). Wiring crossing hinges or moving axes uses extra-flexible stranding anchored at both ends of the flex. Each wire is identified at every termination with a marker matching the schematic. Voltage segregation: conductors of different voltages may share a raceway only if every conductor is insulated for the highest voltage in the group. Low-level signal wires (thermocouple, 4–20 mA) are kept apart from motor leads to prevent crosstalk.

The 2024 wire-colour scheme:

- **Black** — AC power (line voltage).
- **Red** — AC control circuits.
- **Blue** — DC control circuits.
- **Orange** — interlock circuits powered from an external source (live with the main disconnect OFF).
- **Green** or **Green with one or more yellow stripes** — equipment grounding conductor (PE).

The orange rule is the most-missed of the five: any external-source interlock wire must be orange, and the cabinet must carry the multi-source warning called out in Chapter 7.

### Chapter 19 — Marking and Documentation

Every machine carries a permanent nameplate near the main disconnect listing: manufacturer's name, model or serial designation, voltage, frequency, number of phases, full-load current (FLA), and the **Short-Circuit Current Rating (SCCR)** of the panel. Warning signs follow **ANSI Z535** for colour and signal-word conventions (DANGER / WARNING / CAUTION). Every device inside the panel — relays, breakers, PLCs, terminal blocks — is labelled with a reference designation that matches the electrical schematic. Documentation supplied with the machine includes electrical schematics (NFPA/IEEE or IEC symbols), interlock diagrams describing the safety sequence and function, maintenance procedures, recommended spare parts, and the SCCR calculation record. Recent editions place safety-function validation results (when functional safety software is involved) inside the technical documentation set as well.

---

## Worked Example — UL-Listed Packaging Machine for the US Market

**Scenario.** Packaging machine for a US food-and-beverage facility: 480 V 3-phase supply, 50 A FLA, panel-mounted controls, two E-stop zones (operator station + maintenance side), one safety light curtain on the infeed, NEMA 12 enclosure, indoor industrial environment.

1. **Supply disconnect (Ch 5).** A listed molded-case switch sized for the 50 A continuous load with appropriate margin. Handle external to the cabinet, padlockable in OFF only, mounted with the grip ≤ 2.0 m above floor. Door interlock so the panel cannot open with power on.
2. **Branch-circuit OCP and machine SCCR (Ch 6).** Listed branch-circuit OCPDs upstream of motor branches and the control supply. Calculate machine SCCR from the worst-case component combination — a typical 480 V machine using Class J fuses paired with combination motor controllers reaches 65 kA or 100 kA SCCR depending on starter selection. Document on the nameplate; verify the install site's available fault current is ≤ machine SCCR (NEC Article 670 task at the building level).
3. **Wire size and colour (Ch 16).** Conductor ampacity sized per NFPA 79 tables; for 50 A FLA the supply branch typically lands at AWG 6 THHN copper. Power conductors black, AC control red, 24 VDC control blue, PE green or green/yellow. Any external-interlock wire (e.g., a light-curtain feed from a separate disconnect) must be orange — and the cabinet carries the "multiple disconnects" warning.
4. **Grounding and bonding (Ch 8).** Single PE bus in the control panel labelled "PE". PE conductor sized from the upstream OCPD via Table 8.2.2.3 (not from load current). Cabinet door, swinging operator station, and any bolted-on accessories use flexible braided bonding jumpers — paint scraped at lugs or star-washers used. No daisy-chained grounds.
5. **Control transformer for 24 VDC (Ch 15).** Isolated control transformer (not autotransformer) sized to cover the magnetising inrush of all simultaneously-energised solenoids and contactors at start-up. Secondary OCP installed; common bonded to PE so a 24 V short-to-frame trips the secondary fuse. SMPS feeding sensor networks selected as Class 2 where the load profile fits.
6. **E-stop wiring and category (Ch 9).** Both E-stop pushbuttons are red mushroom-head on yellow background, self-latching, wired through a safety relay or safety-PLC inputs. Stop architecture is **Category 1**: the safety relay drops contactors with delay, allowing the drive a controlled deceleration before power removal. The reliability metric (PL / SIL) lives in [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) — a Cat-1 stop on PLd / SIL 2 dual-channel architecture is the typical pairing for a safety light curtain on an infeed.
7. **Nameplate and documentation (Ch 19).** Permanent nameplate listing voltage, frequency, phases, FLA = 50 A, machine SCCR, manufacturer, serial. Inside the panel: every device labelled with the schematic's reference designation. Documentation set: schematics, interlock diagram, safety-function validation record, maintenance procedure, recommended spares, SCCR calculation.

**What NFPA 79 leaves to UL 508A.** Panel construction itself — component spacing, insulation classes, the SCCR documentation per [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) Supplement SB4 — is UL 508A's domain. NFPA 79 governs which circuits exist and how they behave; UL 508A governs how the panel that contains them is built and listed.

**What NEC handles.** Once the machine ships, the [NEC]({{ '/standards/us-electrical/nec/' | relative_url }}) governs the installation: feeder sizing from the building disconnect to the machine, raceway runs, available fault current at the machine's supply terminals, and any required additional disconnect at the wall.

---

## Common Mistakes

1. **Confusing branch-circuit OCP rating with machine SCCR (Ch 6).** They are separate analyses. The panel needs an OCPD upstream that protects the conductor ampacity, **and** a documented machine SCCR per UL 508A SB4 that the install site's available fault current cannot exceed. A panel can carry a 30 A breaker upstream and still hold a 5 kA SCCR — code-compliant on paper, a disaster waiting for an industrial substation.
2. **Using NEC PE colour rules on a machine intended for IEC 60204-1 markets.** NEC 250 permits bare or green PE; IEC 60204-1 mandates yellow-green stripe only. Building a machine for both markets requires picking the more-restrictive rule (yellow-green) up front. This is a common CE audit finding when a US machine builder ships to Europe without adjusting wire colours.
3. **Sizing control transformers from steady-state current and missing magnetising inrush (Ch 15).** Steady-state load may be 50 VA, but contactors closing simultaneously can demand 5–10× that for milliseconds. An undersized transformer causes voltage sag → safety-relay chatter → PLC reboot. NFPA 79's reference library does not assign a specific sub-clause number to this rule; treat it as a chapter-level requirement.
4. **Tying E-stop pushbuttons in series without considering Category 3 / PLd architectural requirements.** The wiring works (the circuit opens on any button press), but the safety architecture per [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) does not — single-channel series wiring fails Cat 3's requirement for fault detection and tolerance. NFPA 79 Chapter 9 does not object; ISO 13849-1 does.
5. **Treating NFPA 79 as the installation code.** It is the **design** code for the machine. Once shipped, NEC Article 670 (Industrial Machinery) governs site installation — feeder, building disconnect, available fault current. A site electrician who reaches for NFPA 79 to size a feeder is reading the wrong document.
6. **Missing the disconnecting-means lockable-in-OFF requirement on shipped machines (Ch 5).** Chapter 5 requires the disconnect to be padlockable in OFF only via a permanent mechanism. Caught at the OEM's factory: free fix. Caught at site commissioning: field rework, new disconnect, re-labelling, and possibly a new UL field evaluation. Every time.

---

## Practical Checklist

#### Design

- [ ] Confirm the machine falls within NFPA 79 scope (≤ 600 V; up to point-of-supply-connection).
- [ ] Pick NFPA 79 vs. IEC 60204-1 by destination market — do not hybridise wire colours or PE rules.
- [ ] Calculate machine SCCR from worst-case component combination; verify expected available fault current at the install site is ≤ machine SCCR.
- [ ] Single main disconnect specified, padlockable in OFF only, ≤ 2.0 m handle height, door-interlocked.
- [ ] Branch-circuit OCPDs are listed branch-circuit type; supplemental protectors only used where genuinely supplemental.
- [ ] Stop categories selected per stop function: 0 for uncontrolled removal, 1 for controlled-then-removed, 2 only where stop-with-power is appropriate (never E-stop).
- [ ] E-stop architecture carries a PL / SIL target from ISO 13849-1 / IEC 62061 — Cat-1 stop on PLd / SIL 2 dual-channel for typical infeed light-curtain protection.
- [ ] Software safety functions run on a safety-rated controller, not on a standard PLC.
- [ ] Control transformer is isolated (not autotransformer); sized for magnetising inrush; secondary OCP and grounding scheme chosen.
- [ ] PE bus single-point in the panel; PE conductor sized from Table 8.2.2.3 (largest upstream OCPD, not load current).

#### Build

- [ ] Wire colours per Ch 16: black AC power, red AC control, blue DC control, orange external-interlock, green or green/yellow PE.
- [ ] Every wire labelled at every termination, matching the schematic.
- [ ] Voltage segregation enforced: conductors of different voltages share a raceway only if all are insulated for the highest voltage.
- [ ] Flexing wires (door, drag chain, robot axis) use extra-flexible stranding rated for continuous flex, anchored at both ends.
- [ ] Bonding jumpers (braided copper) on doors, swing arms, and bolted-on accessories. Paint scraped or star-washers at lugs. No daisy-chained grounds.
- [ ] Capacitor-energy components (drives, large filters) labelled with discharge wait-time if they cannot reach < 60 V in 5 s.
- [ ] Cabinet line-side terminals guarded; "LIVE TERMINALS" label affixed.
- [ ] Multi-disconnect cabinets carry the "more than one disconnect may be required" warning.

#### Ship & Install

- [ ] Permanent nameplate: manufacturer, model, serial, voltage, frequency, phases, FLA, machine SCCR.
- [ ] Component reference designations inside the panel match the electrical schematic.
- [ ] Documentation set ships with the machine: schematics (NFPA/IEEE or IEC symbols), interlock diagram, maintenance procedure, recommended spares, SCCR calculation record, safety-function validation results.
- [ ] Field installer informed that NEC Article 670 governs the installation: feeder sizing, building disconnect, available fault current verification.
- [ ] Pre-energisation check by qualified person: PE continuity, insulation resistance, OCPD ratings audit, disconnect interlock function.

---

## Lifecycle Application

| Stage | NFPA 79 activity |
|-------|------------------|
| [Standards Selection]({{ '/lifecycle/standards-selection/' | relative_url }}) | Confirm scope (≤ 600 V, machine electrical equipment); decide NFPA 79 vs. IEC 60204-1 by destination market; identify required UL listing path (508A) |
| [Detailed Design]({{ '/lifecycle/detailed-design/' | relative_url }}) | Disconnect type and sizing (Ch 5); branch-circuit OCP and machine SCCR (Ch 6); shock-protection scheme (Ch 7); PE bus and bonding plan (Ch 8); stop categories and E-stop architecture (Ch 9 + ISO 13849-1 handoff); control transformer (Ch 15); wiring and colour scheme (Ch 16) |
| [Build]({{ '/lifecycle/build/' | relative_url }}) | Panel construction per design; UL 508A panel listing if required; wire labels and reference designations; bonding jumpers; line-side guarding |
| [Installation]({{ '/lifecycle/installation/' | relative_url }}) | NEC Article 670 governs at the site: feeder sizing, building disconnect, available fault current verification ≤ machine SCCR |
| [Pre-Commissioning]({{ '/lifecycle/pre-commissioning/' | relative_url }}) | PE continuity test; insulation resistance; OCPD ratings audit; disconnect interlock function check; nameplate and documentation review |
| [Commissioning]({{ '/lifecycle/commissioning/' | relative_url }}) | Power-on verification; safety-function validation per ISO 13849-1 / IEC 62061; SCCR calculation record signed off; operator and maintenance documentation handoff |

---

## Relationship to NEC and UL 508A

```
NEC Article 670 (Industrial Machinery) references NFPA 79
        ↓
NFPA 79 governs machine electrical design
        ↓
UL 508A governs panel construction if UL listing required
        ↓
NEC Article 409 governs panel installation
```

**When all three apply.** Machine for the US market with a UL-listed control panel: NFPA 79 defines the electrical design requirements; UL 508A governs panel construction and listing; the NEC covers site installation.

---

## PL / SIL Relevance

NFPA 79 Chapter 9 addresses safety-related control circuits and emergency-stop functions. For formal safety-function design (Performance Level or SIL), NFPA 79 provides the electrical implementation requirements — the safety architecture and PL/SIL calculation come from [ISO 13849-1]({{ '/standards/functional-safety/iso-13849-1/' | relative_url }}) or [IEC 62061]({{ '/standards/functional-safety/iec-62061/' | relative_url }}).

---

## Related Standards

- [IEC 60204-1]({{ '/standards/machinery/iec-60204-1/' | relative_url }}) — International equivalent; use for CE-marked machinery
- [NEC]({{ '/standards/us-electrical/nec/' | relative_url }}) — Installation code; Article 670 references NFPA 79
- [UL 508A]({{ '/standards/us-electrical/ul-508a/' | relative_url }}) — Panel listing; applies alongside NFPA 79
- [NFPA 79 ↔ IEC 60204-1 crosswalk]({{ '/tools/crosswalks/nfpa79-iec60204/' | relative_url }})
