<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S14
EDITION: S14-1110 (current revision)

INDEX_TAGS:
  topics: ["fire_risk_assessment", "flammability", "ignition_sources", "fire_suppression", "cleanroom_fire", "fab_safety"]
  systems: ["semiconductor_equipment", "fab_equipment", "process_equipment"]
-->

# SEMI S14 — Safety Guideline for Fire Risk Assessment and Fire Safety for Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

Semiconductor equipment uses flammable process gases, solvents, and chemicals in a cleanroom environment where fire suppression is complex and fire spread can be rapid. SEMI S14 requires a fire risk assessment for all equipment, and the control system design directly affects fire risk — gas shutoff interlocks, exhaust monitoring, and automatic fire response are control engineering deliverables.

## 1. Fire risk assessment process

The S14 fire risk assessment evaluates:
1. **Ignition sources** — electrical arcs, hot surfaces, static discharge, mechanical friction
2. **Fuel sources** — flammable gases, process chemicals, plastic components, wiring insulation
3. **Oxidizers** — oxygen from air, process oxygen, oxidizing gases
4. **Fire scenarios** — credible combinations of ignition, fuel, and oxidizer
5. **Mitigation measures** — controls, detection, suppression, separation

The assessment result determines the fire protection measures required for each identified scenario.

## 2. Material flammability classification

S14 classifies materials in the equipment by flammability:

| Class | Flammability | Examples | Controls Required |
|-------|-------------|---------|-----------------|
| Non-combustible | Cannot burn | Metals, ceramics | None |
| Limited combustibility | Will not propagate flame | Certain plastics (UL94 V-0) | Minimize mass |
| Combustible | Burns with difficulty | Many plastics | Fire detection + suppression consideration |
| Flammable | Burns readily | Solvents, some polymers | Substitution, isolation, suppression |
| Highly flammable | Burns with vigorous flame | Process gases, low-flash solvents | Substitution preferred; tight controls if unavoidable |

## 3. Ignition source control (controls engineering)

Control engineers must address these ignition sources in equipment design:

- **Electrical arcs:** Use arc-flash-rated enclosures for high-energy circuits; size overcurrent protection to limit arc duration
- **Hot surfaces:** Heater circuits must have over-temperature protection independent of the process controller — a separate thermocouple and hardwired high-temperature cutout
- **Static discharge:** Ground all conductive components; antistatic materials for plastic components near flammable materials
- **Motor overheating:** Motor overload protection must be sized and set correctly; thermal overload relays preferred over circuit breakers alone for continuous-duty motors in enclosed equipment

## 4. Fire detection and response

S14 requires automatic fire detection for equipment containing:
- Flammable or pyrophoric gases
- Flammable liquid volumes above defined thresholds
- Materials that, if on fire, could spread to adjacent equipment or the cleanroom

**Detection methods:** Point heat detectors, optical flame detectors, or aspirating smoke detectors depending on the enclosure environment.

**Automatic response sequence (example for flammable gas equipment):**
1. Fire detected → immediate closure of all flammable gas supply valves
2. Increase exhaust flow to maximum
3. Alert operator (audible + visual)
4. If suppression system present: initiate after delay (allow personnel evacuation)
5. Disable process restart until manual reset by qualified personnel

## 5. Cleanroom-specific considerations

- Cleanroom HVAC systems can spread fire products rapidly — equipment fire control must be self-contained where possible
- Water-based suppression is generally prohibited in cleanrooms (wafer damage, equipment damage, slip hazard)
- Clean agent systems (FM-200, Novec 1230, CO2 for some areas) are the standard approach
- Equipment with local suppression must coordinate with the facility-wide fire alarm and suppression systems

## 6. Change log

- 2026-03-08 — Initial draft; risk assessment process, material classification, ignition source control, fire detection/response, cleanroom considerations.
