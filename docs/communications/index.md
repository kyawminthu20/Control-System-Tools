---
layout: default
title: "Industrial Communications"
description: "Industrial network protocols, design, configuration, and diagnostics — EtherNet/IP, PROFINET, Modbus, OPC UA, BACnet/IP, IO-Link, and Wireshark-based troubleshooting."
breadcrumb:
  - name: "Communications"
related_standards:
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Industrial Communications</span>
  <h1>Industrial Communications &amp; Network Diagnostics</h1>
  <p>How industrial networks are designed, configured, commissioned, and — when they misbehave — diagnosed. Every protocol page answers the same six questions: what it is, where it's used, how the network is designed, how devices are configured, how it's commissioned, and how it's diagnosed.</p>
</div>

> **First release.** This section starts with the protocols and tools most
> common in machine and process work. Pages carry a review-status block —
> most are <em>Review pending</em> until checked against the governing
> specifications. Verify protocol details against the specification and your
> device documentation.

## Which Protocol Am I Looking At?

| Protocol | Main use | Transport | Typical cycle behavior | Common diagnostic method |
|---|---|---|---|---|
| [EtherNet/IP]({{ '/communications/ethernet-ip/' | relative_url }}) | PLC, I/O, drives, machine devices | TCP/UDP over IP | Cyclic implicit I/O + explicit messages | Wireshark, controller diagnostics, switch counters |
| [PROFINET]({{ '/communications/profinet/' | relative_url }}) | PLC, I/O, drives, motion | Layer-2 RT plus IP services | Cyclic RT or IRT | Wireshark, topology tools, PLC diagnostics |
| [Modbus TCP]({{ '/communications/modbus-tcp/' | relative_url }}) | Meters, VFDs, packaged equipment | TCP port 502 | Client polling | Wireshark, register testing |
| [OPC UA]({{ '/communications/opc-ua/' | relative_url }}) | SCADA, MES, system integration | Commonly TCP with security sessions | Subscriptions and requests | Wireshark, certificate logs, server diagnostics |
| [BACnet/IP]({{ '/communications/bacnet-ip/' | relative_url }}) | Building automation | UDP/IP (commonly UDP 47808) | Object reads/writes and COV | Wireshark, BACnet discovery tools |
| [Modbus RTU]({{ '/communications/modbus-rtu-rs485/' | relative_url }}) | Serial instruments and VFDs | Serial, typically RS-485 | Request/response polling | Serial analyzer, oscilloscope |
| [PROFIBUS DP]({{ '/communications/profibus-dp/' | relative_url }}) | Distributed I/O, legacy drives | PROFIBUS physical layer (RS-485-based) | Cyclic master/slave | Bus analyzer, waveform diagnostics |
| [IO-Link]({{ '/communications/io-link/' | relative_url }}) | Smart sensors and actuators | Point-to-point device link | Cyclic process data + acyclic parameters | Master diagnostics, IODD tools |

## Start by Task

**I need to connect a PLC to a drive or device** —
[Ethernet fundamentals]({{ '/communications/ethernet-fundamentals/' | relative_url }}) →
the applicable protocol page → its device-description file section → its
commissioning checklist → its diagnostic filters.

**I need to troubleshoot an intermittent dropout** —
[Diagnostics methodology]({{ '/communications/wireshark-methodology/' | relative_url }}) →
[managed-switch counters]({{ '/communications/managed-switches/' | relative_url }}) →
[packet-capture methods]({{ '/communications/packet-capture-methods/' | relative_url }}) →
capture a baseline → protocol-specific diagnosis.

**I need to integrate a SCADA system** —
[Ethernet fundamentals]({{ '/communications/ethernet-fundamentals/' | relative_url }}) (addressing/routing) →
[OPC UA]({{ '/communications/opc-ua/' | relative_url }}) or
[Modbus TCP]({{ '/communications/modbus-tcp/' | relative_url }}) →
firewall ports → certificates and authentication → tag-quality and timeout diagnosis.

**I need to troubleshoot RS-485** —
[Modbus RTU / RS-485]({{ '/communications/modbus-rtu-rs485/' | relative_url }})
(physical layer first: termination, bias, polarity) → serial parameters →
frame-level checks with a serial analyzer and oscilloscope.

