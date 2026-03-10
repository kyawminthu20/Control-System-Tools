<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT

STANDARD_FAMILY: IEC_60079
STANDARD_ID: IEC_60079-17
EDITION: 2013

IEC_HIERARCHY:
  part: "17"
  part_title: "Explosive Atmospheres — Inspection and Maintenance of Electrical Installations"

INDEX_TAGS:
  topics: ["inspection", "maintenance", "periodic_inspection", "inspection_grade", "competency", "Ex_records"]
  systems: ["process_control", "oil_gas", "hazardous_area_maintenance"]
-->

# IEC 60079-17 — Explosive Atmospheres: Inspection and Maintenance

## 0. Why this matters for control engineers

Hazardous area equipment degrades over time — flame paths corrode, cable glands loosen, IS parameters drift, and equipment is modified without re-certification. IEC 60079-17 defines the inspection regime that keeps an Ex installation compliant between the initial commissioning inspection (IEC 60079-14) and decommissioning. Many insurance policies and regulatory frameworks require documented inspections per this standard.

## 1. Inspection grades

Three grades of inspection are defined, each with different scope:

| Grade | What is inspected | Typical frequency |
|-------|------------------|------------------|
| **Visual** | External condition — damage, corrosion, nameplate legible, glands tight, no obvious defects | More frequent (continuous or monthly) |
| **Close** | Visual checks + covers removed to verify flame path condition, IS parameters, internal connections | Less frequent (typically annually) |
| **Detailed** | Close checks + full verification against current certificate, entity recalculation, dimensional checks on flame paths | Infrequent (typically every 3–5 years or after incidents) |

The inspection schedule is risk-based: Zone 0/1 installations and equipment in severe environments warrant more frequent inspection.

## 2. Inspection procedure

For each item of Ex equipment:
1. Identify equipment type and protection method from nameplate
2. Refer to the appropriate inspection schedule for that protection method
3. Record findings against each inspection point
4. Classify defects as: no defect / defect not affecting safety / potential hazard / immediate hazard
5. Action defects appropriately (document, repair, or de-energize immediately)

## 3. Competency requirements

IEC 60079-17 requires that inspections be performed by a **competent person** — defined as having:
- Knowledge of the Ex protection concepts relevant to the equipment being inspected
- Knowledge of the applicable installation standards
- Practical experience with the protection methods present
- Understanding of the hazardous substances present

Documented training and qualification (e.g., CompEx, EEHA, or equivalent national scheme) satisfies the competency requirement in most jurisdictions.

## 4. Common inspection findings (defects)

| Defect | Classification | Action |
|--------|---------------|--------|
| Missing or loose cover fasteners (Ex d) | Potential hazard | Repair before next shift |
| Corroded flame path | Potential hazard / immediate hazard (if gap out of tolerance) | Remove from service if gap exceeds limit |
| Non-certified cable gland | Immediate hazard | Replace |
| Unsigned / missing inspection record | Documentation defect | Update records |
| Modified enclosure (extra holes) | Immediate hazard | Remove from service; re-certify or replace |
| IS earth resistance >1 Ω (zener barriers) | Potential hazard | Improve bonding |

## 5. Records

Inspection records must be retained and include:
- Date of inspection
- Inspector name and qualification
- Inspection grade applied
- Equipment identified (tag number, type, certificate number)
- Defects found and actions taken
- Next inspection due date

Records are required for regulatory audits, insurance inspections, and incident investigations. Loss of inspection records is treated as evidence that inspection did not occur.

## 6. Change log

- 2026-03-08 — Initial draft; inspection grades, procedure, competency, common defects, record requirements.
