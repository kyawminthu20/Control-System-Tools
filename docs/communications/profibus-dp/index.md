---
layout: default
title: "PROFIBUS DP"
description: "PROFIBUS DP fieldbus — RS-485 physical rules, master/slave cyclic exchange, GSD files, commissioning checks, and serial-bus diagnostics."
breadcrumb:
  - name: "Communications"
    url: "/communications/"
  - name: "PROFIBUS DP"
review:
  standard: "PROFIBUS & PROFINET International (PI) — PROFIBUS DP / IEC 61158"
  edition: "exact governing revision not yet recorded"
  status: "Review pending"
  coverage: "DP-V0 cyclic exchange, RS-485 physical layer, GSD configuration, and diagnostics; DP-V1/V2 acyclic services and PA engineering are noted but not covered in depth."
  last_reviewed: "July 2026"
related_standards:
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Industrial Communications</span>
  <h1>PROFIBUS DP</h1>
  <p>Serial fieldbus for remote I/O and drives — RS-485 electrically, but with its own physical rules that decide whether the bus runs or drops.</p>
</div>

## Overview

PROFIBUS DP (Decentralized Periphery) is a serial fieldbus, still widespread in installed plants — particularly around Siemens controllers — for connecting remote I/O, drives, and instruments to a PLC. A DP master (typically the PLC's DP interface, Class 1) polls each configured slave cyclically: it sends output data and receives input data plus status in a fixed rotation, so update timing is deterministic for a given configuration and baud rate.

Electrically, standard DP uses RS-485 — but treat PROFIBUS as having its own physical rulebook layered on top: purple type-A cable, powered termination in the connectors, baud-rate-dependent segment lengths, and strict station limits. Most field problems trace back to violations of those rules, not to the protocol itself. (RS-485 is only the electrical layer here; PROFIBUS DP is the protocol running over it — the same distinction that applies between RS-485 and Modbus RTU.)

```mermaid
flowchart LR
    PLC[PLC / DP Master Class 1] --- IO1[Remote I/O Slave]
    IO1 --- VFD[VFD Slave]
    VFD --- VLV[Valve Terminal Slave]
    VLV --- REP[Repeater]
    REP --- IO2[Remote I/O Slave — second segment]
```

## Where It Is Used

- PLC to remote I/O racks (the classic use case).
- PLC to VFDs and motion drives, often via drive-specific telegram types.
- PLC to instruments and analyzers with DP interfaces.
- Legacy machine and process installations — new greenfield designs typically choose PROFINET instead, so most DP work today is maintenance, extension, and migration of existing segments.

**DP vs PA in one paragraph:** PROFIBUS PA is the process-automation sibling. It carries the same protocol logic but over a MBP (Manchester-coded, bus-powered) physical layer suitable for intrinsically safe instrument loops in hazardous areas, at a fixed 31.25 kbit/s, with power and signal on the same pair. PA segments connect to a DP backbone through a DP/PA coupler or link. If you are wiring purple cable to I/O and drives, you are on DP; if instruments are bus-powered two-wire devices in the field, that side is PA — the physical rules and troubleshooting tools differ, so do not mix the two mentally.

## Network Design

- **Topology:** a linear trunk (daisy chain), device to device. Avoid star wiring and long spurs — at 1.5 Mbit/s and above, spurs/stubs should normally be avoided entirely; verify allowable stub lengths against PI installation guidelines for lower baud rates.
- **Segment length depends on baud rate** (type-A cable, commonly cited values — verify against the PI installation guideline for your cable type):

| Baud rate | Max segment length |
|---|---|
| 9.6 – 93.75 kbit/s | 1200 m |
| 187.5 kbit/s | 1000 m |
| 500 kbit/s | 400 m |
| 1.5 Mbit/s | 200 m |
| 3 – 12 Mbit/s | 100 m |

- **Station limits:** a maximum of 32 physical devices per segment — and repeaters count as devices on both segments they join. Repeaters extend the network into further segments; the total addressable station count on one DP network is 126 (addresses 0–125 usable in practice; 126 is commonly the as-delivered default address, 127 is broadcast).
- **Addressing:** every master and slave needs a unique station address, set by rotary/DIP switches, a local display, or an engineering tool depending on the device.
- **Termination is powered:** DP termination is not just a resistor across A and B — the standard termination network includes bias resistors fed from the +5 V of the station the connector plugs into. Termination must be ON at the two physical ends of each segment (and only there), and the devices supplying power to those terminators must stay powered, or the whole segment can destabilize.
- **Cable:** shielded twisted-pair type-A cable (the familiar purple jacket), shield bonded at every device per the installation guideline, with attention to bend radius and separation from power cabling.

Beyond basic cyclic exchange (DP-V0), the protocol has extensions: DP-V1 adds acyclic read/write services used for instrument parameterization (e.g., via engineering tools and DTMs), and DP-V2 adds slave-to-slave communication and isochronous mode for drives. For most remote-I/O and drive installations, DP-V0 cyclic exchange plus DP-V1 diagnostics is what you are commissioning. A Class 2 master (an engineering/diagnostic station) can coexist on the bus with the Class 1 master, which is how portable bus analyzers and configuration tools attach without disturbing control.

Design information worth recording per network, before commissioning:

- master station address and baud rate;
- station address, GSD file (and version), and module list per slave;
- segment boundaries, repeater locations, and which stations power the terminators;
- measured segment lengths against the baud-rate table;
- watchdog times and configured fail-safe output behavior.

## Configuration

1. **Obtain the GSD file** for each slave — the device-description file (GSD, or language variants such as GSE/GSF) that tells the engineering tool the slave's identity number, supported baud rates, and available modules. Match it to the exact device model and, where the vendor distinguishes them, the firmware/hardware version.
2. **Import the GSD** into the master's engineering tool (e.g., Siemens TIA Portal / STEP 7 hardware catalog) and add the slave to the DP network at its station address.
3. **Configure the modules** — for modular slaves, the configured module list and order must match the physical rack exactly; a mismatch typically produces a configuration-fault diagnostic rather than a working connection.
4. **Set the station address on the device** (switches or tool) to match the project. Note that some devices only read address switches at power-up.
5. **Set the baud rate at the master only.** Most DP slaves auto-detect the baud rate; the master defines it for the network. All segments joined by plain repeaters run at the same baud rate.
6. **Set watchdog and fail-safe behavior** — what outputs do on communication loss is a configuration decision; verify it deliberately rather than accepting defaults.
7. **Use proper DP connectors.** The standard 9-pin DP connector carries the trunk in and out and contains the termination network behind a switch. When the termination switch is ON, most connector designs disconnect the outgoing trunk — a useful behavior at the real segment end, and a source of mysteriously dead downstream stations when someone flips the switch mid-segment. Connectors with a piggy-back (PG) port give diagnostic tools a non-intrusive attachment point; specify at least one per segment where practical.

## Commissioning Checks

- [ ] Termination switched ON at the two physical ends of each segment — and nowhere in the middle.
- [ ] The stations powering the end terminators are devices that remain powered during normal operation (not a maintenance laptop connector or a device on a switched circuit).
- [ ] Every station address is unique across the network; no device left at the delivery default (commonly 126).
- [ ] Configured baud rate is consistent with the physical segment lengths actually installed (see table above).
- [ ] No spurs/stubs at 1.5 Mbit/s or above; stub lengths at lower rates verified against the installation guideline.
- [ ] Station count per segment ≤ 32 including repeaters.
- [ ] GSD-configured module list matches each physical slave rack.
- [ ] Shield bonded at every connector/device; cable routing separated from power conductors.
- [ ] Live list at the master shows every configured slave present and in data exchange, with no diagnostics pending.
- [ ] Fail-safe/output behavior on bus loss tested by deliberately disconnecting one slave.

## Diagnostics

Work layered: physical first, then addressing/configuration, then protocol-level diagnostics.

**Wireshark cannot see this bus.** PROFIBUS DP on RS-485 is not capturable through a laptop Ethernet port; there is no display filter to type. Do not budget troubleshooting time around packet capture — budget it around these instead:

- **Live list from the master.** The engineering tool (or the master's own diagnostics) shows which station addresses are present, which configured slaves are missing, and which are reporting faults. This is the fastest first look and needs no extra hardware.
- **Slave diagnostic telegrams.** DP slaves report standardized diagnostic data to the master — station status, configuration faults, and vendor/module-specific detail. Read these before touching the wiring: a "configuration mismatch" diagnostic and a dead segment are very different problems.
- **PROFIBUS testers and bus-health analyzers** (e.g., instruments of the ProfiTrace/Softing/Fluke class). These connect to the bus via the piggy-back connector, capture DP telegrams natively, and — critically — measure electrical signal quality per station: amplitude, edge steepness, and reflections. A protocol-level retry count paired with a poor waveform at one station localizes a physical fault quickly.
- **Oscilloscope with differential probe** where a dedicated tester is not available — reflections from missing/duplicated termination and amplitude loss from over-long segments are visible on the waveform.
- **Diagnostic repeaters** (where installed) can report segment-level wiring faults, including approximate distance to a fault, to the master.

Signal-quality measurement matters because DP faults are often marginal: the bus works until temperature, vibration, or one more drive start tips it over. A clean live list at commissioning does not prove electrical margin — a bus analyzer measurement does.

Documentation worth retaining from a diagnostic or commissioning session:

- live list snapshot with all stations in data exchange;
- per-station signal-quality measurements from the bus analyzer (the baseline for the next fault call);
- retry/error counters at the master before and after any fix;
- the as-found and as-left termination and segment layout, sketched, with the powered-terminator stations marked.

## Common Faults

| Symptom | Likely causes | First checks |
|---|---|---|
| Intermittent slave dropouts, worse under load or vibration | Termination missing/unpowered, spur too long, loose connector, EMC coupling from adjacent power cables | Verify powered termination at both segment ends; inspect connectors; check retry counts and signal amplitude per station with a bus analyzer |
| Bus faults appear only at higher baud rate | Segment length exceeds the limit for that baud rate; stubs present | Measure actual cable length against the baud-rate table; remove spurs or reduce baud rate as an interim measure |
| One slave never enters data exchange | Wrong station address, GSD/module configuration mismatch, address switch changed but device not power-cycled | Read the slave's diagnostic telegram; compare configured vs physical module list; confirm address and power-cycle |
| Two slaves misbehave erratically | Duplicate station address | Walk the live list against the address plan; check devices left at default address |
| Whole segment dead after a device was removed/replaced | The removed device powered a terminator, or the trunk was broken at that connector | Check which stations feed the end terminators; verify trunk continuity through the swapped connector |
| Sporadic faults on the far segment only | Repeater fault, second segment exceeds its own length/station limits | Treat each repeater-separated segment as its own bus: re-verify termination, length, and count per segment |
| High retry counts but no dropouts yet | Marginal signal quality — degrading cable, corroded connector, shield discontinuity | Bus-health measurement per station; compare amplitudes; fix the worst station before it becomes a dropout |

## Related Pages

- [Industrial Communications overview]({{ site.baseurl }}/communications/)
- [Modbus RTU]({{ site.baseurl }}/communications/modbus-rtu-rs485/) — a different application protocol over the same RS-485 electrical layer
- [PROFINET]({{ site.baseurl }}/communications/profinet/) — the Ethernet-based successor in the same ecosystem
- [OPC UA]({{ site.baseurl }}/communications/opc-ua/) — typical northbound path from the controllers these buses serve
- [IEC 62443 — Industrial Cybersecurity]({{ site.baseurl }}/standards/cybersecurity/iec-62443/)
