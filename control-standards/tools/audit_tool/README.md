# Audit Tool (Tool 5)
**AI_READ_ACCESS: ALLOWED**

## Purpose
Provides compliance scoring, risk ranking, and technical debt assessment for existing control systems.

## Contents
- **scoring_model.yaml**: Compliance scoring framework + weights
- **risk_ranking.yaml**: Risk categories, severity, likelihood rubric
- **technical_debt_model.yaml**: Technical debt categorization
- **report_templates/**: Audit report templates
- **outputs/**: Generated audit reports (MD → PDF)

## Audit Dimensions
- **Compliance**: NEC, NFPA 79, UL 508A, ISO/IEC adherence
- **Safety**: Risk assessment, safeguarding adequacy
- **Reliability**: MTBF, component quality, redundancy
- **Maintainability**: Documentation, accessibility, parts availability
- **Technical Debt**: Obsolescence, architectural issues, deferred maintenance
