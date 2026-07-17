# Phase 49c — Chemical & Biological Evidence Closure and Adversarial Findings

**Generated:** 2026-07-17 · **Status:** Work tier — non-authoritative research capture. Not site or
corpus content, and **no register row is changed by this document.**
**Inputs:** three parallel source-closure workstreams (equilibrium/thermodynamics + transport;
bio/microbiology governing models; AI-in-process-safety regulatory frame) + this adversarial synthesis.
**Predecessors:** `evidence-table.md` (WS6), `authority-ceilings.md` (chem/bio marked *unattacked*),
`source-register.md`, `49a-findings.md`.

Phase 49c was authorised by the owner on 2026-07-17. **Authorisation covered the work, not the
ceiling:** the chemical/biological register rows stay `Planned` until the owner acts on the
recommendation in §6. This file closes the two gaps 49a left open — (1) the equilibrium/thermodynamics
family had *no* verified source, and (2) the chemical and biological families received *no* adversarial
coverage.

---

## 1. Headline

**Both gaps are closed, and the governing finding holds and now extends explicitly to the process,
chemical, and bioprocess sectors.** Nothing found supports a learned model holding more than
**estimator / soft-sensor + supervisory-optimisation** authority in these domains, with a deterministic
layer retaining the veto. The adversarial pass refuted every attempt to raise that ceiling and, for
safety-function participation, pushed it to zero — the same asymmetry seen in 49a.

Two results are worth stating plainly:

- **The equilibrium/thermodynamics family now has a publisher-verified anchor.** The **NIST Chemistry
  WebBook** was read at NIST's own site (VERIFIED_AT_PUBLISHER): equilibrium is fixed by Gibbs-energy
  minimisation / ΔrG° with activities as the exact variable — the hard leg. The empirical closures that
  *supply* the activity/fugacity coefficient (NRTL, Wilson, UNIQUAC, UNIFAC, EoS parameters) are fitted
  and regime-limited — the soft leg. This is the identical hard/soft shape 49a found for kinetics.
