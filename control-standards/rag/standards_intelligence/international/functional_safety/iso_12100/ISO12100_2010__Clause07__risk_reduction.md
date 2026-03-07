<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: ISO
STANDARD_ID: ISO_12100
EDITION: 2010

HIERARCHY:
  clause: "7"
  clause_title: "Risk reduction — three-step method"

INDEX_TAGS:
  topics: ["risk_reduction", "three_step_method", "inherently_safe_design", "safeguarding", "information_for_use", "CE_marking", "machinery_safety"]
  systems: ["machinery"]
-->

# ISO 12100:2010 — Clause 7 — Risk Reduction — Three-Step Method

## 0. Why this clause matters

The three-step method is the legal and technical backbone of machine safety design under the EU Machinery Directive and its successor the EU Machinery Regulation 2023/1230. Compliance with the Directive's Essential Health and Safety Requirements implicitly requires following the three-step method — it is embedded in the General Principles of the Directive. For the designer, this means the three-step method is not optional guidance: it is the mandatory sequence for risk reduction, and deviations must be justified. The method also drives the design of safety functions: Step 2 safety devices are where ISO 13849-1 and IEC 62061 apply.

## 1. Step 1 — Inherently safe design

Inherently safe design (ISD) eliminates or reduces the hazard at its source without requiring a separate protective device or information. Because it removes the hazard rather than controlling it, ISD provides the highest assurance and cannot be made less effective by guard defeat, component failure, or operator behaviour.

Examples of ISD measures:

| Hazard type | ISD example |
|-------------|------------|
| Mechanical crushing/shearing | Geometry change — remove nip point by increasing clearance beyond 500 mm; use rounded instead of sharp edges |
| Electrical shock | Use SELV (Safety Extra-Low Voltage, ≤ 50 V AC / 120 V DC) to eliminate lethal voltage |
| Noise | Reduce noise at source by changing process (e.g., welding instead of riveting); use lower-noise drive technology |
| Stored energy | Design for minimum stored energy; use de-energise-to-stop principle |
| Hazardous substances | Substitute with less hazardous material or process |
| High speed | Reduce travel speed or mass to lower kinetic energy to a non-injurious level |

ISD is applied first because it yields the most robust reduction. Clause 7.2 is explicit: inherently safe design measures shall be preferred over safeguarding.

## 2. Step 2 — Safeguarding and protective measures

Where a hazard cannot be eliminated by ISD (or the required ISD measure is not reasonably practicable), Step 2 applies safeguarding — physical barriers and safety devices — to prevent persons from reaching the hazard zone or to halt the hazard when a person enters.

Major categories of safeguarding:

| Category | Examples | Notes |
|----------|---------|-------|
| Fixed guards | Bolted enclosures, fixed barriers | Preferred where access is not needed during normal operation |
| Movable interlocked guards | Door-and-interlock assemblies with guard-locking devices | Access allowed only when machine is in a safe state; ISO 14119 applies |
| Electro-sensitive protective equipment (ESPE) | Light curtains, area scanners, safety mats | Presence-sensing; IEC 61496 applies; PL/SIL determination required |
| Two-hand controls | Simultaneous two-hand actuation during hazardous motion | ISO 13851 applies |
| Enabling devices | Deadman grip for teaching/jogging | ISO 10218-1 for robots |
| Safe-direction / safe-speed control | PLC-based speed/direction monitoring | Safety-rated drive functions (STO, SS1, SLS); IEC 61800-5-2 applies |
| Pressure-sensitive devices | Safety edges, bumpers on AGVs | Contact detection |

Step 2 measures introduce a safety function — a function of the machine whose failure results in an immediate increase in risk. Safety functions must be designed to a PL or SIL commensurate with the PLr or SIL target from the ISO 12100 risk estimation.

## 3. Step 3 — Information for use

Step 3 addresses the residual risk that remains after Steps 1 and 2 have been applied. It does not reduce risk in the engineering sense — it informs users that residual risk exists and specifies what precautions they must take.

Step 3 measures include:

| Measure | Examples |
|---------|---------|
| Warning labels and signs | ISO 11684 hazard pictograms; "Do not reach past guard" labels |
| Operating instructions | Operator manual; maintenance procedures; PPE requirements |
| Training requirements | Specification of required qualifications and training for each operator role |
| Personal protective equipment (PPE) | Hearing protection, cut-resistant gloves, face shields |
| Access restriction | Permits-to-work; lockout/tagout procedures; key-controlled access |

Step 3 is the weakest form of protection because its effectiveness depends entirely on human compliance. It cannot substitute for Steps 1 or 2 where those steps are reasonably practicable.

## 4. Hierarchy enforcement

ISO 12100 Clause 7.1 is explicit about the hierarchy:

- Step 2 safeguarding measures may only be used where Step 1 ISD cannot eliminate or sufficiently reduce the hazard.
- Step 3 information may only address residual risk that remains after Steps 1 and 2 have been applied.
- A designer may not use a warning label to address a risk that could be eliminated by a design change or controlled by a guard.

This hierarchy has legal force. The EU Machinery Directive General Principles state that designers must "eliminate or reduce risks as far as possible, taking account of the state of the art." Using Step 3 where Step 1 or Step 2 is practicable is a non-conformity.

In practice, most machines require all three steps applied to different hazards or to the same hazard at different lifecycle stages.

## 5. Relationship to ISO 13849-1 and IEC 62061

Step 2 safety devices introduce safety functions. Each safety function must be designed and validated to achieve a PL or SIL that meets or exceeds the PLr or SIL target established by the ISO 12100 risk estimation.

The design pathway:

```
ISO 12100 Clause 5 (risk estimation: S, F, P)
    → ISO 13849-1 Annex A (risk graph → PLr)
    → ISO 13849-1 Clauses 4–9 (architecture, MTTF, DC, CCF → PL achieved)
    → Validate PL achieved ≥ PLr
```

Alternatively:

```
ISO 12100 Clause 5 (risk estimation: Se, Fr, Av)
    → IEC 62061 Annex A (risk parameters → SIL target)
    → IEC 62061 Clauses 5–9 (SILCL, PFH, architecture → SIL achieved)
    → Validate SIL achieved ≥ SIL target
```

ISO 13849-1 and IEC 62061 are not alternatives to ISO 12100 — they are downstream of it. Both assume that a valid ISO 12100 risk assessment has been completed before they are applied.
