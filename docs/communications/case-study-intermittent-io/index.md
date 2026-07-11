---
layout: default
title: "Case Study — Intermittent EtherNet/IP I/O Dropout"
description: "A worked end-to-end fault investigation: from a vague symptom to a proven root cause, using the diagnostics methodology, switch counters, and a ring-buffer capture."
breadcrumb:
  - name: "Communications"
    url: "/communications/"
  - name: "Case Study"
review:
  standard: "— (constructed teaching example)"
  edition: "—"
  status: "Review pending"
  coverage: "One complete investigation walkthrough; values are illustrative, not from a real site"
  last_reviewed: "July 2026"
---

<div class="page-header">
  <span class="page-header__label">Industrial Communications</span>
  <h1>Case Study — Intermittent EtherNet/IP I/O Dropout</h1>
  <p>One complete investigation, from "the conveyor faults sometimes" to a proven root cause — showing every step of the methodology actually being used.</p>
</div>

> **Constructed teaching example.** This walkthrough is fictional and
> deliberately typical: the machine, addresses, and numbers are invented to
> demonstrate the method, and no real capture data appears. Real
> investigations are messier — but the sequence is the same. It follows the
> [8-step diagnostics methodology]({{ '/communications/wireshark-methodology/' | relative_url }})
> step by step.

## Step 1 — Define the Symptom Precisely

The maintenance ticket says: *"Conveyor 2 network keeps dropping."*

After talking to the operator and reading the PLC fault log, the real
symptom statement becomes:

> PLC `192.168.10.10` loses the cyclic EtherNet/IP I/O connection to VFD
> `192.168.10.40` (conveyor 2 drive) one to three times per day-shift.
> Each dropout lasts 2–5 seconds, the PLC logs connection fault code and
> auto-reconnects, and the line stops on the drive's comm-loss trip.
> Night shift reports it rarely. It started roughly two weeks ago.

Already useful: it's one device pair, it's intermittent, it self-recovers,
and it correlates with day shift — which is when the cell is busiest and
when people are moving around the machine.

## Step 2 — Establish the Boundary

The path is: PLC → panel patch cord → managed switch `SW-01` port 1 →
port 4 → bulkhead → 18 m field cable in cable tray → VFD. The HMI
(`192.168.10.20`, port 2) never logs comm errors — so the switch and the
PLC side are probably healthy, and suspicion narrows to the port-4 leg.

## Step 3 — Physical Checks First

Visual inspection finds nothing obviously wrong: connectors seated, no
crushed cable visible, drive grounded. Worth noting for later: the port-4
field cable shares a tray section with the conveyor 2 motor cable for about
6 m, and a VFD output-cable separation rule exists on the drawings but the
tray divider was never installed.

Nothing conclusive — resist the urge to declare victory here. Log it,
keep going.

## Step 4 — Configuration Checks

- PLC connection to the VFD: RPI 20 ms, unicast, connection timeout at the
  default multiplier — unchanged for two years.
- Switch config last changed two weeks ago? **Check the change log** — no
  entries. (If a real MOC log existed, this is where it earns its keep.)
- Duplex/speed: both ends auto-negotiated to 100 Mb/s full duplex.

Nothing configured wrong, but one timeline fact emerges from the ticket
system: conveyor 2's motor was replaced two-and-a-half weeks ago.

## Step 5 — Device and Switch Diagnostics

Switch port counters (see
[interpreting port counters]({{ '/communications/managed-switches/' | relative_url }})):

| Counter | Port 1 (PLC) | Port 2 (HMI) | Port 4 (VFD) |
|---|---|---|---|
| CRC/FCS errors | 0 | 0 | **14,712 and climbing** |
| Link up/down events | 0 | 0 | 0 |
| Output discards | 0 | 0 | 0 |

Counters are cleared and re-read an hour later: port 4 accumulates a few
hundred more CRC errors — **only while the conveyor is running.**

This is the pivot point of the investigation: CRC errors are a
physical-layer signature, the link never actually drops, and the errors
correlate with motor operation.

## Step 6 — Capture with a Plan

Hypothesis: noise-induced frame corruption on the port-4 leg occasionally
destroys enough consecutive cyclic packets to trip the connection timeout.

Corrupted frames are discarded by the switch port hardware, so the capture
plan is to mirror **port 4** and watch for *gaps*, not errors: a
[ring-buffer capture]({{ '/communications/packet-capture-methods/' | relative_url }})
(5-minute files × 24) runs on a mirror of port 4, and the operator writes
down the wall-clock time of each trip. Capture-laptop clock offset vs PLC
clock: recorded (+3 s).

At 10:41 the line trips. The file covering 10:40–10:45 shows, using the
I/O Graph: a flat ~50 packet/s cyclic band in each direction, then the
VFD→PLC direction thins and stops for ~2.1 s while the PLC→VFD direction
continues, then a burst of connection re-establishment (Forward Open) and
the band resumes. TCP keepalive and explicit traffic from other devices
continue normally throughout — the segment itself never died; frames from
the drive stopped surviving the trip down that one cable.

## Step 7 — Compare Against a Baseline

A capture of the identical mirror during night shift (conveyor idling)
shows the same cyclic band with zero gaps over two hours, and port-4 CRC
counters stay frozen. The fault signature exists only under motor load.

## Step 8 — Prove Root Cause, Not Correlation

Evidence chain assembled so far:

1. CRC errors accumulate on port 4 only, only under motor load
2. Capture shows one-directional cyclic loss with the rest of the segment healthy
3. Timeline matches the motor replacement — after which the (never-divided)
   tray section carries a new motor cable pressed directly against the
   Ethernet field cable
4. Cable certification test on the port-4 field run: **fails** return-loss
   margin near the tray section

Fix: re-route the Ethernet cable to the divided side of the tray per the
original drawing and replace the marginal run. Verification: CRC counters
stay at zero across three full day-shifts, no trips, and a repeat capture
shows an unbroken cyclic band. Root cause proven by elimination *and*
reproduction — not just plausibility.

## What Made This Work

- The symptom was **restated precisely** before anyone touched a tool
- Switch counters localized the problem to one leg **before** Wireshark
  was opened — the capture then answered one specific question
- A **baseline** capture separated "always looks like this" from "fault"
- The fix was verified against the same evidence that proved the fault

Investigations that skip these steps still end — usually with a swapped
switch, an unexplained recovery, and a fault that returns in a month.

## Related Pages

- [Diagnostics methodology]({{ '/communications/wireshark-methodology/' | relative_url }})
- [Wireshark fundamentals]({{ '/communications/wireshark-fundamentals/' | relative_url }})
- [Packet capture methods]({{ '/communications/packet-capture-methods/' | relative_url }})
- [Managed switches — counter interpretation]({{ '/communications/managed-switches/' | relative_url }})
- [EtherNet/IP]({{ '/communications/ethernet-ip/' | relative_url }})
