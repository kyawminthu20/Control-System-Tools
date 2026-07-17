# AI Integration — 7-Page Authority-First Build Plan

**Recorded:** 2026-07-17
**Owner decision:** full 7-page build authorised (expanding the single
`/design/ai-integration/` register page into the structure the Phase 49
presentation plan already designed).
**Design source:** `planning/2026-07-12-ai-ml-control-systems-presentation-plan.md` (§3).
**Evidence source:** `control-standards/work/research/ai-ml-control-systems/`
(49a-findings, source-register, evidence-table — 98 claims, 72 publisher-verified).

## Non-negotiables carried into every slice

- **Authority-first.** The gate (index) is reachable before any capability page; every
  page restates that safety functions stay independent of the AI path.
- **Corpus-first.** A corpus prose note is written under
  `control-standards/rag/design_framework/ai_integration/` (headered
  `CONTENT_CLASS: RAG_APPROVED / AI_READ_ACCESS: ALLOWED / STATUS: DRAFT`) and the register's
  `_index.yaml` updated **before** the matching site page. Pages distil corpus; they do not
  invent technical content. Re-run `tools/generate_rag_tree.py` to mirror.
- **Verified claims only.** Every non-obvious claim traces to a `source-register.md` entry.
  New claims clear publisher verification first. `preprint`/`engineering judgement` strength is
  labelled as such; nothing borrows authority it lacks.
- **Chem/bio stays Planned.** No authority claims; structure + reality-check only (Phase 49c
  unauthorised). Level ceiling for learned methods stays 4 (architectural), assigned to none.
- **Status Review pending** on every page; original diagrams only; `review:` block per
  CONTENT_STANDARDS §4; no orphan pages (cross-link).

## Page → slice map (authority-first order)

| # | Page (URL) | Slice | Corpus note needed | Evidence status | Notes |
|---|---|---|---|---|---|
| 1 | index `/design/ai-integration/` — **the gate** | A | reuse register README | shipped/verified | Restructure to gate: plain terms, the pre-flight question, authority ladder, envelope, domain limits, links out. Register moves out. |
| 3 | `/method-register/` | A | methods.yml (exists) | GO | The 42-method register, moved verbatim from the index. No new claims. |
| 2 | `/safety-boundaries/` | B | **new**: `safety_boundary.md` | GO (strongest) | TR 5469 (report, not certifiable), EU MR 2023/1230 Annex I/III, AI Act Art 6(1), ISO 13849-1/62061/61511 independence, IEC 62443 zones (cite NIST SP 800-82r3, not 62443 clause numbers). The load-bearing page. |
| 5 | `/interfaces/` | C | **new**: `interfaces_edge.md` | GO (with the applied kHz rewrite) | Move + expand the high-rate rule and result contract; OPC UA Observer role, no AI companion spec, Sparkplug B; edge-inference on the four constraints (not "protocol too slow"). |
| 3b | `/model-families/` | D | **new**: `model_families.md` | GO | CNN (vision + 1-D signals; the leakage/split result), PINN (fails vs FEM; optimisation not expressivity; FP64 caveat), LLM (draft-then-verify; preprints stay preprints). Capability **and** poor-fit. |
| 4 | `/digital-twin/` | E | **new**: `digital_twin.md` | mixed | Integration spine; live data mirror ≠ behavioural twin; physical→digital and digital→physical as separate problems. Draws on research `digital-twin-integration.md` — re-verify before promoting. |
| 6 | `/validation-lifecycle/` | F | **new**: `validation_lifecycle.md` | GO for framing; some gaps | Data lineage, drift/OOD, uncertainty, rollback, MoC; NIST AI RMF vocabulary. Model-evidence ledger → downloadable template under `/tools/templates/`. NIST AI RMF GenAI Profile add lands here (deferred from 50.12). |
| 7 | `/worked-architectures/` | G | **new**: `worked_architectures.md` | mixed | Vision cell · predictive-maintenance pipeline · PINN soft sensor · read-only LLM copilot — each walked through the ladder. Depends on B–F. |

## Source gaps to close as the dependent page approaches (not blocking A–C)

- **IEC 62061** never checked for ML/self-evolving content — required before the safety page
  may claim "no machinery functional-safety standard addresses learned components" (slice B).
- **FP64/PINN preprint** — verify before the PINN claims in slice D.
- **Two 2024 arXiv preprints** (LLM4PLC, Xia et al.) — re-check publisher/peer-review status
  before slice D LLM claims; they stay `preprint` strength regardless.
- **TR 5469 body** paywalled — slice B must not imply knowledge of its internal clauses; it uses
  the report's *existence and scope*, which is verified.

## Slice sequence (each ends green + Review pending, merged, deploy-verified)

- **A — skeleton (this slice):** move the register to `/method-register/`; index becomes the gate;
  nav children added; cross-links. Presentation-only, no new claims.
- **B — safety boundaries** (corpus-first; highest value). Close the IEC 62061 gap first.
- **C — interfaces & handshakes** (corpus-first; content largely exists on the index).
- **D — model families & fit** (corpus-first; close FP64 + preprint gaps first).
- **E — digital twin** (corpus-first; re-verify the research note).
- **F — validation & lifecycle** (corpus-first; + NIST AI RMF GenAI Profile; + template).
- **G — worked architectures** (corpus-first; depends on B–F).

Deferred still: the scientific-domain track (space/microbiology) — out of scope until its
coupled-interface sources exist (presentation plan §3 "Deferred").
