<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# Worked architectures

This note is the corpus source for the site's Worked Architectures page. It carries four end-to-end
examples — a vision inspection cell, a predictive-maintenance pipeline, a PINN soft sensor, and a
read-only LLM copilot — each walked through the authority ladder: **which rung, what evidence, and what
stays independent when the model is wrong.** It invents no new technical claims; it composes the
verified positions already established in the [method register](README.md),
[safety boundary](safety_boundary.md), [interfaces & edge](interfaces_edge.md),
[model families](model_families.md), [digital twin](digital_twin.md), and
[validation & lifecycle](validation_lifecycle.md) notes. It is a decision aid, not permission to deploy.

## How to read each example

For every architecture, four questions are answered in the same order:

1. **The job** — the decision the model influences.
2. **The rung** — the highest authority the evidence supports (from the register), and why not higher.
3. **What stays independent** — the non-learned protection that holds when the model is wrong, stale,
   unavailable, or compromised.
4. **The seam and the contract** — where the model's result crosses into the control system, and what
   it must carry to be gated.

The recurring shape is the [envelope architecture](README.md): the learned component informs or
proposes; a verified non-learned layer decides and protects; no safety function routes through the
learned path.

## 1. Vision inspection cell

**The job.** A 2-D CNN inspects each part on a line — presence/absence, defect class, or a measurement —
so the cell can reject or pass it.

**The rung: advisory (level 2), with the PLC owning the action.** The CNN produces a classification; a
person or a deterministic rule sets the accept/reject policy, and **the PLC owns the reject-trigger
timing and actuation.** It is not higher because a perception model's field accuracy cannot be inferred
from its bench accuracy, and a misclassification must be caught downstream, not trusted as a plant fact.

**What stays independent.** The reject/divert mechanism, part-tracking, and any interlock are
deterministic and outside the model. A missed or false classification degrades yield or lets a bad part
through to a downstream check — it does not defeat a safety function, because none depends on the CNN.

**The seam and the contract.** The CNN runs at the cell (edge inference) and publishes a result — class,
confidence, model version, timestamp, quality — that the PLC reads and gates. Low confidence or a stale
result routes to the defined response (hold, divert to manual inspection), never a silent pass.

## 2. Predictive-maintenance pipeline

**The job.** A 1-D CNN or temporal model watches vibration (and possibly motor current) on a rotating
asset and flags likely bearing or gearbox wear for maintenance planning.

**The rung: advisory (level 2).** It flags; a person schedules. It is not higher because the
fault-diagnosis literature's near-100% accuracies are, as a class, an artefact of train/test leakage:
under a leakage-free component-wise split the honest number can fall to near chance, and **no source
measures learned diagnosis on a real industrial fleet.** A fleet operator whose training set contains
many of its own bearings may earn more — but that is a claim the operator's own validation must make.
Sensor choice matters: on the reference rig, vibration beat motor current in every case, so motor-current
diagnosis is a cost-driven degradation, not an equivalent.

**What stays independent.** Nothing trips, derates, or issues an automated work order on the model's
say-so above advisory; protection and process control are untouched. The failure mode is a missed or
false maintenance flag, absorbed by the planning process.

**The seam and the contract.** Acquire and infer at the edge (kHz vibration cannot be reconstructed by
oversampling a decoupled tag); publish the verdict — class, confidence, model version, freshness — into
the historian/CMMS, not the raw waveform. Drift monitoring against the validated envelope decides when
the flag is no longer trustworthy.

## 3. PINN soft sensor

**The job.** A physics-informed model estimates an unmeasured or hard-to-measure variable (a field, a
parameter) from sparse instruments — a soft sensor feeding operator awareness.

**The rung: read-only to advisory (level 1–2); level 0 for anything the loop closes on.** A PINN may
support estimation and calibration, but it must **not** be the authoritative estimator in a control
loop: a data-driven PINN can revert to a steady-state solution when the data flow stops (operationally,
between measurement updates), and because the PDE residual can be low while the solution is wrong, a
residual-based health monitor can be fooled — silent, plausible, wrong. Compare against an established
numerical solver before trusting it, and **validate at the deployment numerical precision** (an FP32
edge target can break a PINN that was healthy in FP64).

**What stays independent.** The real instruments, the deterministic estimators (EKF/UKF/observers), and
the control loops that would otherwise use them. The soft sensor is a second opinion cross-checked
against measurements, not a replacement for them; the loop never closes on it.

**The seam and the contract.** The estimate crosses as a result with an explicit uncertainty band and a
freshness bound; when it drifts out of the validated regime, or disagrees with an independent
measurement, it is flagged and the operator falls back to the measured/deterministic value.

## 4. Read-only LLM copilot

**The job.** An LLM answers engineering and maintenance questions over the plant's own documentation,
alarms, history, and model evidence — and can draft procedures or code for a human to verify.

**The rung: advisory (level 2) for the copilot; offline (level 0) for any code it drafts.** It consumes
**curated, read-only** context through allow-listed tools, never raw tag streams, and it holds **no
write access.** Drafted control code is a starting point that goes through grammar/compiler/formal
verification with a human owner before it is anything more — raw output is not a control artefact. The
NIST AI RMF Generative AI Profile is the relevant companion here, and confabulation (fluent, plausible,
wrong output) is the failure mode to design against.

**What stays independent.** Everything. The copilot cannot act; it can only inform. Its worst failure is
a wrong answer a reviewing engineer must catch — which is why every output is reviewed and every drafted
artefact is verified before use.

**The seam and the contract.** Read-only, least-privilege access inside the OT security zones (NIST SP
800-82r3 placement); each answer cites the twin state, document, or model evidence it rests on, so a
human can check it. No proposal reaches the plant without schema validation, authorization, and — where
required — human confirmation.

## What the four share

- **The ladder, not the model, sets the authority.** Three of the four top out at advisory; none holds a
  safety function; none closes a control loop on a learned estimate.
- **The non-learned envelope always holds the veto**, and the safety-function path never routes through
  the learned component.
- **The result crosses as a gated contract** — class/estimate, confidence/uncertainty, model version,
  timestamp, freshness — not as a raw stream, and a stale or low-confidence result triggers the defined
  response.
- **Authority is perishable** — each example depends on drift monitoring, honest (leakage-free,
  deployment-condition) validation, and a maintained model-evidence ledger to keep its rung.

## Sources

This note composes already-verified positions; the underlying sources live in the notes it draws on:

- [method register](README.md) — the authority ladder and per-method ceilings.
- [safety boundary](safety_boundary.md) — why no learned component holds a safety function.
- [interfaces & edge](interfaces_edge.md) — edge inference and the result contract.
- [model families](model_families.md) — CNN leakage, PINN limits + FP64, LLM draft-then-verify.
- [digital twin](digital_twin.md) — the integration spine and the device-communication seam.
- [validation & lifecycle](validation_lifecycle.md) — drift, failure response, rollback, the ledger,
  and the NIST AI RMF vocabulary.

## Changelog

- 2026-07-17 — Slice G corpus note drafted as the closing page of the seven-page AI-integration build.
  It introduces **no new technical claims** — it walks four worked architectures through the authority
  ladder using positions already verified in Slices B–F. Review pending.
