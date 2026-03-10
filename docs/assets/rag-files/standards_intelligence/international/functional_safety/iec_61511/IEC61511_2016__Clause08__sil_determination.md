<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: COMPLETE

STANDARD_FAMILY: IEC
STANDARD_ID: IEC_61511
EDITION: 2016

HIERARCHY:
  clause: "8"
  clause_title: "Hazard and Risk Assessment"

INDEX_TAGS:
  topics: ["sil_determination", "lopa", "risk_graph", "hazop", "risk_assessment", "protection_layers", "pfdavg"]
  systems: ["process_industry", "oil_gas", "chemical", "sis"]
-->

# IEC 61511:2016 — Clause 8 — Hazard and Risk Assessment and SIL Determination

## 0. Why this matters

Clause 8 covers the hazard and risk assessment process that determines the SIL target for each Safety Instrumented Function. The SIL target is the outcome of this clause — it drives the entire downstream design process. An incorrect SIL determination (too low or too high) leads to either under-protection or unjustified cost and complexity.

The three primary SIL determination methods in process industry practice are LOPA, risk graph, and fault tree analysis. LOPA is the dominant method in practice because it provides a quantitative basis without the full complexity of fault tree analysis.

## 1. HAZOP — identifying hazardous events

Before SIL determination can begin, hazardous events must be identified. The standard method in the process industry is HAZOP (Hazard and Operability Study).

**HAZOP structure:**
- **Node:** A defined section of the process (pipe segment, vessel, loop)
- **Guide words:** More of, less of, none of, reverse, other than, early, late
- **Deviation:** Guide word applied to a process parameter (more + pressure, no + flow)
- **Cause:** What could cause the deviation
- **Consequence:** What happens if the deviation is not controlled
- **Safeguards:** Existing barriers that reduce the risk (BPCS, safety instrumentation, procedural controls, mechanical devices)

The HAZOP identifies the initiating causes, consequences, and existing safeguards for each hazardous scenario. These feed directly into the LOPA.

**HAZOP is not part of IEC 61511 — it is an input.** IEC 61511 Clause 8 requires a hazard and risk assessment; it does not mandate HAZOP as the method. However, HAZOP is the standard process industry method and is expected by most certification bodies and insurers.

## 2. LOPA — Layer of Protection Analysis

LOPA is the primary SIL determination method used in process safety. It is a semi-quantitative method that calculates the residual risk after accounting for all independent protection layers (IPLs).

### LOPA equation

For each hazardous scenario:

**Residual risk = Initiating event frequency × Probability of failure of each IPL × Conditional probability of consequence**

If residual risk > tolerable risk: the SIL gap must be filled by the SIF.

**Required PFDavg for the SIF = Tolerable risk ÷ (Initiating event frequency × all non-SIS IPL failure probabilities)**

### Initiating event frequencies

| Initiating cause | Typical frequency (per year) |
|-----------------|------------------------------|
| Control loop failure (BPCS) | 0.1 to 1.0 |
| Pump seal failure | 0.01 to 0.1 |
| Safety relief valve failure to open | 0.001 to 0.01 |
| Manual valve in wrong position | 0.01 to 0.1 |
| External impact (vehicle) | 10⁻³ to 10⁻⁴ (site-specific) |

These are generic values. Site-specific or industry databases (OREDA, CCPS LOPA guidance) provide more accurate frequencies for specific equipment and industries.

### Independent Protection Layers (IPLs)

An IPL is a device, system, or action that:
1. Is independent of the initiating cause and all other IPLs
2. Is capable of preventing the consequence if functioning
3. Is auditable (its performance can be confirmed)

| IPL type | Typical PFD credit |
|----------|-------------------|
| BPCS control loop (independent of initiating cause) | 0.1 (SIL 1 equivalent) |
| Human intervention (trained operator, > 10 min available) | 0.1 |
| Pressure relief valve (per API 521) | 0.01 |
| Rupture disc | 0.01 |
| Dike/bund containment | 0.01 |
| SIS (depends on design) | 0.1 to 0.001 (SIL 1 to SIL 3) |

**The SIS cannot be credited as an IPL for a consequence it is designed to prevent if it is also the initiating cause detector (common cause).** Each SIF is evaluated independently.

### Tolerable risk targets

