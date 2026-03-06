# Promotion Checklist: Work → RAG
**AI_READ_ACCESS: ALLOWED**

Use this checklist before promoting any content from `../work/` or `../restricted/` into `../rag/`.

## Pre-Promotion Checklist

### 1. Technical Accuracy
- [ ] Technical claims verified against authoritative sources
- [ ] Standards references checked (NEC, NFPA 79, UL 508A, ISO/IEC)
- [ ] Calculations and formulas reviewed
- [ ] No copyrighted standard text reproduced (paraphrase only)

### 2. Completeness
- [ ] Content is complete enough to be useful
- [ ] No placeholder "TBD" or "TODO" sections
- [ ] All examples are realistic and tested (where applicable)
- [ ] References and links are valid

### 3. Consistency
- [ ] Terminology matches /rag/_glossary.md
- [ ] Format matches existing RAG content in same category
- [ ] File naming follows conventions
- [ ] No conflicts with existing RAG content

### 4. Documentation
- [ ] Embedded changelog added to top of file
- [ ] AI_READ_ACCESS tag present
- [ ] Status marked as "Authoritative" or appropriate status
- [ ] Author and date captured in changelog

### 5. Review
- [ ] Peer review completed (if applicable)
- [ ] Subject matter expert sign-off (for complex technical content)
- [ ] Decision logged in `decision_log.md` if significant

## Promotion Process
1. Complete checklist above
2. Copy or adapt the file from `../work/` or `../restricted/` into the appropriate `../rag/` location
3. Add/update embedded changelog in promoted file
4. Update any indexes or navigation (e.g., _index.yaml)
5. Delete or archive the draft version
6. Document in `decision_log.md` if significant

## Rejection Handling
If content doesn't pass checklist:
1. Document gaps/issues in draft file header
2. Keep in `../work/` or `../restricted/` until issues are resolved
3. Add to draft file: "BLOCKED: [reason]"
