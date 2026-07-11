<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
TOPIC: wiring practices — PLC power, I/O, and commons
SOURCE_BASIS: paraphrase of published-standard requirements + generally accepted practice (flagged)
INDEX_TAGS:
  topics: [wiring, plc, io, digital_io, commons, sink_source, freewheeling_diode, emc]
  systems: [control_panels, plc_systems, io_systems]
-->

# Wiring Practices — PLC Power, I/O, and Commons

Distilled engineering knowledge behind the site guide "PLC Wiring — Power,
I/O, and Commons." Requirements are paraphrased at chapter/article level
with references; field practice not derivable from a standard is flagged as
generally accepted practice. Terminal designations, per-point ratings, and
torque values are vendor-specific and always taken from the module
datasheet, never generalized.

## 1. Terminal groups

A PLC I/O system presents a small number of distinct wiring zones, and the
**module type dictates the wiring** for each:

* **Controller/backplane power** — the logic supply that runs the CPU and
  backplane (commonly 24 VDC, sometimes 120 VAC on older/larger racks).
* **Digital input group(s)** — field contacts and sensors landing on an
  input module, referenced to an input common (per-point or per-group).
* **Digital output group(s)** — the module's switching elements driving
  field loads, referenced to an output common, with the output *type*
  (relay dry contact, sourcing/sinking transistor, triac) setting the rules.
* **Analog I/O** — low-level signal wiring on shielded home-runs; deferred
  to the 4-20 mA guide.
* **Field-device power** — the separate 24 VDC (or line) supply that powers
  sensors and actuators, distinct from backplane/logic power.

The common/return terminals are the recurring source of confusion: whether a
group shares one common or provides isolated commons determines what field
supplies may be tied together.

## 2. Before you start (datasheet-driven)

Field wiring cannot be finalized from the schematic alone — the module
datasheet decides:

* **Input type** — sinking vs sourcing (which polarity the input common
  sits at), and whether the sensor is PNP or NPN; the two must agree.
* **Output type** — relay (dry contact, AC/DC, isolated), sourcing or
  sinking transistor (DC only), or triac (AC only); load compatibility and
  freewheeling requirements follow from this.
* **Voltage and per-point current limits**, and whether commons are
  per-point or per-group (common groupings define isolation boundaries).
* **Simultaneity / derating** — many modules cannot carry every point at
  full current at once or at elevated ambient; the datasheet gives the
  simultaneity curve.

## 3. Sizing and protection

* **Control-power fusing:** control circuits are typically supplied at a
  reduced voltage (24 VDC or 120 VAC) via a control transformer or power
  supply, and protected as a control circuit (NFPA 79 Ch. 7 control-circuit
  protection; Ch. 6 overcurrent protection at chapter level). The 24 VDC
  logic supply and field-device supply are each fused per their rating.
* **Output-point current limits:** each output point has a maximum
  continuous current and, on grouped modules, a per-group total that the
  simultaneity rating caps. Fused-output modules protect each point/group
  internally; unfused-output modules require external fusing sized to the
  point rating — verify which type you have from the datasheet.
* **Inrush vs steady-state:** the field-device rating that matters is the
  load's inrush (lamp filaments, contactor coils, capacitive inputs of
  downstream supplies), not just its steady-state draw. A transistor output
  rated for the steady current can be destroyed by tungsten-lamp or
  capacitive inrush. Generally accepted practice — size to inrush and
  verify against the module's surge rating.
* **Interposing relays:** when the field load exceeds the output point's
  rating (current, voltage, AC vs DC, or isolation), drive an interposing
  relay from the PLC output and switch the load through the relay contact.
  Generally accepted practice.

## 4. Power wiring practice

* **24 VDC supply:** most modern PLC logic and field I/O run on a regulated
  24 VDC supply sized for the summed logic + field load with headroom for
  inrush. Generally accepted practice.
* **Redundant / diode-OR supplies:** critical systems may use dual supplies
  combined through a redundancy (diode-OR) module so one supply can fail
  without dropping the rail; an overview point, detailed sizing left to the
  supply vendor.
