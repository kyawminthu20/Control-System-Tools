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

## Serial &amp; Device-Level

<div class="workflow-card-grid">
  <div class="workflow-card">
    <h3><a href="{{ '/communications/modbus-rtu-rs485/' | relative_url }}">Modbus RTU over RS-485</a></h3>
    <p>Application protocol vs physical layer, multidrop wiring, termination and bias, and serial-side diagnostics.</p>
  </div>
  <div class="workflow-card">
    <h3><a href="{{ '/communications/profibus-dp/' | relative_url }}">PROFIBUS DP</a></h3>
    <p>Segment rules, powered termination, GSD files, and bus-health diagnostics beyond packet capture.</p>
  </div>
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
</div>

## Planned Next

EtherCAT · DNP3 · IEC 61850 · HART · Foundation Fieldbus · industrial wireless
— added as they reach review, per the same six-question template.
