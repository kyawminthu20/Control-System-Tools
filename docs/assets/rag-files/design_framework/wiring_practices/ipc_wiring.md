<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — industrial PCs (IPCs)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, ipc, edge, hmi, power_supply, grounding, emc, ups]
  systems: [control_panels, edge_devices, hmi, industrial_computing]
-->

# Wiring Practices — Industrial PCs (IPCs)

Distilled engineering knowledge behind the site guide "Industrial PC (IPC)
Wiring & Installation." Requirements are paraphrased at chapter/article level
with references; field practice not derivable from a standard is flagged as
generally accepted practice.

An IPC — box PC, panel PC, edge gateway, or PC-based controller/HMI — is at
heart a computer with non-volatile storage and an operating system, wearing
industrial packaging. That packaging (DC input, fanless/wide-temperature
design, DIN-rail or panel mounting, conformal-coated boards) is what separates
it from an office PC, and the wiring rules follow from treating it as a
computer that must survive a panel environment.

## 1. Terminal / port groups

An IPC presents several distinct connection groups, each with its own rules:

* **Power input** — most commonly a 24 VDC feed on a pluggable terminal
  (often with a redundant/second input); some larger units are AC-input.
* **Protective earth / functional earth** — a chassis PE lug and, frequently,
  a separate functional-earth (FE) stud for the reference/shield network.
* **Network ports** — one or more Ethernet ports (often segregated: a
  control/fieldbus port and a plant/IT port).
* **Field and peripheral ports** — USB, isolated or non-isolated serial
  (RS-232/RS-485), digital I/O on some models.
* **Display / KVM** — DisplayPort/HDMI/DVI/VGA and USB for panel-mount or
  remote operator interface; length limits are interface-specific.

Terminal designations, connector pinouts, torque values, and input-voltage
tolerance windows are vendor-specific — always taken from the device manual,
never generalized.

## 2. Before-you-start decisions

* **Input variant:** DC (typically nominal 24 VDC) vs AC. The tolerance band,
  peak/idle draw, and inrush are on the nameplate/datasheet — verify, do not
  assume a generic 24 V device tolerates your rail.
* **Holdup / UPS:** an IPC runs a real filesystem. A power blip mid-write can
  corrupt storage or the OS image. Orderly shutdown on power loss requires
  either an internal holdup capacitor/UPS, an external 24 VDC UPS module, or a
  shutdown signal (loss-of-power input) wired so the OS can flush and halt.
  Generally accepted practice — treat holdup as a requirement, not an option.
* **Mounting / orientation:** fanless units reject heat by convection through
  the chassis; the datasheet specifies allowed mounting orientation and
  clearance. Wrong orientation or blocked airflow silently derates the unit.
* **Environmental rating vs location:** enclosure/ingress rating, ambient
  temperature, and vibration limits are vendor-specific — verify the unit
  against the actual mounting location.

## 3. Sizing and protection

* **24 VDC supply sizing:** size the 24 V supply for the IPC's **peak** draw
  plus margin, not its idle draw, and account for **inrush** at power-up
  (input bulk capacitance charges as a brief high current). Datasheet peak,
  inrush, and any UPS-charging load are vendor-specific values — sum them and
  verify against the supply rating. `cst voltage-drop` checks the feeder run.
* **Fusing the IPC feed:** provide branch protection on the IPC's DC feed
  sized to the device rating; a dedicated fused feed (rather than sharing an
  OCPD with unrelated loads) keeps a downstream fault from dropping the
  computer. Generally accepted practice — verify against your panel design and
  NFPA 79 Ch. 7 control-circuit protection provisions.
* **Shared-rail risk:** powering the IPC from the same 24 V rail as contactor
  coils, solenoids, and brakes exposes the computer to the switching
  transients and voltage sags those inductive loads produce. A sag below the
  IPC's dropout threshold reboots it. Give the IPC a clean, dedicated (ideally
  UPS-backed) supply. Generally accepted practice.
