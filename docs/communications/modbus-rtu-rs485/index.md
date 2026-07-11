---
layout: default
title: "Modbus RTU over RS-485"
description: "Modbus RTU as an application protocol on the RS-485 physical layer — multidrop wiring, termination, biasing, addressing, timing, and serial-line diagnostics."
breadcrumb:
  - name: "Communications"
    url: "/communications/"
  - name: "Modbus RTU / RS-485"
review:
  standard: "Modbus.org (Modbus over Serial Line) / TIA-485"
  edition: "exact governing revision not yet recorded"
  status: "Review pending"
  coverage: "RTU framing, 2-wire multidrop wiring, termination/bias, addressing, timing, and no-Wireshark diagnostics; does not cover Modbus ASCII, 4-wire RS-485, or register maps of specific devices"
  last_reviewed: "July 2026"
related_standards:
  - name: "IEC 62443"
    url: "/standards/cybersecurity/iec-62443/"
---

<div class="page-header">
  <span class="page-header__label">Industrial Communications</span>
  <h1>Modbus RTU over RS-485</h1>
  <p>Two different things wearing one nickname: Modbus is the application protocol, RS-485 is the electrical physical layer — and most field faults live in the RS-485 half.</p>
</div>

## Overview

Get one distinction straight before anything else, because half the confusion in the field comes from conflating the two:

- **Modbus RTU** is an *application protocol* (defined by Modbus.org): a client/server request-response message format with node addresses, function codes, and a CRC. It says nothing about voltages or wires.
- **RS-485** (TIA-485) is an *electrical physical layer*: a differential two-wire signaling standard for multidrop buses. It says nothing about message content — CANopen-era devices, PROFIBUS, BACnet MS/TP, and countless proprietary protocols also run over RS-485.

"A Modbus network" and "an RS-485 network" are therefore not synonyms. Modbus RTU can also run over RS-232 or RS-422, and the same Modbus application data runs over TCP/IP as Modbus TCP. When someone says "the Modbus is down," the first diagnostic question is which layer is actually failing — the electrical bus or the protocol conversation.

The pairing is popular because it is cheap, simple, and robust over distance: one twisted pair daisy-chained through up to 32 unit loads (more with fractional-load transceivers — verify against the transceiver datasheets), spans that copper Ethernet cannot match, and devices from any vendor that got the register map right.

```mermaid
flowchart LR
    PLC[PLC / Client] --- T1((TERM))
    T1 --- VFD[VFD addr 1]
    VFD --- PM[Power meter addr 2]
    PM --- TC[Temp controller addr 3]
    TC --- T2((TERM))
```

## Where It Is Used

- VFDs and soft starters — speed reference, status, energy data where hard-wired I/O would be excessive.
- Power meters, protection relays, and energy monitoring.
- Temperature/process controllers, chillers, boilers, compressors, gensets.
- Legacy integration — decades of installed devices speak Modbus RTU and nothing else.
- BMS and utility interfaces where a gateway maps RTU devices up to Modbus TCP or BACnet.

Honest scope notes: Modbus RTU is a single-client polled protocol — one client (historically "master") polls servers ("slaves") one at a time, so update rate divides across the device count. There is no device description file standard, no built-in security (no authentication or encryption — segment and gateway accordingly, see IEC 62443), and no standardized register map: every vendor's mapping is different, and the device manual is authoritative. It is a poor fit for fast cyclic I/O; it is a fine fit for slowly changing process values from many inexpensive devices.

## Network Design

**Topology: one daisy-chained trunk.** 2-wire RS-485 is a single twisted pair (plus common) running device to device. Each device taps the trunk with the shortest practical stub. Star, tree, and long-branch layouts are the classic mistake — see below.

