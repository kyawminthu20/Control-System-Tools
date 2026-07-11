<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — control power distribution (CPT, 24 VDC PSU, fusing)
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, control_power, transformer, cpt, power_supply, fusing, inrush, grounded_control_circuit, coordination]
  systems: [control_panels, control_circuits, power_distribution]
-->

# Wiring Practices — Control Power Distribution

Distilled engineering knowledge behind the site guide "Control Power
Distribution — Transformers, Supplies, and Fusing." Requirements are
paraphrased at chapter/article level with references; field practice not
derivable from a standard is flagged as generally accepted practice.

## 1. Where control power comes from

A machine's control power is derived and distributed, not taken raw from the
line. Two schemes dominate, often together:

* **Control power transformer (CPT)** — steps line voltage down to the AC
  control voltage (commonly 120 VAC in North America) for contactor coils,
  relays, pilot devices, and legacy control.
* **Switch-mode power supply (PSU)** — produces regulated 24 VDC for PLC I/O,
  sensors, HMIs, network devices, and modern control.

Both feed **terminal groups** — fused distribution terminals or bus bars —
from which individual control branches are taken. The distribution and
protection scheme (what is fused, where, and how the branches are grouped)
is as important as the source device.

## 2. Before you start

* **Control voltage choice — 120 VAC vs 24 VDC.** Set upstream by the
  installed base, device availability, and safety preference (24 VDC is
  low-voltage and common on modern machinery). Many panels run both.
* **Load inventory and inrush.** Total the steady-state VA/current of every
  control load AND its inrush — coil pickup for AC, capacitive input surge
  for DC devices. Inrush, not steady state, is the sizing trap (see below).
* **Grounded vs ungrounded control circuit.** Decide whether the control
  circuit has one side intentionally bonded to ground or is left ungrounded.
  This is a design decision with code and fault-detection consequences, made
  before wiring.

## 3. Sizing and protection (the core)

### CPT sizing — steady-state PLUS inrush

