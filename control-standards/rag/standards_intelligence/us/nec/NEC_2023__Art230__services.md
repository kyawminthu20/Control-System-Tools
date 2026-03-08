<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "230"
  article_title: "Services"

INDEX_TAGS:
  topics: ["service_entrance", "service_disconnect", "service_conductors", "available_fault_current", "SCCR"]
  systems: ["power_distribution", "industrial_facility"]
-->

# NEC 2023 — Article 230 — Services

## 0. Why this article matters for control engineers

The service is the origin of all facility wiring. Its characteristics — especially the **available fault current** — determine the SCCR requirements for every panel, MCC, and piece of equipment downstream. Control engineers must understand the service to correctly verify that panel SCCR ratings (Art. 409) are adequate for the installation.

## 1. Service components

A complete service installation includes:

| Component | Description |
|-----------|-------------|
| Service drop / lateral | Utility conductors from the utility grid to the service entrance |
| Service entrance conductors | Conductors from the service point to the service equipment |
| Service equipment | The main disconnect and OCPDs at the service entrance point |
| Metering equipment | Utility revenue meters (utility-owned) |

**Service point:** The junction between the utility facilities and the premises wiring. This is where NEC authority begins. Everything on the utility side of the service point is outside NEC scope.

## 2. Service disconnecting means (230.70, 230.71)

Every service must have a means to disconnect all ungrounded service conductors. Requirements:

- Located at a readily accessible location — nearest the point of entrance, on the exterior or interior of the building
- Cannot be in bathrooms
- Must be clearly marked to identify it as the service disconnect
- **Maximum six disconnects per service** — a single service may have up to six service disconnecting means (six-disconnect rule)

**Industrial facilities** typically use a single main switchgear or main breaker to satisfy the service disconnect requirement, with all downstream distribution originating from that point.

## 3. Available fault current and SCCR (230.67 reference, 110.24)

**Available fault current** at the service entrance is determined by the utility transformer impedance, conductor impedance, and system configuration. Facilities must:

1. Determine the available fault current at the service point (typically from the utility)
2. Verify all service equipment is rated for that available fault current
3. Document the available fault current at the service disconnecting means per NEC 110.24
4. Ensure all downstream equipment (panels, MCCs, drives) has SCCR ≥ available fault current at their installation point

**Typical industrial values:**
- Small commercial/industrial facilities: 10–25 kA available at service
- Large industrial facilities: 42–100 kA or higher at the service point

Available fault current decreases downstream as conductor impedance increases. This is why SCCR requirements for a panel in a remote building are lower than for a panel directly at the main switchgear.

## 4. Service conductor sizing (230.42)

Service entrance conductors must have ampacity not less than the load determined per Art. 220. They are sized similarly to feeders but are not protected from overcurrent at their supply end (the utility connection). Protection is provided by the service equipment OCPD.

## 5. Grounding at the service (250.24)

The neutral conductor is grounded at the service equipment — the **neutral-to-ground bond**. This bond occurs **only at the service**. Downstream panels and separately derived systems must NOT have a neutral-to-ground bond (they connect only the EGC to ground). Creating a second neutral-to-ground bond downstream creates a parallel ground path, causes nuisance breaker trips, and creates safety hazards.

## 6. Change log

- 2026-03-08 — Initial draft; service components, available fault current, neutral-to-ground bond rule.
