<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-1
EDITION: 2014

IEC_HIERARCHY:
  part: "1"
  part_title: "Explosive Atmospheres — Flameproof Enclosures (Ex d)"

INDEX_TAGS:
  topics: ["flameproof", "Ex_d", "enclosure", "flame_path", "cable_gland", "conduit_seal"]
  systems: ["process_control", "oil_gas", "motors", "junction_boxes"]
-->

# IEC 60079-1 — Explosive Atmospheres: Flameproof Enclosures (Ex d)

## 0. Why this matters for control engineers

Flameproof (Ex d) is the most common protection method for motors, solenoid valves, and large terminal boxes in Zone 1 locations. Unlike intrinsic safety which prevents ignition by limiting energy, Ex d allows an internal explosion to occur but contains it — the enclosure is designed to withstand the explosion and cool escaping gases below ignition temperature before they reach the surrounding atmosphere.

## 1. Principle of protection

The Ex d enclosure:
1. **Withstands** internal ignition — the enclosure does not rupture
2. **Quenches** escaping gases — flame paths (gaps at joints and cable entries) are long enough and tight enough to cool gases below their autoignition temperature
3. **Does not ignite** the external atmosphere — surface temperatures stay within the T-code limit

This means Ex d equipment **can** have internal sparking sources (switches, motors, terminals). The enclosure provides the protection, not the internal circuit design.

## 2. Flame path requirements

The flame path is the joint between mating surfaces of the enclosure. Key parameters:

| Parameter | Purpose |
|-----------|---------|
| Gap width (w) | Must not exceed maximum allowable for gas group |
| Flame path length (L) | Minimum length to quench the flame |
| Surface finish | Must be machined — no paint or sealant on flame path surfaces |

Maximum gaps vary by gas group: IIA allows wider gaps than IIC. IIC (hydrogen service) requires the tightest tolerances. **Never apply paint, thread sealant, or anti-seize to flame path surfaces** — this changes the effective gap.

## 3. Cable entry methods

All openings in an Ex d enclosure must be sealed. Three accepted methods:

| Method | Description | Notes |
|--------|-------------|-------|
| Ex d certified cable gland | Gland with integral flame path | Most common; gland must match cable type and enclosure gas group |
| Ex d stopping plug | Blanks unused entries | Must be certified; do not use standard plugs |
| Conduit with conduit sealing fitting | Threaded conduit + EYS/EYC seal filled with sealing compound | Required for NEC conduit systems in Division locations; not typical in IEC Zone installations |

## 4. Installation requirements

- **Do not open** energized Ex d equipment in a hazardous atmosphere — de-energize first and allow cooling if the equipment generates heat
- **Inspect flame paths** at every opening — replace if damaged, corroded, or out of tolerance
- **Fastener torque** — all cover fasteners must be fully engaged; missing fasteners invalidate the protection
- **Conduit drainage** — condensation in conduit must drain away from the Ex d enclosure, not into it
- **Breathing and draining devices** — use only Ex d certified versions

## 5. Common installation errors

- Over-torquing covers causes distortion of flame paths (Ex d enclosures are precision-machined)
- Applying thread compound to threaded flame path entries
- Using non-certified cable glands (standard industrial glands are not Ex d rated)
- Leaving unused entries with standard plugs instead of Ex d certified stopping plugs
- Adding field modifications (extra holes, larger openings) that are not on the certificate

## 6. Change log

- 2026-03-08 — Initial draft; Ex d principle, flame path requirements, cable entry methods, installation errors.
