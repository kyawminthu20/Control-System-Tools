<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: SEMI
STANDARD_ID: SEMI_S8
EDITION: S8-0706 (current revision)

INDEX_TAGS:
  topics: ["ergonomics", "human_factors", "maintenance_access", "control_placement", "force_limits", "reach_envelope"]
  systems: ["semiconductor_equipment", "fab_equipment"]
-->

# SEMI S8 — Safety Guideline for Ergonomics Engineering of Semiconductor Manufacturing Equipment

## 0. Why this matters for control engineers

SEMI S8 defines ergonomics requirements for equipment that humans operate and maintain. For control engineers, the most relevant sections govern control placement, display design, and maintenance access — areas where the electrical/controls design directly affects human factors compliance. Non-compliance with S8 is a common reason for equipment rejection during fab qualification.

## 1. Control placement

- Primary controls (E-stop, operator panel) must be reachable without bending, stretching, or awkward postures
- E-stop buttons: no higher than 1,400 mm, no lower than 600 mm from the floor; reachable from normal operator position
- Displays: within the operator's normal visual field; no glare from facility lighting; text legible at normal operating distance
- Frequently used controls: within easy reach (forward reach ≤600 mm from operator's body)

## 2. Force and torque limits

Controls must be operable without excessive force:
- Pushbuttons and switches: actuation force ≤22 N (5 lb)
- Emergency stops: must be easy to actuate under stress — typically mushroom-head, ≤40 N maximum
- Panels and doors for maintenance: opening force ≤222 N (50 lb) for normally accessed panels

For maintenance tasks requiring tools, the torque required to remove fasteners should be within normal hand tool capability without extreme effort.

## 3. Maintenance access

- All field-replaceable items (components, consumables, filters) must be accessible without removing non-related assemblies
- Maintenance access must be achievable without entering confined spaces where hazardous energy is present
- Minimum clearance for maintenance access: 600 mm width, 900 mm height (for full-body access)
- Components requiring frequent access (>once per month): accessible without tools or with common tools only

## 4. Lifting and manual handling

- Single-person lifts within the equipment (replacing modules, loading wafers): ≤16 kg without mechanical assist
- Equipment that requires handling loads >16 kg must provide lifting aids (handles, hoists, carts)
- Consumable containers (chemicals, gases): sized and located for ergonomic handling

## 5. Vibration and noise

- Vibration transmitted to operators during normal use: within ACGIH/ISO 5349 hand-arm vibration limits
- Noise at operator position during normal operation: ≤80 dBA (time-weighted average 8-hour)
- Where noise exceeds 80 dBA, hearing protection requirement must be labeled on the equipment

## 6. Change log

- 2026-03-08 — Initial draft; control placement, force limits, maintenance access, lifting, vibration/noise.
