# IEC 62443 — IACS Security Lifecycle

**AI_READ_ACCESS: ALLOWED**

## Overview

The IEC 62443 series defines a security lifecycle for Industrial Automation and Control Systems (IACS). Like the functional safety lifecycle (IEC 61511, IEC 62061), the security lifecycle is not a one-time activity — it is a continuous process of assessment, implementation, and maintenance that runs in parallel with the operational life of the system.

---

## IACS Security Lifecycle Phases

```
ASSESS → IMPLEMENT → MAINTAIN
  ↑                       |
  └───────────────────────┘
        (periodic review)
```

### Phase 1: Assess

The Assess phase establishes the security baseline and determines what needs to be protected.

| Activity | Description | IEC 62443 reference |
|----------|-------------|-------------------|
| Asset inventory | Identify and document all IACS hardware, software, network connections, and access paths | IEC 62443-2-1 |
| Security risk assessment | Identify threats, assess vulnerabilities, determine consequences, rate risks | IEC 62443-3-2, 2-1 |
| Zone and Conduit definition | Group assets into Zones based on security policy; define authorized Conduits | IEC 62443-3-3 |
| SL-T assignment | Assign target Security Level to each Zone based on risk assessment | IEC 62443-3-3 |
| Security requirements specification | Specify system security requirements for the Zone/Conduit design | IEC 62443-3-3 |
| Gap analysis | Compare current security posture against SL-T requirements; identify gaps | IEC 62443-2-1 |

**Key output of Assess:** A documented set of Security Level Targets (SL-T) per Zone and a gap analysis identifying what must be implemented.

### Phase 2: Implement

The Implement phase closes the gaps identified in the Assess phase.

| Activity | Description | IEC 62443 reference |
|----------|-------------|-------------------|
| Network segmentation | Implement Zone/Conduit architecture; deploy firewalls, data diodes, or unidirectional gateways | IEC 62443-3-3, FR 5 |
| Access control hardening | Implement FR 1 and FR 2 requirements — authentication, authorization, account management | IEC 62443-3-3, FR 1/2 |
| Integrity controls | Implement FR 3 requirements — secure boot, change detection, software integrity | IEC 62443-3-3, FR 3 |
| Data protection | Implement FR 4 requirements — encryption for data in transit and at rest where required | IEC 62443-3-3, FR 4 |
| Audit and monitoring | Deploy security event logging and monitoring; connect to SIEM if applicable | IEC 62443-3-3, FR 6 |
| Availability controls | Implement FR 7 requirements — backups, recovery testing, DoS protection | IEC 62443-3-3, FR 7 |
| Security verification | Test and verify that SL-A ≥ SL-T for each Zone; document verification results | IEC 62443-3-3 |
| Documentation update | Update asset inventory, network diagrams, security procedures, and CSMS documentation | IEC 62443-2-1 |

**Key output of Implement:** Verified achievement of SL-A ≥ SL-T for all Zones; documented security baseline.

### Phase 3: Maintain

The Maintain phase sustains the security posture over the operational life of the system.

| Activity | Frequency | Description |
|----------|-----------|-------------|
| Vulnerability monitoring | Ongoing | Monitor ICS-CERT, vendor advisories, and CVE feeds for vulnerabilities in deployed components |
| Patch assessment | On notification | Assess each vulnerability for applicability, exploitability, and consequence in the IACS context |
| Patch deployment | Per patch management procedure | Test patches in non-production environment; deploy with change management authorization; update documentation |
| Compensating control review | When patching is deferred | Document the compensating control, its rationale, and a review date when the patch will be re-evaluated |
| Security audit | Annual minimum | Review CSMS compliance, access control lists, account management, and log integrity |
| Penetration test / security assessment | Periodic (typically 2–3 years) | Active assessment of security posture by qualified personnel |
| Incident response drill | Annual | Test incident detection, containment, and recovery procedures |
| Security review after changes | On change | Any modification to the IACS (new equipment, network change, software update) triggers a security review for affected Zones |
| SL-T review | When risk changes | Re-run risk assessment if threat landscape changes, system changes materially, or a security incident occurs |

---

## SL-T vs. SL-C vs. SL-A — Lifecycle Perspective