**Termination — at the two physical ends only.** A resistor (typically 120 Ω, matching the cable's characteristic impedance) goes across the pair at each physical end of the trunk: two terminators total, nowhere else. Termination absorbs the signal at the ends so it does not reflect back and corrupt later bits. Missing termination causes reflections; extra terminators in the middle overload the drivers. Many devices include a DIP-switch or jumper terminator — which means the field failure mode is usually *too many* enabled, not none.

**Why long stubs and stars cause reflections.** A signal edge reaching any unterminated branch point or stub end sees an impedance discontinuity and partially reflects. At low baud rates a short stub's reflection dies out before the receiver samples the bit; a long stub or star branch reflects late enough to corrupt sampling. The tolerable stub length shrinks as baud rate rises — a wiring layout that "worked fine" at 9600 baud can fail when someone raises it to 115200. If a star layout is unavoidable, an RS-485 repeater/hub designed for it is the supported approach, not passive branching.

**Bias resistors.** When no driver is transmitting, the pair floats and receivers may read noise as start bits, producing framing errors between messages. Bias (fail-safe) resistors — a pull-up on one line, pull-down on the other — hold the bus in a defined idle state. The bus needs biasing at typically **one point** (commonly the client end); many adapters and some devices have switchable bias, so as with termination, audit for *duplicates*. Some modern transceivers are internally fail-safe and tolerate an unbiased bus — verify against the datasheets rather than assuming.

**Common reference and isolation.** RS-485 is differential but not floating: transceivers have a limited common-mode range (roughly −7 V to +12 V per TIA-485 — verify against the specification). "2-wire" therefore normally still needs a common reference conductor between nodes. Between buildings, across drive systems, or anywhere ground potentials differ, use galvanically isolated transceivers or isolated repeaters — ground-potential differences are a top cause of "mysterious" intermittent RS-485 faults and dead transceivers.

**Addressing.** Server addresses are **1–247**; address 0 is broadcast (write-only, no responses), and 248–255 are reserved. Every server on a segment needs a unique address, and every device must match on baud rate, parity, and stop bits. Document the address map with the project.

**Timing.** RTU frames are delimited by silence: the spec defines an inter-frame gap of at least **3.5 character times**, and characters within a frame must not be separated by more than 1.5 character times. Practical consequences: devices (and gateways) that insert pauses mid-message corrupt frames; response-timeout settings in the client must exceed the slowest server's worst-case response plus transmission time; and at high baud rates some hardware cannot honor the tight gaps, which is why the spec fixes minimum gap times at higher rates — see the Modbus over Serial Line specification.

## Configuration

There is no EDS/GSDML equivalent for Modbus RTU — configuration means matching serial settings by hand and reading the vendor's register map.

1. **Set serial parameters identically everywhere:** baud rate, parity, stop bits (a common default is 19200, even parity, 1 stop bit; 8 data bits is required for RTU). Mixed parity on one bus is a classic commissioning fault.
2. **Assign unique addresses 1–247** via each device's keypad, DIP switches, or configuration software. Beware vendor defaults — every new device tends to ship as address 1.
3. **Map the registers.** From each device manual, record which holding registers/input registers/coils carry the needed data, their data types, word order for 32-bit values (vendors disagree on high/low word order), and any offset convention (documentation "40001" vs on-the-wire address 0).
4. **Know the function codes at overview level:** FC01/02 read coils/discrete inputs, FC03/04 read holding/input registers, FC05/06 write single coil/register, FC15/16 write multiple. Devices implement subsets — verify the manual before designing around FC16, for example.
5. **Set the client's poll plan:** poll rate per device, response timeout, retry count. Total poll cycle = sum of all transactions; do not promise 100 ms updates from 20 devices at 9600 baud.
6. **Physical setup:** shielded twisted pair suited to RS-485, terminators at the two ends only, bias at one point, shield grounded per site practice (commonly one end, verify), address/settings label on each device.

## Commissioning Checks

- [ ] A/B polarity consistent along the whole trunk (vendor labeling of A/B/D+/D− is inconsistent — verify by voltage, not label)
- [ ] Exactly two terminators, at the two physical ends; all mid-bus termination switches confirmed off
- [ ] Bias enabled at exactly one point; idle differential voltage present and of correct polarity
- [ ] With power off, resistance across the pair ≈ 60 Ω (two 120 Ω terminators in parallel) — a quick count-the-terminators test
- [ ] Common/reference conductor connected; isolation in place where ground potentials may differ
- [ ] Every device: unique address recorded, baud/parity/stop bits matching the bus
- [ ] No long stubs or star branches; measured stub lengths noted on the drawing
- [ ] Each device polled individually and responds; then full poll cycle runs with zero CRC/timeout errors over a soak period
- [ ] Client timeout exceeds the slowest observed response with margin; retries logged, not silent
- [ ] Address map, register map, serial settings, and cable routing archived with the project

## Diagnostics

**What Wireshark cannot see.** Wireshark captures on network interfaces; it cannot capture a raw RS-485 bus through a laptop's Ethernet port. There is no promiscuous "sniff the wire" via Wireshark for a serial bus in the general case. Plan serial diagnostics around serial tools:

1. **Protocol level — isolated USB-to-RS-485 adapter + serial monitor software.** Tap the adapter onto the bus (A, B, common) as a listen-only node and log traffic with a serial/Modbus monitor tool. You see requests, responses, exception codes, CRC failures, and timing. Use a *galvanically isolated* adapter — a cheap non-isolated one ties your laptop ground to the bus and can create the very common-mode problem you are hunting, or damage the laptop.
2. **Electrical level — oscilloscope with differential measurement.** When frames are corrupted rather than merely wrong, look at the signal: differential amplitude at the far end, edge shape (reflections show as steps/ringing after edges), idle-state bias level, and noise. A scope answers "is the physical layer delivering clean bits" — no protocol tool can.
3. **Static checks — multimeter.** Pair resistance (~60 Ω with both terminators), idle bias voltage and polarity, continuity of the common conductor.
4. **Device-side counters.** Many clients (PLC comms cards, gateways) count timeouts, CRC errors, and retries per server — a per-address error pattern localizes the fault segment quickly.

**Modbus TCP gateway caveat.** If the RTU segment sits behind a Modbus TCP gateway, you *can* Wireshark the Ethernet side:

```text
mbtcp
modbus
tcp.port == 502
modbus.exception_code
```

Verify filter names against the Wireshark version in use. But understand what you are seeing: the capture shows the gateway's TCP conversation, not the serial wire. The gateway regenerates framing and timing, may retry serially without showing it on TCP, and reports serial failures only as gateway-generated exception responses (commonly exception 0x0B, gateway target device failed to respond) or TCP timeouts. A clean TCP capture proves the gateway conversation, not RS-485 signal integrity.

**RS-485 field checklist** — the order that finds most faults fastest:

- [ ] A/B polarity — swapped pair on one device (or one segment) is the single most common fault
- [ ] Termination count and location — exactly two, at the ends
- [ ] Bias — present once, correct polarity, not duplicated
- [ ] Baud/parity/stop mismatches — check every device against the bus settings
- [ ] Duplicate addresses — two devices answering as one address corrupts both responses
- [ ] Common reference / isolation — especially if faults correlate with drives running or weather
- [ ] Stub lengths and topology vs the drawing
- [ ] Timeouts/retries in the client log — which addresses, and does the pattern follow the cable route?

## Common Faults

| Symptom | Likely causes | First checks |
| --- | --- | --- |
| One device never responds | Wrong/duplicate address, A/B swapped at that device, wrong serial settings, termination switch left on at a mid-bus device | Poll it alone, verify address and serial settings, check its A/B wiring and DIP switches |
| No device responds | Client port settings, broken trunk near client, A/B swapped at client, adapter/transceiver failure | Client TX activity (LED/scope), pair resistance, polarity at the client end |
| Random CRC errors across many devices | Missing/extra termination, missing bias, noise/EMI, ground-potential difference, marginal cable | Terminator count (≈60 Ω test), idle bias voltage, scope the far end, segregate from power cables |
| Errors only when a drive/motor runs | EMI coupling, shield discontinuity, common-mode shift from drive grounds | Shield continuity and grounding, isolation at the drive, reroute away from motor cables |
| Works at low baud, fails when raised | Reflections from stubs/star topology now inside the bit window, cable length vs rate | Topology audit against the drawing, stub lengths, scope for ringing after edges |
| Devices at far end unreliable, near end fine | Attenuation, missing far-end terminator, damaged mid-trunk splice, too many unit loads | Far-end differential amplitude on scope, terminator at far end, unit-load count |
| Two devices' data appears scrambled/interleaved | Duplicate node address | Poll each suspect alone with others disconnected |
| Intermittent timeouts, no CRC errors | Client timeout too short, slow device, gateway buffering, mid-frame gaps from a poor converter | Measured worst-case response time vs timeout setting, serial monitor timing view |

## Related Pages

- [Industrial Ethernet Fundamentals]({{ site.baseurl }}/communications/ethernet-fundamentals/) — the contrasting world of switched networks and IP addressing
- [Managed Switches in Industrial Networks]({{ site.baseurl }}/communications/managed-switches/) — relevant once RTU devices sit behind a Modbus TCP gateway
- [IEC 62443 — Industrial Cybersecurity]({{ site.baseurl }}/standards/cybersecurity/iec-62443/) — compensating controls for a protocol with no built-in security
