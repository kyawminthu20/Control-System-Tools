<!--
CONTENT_CLASS: RAG_APPROVED
AI_READ_ACCESS: ALLOWED
STATUS: DRAFT
-->

# AI integration method register

This subtree is the canonical, review-pending source for the site's AI/ML method register. It is a
decision aid, not permission to deploy a learned component. Each row names the deterministic
alternative, an authority ceiling, required validation, failure modes, and the protection that must
remain independent.

The authority ladder is:

0. offline analysis only
1. read-only observation
2. advisory output
3. operator-approved action
4. bounded supervisory action inside independent constraints
5. direct closed-loop action

No learned component in this register is assigned level 5 or a safety function. Chemical and
biological rows remain `Planned`: current evidence supports structuring the engineering questions,
but not an authority claim.

`methods.yml` and `sources.yml` use JSON syntax, which is valid YAML. Run
`uv run python tools/generate_ai_method_register.py` to validate and publish exact copies under
`docs/_data/ai_methods/`.

## Selector-classification vocabulary (Phase 50.13)

Every row carries four validated classification fields (never inferred in page JavaScript). The
generator enforces controlled-vocabulary membership and the cross-field invariants below.

- **`method_class`** — `deterministic` · `learned` · `hybrid`.
- **`decision_type`** — `regulatory-control` · `state-estimation` · `monitoring-detection` ·
  `prediction-simulation` · `perception` · `engineering-support` · `data-transport`.
- **`data_availability`** (measured-plant-data burden) — `none-or-spec` · `commissioning-tests` ·
  `operating-history` · `labelled-examples` · `pretrained-plus-context`.
- **`safety_relevance`** — `safety-related` (must be deterministic and verifiable; holds the veto/limit)
  · `safety-adjacent` (informs a live decision but is not the safety function) · `non-safety`.

Generator-enforced invariants: (1) `safety-related` ⟹ `method_class == deterministic`; (2) `safety-related`
⟹ `max_authority != Planned`; (3) `pretrained-plus-context` ⟹ `method_class == learned` and not
`safety-related`. Exactly two rows are `safety-related` — `rule_engine` and `robust_mpc_safety_filter`,
both deterministic. Chemical/biological `safety_relevance` values are provisional (Planned authority, no
adversarial coverage yet). Full rationale: `planning/2026-07-17-phase50-13-classification-vocabulary.md`.

## Changelog

- 2026-07-13 — Initial Phase 49b register drafted from the Phase 49a evidence findings; review pending.
- 2026-07-17 — Phase 50.13a: added the four selector-classification fields to all 42 rows with
  generator-enforced vocabularies and invariants (safety-related ⟹ deterministic + real authority).