| Lifecycle event | Impact on SL designations |
|----------------|--------------------------|
| Risk assessment completed | SL-T is established for each Zone |
| System designed by System Integrator | SL-C is determined by component selection and system architecture |
| System implemented and verified | SL-A is measured; must equal or exceed SL-T |
| Component reaches end of support | SL-C of that component may decline (unpatched vulnerabilities); compensating controls or replacement required to maintain SL-A |
| New threat vector identified | SL-T may need to increase; re-assess SL-C and SL-A |
| Security incident occurs | Re-assess SL-T and SL-A for affected Zones; determine root cause; update controls |

---

## Patch Management in IACS

Patch management in IACS environments is significantly more constrained than in IT environments. Key differences:

| Aspect | IT environment | IACS environment |
|--------|---------------|-----------------|
| Patch urgency | Patch as quickly as possible | Test before deployment; assess impact on control system stability |
| Testing environment | Test in lab; deploy to production | IACS-representative test environment required; production systems may differ |
| Downtime tolerance | Short maintenance windows acceptable | Patching may require planned production downtime; some systems run 24/7 |
| Rollback capability | Usually automated | Manual rollback procedures required; tested before patch deployment |
| Vendor authorization | Typically not required | Some safety system vendors require patch authorization to maintain certification |
| Consequence of failed patch | Application instability | Loss of process control; potential safety hazard |

### IACS Patch Management Procedure

1. **Receive** — monitor vendor advisories and ICS-CERT; receive vulnerability notifications.
2. **Assess** — determine applicability: does the vulnerability affect a component in the IACS? What is the CVSS score? Is the attack vector accessible from the IACS network? What is the consequence if exploited?
3. **Prioritize** — assign priority based on exploitability, consequence, and Zone SL-T. High-consequence Zones with accessible attack vectors have higher priority.
4. **Test** — test the patch in a representative test environment; verify control system behavior, communication protocols, and application functionality.
5. **Schedule** — schedule deployment during an authorized maintenance window; communicate with operations and safety personnel.
6. **Check vendor authorization** — for safety systems, confirm with the safety PLC vendor whether the patch requires a new safety validation; document the outcome.
7. **Deploy** — deploy the patch per the change management procedure; retain backup of previous configuration.
8. **Verify** — verify system operation after patching; re-run critical tests; confirm SL-A is maintained.
9. **Document** — record the patch, deployment date, test results, and any residual risks.
10. **Deferred patches** — if a patch cannot be deployed, document a compensating control (network isolation, protocol filtering, enhanced monitoring) and assign a review date.

---

## Incident Response for IACS

An IACS cybersecurity incident response plan must address the unique requirements of operational technology (OT) environments.

### Incident Response Phases

| Phase | IACS-specific considerations |
|-------|------------------------------|
| **Detect** | OT-specific detection: anomaly detection on industrial protocols (Modbus, EtherNet/IP, PROFINET); integrity alerts from controllers; operator reports of abnormal behavior |
| **Report** | Reporting chain must include operations management and safety personnel, not only IT/security; safety system incidents must trigger safety assessment |
| **Contain** | Containment must not create new safety hazards; isolating a Zone may disable a safety function; pre-approved containment playbooks required |
| **Investigate** | OT forensics requires preserving controller memory and network captures; forensic activities must not disrupt ongoing production unless authorized |
| **Recover** | Recovery from verified backups; re-verify safety system integrity before restart; document recovered state |
| **Learn** | Post-incident review must include both security and safety teams; update risk assessment and CSMS |

### Intersection with Functional Safety

A cyberattack affecting a safety system is simultaneously a cybersecurity incident and a potential safety hazard. The incident response plan must specify:
- When to declare a safety alarm
- When to execute the process shutdown procedure
- How to re-validate the safety system before restart after a security incident
- Who has authority to authorize restart after a safety system security incident

---

## Coordination with the Functional Safety Lifecycle

IEC 62443 and IEC 61511 (or IEC 62061) share key lifecycle touchpoints:

| Lifecycle event | Functional safety action | Cybersecurity action |
|----------------|--------------------------|---------------------|
| Hazard and risk assessment | HAZOP / risk graph; SIL determination | Security risk assessment; SL-T determination for safety Zone |
| System design | Safety architecture; SIF design | Zone/Conduit design; SL-C verification |
| Commissioning | Safety system validation | Security verification (SL-A assessment) |
| Management of change | Safety impact assessment | Security impact assessment; Zone re-evaluation if applicable |
| Decommissioning | Safety system decommissioning | Secure data disposal; access revocation; network boundary update |

The 2016 edition of IEC 61511 explicitly requires that a security assessment be conducted as part of the functional safety lifecycle. The IEC 62443 series provides the framework for that assessment.