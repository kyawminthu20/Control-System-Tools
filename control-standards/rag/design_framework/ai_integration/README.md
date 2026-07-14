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

## Changelog

- 2026-07-13 — Initial Phase 49b register drafted from the Phase 49a evidence findings; review pending.
