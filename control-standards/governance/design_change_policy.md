# Design Change Policy
**AI_READ_ACCESS: ALLOWED**

Defines when and how to update design frameworks, patterns, and authoritative guidance.

## Change Categories

### 1. Correction (Immediate)
**When**: Technical error, standards misinterpretation, safety issue
**Process**:
- Fix immediately in RAG
- Update changelog with "CORRECTION" tag
- Log in decision_log.md if significant
- No version bump needed for minor corrections

### 2. Enhancement (Scheduled)
**When**: Adding new patterns, expanding coverage, improving clarity
**Process**:
- Draft in `../work/` first
- Follow promotion checklist
- Update changelog with "ENHANCEMENT" tag
- Consider minor version bump

### 3. Breaking Change (Controlled)
**When**: Fundamental approach change, deprecating old patterns
**Process**:
- Document rationale in `../work/` first
- Archive superseded version to `../archive/`
- Update all dependent content
- Major version bump
- Update decision_log.md
- Notify stakeholders

## Changelog Format (Embedded in Files)

```markdown
## Changelog
- YYYY-MM-DD: [CORRECTION|ENHANCEMENT|BREAKING] Brief description
- YYYY-MM-DD: [type] Brief description
```

## Versioning (for major modules)
- **Major.Minor.Patch** (e.g., 2.1.3)
- **Major**: Breaking changes, architectural shifts
- **Minor**: New features, enhancements
- **Patch**: Corrections, clarifications

## Approval Authority
- **Corrections**: Any authorized contributor
- **Enhancements**: Technical lead approval
- **Breaking Changes**: Stakeholder consensus required