Tolerable risk targets are not set by IEC 61511 — the standard requires a risk assessment but leaves the tolerable risk level to the organization, jurisdiction, or applicable sector guidance.

Common tolerable risk targets in the oil and gas industry:

| Consequence type | Typical tolerable frequency (per year) |
|-----------------|----------------------------------------|
| Minor injury or property damage | 10⁻³ to 10⁻² |
| Single fatality | 10⁻⁴ to 10⁻⁵ |
| Multiple fatalities | 10⁻⁵ to 10⁻⁶ |
| Catastrophic event (site-wide) | 10⁻⁶ to 10⁻⁷ |

### LOPA worked example

**Scenario:** High pressure in a reactor vessel can lead to vessel rupture.

| Item | Value |
|------|-------|
| Initiating cause | BPCS pressure control failure |
| Initiating event frequency | 0.5 / year |
| Conditional probability of rupture if deviation not stopped | 1.0 |
| IPL 1: BPCS high pressure alarm + operator action (> 10 min) | PFD = 0.1 |
| IPL 2: Pressure relief valve | PFD = 0.01 |
| Residual risk before SIF | 0.5 × 1.0 × 0.1 × 0.01 = 5 × 10⁻⁴ / year |
| Tolerable risk (single fatality) | 10⁻⁵ / year |
| Required PFDavg for SIF | 10⁻⁵ ÷ 5 × 10⁻⁴ = 0.02 |
| Required SIL | SIL 1 (PFDavg < 0.1) |

In this example, the SIF requires SIL 1 (PFDavg ≤ 0.1). If the relief valve IPL were not available, the residual risk would be 5 × 10⁻² / year, requiring SIL 3 from the SIF.

## 3. Risk graph method

The risk graph is a simpler, more qualitative alternative to LOPA. It is permitted by IEC 61511 and described in IEC 61511 Part 3.

**Risk graph parameters:**
- **C — Consequence severity:** C1 (minor injury), C2 (serious injury), C3 (one death), C4 (multiple deaths)
- **F — Frequency and duration of exposure:** F1 (rare/short), F2 (frequent/continuous)
- **P — Probability of avoiding the hazard:** P1 (possible), P2 (barely possible)
- **W — Demand rate without SIF:** W1 (very low), W2 (low), W3 (relatively high)

The parameters are combined using the risk graph to select the required SIL or "no special safety requirements."

**Risk graph limitations:**
- More conservative than LOPA — tends to assign higher SIL requirements
- Less transparent than LOPA — does not quantify individual protection layer credits
- Risk graph parameters require calibration to be meaningful; different organizations use different calibrations
- Preferred by smaller projects or early-stage assessment where LOPA data is not available

## 4. Fault tree analysis (FTA) for SIL determination

FTA is a fully quantitative method that can be used for SIL determination when the scenario is complex or when existing IPL credit in LOPA is insufficient. FTA is more resource-intensive but provides the most rigorous basis.

FTA is typically used when:
- Multiple initiating causes contribute to the same top event
- Complex combinations of IPL failures must be modeled
- Regulatory or certification requirements demand quantitative risk analysis

## 5. Common SIL determination mistakes

1. **Crediting the BPCS as an IPL in a LOPA where the BPCS is also the initiating cause** — the BPCS that failed to control the process cannot also be credited as the IPL that would have detected the failure; these are not independent

2. **Crediting the SIF twice** — in complex LOPA with multiple SIFs, engineers sometimes accidentally credit a SIF as both a primary SIF and as an IPL credit in an adjacent scenario; each SIF may only be credited once per consequence pathway

3. **Using inappropriate initiating event frequencies** — using generic frequencies from a reference without checking whether they apply to the specific equipment, maintenance regime, and process fluid can lead to significant errors in the SIL requirement

4. **Conflating PFHd and PFDavg** — SIL targets from LOPA are PFDavg requirements; using PFHd thresholds gives incorrect and non-conservative results for low-demand mode systems

5. **Treating LOPA as a design tool rather than a verification tool** — LOPA determines the required SIL; the SIS design then must demonstrate it achieves the required PFDavg; LOPA does not itself demonstrate that the SIS design is adequate

## 6. Change log

- 2026-03-07 — Phase 3 corpus creation; Clause 8 SIL determination document established.
