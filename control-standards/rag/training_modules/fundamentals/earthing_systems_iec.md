<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

MODULE_FAMILY: TRAINING_FUNDAMENTALS
MODULE_ID: earthing_systems_iec
LEARNING_LEVEL: foundational

SOURCE: transcript-derived work note, cleaned and promoted from control-standards/work/design/types of grounding.md
SOURCE_RANGE: 0:00–11:37 (instructional video on IEC earthing system types)
SOURCE_AUDIENCE: site engineers, junior electrical engineers

INDEX_TAGS:
  topics: ["earthing", "grounding", "TN-C", "TN-S", "TN-C-S", "TT", "IT", "PEN", "fault_current", "protective_conductor", "RCCB", "touch_voltage", "PME"]
  standards: ["IEC_60364", "IEC_60204_1"]
  systems: ["machine_supply", "building_electrical", "industrial_installation", "panel_design"]
-->

# IEC Earthing System Types

## 0. Purpose

Use this module to understand how the earthing arrangement of an electrical installation
affects fault-current path, protective-device operation, and touch-voltage risk.

The earthing system must be known early in a machine or panel design project. It affects
protective-device strategy, bonding design, touch-voltage risk, and whether control circuits
can reference earth directly.

## 1. The IEC letter code

The IEC earthing classification uses two or three letters:

### First letter — source connection to earth

| Letter | Meaning |
|---|---|
| `T` | Source neutral directly connected to earth |
| `I` | Source isolated from earth, or connected through high impedance |

### Second letter — exposed-part connection method

| Letter | Meaning |
|---|---|
| `T` | Exposed conductive parts connected to a **local** earth electrode |
| `N` | Exposed conductive parts connected to the **supply-system** neutral or protective conductor |

### Additional letters — neutral and PE relationship (TN systems only)

| Letter | Meaning |
|---|---|
| `C` | Neutral and protective-earth functions **combined** in one conductor (PEN conductor) |
| `S` | Neutral and protective-earth functions **separate** conductors |

## 2. TN-C

Source neutral earthed. Exposed parts connected to a combined PEN conductor (neutral = PE).

### Characteristics
- Fault current returns through the PEN conductor — metallic path, low impedance
- Overcurrent protective devices can clear faults reliably
- No separate protective-earth conductor required — lower conductor cost

### Key risk
A break or loose connection in the upstream PEN conductor can elevate all bonded metalwork
(motor frames, machine casings, panel enclosures) to a dangerous voltage.

### Typical context
Distribution network sections; not recommended inside buildings or industrial facilities.

## 3. TT

Source neutral earthed. Exposed parts connected to a **local** earth electrode independent of
the supply neutral.

### Characteristics
- No dependency on a combined PEN conductor
- Fault current returns through soil back to the transformer neutral — high loop impedance
- Low fault-current magnitude may be insufficient to operate overcurrent devices quickly

### Protection dependency
TT systems depend heavily on:
- Residual-current circuit breakers (RCCB / RCD) for fault detection
- Earth-electrode and soil performance

### Typical context
Rural areas, standalone buildings, farmhouses where a utility earth conductor is not extended
to the installation.

## 4. TN-C-S (PME)

Neutral and PE combined for part of the supply path (PEN), then separated at a defined split point inside the installation. Also known as Protective Multiple Earthing (PME).

### Characteristics
- Inside the installation, equipment connects to a dedicated protective conductor after separation
- Fault current returns through a low-impedance metallic path after the split point
- Overcurrent devices operate faster than TT for internal faults

### Remaining dependency
An upstream PEN break before the split point can still elevate metalwork to dangerous voltage —
the same failure mode as TN-C, but only upstream of the separation point.

### Typical context
Urban residential supplies; the utility brings a PEN conductor, and neutral/PE are split at
the consumer unit or service entrance.

## 5. TN-S

Neutral and protective earth are separate conductors from the transformer onward. No combined
PEN section exists anywhere in the system.

### Characteristics
- Dedicated low-impedance PE path from source to load
- No combined-conductor failure mode
- Faster and more reliable operation of protective devices
- Lower touch-voltage risk
- Better electromagnetic compatibility (EMC) — cleaner separation of return and earth paths

### Tradeoff
Higher conductor cost — a dedicated PE conductor must run from the source throughout the system.

### Typical context
Large industrial plants, hospitals, data centers, high-reliability installations.

## 6. IT

Source isolated from earth or connected through high impedance. Exposed parts are earthed locally.

### Characteristics
- First phase-to-earth fault does not immediately trip the system
- Supply continuity is maintained after the first fault
- Insulation monitoring device (IMD) required to detect the first fault
- Second earth fault on a different phase does create a short circuit — action required after the first fault is detected

### Tradeoff
Requires disciplined insulation monitoring and a design culture that responds promptly to first-fault alarms.

### Typical context
Hospitals (operating theatres), mines, critical process industries where loss of supply is more
dangerous than a first earth fault.

## 7. Practical comparison

| System | Fault-return path | Clearing method | Main risk | Typical context |
|---|---|---|---|---|
| TN-C | Metallic PEN | Overcurrent device | PEN break energizes metalwork | Distribution, older workshops |
| TT | Soil to source neutral | RCCB essential | High loop impedance; soil/electrode dependent | Rural installations |
| TN-C-S | Metallic PE after split | Overcurrent device | Upstream PEN break still possible | Urban residential, PME supply |
| TN-S | Dedicated metallic PE | Overcurrent device | Higher conductor cost | Industrial, hospital, data centre |
| IT | Isolated/impedance source | IMD + overcurrent on second fault | First fault undetected without IMD | Hospital theatres, mines |

## 8. The practical questions to ask

When assessing or designing for any earthing system:

1. Does fault current return through a metallic path or through soil?
2. Is protection primarily relying on overcurrent devices or residual-current devices?
3. Is there a dependency on a combined PEN conductor — and where?
4. Is continuity of service more important than immediate trip on first earth fault?
5. What earthing arrangement does the utility actually deliver to the installation boundary?

## Related standards

- IEC 60204-1 Clause 5 — Incoming supply requirements for machine electrical equipment
- IEC 60204-1 Clause 8 — Equipotential bonding requirements
- IEC 60364 — Low-voltage electrical installations (earthing arrangements defined here)
- NEC Article 250 — US grounding and bonding (different terminology, different classification model)

## Related modules (this corpus)

- [conductor_ampacity_and_termination_temperature.md](./conductor_ampacity_and_termination_temperature.md) — conductor sizing; termination temperature rules
- [NEC grounding and bonding module](../nec_application/grounding_bonding_control_panels.md) — US Art. 250 grounding (different system, complementary topic)

## Important caution

This module is derived from a transcript-based work note. The ranking and descriptions are
intentionally simplified for teaching. Actual system selection and protection design still
depend on the governing standard set, utility practice, fault levels, bonding details,
residual-current protection strategy, and the operating continuity requirements of the
installation.
