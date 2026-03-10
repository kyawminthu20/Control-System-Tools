<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: NEC
STANDARD_ID: NFPA_70
EDITION: 2023

NEC_HIERARCHY:
  article: "215"
  article_title: "Feeders"

INDEX_TAGS:
  topics: ["feeders", "conductor_sizing", "overcurrent_protection", "continuous_load", "demand_factor"]
  systems: ["power_distribution", "industrial_control_panel", "MCC"]
-->

# NEC 2023 — Article 215 — Feeders

## 0. Why this article matters

Feeders are the conductors between the service equipment (or separately derived system) and the branch circuit overcurrent devices. In an industrial facility, feeders typically run from the main switchgear or MCC to sub-panels, motor control centers, or individual large loads. Understanding feeder sizing rules is essential for specifying the conductors supplying a control panel or MCC.

## 1. Feeder conductor sizing (215.2)

Feeder conductors must have ampacity not less than the **load calculated per Article 220**, and in no case less than:

- **Non-continuous loads:** 100% of the non-continuous load
- **Continuous loads:** 125% of the continuous load (load on for 3 hours or more)
- **Combined loads:** 125% of continuous + 100% of non-continuous loads

**Practical rule:** For a feeder supplying industrial loads, most loads are continuous. Size the feeder conductors at 125% of the calculated load, then check that the ampacity (from NEC Table 310.12 or 310.15) supports that value at the conductor's temperature rating.

## 2. Feeder overcurrent protection (215.3)

The feeder overcurrent protective device (OCPD — breaker or fuse) must not exceed:

- The **ampacity of the feeder conductors** (from Art. 310)
- Where the load includes motors, apply the maximum OCPD rating per Art. 430, Part IV, to the largest motor, then add the FLA of all other motors plus the non-motor loads

**Note on continuous loads:** Where 100% rated OCPDs are used, the device may be rated at 100% of the continuous load. Standard OCPDs (not marked "100% rated") must be sized so that the continuous load does not exceed 80% of the OCPD rating.

## 3. Feeder for multiple branch circuits (215.2(A))

A feeder supplying multiple branch circuits must have ampacity sufficient for:
- All branch circuit loads simultaneously
- Or the calculated demand load using applicable demand factors from Art. 220

**Demand factors:** Article 220 permits demand factors for certain load types (e.g., lighting in dwelling units, electric dryers). For industrial motor loads, demand factors are not typically applied unless a documented load study justifies a reduced design load.

## 4. Feeder identification (215.12)

Feeders must be identified at each point where they enter an enclosure. The identification must include the origin (e.g., "Panel A, Circuit 12") to allow safe disconnection during maintenance.

## 5. Relationship to Art. 230 and Art. 409

```
Service (Art. 230)
    ↓ Service conductors
Service Disconnecting Means
    ↓ Feeder (Art. 215)
Panelboard / MCC / Sub-panel
    ↓ Branch circuits (Art. 210)
Industrial Control Panel (Art. 409)
```

The feeder is the link between the service equipment and the panel or MCC that contains the branch circuit OCPDs. For machine installations, Article 670 governs from the feeder connection point to the machine.

## 6. Change log

- 2026-03-08 — Initial draft; feeder sizing, continuous load rule, relationship to service and branch circuits.
