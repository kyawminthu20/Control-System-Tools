<!-- TEMPLATE — Safety Requirements Specification skeleton for machinery
     safety functions (ISO 13849-1 / IEC 62061 practice). One SRS section per
     safety function. Adapt to the governing standard and edition for your
     project; a process-SIF SRS per IEC 61511 has additional required content. -->

# Safety Requirements Specification (SRS)

| Project |  | Document no. |  |
|---|---|---|---|
| Machine / system |  | Revision |  |
| Risk assessment ref. |  | Date |  |
| Prepared by |  | Verified by (independent) |  |

## 1. General

- Governing standard and edition (ISO 13849-1 / IEC 62061 / other):
- Source risk assessment (document, revision, date):
- Machine limits and intended use (reference or summary):

## 2. Safety Function Register

| SF# | Safety function (what, triggered by what, resulting state) | PLr / SILr | Hazard ref. |
|---|---|---|---|
| SF-01 |  |  |  |

## 3. Per-Function Specification (repeat per SF)

### SF-01 — [name]

- **Functional description:** [sensor → logic → actuator chain; what the
  function does, in one testable sentence]
- **Trigger condition(s):**
- **Safe state and how it is achieved** (stop category 0/1/2 where relevant):
- **Required integrity:** PLr ___ / SILcl ___ (from risk assessment)
- **Response time requirement:** [detection → safe state, with basis]
- **Operating modes covered** (auto / manual / setup / bypass rules):
- **Reset behavior** (manual/automatic; reset location; monitored reset?):
- **Fault behavior and diagnostics** (behavior on component fault, wire break,
  power loss):
- **Frequency of operation / demand rate:**
- **Environmental constraints** affecting the function:
- **Muting / suspension conditions** (if any, with justification):
- **Verification method** (analysis + test; reference test procedure):

## 4. Assumptions and Constraints

[Anything the integrity calculations depend on: mission time, proof-test
intervals, component data sources, CCF measures.]

## 5. Change History

| Rev | Date | Change | By |
|---|---|---|---|