## Fundamentals

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/ethernet-fundamentals/' | relative_url }}">Industrial Ethernet Fundamentals</a></h3>
    <p>MAC vs IP, subnets, ARP, TCP vs UDP, multicast, VLANs, and why office-network habits break industrial networks.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/managed-switches/' | relative_url }}">Managed Switches</a></h3>
    <p>What managed switches add — VLANs, IGMP snooping, port mirroring, redundancy — and when unmanaged is acceptable.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/copper-ethernet/' | relative_url }}">Copper Ethernet</a></h3>
    <p>Category ratings, M12 vs RJ45, shield bonding, VFD-cable separation, and what a cable certifier proves that a continuity tester can't.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/fiber-optics/' | relative_url }}">Fiber Optics</a></h3>
    <p>Single-mode vs multimode, optical power budgets, connector cleanliness, and DOM readings as free diagnostics.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/rs485-physical-layer/' | relative_url }}">RS-485 Physical Layer</a></h3>
    <p>Differential signaling, termination and bias, polarity labeling chaos, and what a healthy bus looks like on an oscilloscope.</p>
  </div>
</div>

## Ethernet Protocols

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/ethernet-ip/' | relative_url }}">EtherNet/IP</a></h3>
    <p>CIP on Ethernet: explicit vs implicit messaging, RPI, multicast I/O, EDS files, connection ownership.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/modbus-tcp/' | relative_url }}">Modbus TCP</a></h3>
    <p>The register model, function codes, gateways and unit IDs, word-order pitfalls, and exception diagnostics.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/profinet/' | relative_url }}">PROFINET</a></h3>
    <p>IO-Controller/IO-Device model, device naming via DCP, GSDML, RT vs IRT, and name-based commissioning.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/opc-ua/' | relative_url }}">OPC UA</a></h3>
    <p>Client/server sessions, subscriptions, security modes, and the certificate-trust commissioning trap.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/bacnet-ip/' | relative_url }}">BACnet/IP</a></h3>
    <p>Objects and device instances, Who-Is/I-Am discovery, and BBMD for multi-subnet building integration.</p>
  </div>
</div>

## Serial, Fieldbus &amp; Device-Level

**Serial and fieldbus** — multidrop networks on shared physical media:

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/modbus-rtu-rs485/' | relative_url }}">Modbus RTU over RS-485</a></h3>
    <p>Application protocol vs physical layer, multidrop wiring, termination and bias, and serial-side diagnostics.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/profibus-dp/' | relative_url }}">PROFIBUS DP</a></h3>
    <p>Segment rules, powered termination, GSD files, and bus-health diagnostics beyond packet capture.</p>
  </div>
</div>

**Smart device interfaces** — point-to-point links, not multidrop buses:

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/io-link/' | relative_url }}">IO-Link</a></h3>
    <p>Point-to-point sensor communication: masters as fieldbus gateways, IODDs, and parameter data storage.</p>
  </div>
</div>

## Diagnostics

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/wireshark-methodology/' | relative_url }}">Diagnostics Methodology</a></h3>
    <p>The 8-step workflow: define the symptom, check physical first, capture with a plan, compare against a baseline, prove root cause.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/packet-capture-methods/' | relative_url }}">Packet Capture Methods</a></h3>
    <p>Workstation capture vs port mirroring vs TAP — what each sees, what each risks, and where to capture.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/wireshark-fundamentals/' | relative_url }}">Wireshark Fundamentals</a></h3>
    <p>Interface selection, capture vs display filters, Expert Information, and capture hygiene — the tool basics.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/case-study-intermittent-io/' | relative_url }}">Case Study: Intermittent I/O Dropout</a></h3>
    <p>One complete investigation from vague symptom to proven root cause — the methodology in action.</p>
  </div>
</div>

Network-documentation starting points (IP register, switch-port schedule,
VLAN register, firewall matrix, capture log) live on the
[templates page]({{ '/tools/templates/' | relative_url }}).

## Planned Next

EtherCAT · DNP3 · IEC 61850 · HART · Foundation Fieldbus · industrial wireless
— added as they reach review, per the same six-question template.