The classic control-power mistake is sizing a CPT on **holding VA** alone.
Contactor and solenoid coils draw several times their holding VA at the
instant of pickup (sealed/holding VA vs inrush/sealed-in VA differ markedly).
A CPT sized only for the summed holding load will sag when several coils pick
up together — the voltage dips, coils chatter or fail to seal, and the panel
behaves erratically. Size the CPT so it holds the steady-state load **and**
supplies the simultaneous inrush without excessive voltage dip; transformer
makers publish inrush/sealed VA sizing guidance for exactly this. Generally
accepted practice, grounded in the coil inrush characteristic — verify with
the transformer manufacturer's sizing data and coil VA ratings. The `cst
transformer` tool computes the OCPD limits (NEC Table 450.3(B)) for a given
CPT; coil VA totals come from the device data.

### CPT fusing — primary and secondary

* **Both primary and secondary are protected.** The primary OCPD protects
  the transformer and the supply-side conductors; the secondary OCPD
  protects the control-circuit conductors and allows the primary device to
  be sized around inrush. NFPA 79 (control-circuit protection chapter) and
  NEC Art. 450 (transformer overcurrent protection, Table 450.3(B)) and Art.
  430 Part VI (motor-control-circuit protection) govern the permitted
  ratings — at chapter/article level; the specific percentages come from the
  code tables, not reproduced here.
* Where the control circuit is derived from a motor controller, NEC Art. 430
  Part VI applies to the control-circuit tap and its protection.

### 24 VDC PSU sizing and per-branch fusing

* **Size the PSU with margin and for inrush.** Sum the 24 VDC load with
  headroom (a common target is meaningful spare capacity), and account for
  the capacitive inrush of the connected devices at power-up — an
  undersized supply sags or hiccups on turn-on. The exact margin and inrush
  behavior are vendor-specific — consult the supply datasheet. Generally
  accepted practice.
* **Fuse 24 VDC per branch.** Distribute 24 VDC through individually
  protected branches (fused terminals or electronic circuit protectors) so a
  single shorted device or field fault trips only its branch, not the whole
  supply. One shorted solenoid should not drop the PLC. Generally accepted
  practice.
* **Selective coordination.** Arrange branch and main protection so the
  device nearest the fault clears first, leaving the rest of the panel up.
  The concept applies to both the AC control side and the 24 VDC side;
  coordination is verified against the device time-current data.

## 4. Power wiring

* **CPT connections.** Primary to the line side through its OCPD; secondary
  to the control bus through the secondary OCPD. Terminal designations and
  torque are vendor-specific — consult the manual.
* **Grounded control circuit.** NFPA 79 requires that where one side of the
  control-circuit transformer secondary is grounded, the grounded conductor
  is arranged so a ground fault cannot energize a coil or start a machine
  function; the ungrounded side carries the switching and the OCPD.
* **PSU input/output distribution.** Input through its protection; output to
  a 24 VDC bus bar or distribution terminals, from which fused branches
  leave.
* **Redundancy.** Where uptime demands it, diode-OR (redundancy) modules
  combine two supplies so one can fail without dropping the bus; the 24 VDC
  bus is then fed from the redundancy module. Generally accepted practice.

## 5. Control / signal wiring

* **Conductor identification.** NFPA 79 (wiring/conductor-identification
  chapter) specifies control-circuit conductor colors/identification —
  distinct identification for AC control, DC control, and for conductors
  that remain energized with the main disconnect open (externally supplied).
  Follow the chapter; specifics not reproduced here.
* **Keep control power separate from field signal.** Do not run control
  power (coil/relay switching) in the same bundle as low-level analog or
  network signal wiring; segregation is covered in the EMC guide.

## 6. Grounding, shielding, and EMC

* **CPT secondary bonding.** Bond the designated secondary conductor to the
  equipment grounding system per NFPA 79 for a grounded control circuit; the
  deep bonding treatment is owned by the grounding/bonding guide.
* **PSU 0 V reference policy.** Decide whether the 24 VDC 0 V (common) is
  referenced to ground or left floating — a per-design decision with
  fault-detection consequences mirroring the AC grounded/ungrounded choice;
  follow a consistent policy across the panel. Generally accepted practice.
* **Suppression on the control-power side.** Coil suppression (RC/diode/MOV)
  and input surge protection reduce switching noise coupled back into the
  control supply; device-specific, per the manual.

## 7. Common mistakes

1. **CPT sized on holding VA, not inrush** — the transformer browns out when
   several coils pick up together; contactors chatter or fail to seal.
2. **No secondary fuse** — the CPT is protected but the control-circuit
   conductors are not, and the primary device cannot be sized around inrush
   without over-protecting the wiring.
3. **One 24 VDC supply with no per-branch fusing** — a single shorted field
   device collapses the whole 24 VDC bus and drops the PLC.
4. **Ungrounded control circuit where a first ground fault goes undetected**
   — the machine keeps running on a hidden fault until a second fault causes
   an unexpected operation.
5. **Undersized 24 VDC PSU** — the supply sags or hiccups under device
   inrush at power-up; the PLC resets or I/O drops out on every start.
6. **Mixing grounded and ungrounded schemes** — part of the control circuit
   is grounded and part floating, defeating both fault-detection strategies
   and confusing troubleshooting.

## 8. Verification

* Measure control voltage **under load and during coil pickup**, not just at
  rest, to confirm the CPT holds the inrush without excessive dip.
* Verify fuse/OCPD ratings and coordination against the device data — the
  branch nearest a fault clears first.
* Test ground-fault behavior appropriate to the chosen scheme (a grounded
  circuit trips its branch; an ungrounded circuit is monitored).

## 9. Standards references

* **NFPA 79** — control-circuit and control-power protection chapter,
  grounded-control-circuit requirements, and conductor-identification
  chapter, at chapter level.
* **NEC (NFPA 70)** — Art. 450 (transformer overcurrent protection, Table
  450.3(B)); Art. 430 Part VI (motor-control-circuit protection), at
  article level.
* **IEC 60204-1** — control-circuit and control-supply clause (including
  control-transformer and protective measures), at clause level.