* **Surge protection:** DC power and network entries into the panel are
  candidates for surge protection where the installation is exposed
  (long runs, outdoor/field devices, lightning-prone sites). SPD selection is
  application-specific — verify need and rating for the installation.

## 4. Power wiring practice

* **Dedicated clean feed:** run a dedicated 24 VDC feed from the clean side of
  the supply, separated from noisy inductive-load wiring.
* **Redundant / UPS-backed input:** where the IPC has dual inputs, feed them
  from independent supplies (diode-OR / redundancy module) or back the feed
  with a 24 VDC UPS so a supply loss triggers an orderly shutdown rather than
  a hard cut. Generally accepted practice.
* **Protective earth is not optional on a DC device.** A DC-powered IPC still
  requires its chassis bonded to protective earth (IEC 60204-1 equipotential
  bonding; NFPA 79 Ch. 8 grounding/bonding). The PE connection is a safety and
  reference-integrity requirement independent of the power being DC.
* **Functional earth stud:** many IPCs provide a separate FE stud for the
  signal-reference/shield network; connect it per the device manual — FE and
  PE serve different purposes and are not interchangeable.
* **Terminations / torque:** conductor range and terminal torque come from the
  device manual; record the values used.

## 5. Ports and connections practice

* **Network segregation:** where the IPC has separate control and plant/IT
  ports, keep them on their intended networks; do not bridge unintentionally.
  Route network cable away from drive-output and other power wiring — the
  separation rules are owned by the EMC and copper-Ethernet material.
* **USB / serial for field devices:** USB is convenient but not a rugged field
  bus — captive/locking connectors and short runs where used for anything
  permanent. For serial field devices confirm **isolated vs non-isolated**
  RS-232/RS-485 ports: a non-isolated serial port tied to a device on a
  different ground reference is a ground-loop path. Consult the device manual.
* **Display / KVM length limits:** DisplayPort/HDMI/DVI/VGA and USB each have
  interface-specific maximum passive-cable lengths; beyond them use active
  cable or KVM-extender hardware. Verify limits per interface and cable.

## 6. Grounding, shielding, EMC

Device-specifics here; the deep treatment is owned by the EMC guide.

* **Chassis PE bond:** short, low-impedance bond from the chassis PE lug to
  the panel ground system; mask/scrape paint at the bond point.
* **Functional-earth stud purpose:** the FE stud references the internal
  signal ground and shield terminations; wiring it correctly (per manual)
  keeps shield currents off the PE safety path.
* **Clean-side placement:** mount the IPC on the clean side of the panel, away
  from VFD output cables and other high-dV/dt sources; separation distances
  are owned by the EMC guide.
* **Shielded network entries:** use shielded network cable for runs exposed to
  panel noise and bond the shield per the port/segregation scheme.

## 7. Verification highlights

* **Clean-shutdown-on-power-loss test:** with holdup/UPS in place, cut the
  feed and confirm the IPC performs an orderly shutdown (or rides through)
  rather than a hard power-off — the single most valuable IPC commissioning
  check. Generally accepted practice.
* **Thermal check under load:** run the unit at expected load in the final
  orientation and enclosure and confirm it stays within the datasheet thermal
  envelope.
* **Port / comms verification:** confirm each network port on its intended
  network, serial isolation/wiring correct, and display/peripheral runs within
  length limits.

## 8. Standards references

* **NFPA 79:2024** — Ch. 7 (control-circuit protection), Ch. 8 (grounding and
  bonding, PE requirements), Ch. 13 (control equipment location/mounting) at
  chapter level.
* **IEC 60204-1** — protective bonding / equipotential bonding for machine
  electrical equipment (PE requirement independent of DC supply).
* **Manufacturer environmental/electrical specification** — input tolerance,
  inrush, holdup, thermal, mounting, and ingress ratings are the governing
  vendor category for values this guide deliberately does not reproduce.

## 9. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/ipc/.
