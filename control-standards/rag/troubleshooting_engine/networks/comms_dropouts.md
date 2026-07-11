<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: troubleshooting — communication dropouts (industrial Ethernet / serial)
SOURCE_BASIS: diagnostic reasoning + generally accepted field practice (flagged)
INDEX_TAGS:
  topics: [troubleshooting, networks, dropouts, ethernet, rs485, emc, triage]
  systems: [industrial-ethernet, managed-switch, serial-bus, plc-io]
-->

# Communication dropouts — triage reasoning

This note is a **triage front-end**, not a diagnostic methodology. The full
network-diagnostics workflow — define the symptom, establish the boundary,
physical-first, capture with synchronized clocks, compare to a baseline, prove
root cause — lives in the communications diagnostics section and is not
duplicated here. The job of this note is to sort the symptom quickly so the
technician enters that workflow at the right place instead of opening a packet
capture blind.

## The three triage questions

Before any tool, three questions collapse most of the search space:

1. **Total loss or intermittent?** A device or segment that is *down and stays
   down* is a different investigation from one that *drops for seconds and
   self-recovers*. Total loss favors a hard fault — dead device, pulled cable,
   wrong config, failed switch. Intermittent favors a marginal cause — a
   flexing cable, a duplicate address surfacing under load, EMC events,
   oversubscription.

2. **Single device or whole segment?** One device unreachable while everything
   else is fine points at that device, its port, its cable, or its config.
   Every device on one switch or ring failing together points at the switch,
   the uplink, a broadcast storm, or the controller — a boundary the full
   workflow calls out explicitly. This is the boundary question; answer it
   before capturing.

3. **Does it correlate with a machine action?** A dropout that lands every time
   a motor or VFD starts is a physical/EMC story — coupling into the comm cable,
   a shared ground disturbed by inrush, a connector loosened by vibration. A
   dropout at random times is more likely address, load, or configuration. The
   correlation is the most valuable single clue and it costs nothing to observe.

## Symptom → likely direction

- **Total loss, single device.** Wrong IP/mask/VLAN, cable or connector fault,
  device powered down, or a duplicate address that knocked it off. Physical and
  configuration layers first; the device's own link/activity LEDs and the switch
  port counters usually settle it before a capture.
- **Total loss, whole segment.** Switch or ring failure, uplink loss, broadcast
  storm, or controller fault. Establish the boundary first — this is not a
  single-device problem.
- **Intermittent, correlates with motor/VFD start.** EMC coupling or a physical
  link stressed by the machine — the comm cable routed with power, a connector
  under vibration, a shield problem. This is the case where a marginal cable
  passes for hours at low load then fails when the machine runs. Route to the
  comm-cable wiring guide and the intermittent-I/O case study.
- **Intermittent, random.** Duplicate IP surfacing under traffic, multicast
  flooding, an oversubscribed link, or an overloaded device CPU. This is where a
  ring-buffer capture spanning the event, compared to a baseline, earns its keep.
- **Serial (RS-485) dropouts.** Missing or wrong bus termination, biasing,
  stub length, or grounding — the physical layer a laptop packet capture
  **cannot see at all**. Route to the RS-485 physical-layer page and scope
  practice, not to Wireshark.

## Physical-first quick checks (before escalating to captures)

The single most common time-waster is opening a capture before the physical
and configuration layers are checked. Do these first — none of them show up
cleanly in a packet capture:

- **Link and activity LEDs.** Is the port linked? Is it linked at the expected
  speed/duplex? A dark or flickering link LED ends many "network problems" at
  the connector.
- **Connector and cable under load.** Seat the connector; on a moving or
  vibrating machine, suspect the connector and the cable's flex point first.
- **The switched-network visibility reminder.** On a switched network a laptop
  sees only its own port's traffic plus broadcast/multicast — it does **not**
  see unicast between two other devices. Diagnosing a drop between a PLC and a
  drive requires a mirror/SPAN port or a tap, not just plugging in a laptop.
  Managed-switch port counters (CRC errors, discards, link flaps) often reveal
  the fault without any capture at all.

Only after physical, configuration, and device-diagnostic layers are clean does
a capture become the right next move — and then it belongs to the full
methodology, with synchronized clocks and a baseline to compare against.

## What to measure (all by routing, not re-explained here)

- **Switch port counters** — CRC/alignment errors, discards, link-flap count on
  the managed switch. Owned by the managed-switches page.
- **Link status** — speed/duplex, port state, uplink health.
- **Packet capture** — ring buffer spanning the event, correct capture location
  for the boundary, synchronized clocks. Owned by the packet-capture-methods and
  network-diagnostics-methodology pages.

## Common root causes

- **Duplicate IP address** — two devices claiming one address; one or both drop
  intermittently, often surfacing under traffic.
- **Cable / connector under vibration** — a marginal or flexing link that passes
  at rest and fails when the machine moves.
- **VFD / motor-cable coupling** — switching noise coupled into a comm cable
  routed too close to power; dropouts correlate with drive activity.
- **Bus termination (serial)** — missing, wrong-value, or double termination on
  RS-485 causing reflections and garbled frames.
- **Oversubscription** — a link or device saturated by multicast, broadcast, or
  cyclic traffic beyond its budget.

## Notes

Field-practice heuristics are *generally accepted practice — verify for your
installation*. Protocol-specific behavior and fault codes belong to each
protocol page and the device manual — this note routes, it does not reproduce a
vendor's fault-code list. The authoritative diagnostic sequence is the
communications diagnostics methodology, not this triage note.
