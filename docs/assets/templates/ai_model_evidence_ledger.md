<!-- ORIGINAL TEMPLATE — a per-component evidence record for a learned/AI model in a
control system or digital twin. Adapt to your project and review before use. It reproduces
no standards text. One ledger per model component; keep it from design time through retirement. -->

# AI / Model Evidence Ledger

**Purpose.** Make one learned component's evidence auditable in a single place, so its allowed
authority can be justified — and challenged — from the record rather than reconstructed after an
incident. Authority is perishable: a model's placement on the authority ladder is only as current as
the last entry below.

> This is an example, not a deliverable. It confers no authority: a learned component's allowed
> authority comes from your hazard analysis, the applicable safety lifecycle, and project review — not
> from having completed this form.

## 1. Identity and authority

| Field | Entry |
|---|---|
| Component / model name | |
| Model version | |
| Owner (name / role) | |
| Allowed authority level (0–5) | |
| Authority basis (why this level, what evidence) | |
| Date placed in service / last review | |
| Status (in service · degraded · retired) | |

## 2. Purpose and scope (Map)

| Field | Entry |
|---|---|
| Scientific domain / modelled phenomenon | |
| What decision the output influences | |
| Validated operating envelope (regime it is trusted in) | |
| Known-invalid regimes (where output must be distrusted) | |
| Coupling variables / interface ownership (if part of a twin) | |

## 3. Model definition

| Field | Entry |
|---|---|
| Governing equations / causal assumptions | |
| Boundary and initial conditions | |
| Material / chemical / biological parameters and their sources | |
| Empirical correlations and their valid ranges | |
| Learned components (architecture, purpose) | |
| Numerical solver, convergence criteria, deployment precision (e.g. FP32/FP64) | |
| Spatial / temporal resolution | |

## 4. Data lineage

| Field | Entry |
|---|---|
| Training / calibration datasets | |
| Dataset provenance (asset, sensor, unit, range, collection conditions) | |
| Dataset licence and redistribution constraints | |
| Feature definitions / feature-pipeline version | |
| Calibration state and date | |

## 5. Validation evidence (Measure)

| Field | Entry |
|---|---|
| Test-set split protocol (component-/asset-wise?) | |
| Headline metric(s) and value(s) | |
| Uncertainty / error band reported with the output | |
| Validation experiments and acceptance limits | |
| Validated at deployment conditions (hardware, precision)? | |

## 6. In-service monitoring and failure response (Manage)

| Field | Entry |
|---|---|
| Drift / out-of-distribution detection method | |
| Independent cross-checks (against measurements) | |
| Failure response when stale / low-confidence / OOD / unavailable (hazard-analysis-derived `on_fail`) | |
| Rollback: last known-good version and how to revert | |
| Human-review cadence (routine + on anomaly) | |

## 7. Change control (Govern)

| Date | Change (retrain · update · authority change) | Approved by | MoC reference | Notes |
|---|---|---|---|---|
| | | | | |

---

*Vocabulary aligns with the NIST AI Risk Management Framework (Govern / Map / Measure / Manage). NIST
AI RMF is voluntary process guidance — completing this ledger structures the evidence; it does not, by
itself, authorise a learned component to hold any safety function.*