* **Backplane vs field power separation:** keep logic/backplane power and
  field/actuator power on separate protected rails so a field short or
  actuator surge cannot brown out the CPU. Generally accepted practice.

## 5. Control / signal wiring practice (the core)

* **Sinking vs sourcing DI:** the classic mismatch. A PNP (sourcing) sensor
  delivers +V when active and needs a *sinking* input group (common tied to
  0 V / negative). An NPN (sinking) sensor pulls the point to 0 V when active
  and needs a *sourcing* input group (common tied to +V / positive). Sensor
  output type and input-card common polarity must match, or the input never
  reads or reads inverted.
* **Shared vs isolated commons:** a shared common ties every point in a
  group to one return. That is fine within one field supply, but tying two
  independently-fed circuits through a shared common — or bridging an
  isolated group's common to another supply — creates sneak (backfeed) paths
  where current finds an unintended return and points read energized that
  are not. Use isolated commons where circuits are fed from different
  supplies or must not interact. Generally accepted practice.
* **DO types and freewheeling diodes:** relay (dry contact) outputs switch
  AC or DC and need no polarity attention but wear and bounce. Sourcing
  transistor outputs (DC only) are fast and silent but are polarity-sensitive
  and vulnerable to the inductive kickback of DC coils. **Every switched
  inductive DC load (relay/contactor coil, solenoid, valve) needs a
  freewheeling (flyback) diode across the coil** to clamp the turn-off spike,
  or the transistor output degrades and fails. AC inductive loads on triac
  outputs use RC snubbers/MOVs instead. Generally accepted practice, echoed
  by every module vendor.
* **Wire numbering / terminal discipline:** every wire identified at each
  termination to match the schematic (NFPA 79 Ch. 16); DC control wiring is
  conventionally blue and AC control red, with orange reserved for
  externally-sourced interlock circuits that stay hot when the main
  disconnect is off (NFPA 79 Ch. 16 color conventions).

## 6. Grounding, shielding, EMC

* **0 V reference bonding policy:** whether the 24 VDC 0 V rail is bonded to
  PE (grounded reference) or left floating is a system decision made once and
  applied consistently; a mix produces ground loops and phantom inputs. Set
  the policy per the panel grounding/bonding guide (NFPA 79 Ch. 8 grounding
  and bonding basis). Generally accepted practice — verify for your
  installation.
* **Analog card grounding:** low-level analog I/O uses shielded home-runs
  with the shield grounded at one end per the 4-20 mA guide; brief pointer
  only here.
* **Suppression on switched inductive loads:** flyback diodes (DC) and
  snubbers/MOVs (AC) at the coil are also EMC measures — they kill the
  switching transient at its source; deep separation/segregation belongs to
  the EMC guide.

## 7. Common mistakes

1. Sink/source mismatch — PNP sensor on a sourcing input group (or NPN on
   sinking); input never asserts or reads inverted.
2. No freewheeling diode on a DC inductive output — transistor output
   degrades then fails; intermittent then dead output.
3. Shared-common sneak paths — points from a second supply backfeed through
   a common, energizing inputs that are physically open.
4. Output overload without an interposing relay — welded relay contacts or a
   blown transistor when the field load exceeds the point rating.
5. Mixing 24 V and higher voltages in one group where insulation is rated
   only for the lower voltage (NFPA 79 Ch. 16 voltage-segregation rule).
6. Floating unused inputs on a module that needs a defined state — noise
   toggles the point; tie unused inputs to the group's defined level.

## 8. Verification highlights

* Point-to-point continuity against the loop/wiring sheets before energizing
  (evidence-retaining checklist in the commissioning templates).
* Confirm each input group's common polarity matches its sensors, and each
  output group's common matches its load supply, before applying field power.
* Force outputs only with the machine in a safe, de-energized-actuator state
  and personnel clear — forcing drives the physical output.

## 9. Change log

* 2026-07-11 — Initial draft (Phase 38 Wave 1); paired with docs/design/wiring/plc/.