- **Transport Phenomena (Bird, Stewart & Lightfoot) is upgraded** from 49a's UNVERIFIABLE to
  VERIFIED_AT_PUBLISHER (confirmed via Wiley's own companion domain): conservation of momentum/energy/
  mass is the hard scaffold; turbulence and transfer-coefficient closures are empirical correlations
  with wide error bands.

---

## 2. What closed, and what did not

**Verification key** as in `evidence-table.md`, plus one honest new tag from the bio workstream:
`VERIFIED_VIA_DOI_REGISTRY` — the publisher's own HTML 403'd, but the bibliographic facts + DOI were
confirmed from the **Crossref publisher-deposited metadata** (upgrade from a blind SECONDARY_ONLY;
*not* the same as reading the publisher page).

| Item | 49a status | 49c status | Basis |
|---|---|---|---|
| Chemical equilibrium / thermodynamics family | **none — no verified source** | **VERIFIED_AT_PUBLISHER** | NIST Chemistry WebBook (SRD 69) read at NIST; IUPAC K°=exp(−ΔG°/RT) via Crossref |
| Activity-coefficient models are empirical closures | asserted | VERIFIED_VIA_DOI_REGISTRY | Kontogeorgis & Folas ch.5 (Wiley) via Crossref; DDBST/NRTL-FAC corroboration (secondary) |
| Transport phenomena | UNVERIFIABLE | **VERIFIED_AT_PUBLISHER** | Bird, Stewart & Lightfoot, Rev. 2nd ed., via Wiley companion domain |
| ML in thermodynamics = property-prediction closure only | — | VERIFIED_AT_PUBLISHER | UNIFAC 2.0 (arXiv + IECR/ACS via Crossref); Gibbs–Helmholtz GNN (ACS via NIH PMC) |
| IEC 61511 has no AI/ML provisions | not checked | **VERIFIED_AT_PUBLISHER** | IEC webstore (Ed. 2.0, 2016); process-sector analogue of the machinery finding |
| IEC 61508-3 rates AI "not recommended" ≥ SIL 2 | — | **SECONDARY_ONLY — DO NOT PUBLISH the table ratings** | IET + Kenexis + ADI (consultancy/institution, not the primary text) |
| CCPS/AIChE & ISA treat AI as advisory | — | SECONDARY_ONLY (ISA-61511 catalog VERIFIED) | AIChE/CEP/GCPS; ISA is the ANSI adopter of 61511, same deterministic text |
| FDA AI-in-drug-manufacturing discussion paper (2023) | — | SECONDARY_ONLY | Federal Register citation 2023-04206 + convergent legal summaries |
| FDA draft guidance on AI for regulatory decisions (Jan 2025) | — | SECONDARY_ONLY | fda.gov media/press + convergent summaries |
| EMA reflection paper on AI in the medicines lifecycle | — | **VERIFIED_AT_PUBLISHER** | EMA site; finalised 2024-09-09; human-oversight, risk-based |
| Yokogawa+JSR RL distillation, 840 h, protection untouched | vendor_claim | **VERIFIED_AT_PUBLISHER** | yokogawa.com press release; ESD/F&G/interlocks independent, non-AI |
| Monod 1949; Droop–Monod comparison; ADM1; von Stosch 2014; Raman/CHO | SECONDARY_ONLY | **VERIFIED_VIA_DOI_REGISTRY** | Crossref publisher-deposited metadata |
| Narayanan 2023; Brunner 2021; Rathore 2021; FDA PAT 2004 | SECONDARY_ONLY | **VERIFIED_AT_PUBLISHER** | Frontiers (open access); NIH PMC version of record; Federal Register doc 04-22203 |
| IWA ASM "STR No. 9" / biofilm "STR No. 18" series designations | SECONDARY_ONLY | **still SECONDARY_ONLY** | book/ebook confirmed (DTU repo, Crossref ebook DOI); print STR numbers only in third-party catalogs |

**Publisher walls hit this run (403/404 to the fetcher):** Wiley Online Library, ScienceDirect, ACS,
IUPAC Gold Book term pages, iwaponline.com, MDPI, and fda.gov guidance URLs. Every fact routed around a
wall is tagged accordingly above. No DOI or pagination was invented; two mis-guessed DOIs in the bio
workstream were caught against the registry and corrected.

---

## 3. The hard/soft boundary — now sourced for both families

The register's spine for chemical and biological methods is the same, and it is now evidenced end to
end rather than asserted:

- **HARD (can bound a learned output):** conservation of mass, energy, charge; stoichiometry; the laws
  of thermodynamics (equilibrium by Gibbs-energy minimisation); flux-balance feasibility (Sv=0 with flux
  bounds); the Petersen/Gujer stoichiometry matrix in the IWA models.
- **SOFT (fitted, regime-limited — cannot be a hard constraint or a safety function):** Arrhenius and
  other rate laws; Monod/Droop growth kinetics; Butler–Volmer interfacial kinetics; **activity and
  fugacity models and EoS parameters** (the equilibrium/thermo closure — the 49c addition); transport
  constitutive closures (turbulence models, transfer coefficients, interfacial area); PLS/chemometric
  calibrations.
- **Where a learned model earns its place:** confined to the *unclosed* term — a residual/closure inside
  a conservation scaffold (hybrid semi-parametric modelling), or a soft sensor mapping a spectrum to a
  concentration. In every verified deployment the learned component is an **estimator or a closure**
  feeding conventional deterministic control; the control law and the protective layer stay non-learned.

---

## 4. Adversarial pass on the chemical & biological ceilings

Method as in 49a: attack each proposed ceiling; **default to refuted when uncertain**; a refutation
almost always lowers the ceiling. The chem/bio proposals had received *no* attack before now.

| Ceiling attacked | Verdict | Adjudicated ceiling after attack |
|---|---|---|
| `CHEM-CONSERVATION-AS-CONSTRAINT` — "conservation laws can bound a learned output" | **UPHELD, narrowed** | True, but only conservation laws / thermodynamic feasibility / stoichiometry qualify as *hard* bounds. A fitted closure (activity model, EoS, kinetic law) may **not** be presented as a bounding constraint — it carries error bands and validity ranges. A learned output bounded only by a fitted closure is unbounded for safety purposes. |
| `CHEM-KINETIC-CLOSURE-AUTHORITY` — learned kinetic/equilibrium closure in a governing model | **REFUTED downward** | Level ≤ 2 (advisory / offline design & simulation). A learned closure may improve a model used for engineering analysis or a soft sensor, but its output may not set a setpoint, trip level, or design margin without independent non-learned re-derivation. **0 for any safety-function input.** |
| `CHEM-EQUILIBRIUM-ML-PROPERTY` — ML activity-coefficient / phase-equilibrium prediction | **REFUTED downward** | Level ≤ 1 for operations (property prediction feeding design/offline studies). The verified ML thermo work (UNIFAC 2.0, GH-GNN) predicts properties, warns about extrapolation and thermodynamic inconsistency, and claims **no** control authority. No online authority. |
| `BIO-SOFT-SENSOR-AUTHORITY` — learned soft sensor (e.g. Raman/PLS glucose) | **REFUTED downward** | Level 2 as an **absolute cap**, defaulted to 1 unless per-instrument/per-cell-line/per-scale recalibration and a validity/fault check are demonstrated — PLS calibrations are documented as non-transferable, and soft-sensor fault tolerance is the field's dominant unsolved problem. The learned part is a **sensor**; the control law stays conventional. Never a released-quality decision alone. |
| `BIO-CLOSED-LOOP-LEARNED-CONTROL` — a learned bioprocess *controller* | **REFUTED to 0/advisory** | No source shows a learned model holding closed-loop bioprocess control authority. Industrial practice is PI/PID + open-loop pre-computed feed profiles; MPC/ANN are research/pilot; regulated practice (FDA PAT, EMA) raises the justification bar and requires human oversight. Advisory only; the deterministic loop holds authority. |
| `PROCESS-RL-SUPERVISORY` — RL in supervisory/regulatory process control (Yokogawa+JSR) | **UPHELD as bounded, capped at 3–4-behind-a-veto** | A learned policy may hold *optimising/regulatory* authority **only** inside a hard envelope enforced by an independent non-learned layer that retains the safe-state command. The verified deployment did exactly this (interlocks/ESD/F&G untouched). It is a feasibility example, not a class-level capability, and carries zero risk-reduction credit. |
| `CHEMBIO-SAFETY-FUNCTION` — any learned chem/bio method in a safety function | **REFUTED to 0, unconditional** | Level 0. IEC 61511 gives no route; IEC 61508-3 disfavours AI ≥ SIL 2; no regulator approves it; no certified ML controller exists. Absence of a route is not permission. |

**Coverage note (honest):** this pass was performed by one adjudicator (me) applying the refute-by-default
rule against the verified evidence, not by an independent multi-agent panel as originally envisioned for
some 49a ceilings. It is single-lens. It is nonetheless the *first* adversarial coverage these families
have received, and every verdict is anchored to a publisher- or registry-verified source in §2.

---

## 5. Adjudicated chemical & biological authority ceilings

- **Deterministic governing models** (mass/energy/charge balance, equilibrium/thermodynamics, transport,
  stoichiometry, flux balance): these are the **hard-constraint layer**, not learned methods. They may
  bound a learned output and may hold control authority per ordinary deterministic rules and the project
  risk assessment — but a *fitted closure inside them* (kinetics, activity model, EoS, transfer
  coefficient) does not inherit that hardness and must be treated as soft.
- **Learned / hybrid chem/bio methods** (learned kinetic/equilibrium closure, hybrid residual/closure,
  Raman-PLS soft sensor, learned bioprocess elements): **≤ Level 2 (advisory / soft-sensor), defaulted to
  1** where transferability, fault tolerance, or validity checking is unproven; **Level 0** for any
  participation in a safety function or any released-quality decision made alone.
- **Supervisory RL / learned optimisation on the process** (the Yokogawa pattern): bounded operational
  authority only, inside an envelope held by an independent non-learned layer; zero risk-reduction credit;
  recorded as a documented feasibility case, not a class capability.

This is the same ceiling the rest of the register already applies to learned methods — the chem/bio
families are **not an exception**, and the earlier "structure-and-reality only, no authority claim"
posture can now be upgraded to an *evidenced, adversarially-tested* conservative ceiling.

---

## 6. Go / No-Go — and the register recommendation (owner decision)

**Go:** the chemical and biological families now have (a) publisher/registry-verified evidence and (b)
first adversarial coverage. The blocker that kept them at `Planned` — "no adversarial coverage" — is
cleared.

**Recommendation (for owner approval — not applied here):** the chem/bio register rows may move **off
`Planned`** to the conservative, evidenced ceilings in §5:

- Assign learned/hybrid chem/bio rows `max_authority: 2` (advisory/soft-sensor) — matching the
  `safety_relevance: safety-adjacent` values 50.13 already set — **except** `raman_pls_soft_sensor`,
  which should carry a "recalibrate-per-context / non-transferable" caveat and may warrant `1`.
- Keep deterministic chem/bio governing-model rows as the hard-constraint layer; do not grant any fitted
  closure hard-constraint or safety-function status.
- The `50.13` chem/bio `safety_relevance` values can drop their **provisional** tag once promoted, since
  adversarial coverage now exists — but every one stays `safety-adjacent` or `non-safety`; **none becomes
  `safety-related`** (the generator invariant would reject it anyway: no learned/hybrid method can be
  safety-related).

**Why this is an owner decision, not an autonomous edit:** moving a safety-relevance-bearing row off
`Planned` is a safety-significant register change, and the authorisation explicitly covered the *work*.
If approved, the change is a bounded slice (update `max_authority` + drop the provisional tags on the
chem/bio rows; regenerate; the generator invariants already guard the safety boundary).

**No-Go remains for:** any learned chem/bio method in a safety function (Level 0, unconditional), and any
promotion of a *fitted closure* to a hard constraint.

---

## 7. Residual gaps and do-not-publish list

- **DO NOT PUBLISH** the IEC 61508-3 Table A.2/C.2 "AI — not recommended" ratings as clause text — they
  are SECONDARY_ONLY (IET/consultancy), the same restriction as 49a. The defensible statement is: *IEC
  61511 provides no route to certify a learned component in a safety instrumented function, and the
  process-safety bodies treat AI as advisory.*
- **IWA STR series numbers** ("No. 9" ASM, "No. 18" biofilm) remain SECONDARY_ONLY — cite the books/DOIs,
  not the print STR numbers, without re-verification.
- **EoS parameters (Peng-Robinson/SRK) are fitted** rests on analogy to the verified activity-model
  evidence, not an independent publisher read — state it as engineering judgement.
- **FDA items** (2023 discussion paper, Jan-2025 draft guidance) are SECONDARY_ONLY on full text —
  existence/status are government-record solid; do not quote internal clause text.
- The Raman/CHO citation should be **pinned** before any use (Biotechnology Progress hosts several
  Raman/CHO feedback papers; the 2023 process-development study is the strongest match but was
  registry-verified, not read).
- Absence-of-evidence stands where stated: no certified ML controller and no permitting standard were
  found — this is not proof none exists privately.
