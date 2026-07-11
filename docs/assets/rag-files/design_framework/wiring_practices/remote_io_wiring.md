<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — remote I/O station wiring
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, remote_io, distributed_io, power_rails, grounding, network_segregation, emc]
  systems: [control_panels, io_systems, fieldbus_networks]
-->

# Wiring Practices — Remote I/O Station Wiring

Distilled engineering knowledge behind the site guide "Remote I/O Station
Wiring." Requirements are paraphrased at chapter/article level with
references; field practice not derivable from a standard is flagged as
generally accepted practice. Coupler/adapter designations, module ratings,
and torque values are vendor-specific and taken from the datasheet, never
generalized.

## 1. Terminal groups

A remote I/O drop is three wiring problems in one enclosure:

* **Network** — the fieldbus/industrial-Ethernet segment landing on the
  drop's adapter/coupler (bus coupler, network adapter, head module).
* **Power** — one or more 24 VDC rails feeding the coupler logic and the
  field modules; often a separate field/actuator rail.
* **Local field wiring** — the digital/analog I/O modules and their field
  terminals, wired like any PLC I/O (see the PLC wiring guide).

Contrast with **central I/O**, where all modules sit in the main PLC rack:
central I/O has one power environment and no network in the I/O path; a
remote drop distributes the I/O out to the process and adds a network, a
local power budget, and a remote environment to every calculation.

## 2. Before you start

* **Network type** — EtherNet/IP, PROFINET, EtherCAT, Modbus TCP, etc.;
  determines cabling, connectors, and addressing. Covered in the
  communications section.
* **Addressing** — node/IP or device-name assignment for the coupler;
  consistency across drops is a commissioning prerequisite.
* **Power budget per drop** — sum of coupler logic + module backplane draw +
  field/actuator load at the drop, with inrush headroom.
* **Environment at the remote location** — ambient temperature, ingress,
  vibration, and distance from the main panel (the last drives 24 VDC
  voltage drop on the feeder).

## 3. Sizing and protection

* **Per-drop 24 VDC supply and fusing:** each drop needs its 24 VDC sized
  and fused for that drop's load; a per-drop disconnect and fusing let one
  drop be isolated without dropping the network or other drops. Generally
  accepted practice; control-circuit protection basis NFPA 79 Ch. 6/Ch. 7.
* **Module-group current:** as with central I/O, grouped modules have a
  per-group total limited by the simultaneity rating — from the datasheet.
* **Separate field vs logic rails (the common gotcha):** many couplers
  provide (or expect) a separate rail for field/actuator power distinct from
  the logic/backplane power that keeps the coupler and network alive. Wiring
  both from one rail is the recurring remote-I/O mistake — see §4.

## 4. Power wiring practice

* **Separate logic vs field/actuator power rails:** run the coupler/logic
  power on its own protected rail and the actuator/field power on another, so
  that an actuator surge or field short cannot reset the coupler and drop the
  whole station off the network. Generally accepted practice.
* **Why a shared rail bites:** a solenoid or contactor inrush on a shared
  rail sags the voltage the coupler sees; the coupler resets, the whole drop
  drops off-bus, and the fault clears before anyone can measure it —
  presenting as random comms loss.
* **Distributing 24 VDC to remote panels / voltage drop:** long 24 VDC
  feeders to distant drops drop voltage under load; at 24 V the margin to the
  coupler's brownout threshold is small, so a feeder that measures fine
  unloaded can brown out the coupler under actuator load. Size the feeder for
  the loaded voltage at the far end — the `cst voltage-drop` command computes
  DC feeder drop for the run length and load. Generally accepted practice.

## 5. Control / signal wiring practice

* **Commons across a distributed drop:** the same sink/source and
  shared-vs-isolated-common discipline as central PLC I/O applies at each
  drop; do not carry a common between drops — reference each drop's I/O to its
  own supply. (See the PLC wiring guide.)
* **Analog on shielded home-runs:** keep analog signals on individual
  shielded home-runs to the drop, not daisy-chained across drops or bundled
  with digital field wiring; daisy-chaining shares noise and a single fault
  across signals. Generally accepted practice.

## 6. Grounding, shielding, EMC

* **Single-point vs multi-panel grounding across drops:** distributed drops
  in separate enclosures at different points of a plant ground reference can
  form inter-panel ground loops if 0 V/shields are bonded to local ground at
  each drop without a considered scheme. Set the grounding/bonding policy
  deliberately across drops (NFPA 79 Ch. 8 basis); the inter-panel ground
  potential difference is the same common-mode problem RS-485 physical-layer
  design addresses. Generally accepted practice.
* **Network cable segregation:** keep network cable segregated from power and
  actuator wiring — separate glands/entries, no shared bundle — per the
  copper-Ethernet guidance and NFPA 79 Ch. 16 segregation rules.

## 7. Common mistakes

1. One 24 VDC rail for both logic and actuators — actuator inrush resets the
   coupler; whole drop drops off-bus intermittently.
2. Undersized 24 VDC feeder to a distant drop — voltage drop under load
   browns out the coupler; fine unloaded, fails under actuator load.
3. Network and power sharing one gland/entry with no segregation — coupling
   and comms errors that track machine activity.
4. Analog daisy-chained across drops instead of shielded home-runs — one
   noise source or fault corrupts multiple signals.
5. Missing per-drop disconnect/fusing — cannot isolate a drop for service
   without taking down the network or other drops.
6. Inconsistent addressing (node/name) across drops — commissioning failures,
   duplicate addresses, or a device that never joins the network.

## 8. Verification highlights

* Coupler comms LED interpretation (generically): steady/solid typically
  indicates an established connection, blinking a link/config state, off no
  link — always confirm the pattern against the coupler manual.
* Per-drop loop checks: point-to-point against the drop's wiring sheets, same
  as central I/O, before the drop is put in service.
* Confirm logic and field rails are on separate fused sources and the feeder
  holds voltage at the far end under load.

## 9. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/remote-io/.
