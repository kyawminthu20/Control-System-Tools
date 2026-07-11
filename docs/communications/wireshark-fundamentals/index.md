---
layout: default
title: "Wireshark Fundamentals for Industrial Networks"
description: "Interface selection, capture vs display filters, time handling, Expert Information, and capture hygiene — the Wireshark basics an automation engineer actually needs."
breadcrumb:
  - name: "Communications"
    url: "/communications/"
  - name: "Wireshark Fundamentals"
review:
  standard: "— (tool guidance; menus and syntax vary by Wireshark version)"
  edition: "exact tool version not pinned"
  status: "Review pending"
  coverage: "Core capture/analysis workflow for plant use; not a full Wireshark manual"
  last_reviewed: "July 2026"
related_standards:
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Industrial Communications</span>
  <h1>Wireshark Fundamentals for Industrial Networks</h1>
  <p>The handful of Wireshark skills that cover most plant-floor diagnostics — and the traps that make a capture worthless.</p>
</div>

## Overview

Wireshark records and decodes network traffic. On the plant floor its job is
narrow: prove or disprove a specific communication hypothesis — "the PLC is
sending but the drive isn't answering," "something is flooding this segment,"
"the connection drops every 34 minutes." This page covers the tool mechanics;
the [troubleshooting methodology]({{ '/communications/wireshark-methodology/' | relative_url }})
covers when to reach for it (step 6, not step 1), and
[packet capture methods]({{ '/communications/packet-capture-methods/' | relative_url }})
covers where to plug in.

Menu names and filter syntax shift between versions — verify against the
Wireshark version in use.

## Choosing the Capture Interface

The most common beginner failure is capturing on the wrong interface — the
capture "works" but shows nothing relevant.

- List interfaces before capturing (GUI welcome screen, or `tshark -D`).
  Laptops typically show Ethernet, Wi-Fi, VPN adapters, and virtual
  interfaces — pick the wired adapter actually connected to the network of
  interest.
- The traffic-sparkline next to each interface on the welcome screen is the
  quickest sanity check: no activity on the interface you expected means a
  wiring/mirroring problem, not a filter problem.
- **Promiscuous mode** (normally on by default) tells the adapter to keep
  frames not addressed to it. Without it, a mirror-port capture silently
  shows only your own traffic. Some Wi-Fi adapters and corporate endpoint
  tools interfere with it — verify on a known-chatty network first.
- Remember the switched-network rule: even with promiscuous mode, a normal
  switch port only delivers your traffic plus broadcast/multicast. Seeing
  device-to-device unicast requires
  [mirroring or a TAP]({{ '/communications/packet-capture-methods/' | relative_url }}).

## Capture Filters vs Display Filters

The single most confusing thing for new users: Wireshark has **two filter
languages with different syntax**, applied at different times.

**Capture filters** (BPF syntax) decide what gets *recorded*. Set before
capturing; anything excluded is gone forever:

```text
host 192.168.10.40 and port 502
```

**Display filters** (Wireshark syntax) decide what gets *shown* from an
already-recorded capture, and can be changed freely afterward:

```text
ip.addr == 192.168.10.40 && tcp.port == 502
```

Practical rule for plant work: **capture broadly, display narrowly.** Disk
is cheap, and the packet that explains the fault is often one you would have
filtered out — ARP, a TCP reset from a third device, a broadcast storm.
Use capture filters only when traffic volume forces it (heavily loaded
mirror ports, long ring-buffer sessions).

## Reading a Capture Efficiently

- **Time display:** switch between "seconds since previous displayed packet"
  (gap hunting) and "time of day" (correlating with PLC/HMI event logs) via
  View → Time Display Format. Record how the capture laptop's clock relates
  to the control-system clocks — see
  [capture hygiene]({{ '/communications/packet-capture-methods/' | relative_url }}).
- **Name resolution:** off by default for MAC/transport, and best left off
  in captures you intend to share — resolution can leak internal hostnames
  and slows large files. Judge devices by address, not name.
- **Conversations and Endpoints** (Statistics menu): the fastest map of who
  is talking to whom and how much. Sort Endpoints by packets to spot the
  device flooding the segment; sort Conversations by duration to find
  connections that cycle.
- **Coloring rules:** the defaults already flag TCP problems (black/red).
  Add rules for your protocol of interest during a long investigation.
- **I/O Graph** (Statistics menu): plot packets-per-second over the capture;
  cyclic industrial I/O shows as a flat band, and dropouts appear as visible
  notches — often the fastest way to locate the fault window in a long
  ring-buffer file.
- **Expert Information** (Analyze menu): Wireshark's own list of anomalies —
  retransmissions, resets, duplicate ACKs, malformed packets — grouped by
  severity. Check it before manually scrolling anything.

## Saving and Sharing Evidence

- **Export Specified Packets** saves just the displayed/selected range —
  attach the 40 packets that show the fault, not the 4 GB session.
- Save as **pcapng** to keep interface metadata and comments. Right-click →
  Packet Comment lets you annotate the exact frames that matter; comments
  travel with the file.
- For intermittent faults, run a
  [ring-buffer capture]({{ '/communications/packet-capture-methods/' | relative_url }})
  and note wall-clock times when symptoms occur.
- **Sanitize before sharing anywhere.** Captures expose addresses,
  hostnames, device identities, firmware banners, and process data. Never
  publish or upload captures from an employer or customer network; even
  internally, share the minimum extract that demonstrates the finding.

## Commissioning Checks

Before relying on a capture during commissioning or FAT:

- [ ] Correct interface confirmed against a known-chatty device
- [ ] Promiscuous mode active and mirror/TAP visibility proven (see a
      third-party conversation you expect)
- [ ] Capture laptop clock offset vs PLC/HMI clocks recorded
- [ ] Ring buffer configured if the session runs unattended
- [ ] Storage location agreed and capture retention/confidentiality cleared
      with the site

## Common Faults

| Symptom | Likely causes | First checks |
|---|---|---|
| Capture shows only my own traffic + broadcasts | Normal switched-port behavior | Configure port mirroring or insert a TAP |
| Capture shows nothing at all | Wrong interface; adapter not connected; capture filter too narrow | Interface sparkline; remove capture filter |
| Expected device traffic missing | Mirror configured for wrong port/direction | Re-check mirror source ports and direction |
| Times don't match PLC event log | Clock offset never recorded | Record offsets before capturing; use time-of-day display |
| Huge file, can't find the fault | No ring buffer; no symptom timestamps | Ring buffer + note wall-clock time at each symptom; I/O Graph to find notches |
| Display filter returns nothing despite traffic | Display filter written in capture (BPF) syntax or vice versa | Check which filter language the box expects |

## Related Pages

- [Network diagnostics methodology]({{ '/communications/wireshark-methodology/' | relative_url }})
- [Packet capture methods]({{ '/communications/packet-capture-methods/' | relative_url }})
- [Case study — intermittent I/O dropout]({{ '/communications/case-study-intermittent-io/' | relative_url }})
- [Managed switches]({{ '/communications/managed-switches/' | relative_url }})
