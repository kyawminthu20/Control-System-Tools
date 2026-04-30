# IEC 62443-2-1 — IACS Security Management System

**AI_READ_ACCESS: ALLOWED**

## Standard Reference

| Field | Value |
|-------|-------|
| **Standard** | IEC 62443-2-1 |
| **Edition** | 2010 (under revision as of 2024) |
| **Full title** | Industrial communication networks — Network and system security — Part 2-1: Establishing an industrial automation and control system security program |
| **Audience** | Asset Owner (AO) — the organization that operates the IACS |
| **Scope** | Requirements for establishing, implementing, and maintaining an IACS cybersecurity management system (CSMS) |

---

## Purpose

IEC 62443-2-1 defines what an Asset Owner must do to manage cybersecurity across the lifecycle of an Industrial Automation and Control System. It is modeled on ISO/IEC 27001 (IT information security management) but adapted for the operational constraints and safety criticality of IACS environments.

The CSMS is not a one-time design activity — it is an ongoing program of risk management, policy enforcement, and continuous improvement.

---

## Key Concepts

### Asset Owner vs. System Integrator vs. Product Supplier

IEC 62443 assigns different obligations to three roles:

| Role | IEC 62443 Part | Primary obligation |
|------|---------------|-------------------|
| **Asset Owner (AO)** | 2-1 | Manage cybersecurity across the IACS lifecycle |
| **System Integrator (SI)** | 2-4, 3-2, 3-3 | Design and integrate systems to defined Security Levels |
| **Product Supplier / Developer** | 4-1, 4-2 | Develop and supply secure products |

An organization may occupy more than one role (e.g., an in-house engineering team acting as both AO and SI).

---

## Security Risk Assessment

The core activity required by IEC 62443-2-1 is a formal security risk assessment. This is distinct from, but must be coordinated with, the functional safety risk assessment required by IEC 61511 or ISO 13849-1.

### Risk Assessment Process

1. **Define the scope** — identify the IACS boundary, all assets within it, and external connections.
2. **Inventory assets** — document all hardware, software, network connections, and human roles.
3. **Identify threats** — enumerate credible threat actors (insider, remote attacker, supply chain) and threat events (unauthorized access, data manipulation, denial of service, physical tampering).
4. **Identify vulnerabilities** — assess each asset for known vulnerabilities and security weaknesses.
5. **Assess consequences** — for each threat-vulnerability pair, determine the consequence to safety, operations, environment, and business.
6. **Determine risk** — combine likelihood and consequence to produce a risk rating.
7. **Determine required Security Level targets (SL-T)** — from the risk assessment, assign the required SL-T for each Zone (see IEC 62443-3-3).
8. **Define countermeasures** — select controls to reduce risk to acceptable levels.
9. **Document and review** — record all findings; schedule periodic review.

### Risk Assessment Coordination with Functional Safety

A critical principle: cybersecurity risk and safety risk interact. A successful cyberattack that disables a safety instrumented function creates a safety hazard. The risk assessment under IEC 62443-2-1 must consider safety consequences, and the results must be shared with the functional safety lifecycle team.

Where safety-critical control systems are involved (safety PLCs, safety instrumented systems), the Zone/Conduit model should align with the safety boundary defined in the safety lifecycle.

---

## Asset Inventory Requirements

An IACS asset inventory is a foundational control under IEC 62443-2-1. It must include:

| Asset category | Information required |
|----------------|---------------------|
| Controllers (PLCs, DCS, safety controllers) | Make, model, firmware version, network addresses, safety classification |
| Workstations and servers (HMI, historian, engineering workstation) | OS version, patch level, software inventory, user accounts |
| Network infrastructure (switches, routers, firewalls) | Make, model, firmware version, configuration baseline |
| Field devices (smart sensors, actuators, IED) | Protocol, firmware where applicable, physical access control |
| Remote access paths | Technology, authentication method, authorization scope, logging capability |
| External connections | Counterparty, purpose, data flow direction, security controls at boundary |

The inventory must be maintained as equipment changes occur — it is a living document, not a one-time deliverable.

---

## Security Policy and Program Elements

IEC 62443-2-1 requires the Asset Owner to establish and document the following policy elements:

1. **Security policy** — a documented statement of cybersecurity objectives, scope, and management commitment, signed by accountable management.
2. **Roles and responsibilities** — explicit assignment of cybersecurity accountability for the IACS; must include operational personnel, not only IT.
3. **Security procedures** — documented procedures for each security-relevant activity: access control, change management, patch management, incident response, backup and recovery, and remote access authorization.
4. **Awareness and training** — all personnel with physical or logical access to the IACS must receive security awareness training appropriate to their role.
5. **Supplier and contractor management** — procedures for managing third-party access; contractors must comply with the site security policy before connecting to the IACS.
6. **Configuration management** — baseline configurations for all assets must be documented; changes require authorization and documentation.
7. **Vulnerability and patch management** — a process for receiving vulnerability notifications, assessing applicability, testing patches, and deploying or documenting compensating controls.
8. **Incident response** — a documented plan for detecting, reporting, containing, and recovering from cybersecurity incidents; must include roles, contact lists, and escalation procedures.
9. **Business continuity and recovery** — backup and recovery procedures for IACS data, programs, and configurations; recovery time objectives must be aligned with operational requirements.
10. **Audit and review** — periodic review of the CSMS against the documented policy; findings must be tracked to closure.

---

## Relationship to ISO/IEC 27001

IEC 62443-2-1 is compatible with ISO/IEC 27001 but diverges in important areas:

| Aspect | ISO/IEC 27001 (IT) | IEC 62443-2-1 (IACS) |
|--------|-------------------|----------------------|
| Primary concern | Confidentiality, then Integrity, then Availability | Availability first; Integrity second; Confidentiality third |
| Patching urgency | Patch promptly | Patch after testing; compensating controls accepted when patching is operationally disruptive |
| Change management | IT change management cadence | Change management aligned with production windows; emergency change controls |
| Consequences of failure | Data breach, business disruption | Safety hazard, environmental release, equipment damage, production loss |
| Availability requirements | Best effort or SLA-based | Near-continuous availability; patching and updates require planned downtime |

> *Terminology: "Confidentiality" here is the IEC 62443 security property (the C in C-I-A) — protection from unauthorized disclosure, not a content-classification label.*

---

## Practical Notes

- IEC 62443-2-1 is written for Asset Owners. A system integrator designing a system for an AO should provide documentation that supports the AO's CSMS requirements — particularly asset inventory data, secure configuration guidance, patch guidance, and system security specification.
- The 2-1 edition published in 2010 is under revision; updated guidance aligns with IEC 62443-1-1 (terminology), IEC 62443-2-4 (SI requirements), and IEC 62443-3-2 (security risk assessment for system design).
- Safety systems under IEC 61511 or ISO 13849-1 require a documented security assessment as a condition of functional safety compliance — IEC 62443-2-1 provides the framework for that assessment.