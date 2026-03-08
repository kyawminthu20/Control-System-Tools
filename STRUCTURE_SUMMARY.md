# Workspace Structure Summary

Use this file as a tree reference for the whole workspace. The primary narrative lives in [README.md](/Users/kyawminthu/Dev/Control System Tools/README.md) and [PROJECT_STARTUP_CONTEXT.md](/Users/kyawminthu/Dev/Control System Tools/PROJECT_STARTUP_CONTEXT.md).

<!-- AUTO-GENERATED TREE START -->
## Directory Tree
**Last Auto-Updated:** 2026-03-08 05:57:01

```text
├── .claude/
│   ├── agents/
│   │   ├── rag-reviewer.md
│   │   └── standards-lookup.md
│   ├── settings.json
│   ├── settings.local.json
│   └── skills/
│       ├── explain-code/
│       │   └── SKILL.md
│       ├── new-rag-module/
│       │   └── SKILL.md
│       ├── promote-draft/
│       │   └── SKILL.md
│       └── validate-rag/
│           └── SKILL.md
├── .gemini/
├── .github/
│   └── workflows/
│       └── pages.yml
├── .gitignore
├── .mcp.json
├── .playwright-mcp/
│   └── console-2026-03-06T07-01-55-004Z.log
├── .python-version
├── .venv/
│   ├── .gitignore
│   ├── .lock
│   ├── CACHEDIR.TAG
│   ├── bin/
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── activate.nu
│   │   ├── activate.ps1
│   │   ├── activate_this.py
│   │   ├── deactivate.bat
│   │   ├── pydoc.bat
│   │   ├── python -> /Users/kyawminthu/.local/share/uv/python/cpython-3.13.5-macos-aarch64-none/bin/python3.13
│   │   ├── python3 -> python
│   │   └── python3.13 -> python
│   ├── lib/
│   │   └── python3.13/
│   │       └── site-packages/
│   │           ├── _virtualenv.pth
│   │           └── _virtualenv.py
│   └── pyvenv.cfg
├── .worktrees/
├── AGENTS.md
├── CLAUDE.md
├── PROJECT_STARTUP_CONTEXT.md
├── README.md
├── STRUCTURE_SUMMARY.md
├── archive/
│   ├── MIGRATION_GUIDE.md
│   ├── MIGRATION_READY.md
│   ├── MIGRATION_SCRIPT.sh
│   └── PRE_MIGRATION_CHECK.sh
├── control-standards/
│   ├── .gitignore
│   ├── QUICK_START.md
│   ├── README.md
│   ├── STRUCTURE_SUMMARY.md
│   ├── archive/
│   │   ├── README.md
│   │   ├── _archive_old_rag_20260115_221742/
│   │   │   ├── _glossary.md
│   │   │   ├── _index.yaml
│   │   │   ├── _standards_map.md
│   │   │   ├── audit_tool/
│   │   │   │   ├── README.md
│   │   │   │   ├── outputs/
│   │   │   │   └── report_templates/
│   │   │   ├── business_metrics_profit_engine/
│   │   │   │   ├── README.md
│   │   │   │   └── exports/
│   │   │   ├── commissioning_checklists/
│   │   │   │   ├── README.md
│   │   │   │   ├── checklists/
│   │   │   │   └── outputs/
│   │   │   ├── design_framework/
│   │   │   │   ├── README.md
│   │   │   │   ├── constraints/
│   │   │   │   ├── design_guides/
│   │   │   │   │   └── 01_panel_design_guide.md
│   │   │   │   ├── outputs/
│   │   │   │   └── patterns/
│   │   │   │       └── io_templates.yaml
│   │   │   ├── design_package_generator/
│   │   │   │   ├── README.md
│   │   │   │   └── kits/
│   │   │   │       ├── conveyor_control_kit/
│   │   │   │       ├── pump_skid_control_kit/
│   │   │   │       └── robotic_cell_control_kit/
│   │   │   ├── ip_library_licensing/
│   │   │   │   ├── README.md
│   │   │   │   └── export_packages/
│   │   │   ├── knowledge_platform/
│   │   │   │   └── README.md
│   │   │   ├── retainer_support_engine/
│   │   │   │   ├── README.md
│   │   │   │   └── outputs/
│   │   │   ├── standards_intelligence/
│   │   │   │   ├── ISO_IEC/
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── iec_60204_1/
│   │   │   │   ├── NEC/
│   │   │   │   ├── NFPA/
│   │   │   │   ├── UL/
│   │   │   │   ├── clause_index/
│   │   │   │   │   ├── iso_iec_clause_index.yaml
│   │   │   │   │   ├── nec_clause_index.yaml
│   │   │   │   │   ├── nfpa79_clause_index.yaml
│   │   │   │   │   └── ul508a_clause_index.yaml
│   │   │   │   ├── outputs/
│   │   │   │   │   └── standards_guidance_report.md
│   │   │   │   └── rules_engine/
│   │   │   │       ├── red_flags.yaml
│   │   │   │       └── rules.yaml
│   │   │   ├── training_cert_builder/
│   │   │   │   ├── README.md
│   │   │   │   ├── assessments/
│   │   │   │   └── modules/
│   │   │   ├── troubleshooting_decision_engine/
│   │   │   │   ├── README.md
│   │   │   │   ├── decision_trees/
│   │   │   │   ├── outputs/
│   │   │   │   └── playbooks/
│   │   │   └── ul508a_panel_automation/
│   │   │       ├── README.md
│   │   │       ├── outputs/
│   │   │       └── ul_documentation_templates/
│   │   ├── _backup_before_migration_20260115_221742/
│   │   │   ├── new_rag/
│   │   │   │   ├── RAG_DIRECTORY_STATUS.md
│   │   │   │   ├── commissioning_checklists/
│   │   │   │   │   ├── dry_run/
│   │   │   │   │   ├── handover/
│   │   │   │   │   ├── live_run/
│   │   │   │   │   └── pre_power/
│   │   │   │   ├── design_framework/
│   │   │   │   │   ├── control_system_design/
│   │   │   │   │   ├── io_architecture/
│   │   │   │   │   ├── network_architecture/
│   │   │   │   │   ├── power_distribution/
│   │   │   │   │   ├── safety_architecture/
│   │   │   │   │   └── us_eu_compliance_wizard/
│   │   │   │   ├── standards_intelligence/
│   │   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │   │   │   ├── _glossary.md
│   │   │   │   │   ├── _index.yaml
│   │   │   │   │   ├── _overlap_matrix/
│   │   │   │   │   │   ├── _index.yaml
│   │   │   │   │   │   ├── file_structure.md
│   │   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │   │   │   │   ├── standards_decision_workflow.md
│   │   │   │   │   │   ├── standards_overlap.md
│   │   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │   │   │   ├── _overlap_notes/
│   │   │   │   │   │   ├── GENERATION_STATUS.md
│   │   │   │   │   │   ├── _index.yaml
│   │   │   │   │   │   ├── file_structure.md
│   │   │   │   │   │   └── overlap__sccr.md
│   │   │   │   │   ├── _standards_map.md
│   │   │   │   │   ├── iec_60204_1/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause01__scope.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause02__normative_references.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │   │   │   │   │   ├── IEC60204_1_2018__Clause15__verification.md
│   │   │   │   │   │   ├── IEC60204_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_61508/
│   │   │   │   │   ├── iec_61511/
│   │   │   │   │   ├── iec_62061/
│   │   │   │   │   ├── iso_12100/
│   │   │   │   │   ├── iso_13849_1/
│   │   │   │   │   │   └── file_structure.md
│   │   │   │   │   ├── nec/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │   │   │   │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │   │   │   │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │   │   │   │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │   │   │   │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │   │   │   │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │   │   │   │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │   │   │   │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │   │   │   │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │   │   │   │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │   │   │   │   ├── NEC_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── nfpa79/
│   │   │   │   │   │   ├── GENERATION_SUMMARY.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch01__administration.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │   │   │   │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │   │   │   │   ├── NFPA_OVERVIEW.md
│   │   │   │   │   │   ├── README.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── standards_applicability.md
│   │   │   │   │   └── ul_508a/
│   │   │   │   │       ├── GENERATION_SUMMARY.md
│   │   │   │   │       ├── README.md
│   │   │   │   │       ├── UL508A_2022__control_circuits_and_devices.md
│   │   │   │   │       ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │   │   │       ├── UL508A_2022__general_construction_requirements.md
│   │   │   │   │       ├── UL508A_2022__grounding_and_bonding.md
│   │   │   │   │       ├── UL508A_2022__marking_and_documentation.md
│   │   │   │   │       ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │   │   │       ├── UL508A_2022__overcurrent_protection.md
│   │   │   │   │       ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │   │   │       ├── UL508A_2022__scope_and_application.md
│   │   │   │   │       ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │   │   │       ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │   │   │       ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │   │   │       ├── UL508A_OVERVIEW.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── training_modules/
│   │   │   │   │   ├── commissioning/
│   │   │   │   │   ├── fundamentals/
│   │   │   │   │   ├── safety/
│   │   │   │   │   └── troubleshooting/
│   │   │   │   └── troubleshooting_engine/
│   │   │   │       ├── analog_io/
│   │   │   │       ├── decision_trees.yaml
│   │   │   │       ├── digital_io/
│   │   │   │       ├── motion_servo/
│   │   │   │       ├── networks/
│   │   │   │       └── pid_control/
│   │   │   └── old_rag/
│   │   │       ├── _glossary.md
│   │   │       ├── _index.yaml
│   │   │       ├── _standards_map.md
│   │   │       ├── audit_tool/
│   │   │       │   ├── README.md
│   │   │       │   ├── outputs/
│   │   │       │   └── report_templates/
│   │   │       ├── business_metrics_profit_engine/
│   │   │       │   ├── README.md
│   │   │       │   └── exports/
│   │   │       ├── commissioning_checklists/
│   │   │       │   ├── README.md
│   │   │       │   ├── checklists/
│   │   │       │   └── outputs/
│   │   │       ├── design_framework/
│   │   │       │   ├── README.md
│   │   │       │   ├── constraints/
│   │   │       │   ├── design_guides/
│   │   │       │   │   └── 01_panel_design_guide.md
│   │   │       │   ├── outputs/
│   │   │       │   └── patterns/
│   │   │       │       └── io_templates.yaml
│   │   │       ├── design_package_generator/
│   │   │       │   ├── README.md
│   │   │       │   └── kits/
│   │   │       │       ├── conveyor_control_kit/
│   │   │       │       ├── pump_skid_control_kit/
│   │   │       │       └── robotic_cell_control_kit/
│   │   │       ├── ip_library_licensing/
│   │   │       │   ├── README.md
│   │   │       │   └── export_packages/
│   │   │       ├── knowledge_platform/
│   │   │       │   └── README.md
│   │   │       ├── retainer_support_engine/
│   │   │       │   ├── README.md
│   │   │       │   └── outputs/
│   │   │       ├── standards_intelligence/
│   │   │       │   ├── ISO_IEC/
│   │   │       │   │   ├── README.md
│   │   │       │   │   └── iec_60204_1/
│   │   │       │   ├── NEC/
│   │   │       │   ├── NFPA/
│   │   │       │   ├── UL/
│   │   │       │   ├── clause_index/
│   │   │       │   │   ├── iso_iec_clause_index.yaml
│   │   │       │   │   ├── nec_clause_index.yaml
│   │   │       │   │   ├── nfpa79_clause_index.yaml
│   │   │       │   │   └── ul508a_clause_index.yaml
│   │   │       │   ├── outputs/
│   │   │       │   │   └── standards_guidance_report.md
│   │   │       │   └── rules_engine/
│   │   │       │       ├── red_flags.yaml
│   │   │       │       └── rules.yaml
│   │   │       ├── training_cert_builder/
│   │   │       │   ├── README.md
│   │   │       │   ├── assessments/
│   │   │       │   └── modules/
│   │   │       ├── troubleshooting_decision_engine/
│   │   │       │   ├── README.md
│   │   │       │   ├── decision_trees/
│   │   │       │   ├── outputs/
│   │   │       │   └── playbooks/
│   │   │       └── ul508a_panel_automation/
│   │   │           ├── README.md
│   │   │           ├── outputs/
│   │   │           └── ul_documentation_templates/
│   │   ├── old_decision_trees/
│   │   ├── past_audits/
│   │   └── superseded_designs/
│   ├── exports/
│   │   ├── README.md
│   │   ├── docx/
│   │   ├── legacy_root/
│   │   │   ├── README.md
│   │   │   ├── csv/
│   │   │   ├── pdf/
│   │   │   └── snapshots/
│   │   ├── pdf/
│   │   └── reports/
│   ├── governance/
│   │   ├── README.md
│   │   ├── decision_log.md
│   │   ├── design_change_policy.md
│   │   ├── promotion_checklist_drafts_to_rag.md
│   │   └── release_notes.md
│   ├── rag/
│   │   ├── MIGRATION_SUMMARY_20260115_221742.md
│   │   ├── RAG_DIRECTORY_STATUS.md
│   │   ├── VERSION_OVERVIEW.md
│   │   ├── commissioning_checklists/
│   │   │   ├── dry_run/
│   │   │   ├── handover/
│   │   │   ├── live_run/
│   │   │   └── pre_power/
│   │   ├── design_framework/
│   │   │   ├── control_system_design/
│   │   │   ├── io_architecture/
│   │   │   ├── network_architecture/
│   │   │   ├── power_distribution/
│   │   │   ├── safety_architecture/
│   │   │   └── us_eu_compliance_wizard/
│   │   ├── standards_intelligence/
│   │   │   ├── README.md
│   │   │   ├── _glossary.md
│   │   │   ├── _index.yaml
│   │   │   ├── _standards_map.md
│   │   │   ├── crosswalks/
│   │   │   │   ├── overlap_matrix/
│   │   │   │   │   ├── _index.yaml
│   │   │   │   │   ├── file_structure.md
│   │   │   │   │   ├── nfpa79_iec60204_overlap.md
│   │   │   │   │   ├── standards_decision_workflow.md
│   │   │   │   │   ├── standards_overlap.md
│   │   │   │   │   └── ul508a_nec_nfpa79_overlap.md
│   │   │   │   └── overlap_notes/
│   │   │   │       ├── GENERATION_STATUS.md
│   │   │   │       ├── _index.yaml
│   │   │   │       ├── file_structure.md
│   │   │   │       └── overlap__sccr.md
│   │   │   ├── file_structure.md
│   │   │   ├── international/
│   │   │   │   ├── cybersecurity/
│   │   │   │   │   └── iec_62443/
│   │   │   │   │       ├── IEC62443_2_1__security_management.md
│   │   │   │   │       ├── IEC62443_3_3__system_security_requirements.md
│   │   │   │   │       ├── IEC62443_4_2__component_requirements.md
│   │   │   │   │       ├── IEC62443_lifecycle.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   ├── functional_safety/
│   │   │   │   │   ├── iec_61508/
│   │   │   │   │   │   ├── IEC61508_2010__Clause07__safety_lifecycle.md
│   │   │   │   │   │   ├── IEC61508_2010__Part1__framework.md
│   │   │   │   │   │   ├── IEC61508_2010__Part2__hardware.md
│   │   │   │   │   │   ├── IEC61508_2010__Part3__software.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_61511/
│   │   │   │   │   │   ├── IEC61511_2016__Clause08__sil_determination.md
│   │   │   │   │   │   ├── IEC61511_2016__Clause10__sis_design.md
│   │   │   │   │   │   ├── IEC61511_2016__Clause16__operation_maintenance.md
│   │   │   │   │   │   ├── IEC61511_2016__Part1__framework.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iec_62061/
│   │   │   │   │   │   ├── IEC62061_2021__AnnexA__silcl_tables.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause04__scope_context.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause06__srecs_design.md
│   │   │   │   │   │   ├── IEC62061_2021__Clause07__subsystem_design.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   ├── iso_12100/
│   │   │   │   │   │   ├── ISO12100_2010__AnnexA__hazard_list.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause04__risk_assessment_principles.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause05__risk_estimation.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause06__risk_evaluation.md
│   │   │   │   │   │   ├── ISO12100_2010__Clause07__risk_reduction.md
│   │   │   │   │   │   └── _index.yaml
│   │   │   │   │   └── iso_13849_1/
│   │   │   │   │       ├── ISO13849_2023__AnnexA__risk_assessment.md
│   │   │   │   │       ├── ISO13849_2023__AnnexF__ccf.md
│   │   │   │   │       ├── ISO13849_2023__Clause04__design_strategy.md
│   │   │   │   │       ├── ISO13849_2023__Clause05__srp_cs.md
│   │   │   │   │       ├── ISO13849_2023__Clause06__categories.md
│   │   │   │   │       ├── ISO13849_2023__Clause07__validation.md
│   │   │   │   │       └── _index.yaml
│   │   │   │   └── machinery/
│   │   │   │       └── iec_60204_1/
│   │   │   │           ├── GENERATION_SUMMARY.md
│   │   │   │           ├── IEC60204_1_2018__Clause01__scope.md
│   │   │   │           ├── IEC60204_1_2018__Clause02__normative_references.md
│   │   │   │           ├── IEC60204_1_2018__Clause03__terms_and_definitions.md
│   │   │   │           ├── IEC60204_1_2018__Clause04__general_requirements.md
│   │   │   │           ├── IEC60204_1_2018__Clause05__incoming_supply.md
│   │   │   │           ├── IEC60204_1_2018__Clause06__protection_against_electric_shock.md
│   │   │   │           ├── IEC60204_1_2018__Clause07__protection_of_equipment.md
│   │   │   │           ├── IEC60204_1_2018__Clause08__equipotential_bonding.md
│   │   │   │           ├── IEC60204_1_2018__Clause09__control_circuits_and_functions.md
│   │   │   │           ├── IEC60204_1_2018__Clause10__operator_interface.md
│   │   │   │           ├── IEC60204_1_2018__Clause11__control_equipment.md
│   │   │   │           ├── IEC60204_1_2018__Clause12__motors_and_drives.md
│   │   │   │           ├── IEC60204_1_2018__Clause13__accessories_and_lighting.md
│   │   │   │           ├── IEC60204_1_2018__Clause14__marking_and_documentation.md
│   │   │   │           ├── IEC60204_1_2018__Clause15__verification.md
│   │   │   │           ├── IEC60204_OVERVIEW.md
│   │   │   │           ├── README.md
│   │   │   │           └── _index.yaml
│   │   │   ├── library_admin/
│   │   │   │   ├── COMPLETE_STANDARDS_PORTFOLIO.md
│   │   │   │   ├── README.md
│   │   │   │   ├── STANDARDS_COMPLETION_STATUS.md
│   │   │   │   ├── STANDARDS_MODULES_SUMMARY.md
│   │   │   │   └── STANDARDS_PURCHASE_TRACKER.md
│   │   │   ├── reference_models/
│   │   │   │   ├── 15-Standard Minimum Compliance Stack.md
│   │   │   │   ├── 7-Layer Industrial Machine Architecture Model.md
│   │   │   │   ├── README.md
│   │   │   │   ├── Software_Safety_and_Intrinsic_Safety_Standards.md
│   │   │   │   ├── Universal Machine Safety Architecture.md
│   │   │   │   └── standards_atlas_diagrams_reference.md
│   │   │   ├── routing/
│   │   │   │   ├── README.md
│   │   │   │   └── standards_applicability.md
│   │   │   ├── scenario/
│   │   │   │   ├── cnc_machine_safety_design/
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   ├── requirements.yaml
│   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   ├── system_description.md
│   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   ├── mini_machine_safety_design/
│   │   │   │   │   ├── README.md
│   │   │   │   │   ├── control_architecture_and_network.md
│   │   │   │   │   ├── hazards_and_risk_assessment.md
│   │   │   │   │   ├── industry_overlays/
│   │   │   │   │   │   ├── commercial.md
│   │   │   │   │   │   ├── energy.md
│   │   │   │   │   │   ├── food_and_beverage.md
│   │   │   │   │   │   ├── marine.md
│   │   │   │   │   │   ├── medical.md
│   │   │   │   │   │   ├── nuclear.md
│   │   │   │   │   │   ├── offshore.md
│   │   │   │   │   │   ├── petroleum.md
│   │   │   │   │   │   └── semiconductor.md
│   │   │   │   │   ├── mechanical_and_electrical_isolation.md
│   │   │   │   │   ├── requirements.yaml
│   │   │   │   │   ├── safety_functions_register.md
│   │   │   │   │   ├── safety_integrity_and_sil_strategy.md
│   │   │   │   │   ├── standards_applicability_matrix.md
│   │   │   │   │   ├── system_description.md
│   │   │   │   │   ├── ul_nec_design_requirements.md
│   │   │   │   │   └── verification_and_validation_plan.md
│   │   │   │   └── mini_machine_safety_design_v2/
│   │   │   │       ├── README.md
│   │   │   │       ├── control_architecture_and_network.md
│   │   │   │       ├── hazards_and_risk_assessment.md
│   │   │   │       ├── industry_overlays/
│   │   │   │       │   ├── commercial.md
│   │   │   │       │   ├── energy.md
│   │   │   │       │   ├── food_and_beverage.md
│   │   │   │       │   ├── marine.md
│   │   │   │       │   ├── medical.md
│   │   │   │       │   ├── nuclear.md
│   │   │   │       │   ├── offshore.md
│   │   │   │       │   ├── petroleum.md
│   │   │   │       │   └── semiconductor.md
│   │   │   │       ├── mechanical_and_electrical_isolation.md
│   │   │   │       ├── requirements.yaml
│   │   │   │       ├── safety_functions_register.md
│   │   │   │       ├── safety_integrity_and_sil_strategy.md
│   │   │   │       ├── standards_applicability_matrix.md
│   │   │   │       ├── system_description.md
│   │   │   │       ├── ul_nec_design_requirements.md
│   │   │   │       └── verification_and_validation_plan.md
│   │   │   └── us/
│   │   │       ├── nec/
│   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │       │   ├── NEC_2023__Art110__requirements_for_electrical_installations.md
│   │   │       │   ├── NEC_2023__Art240__overcurrent_protection.md
│   │   │       │   ├── NEC_2023__Art250__grounding_and_bonding.md
│   │   │       │   ├── NEC_2023__Art300__general_wiring_methods.md
│   │   │       │   ├── NEC_2023__Art310__conductors_for_general_wiring.md
│   │   │       │   ├── NEC_2023__Art408__switchboards_switchgear_and_panelboards.md
│   │   │       │   ├── NEC_2023__Art409__industrial_control_panels.md
│   │   │       │   ├── NEC_2023__Art430__motors_motor_circuits_and_controllers.md
│   │   │       │   ├── NEC_2023__Art670__industrial_machinery.md
│   │   │       │   ├── NEC_2023__Art725__class_1_2_3_control_circuits.md
│   │   │       │   ├── NEC_COMPLETION_STATUS.md
│   │   │       │   ├── NEC_OVERVIEW.md
│   │   │       │   ├── README.md
│   │   │       │   └── _index.yaml
│   │   │       ├── nfpa79/
│   │   │       │   ├── GENERATION_SUMMARY.md
│   │   │       │   ├── NFPA79_2024__Ch01__administration.md
│   │   │       │   ├── NFPA79_2024__Ch02__definitions.md
│   │   │       │   ├── NFPA79_2024__Ch03__general_requirements.md
│   │   │       │   ├── NFPA79_2024__Ch04__general_conditions_of_installation.md
│   │   │       │   ├── NFPA79_2024__Ch05__disconnecting_means.md
│   │   │       │   ├── NFPA79_2024__Ch06__overcurrent_protection.md
│   │   │       │   ├── NFPA79_2024__Ch07__protection_against_electric_shock.md
│   │   │       │   ├── NFPA79_2024__Ch08__grounding_and_bonding.md
│   │   │       │   ├── NFPA79_2024__Ch09__control_circuits_and_control_functions.md
│   │   │       │   ├── NFPA79_2024__Ch10__operator_interface_devices.md
│   │   │       │   ├── NFPA79_2024__Ch11__control_equipment.md
│   │   │       │   ├── NFPA79_2024__Ch12__motors_and_associated_equipment.md
│   │   │       │   ├── NFPA79_2024__Ch13__appliances_and_accessories.md
│   │   │       │   ├── NFPA79_2024__Ch14__lighting.md
│   │   │       │   ├── NFPA79_2024__Ch15__transformers_and_power_supplies.md
│   │   │       │   ├── NFPA79_2024__Ch16__wiring_methods.md
│   │   │       │   ├── NFPA79_2024__Ch17__cables_and_flexible_cords.md
│   │   │       │   ├── NFPA79_2024__Ch18__terminal_blocks_and_connectors.md
│   │   │       │   ├── NFPA79_2024__Ch19__marking_and_documentation.md
│   │   │       │   ├── NFPA79_2024__Ch20__system_integration.md
│   │   │       │   ├── NFPA_OVERVIEW.md
│   │   │       │   ├── README.md
│   │   │       │   └── _index.yaml
│   │   │       └── ul_508a/
│   │   │           ├── GENERATION_SUMMARY.md
│   │   │           ├── README.md
│   │   │           ├── UL508A_2022__control_circuits_and_devices.md
│   │   │           ├── UL508A_2022__enclosures_and_environmental_ratings.md
│   │   │           ├── UL508A_2022__general_construction_requirements.md
│   │   │           ├── UL508A_2022__grounding_and_bonding.md
│   │   │           ├── UL508A_2022__marking_and_documentation.md
│   │   │           ├── UL508A_2022__motor_controllers_and_drives.md
│   │   │           ├── UL508A_2022__overcurrent_protection.md
│   │   │           ├── UL508A_2022__sccr_short_circuit_current_rating.md
│   │   │           ├── UL508A_2022__scope_and_application.md
│   │   │           ├── UL508A_2022__spacing_creepage_clearance.md
│   │   │           ├── UL508A_2022__transformers_and_power_supplies.md
│   │   │           ├── UL508A_2022__wiring_methods_and_conductors.md
│   │   │           ├── UL508A_OVERVIEW.md
│   │   │           └── _index.yaml
│   │   ├── training_modules/
│   │   │   ├── commissioning/
│   │   │   ├── fundamentals/
│   │   │   ├── safety/
│   │   │   └── troubleshooting/
│   │   └── troubleshooting_engine/
│   │       ├── analog_io/
│   │       ├── decision_trees.yaml
│   │       ├── digital_io/
│   │       ├── motion_servo/
│   │       ├── networks/
│   │       └── pid_control/
│   ├── restricted/
│   │   ├── README.md
│   │   ├── do_not_read/
│   │   │   ├── DELIVERABLE.md
│   │   │   ├── PROJECT_STRUCTURE 4.59.29 PM.md
│   │   │   ├── QUICK_START.md
│   │   │   ├── README.md
│   │   │   └── control_system_project_template.tar.gz
│   │   └── legacy_drafts/
│   │       ├── README.md
│   │       ├── copied_standard_text/
│   │       ├── raw_notes/
│   │       └── vendor_docs/
│   ├── templates/
│   │   ├── README.md
│   │   ├── checklists/
│   │   ├── design_guides/
│   │   ├── md_headers/
│   │   │   ├── draft_only_header.md
│   │   │   └── rag_approved_header.md
│   │   └── reports/
│   ├── tools/
│   │   ├── audit_tool/
│   │   │   ├── README.md
│   │   │   ├── outputs/
│   │   │   └── report_templates/
│   │   ├── business_metrics_profit_engine/
│   │   │   ├── README.md
│   │   │   └── exports/
│   │   ├── design_package_generator/
│   │   │   ├── README.md
│   │   │   └── kits/
│   │   │       ├── conveyor_control_kit/
│   │   │       ├── pump_skid_control_kit/
│   │   │       └── robotic_cell_control_kit/
│   │   ├── ip_library_licensing/
│   │   │   ├── README.md
│   │   │   └── export_packages/
│   │   ├── knowledge_platform/
│   │   │   └── README.md
│   │   ├── retainer_support_engine/
│   │   │   ├── README.md
│   │   │   └── outputs/
│   │   └── ul508a_panel_automation/
│   │       ├── README.md
│   │       ├── outputs/
│   │       └── ul_documentation_templates/
│   └── work/
│       ├── README.md
│       ├── design/
│       │   ├── README.md
│       │   ├── decision_workflow.md
│       │   ├── diagrams/
│       │   ├── experiments/
│       │   ├── mermaid_diagrams_to_reference.md
│       │   ├── mini_machine_safety_design_v2_project_status.md
│       │   ├── nec_update.md
│       │   ├── scratch_notes/
│       │   ├── simple_safety_system_design.md
│       │   ├── standards_atlas_homepage_wireframe_and_templates.md
│       │   ├── standards_web_page_design_prompt_v1.md
│       │   ├── standards_web_page_design_prompt_v3.md
│       │   ├── standards_web_page_design_prompt_v4.1.md
│       │   └── standards_web_page_design_prompt_v4.md
│       └── general/
│           ├── 00_inbox_notes.md
│           ├── README.md
│           ├── commissioning_notes/
│           ├── design_working/
│           ├── experiments/
│           ├── standards_notes/
│           └── troubleshooting_logs/
├── data/
│   ├── README.md
│   ├── historian_exports/
│   ├── network_captures/
│   └── plc_exports/
├── docs/
│   ├── .bundle/
│   │   └── config
│   ├── .jekyll-cache/
│   │   ├── .gitignore
│   │   └── Jekyll/
│   │       └── Cache/
│   │           ├── Jekyll--Cache/
│   │           │   └── b7/
│   │           │       └── 9606fb3afea5bd1609ed40b622142f1c98125abcfe89a76a661b0e8e343910
│   │           └── Jekyll--Converters--Markdown/
│   │               ├── 01/
│   │               │   └── 490aeb193504bfbf24410f4a2ca9635a499a3f5f6f946c84532507b40ad03c
│   │               ├── 03/
│   │               │   └── 0cd6164ad2049de1dadb6afb15ff7b238db25e1b7e6ae3b6919d7db7db7708
│   │               ├── 04/
│   │               │   ├── 40782a1a0d97a682c271d1e3c42b89937299677161492792e8e48d4a3c4de4
│   │               │   └── 8ae153d1cc2aef54095eadad06148ac1372da0e9f585dc95e40b643279a3ea
│   │               ├── 06/
│   │               │   └── d3a687ff4b25e2062eb633ed15fbe1736c9f6c4345811632c44f80c9c712bd
│   │               ├── 08/
│   │               │   ├── 4ce4c9fe25a2e3a4783c96c116b5041352ed067bc5c830467b332afcbe86fa
│   │               │   └── cb215652a3ec3a6b7c85b5d2946ec0dd877fb6c4a83a80c02ebb66aef23c78
│   │               ├── 0a/
│   │               │   └── 46242bc7af14bf7af61342f0928754a9f55af3b85e5ed37689bdc43e37538f
│   │               ├── 0b/
│   │               │   ├── 23e434b41214de015244201734a4457b8658eaf57d3ffa015a237ba741d88d
│   │               │   └── 36fd9699ea3c594f2935d5b180504cca916d440e00a16fc4081cc59274562a
│   │               ├── 0c/
│   │               │   ├── 21a7d7aadd1a042168087ad4dd2323df1ae50a4de93a8da4b920963100b904
│   │               │   └── b884b6343a61259ab5eacf2fb4394a401d05919cfd0fc5fcdc94957f0dc271
│   │               ├── 0d/
│   │               │   └── 0b2dfd9fcde91ec81a829dbc690e60db0c9de83282525b18f277a4434ae4bf
│   │               ├── 0f/
│   │               │   └── 260c0f2220909dd3e4dd4990c35bacc6ec27c2c18b194b8205187fb96a4ecf
│   │               ├── 10/
│   │               │   └── da3413b3d068d25f0f0f6333d381ba222d1cdbc1405613dcaeeeba2b097f37
│   │               ├── 18/
│   │               │   ├── c51a279f5cb2e4648501e75da94e6dd98e8d64407b0b7068685ae0cb0ffc8f
│   │               │   └── d3316f7c16039a4102c5a6253e8e9b67d37db908b0678995a7bf4a813b9221
│   │               ├── 1d/
│   │               │   └── 250bb7b7aa156123d8f05946de1c67eab85119aa8ee3e2b875f738549d9bd3
│   │               ├── 23/
│   │               │   └── 7ae4631ab84a0848ee51d4ecb6b14d359e0e4555074581c35f903dfdc94737
│   │               ├── 27/
│   │               │   └── e44a450c423c9eb130be0e89f59aeb0f1ed6640b8c00fe1432a47164899edc
│   │               ├── 28/
│   │               │   ├── b1f2ee513fb5c930f6e83980c3a9d8e84cc57ed5125ba9d1c06112014b8f53
│   │               │   └── dd4852dc932337b5b961300ebd0a735a9adf198f740984d8983e8c6aa279a9
│   │               ├── 2a/
│   │               │   ├── a2e80619f1620666cd536d612c7eb320609bf93834edcf5aca322334f85a7f
│   │               │   ├── aa3f7d45023ddf87b1d0d05b61b38d7d58d66e3010aa79f6a2986399295f5d
│   │               │   └── aafba3bfdbb57933a12300e21feab6c83cfb4e57334fb6f70b4d8ae1ba973a
│   │               ├── 2b/
│   │               │   ├── 1df1b19b5a468913e187313dcf8e21bd90e54fcb0a75b86d6f7f87bf86f888
│   │               │   └── 4168245053a9927df540d1a9bdfc140b6859cc1e2be299779e134136a7a893
│   │               ├── 2c/
│   │               │   └── 9bcd808985cdaa49537e875c91e0ee76020f2c82514987d576738005773fb5
│   │               ├── 2f/
│   │               │   └── 5e1412735984ba77818de876dcf7007c5dce7da5d99c244a86b7d4444a7d59
│   │               ├── 31/
│   │               │   └── dc4b6eda03f83f13fff24585427aaab3d137a586173926a0d1ab717c6363e5
│   │               ├── 33/
│   │               │   ├── b95d3c72b1293a7ca1aa200291cf6491cce8b27ca46349cb20ae2df406a431
│   │               │   └── f71006d652ee55f235e9f005fc6620afcbbf683f2e8332e81378e5d2ae4975
│   │               ├── 36/
│   │               │   └── d582097a42b157b16a059c76c099e57f145550bc3b1266e8823f4c06a7146b
│   │               ├── 3a/
│   │               │   └── 78695388b38b5cceefaf6796b0137877514593543b91af2752d5a17e3d736c
│   │               ├── 3b/
│   │               │   ├── 337c3092c08d7a55343ebef55b0e7ea6c253bd90db4b44ae431484db745587
│   │               │   └── ca9d58be429a9e9a507c2c31486d80a475e1c53683e002ba45d40231a51d4d
│   │               ├── 3c/
│   │               │   └── 0b48fc82605fe676f17415632e8cbd4fb2a2108041b657de120996fe62bf1a
│   │               ├── 3d/
│   │               │   ├── 59b21cc1d68ca8331c7c38de212f1af165ddd8eb490ba34df87b0a36f9a04f
│   │               │   └── f4d444ee0040c89311c2d73c3326794e46176bf3eb9d6c6a849a664aa51167
│   │               ├── 3e/
│   │               │   └── 028e67685c721688f48d32ba0b32b20d0a563cebb4a4f11077f03ffe129ac0
│   │               ├── 44/
│   │               │   └── abc8c9eb91277aafc8354abfa26eb1493cb042ebdfe94ca3e369d42cf1fb34
│   │               ├── 45/
│   │               │   └── 1d199da3fc4eb4913c4062496af6a933e1bc803d68aba072b793205bcad44e
│   │               ├── 4c/
│   │               │   └── c13b24eb0a0019b4f4fff2f237b36c8ed17e43d7e7663945b8791a99fa65d1
│   │               ├── 4d/
│   │               │   ├── 375658a3dee103e24a7a4bc7f92754e1a7e981bade529055cb96a01c852b8a
│   │               │   └── b8b58d02d7843550d6ad60a54ee453b56301f4858fa670c97095dd332c9d32
│   │               ├── 4e/
│   │               │   ├── 469c2281456ea6b8c3574a8de06961878eeb16282aabec232f3e7cdaa20e7c
│   │               │   └── d6a389b09b4429688c735a86f8a0f3b92d5176bcd2d9295630442404a5e6b6
│   │               ├── 4f/
│   │               │   ├── 22047c6ccca17ed77b8b96ad6638fc34c17902034215785307430e687d1d47
│   │               │   └── f6a3baebc55f69a127eca51eeda6a21b39ed4f11852068669241c01e7da412
│   │               ├── 51/
│   │               │   └── 4ee3fa4b04c732c61e969557de745559fdda5f30d80dce60284d3d6a47c56e
│   │               ├── 53/
│   │               │   ├── 3a5829faaa787b1ee6d77d3bdeb72aff57a3359def2c2035e2076de4ec3333
│   │               │   └── 53a85ed48f127b7ee0a50fe5deb94bbc3a6b0ff1c978f7482d575ec0416090
│   │               ├── 58/
│   │               │   └── 48fb5dbf644868d19cef871e3b3e6b8f0cb74b9b14f517953781f7517e3b04
│   │               ├── 59/
│   │               │   └── 8ae6a5381cd39978b24dd3db2fcd95b36e4ea0a99731137cdcaa5262a3af56
│   │               ├── 5b/
│   │               │   ├── aaa7b65775d52ee9cfb41de62b27d7cf0bf3981ac35c58fdc2f6490f31d81d
│   │               │   └── d4b2fa17815610d897c1dbfd754724e6e17f5d8607dfbba9dc9a09b195d453
│   │               ├── 5c/
│   │               │   └── 89640df2443aa0d8cc29262765c2de8514a348524c3c271900ab45566232cc
│   │               ├── 5f/
│   │               │   └── 0b833a96ec0aec240d4945019807eaf088d4f47d501e20e79e187b26bd7e79
│   │               ├── 63/
│   │               │   └── 582519d06633dba633befe67088a06e0abdc9e0cbf034d0ec1ca869fa36213
│   │               ├── 64/
│   │               │   └── f72cfd451333ad8e1f7d8a3a8d1b1e39c649bec4bc6e02b5b7636ff28831e1
│   │               ├── 65/
│   │               │   └── d932887cb12b690a82254985420ce523025c147254a96e75b3563346fb3995
│   │               ├── 67/
│   │               │   └── 4a54a94261204022af06bf75b7d060f96f1b241ce897bcab2e72cb295f7d5f
│   │               ├── 68/
│   │               │   ├── a2d31b07d758ad5a731effd78b6052e7a69b0e44d60d31400db7985c7f743d
│   │               │   └── d36678e02883088f48e6dece1b76e7b2e133928e5366551af20bc4cee6a8bd
│   │               ├── 6a/
│   │               │   └── fd8b42aff0c079bae80128c9428181e50e5edeae6575f3584e464b954b6e61
│   │               ├── 6f/
│   │               │   └── 5c8de5795d1e958681cfe90b53a1dfc00c8e8be18d2f2b662621eac3d01fff
│   │               ├── 70/
│   │               │   ├── 6bf1a4e30a45c09272b0ab99a32a2c2b556106edc929b96d7c5b545048fe62
│   │               │   └── c3114be24f5d35bdb46412573e383fa0ebf515e5e094039e4b3f3615a1dd86
│   │               ├── 71/
│   │               │   └── 3a92a6f35e2100179cec7de3c2189ccb03a159f80d22271a8df5d7e554e49e
│   │               ├── 72/
│   │               │   └── ceb13fd79a594294d73a17d599411f34d2410abf8c489e5b75cc36b1ecd445
│   │               ├── 75/
│   │               │   └── 24553e12d75198ecd44b29e18f860a05e2ca0453b46c13af5c4004ec4c9f30
│   │               ├── 76/
│   │               │   ├── 7fffd58941a23f7d30a6612884ccc11f8d6a9d68e250f66cada79199dffa3e
│   │               │   ├── d5d2ed8c3e2bcef1476c89e6d8ece7a0b379b592f89ff7669668c3b6231cb9
│   │               │   └── f20e4f21d32454e4ccbbabbf6adf78ec95abcb9c60b64a274ab8ad2c3d7ef6
│   │               ├── 78/
│   │               │   └── 9c0a33a7ef2814d2a1ee3d386ffa519dbb166402a4aa7ae54d05b34da87f37
│   │               ├── 7a/
│   │               │   └── 057d9014c25f4b76198a8779e97d958c5f1386f164f8aa91e8b3fae6abd568
│   │               ├── 7b/
│   │               │   └── 5d4789139aa089f579ca5a2261579849a889cd2a0518e55f94e4f0f8e1e267
│   │               ├── 7c/
│   │               │   └── 4141881a2e73d857a5e0a2ee06128726e369fd041a403e0691e7f2c692362b
│   │               ├── 7e/
│   │               │   └── 1dbc1110aecfe097d8f86fe19410161e74d12a58a0ea1fef8809ad81124306
│   │               ├── 7f/
│   │               │   └── 53770c6fc9a4b6368b5d8693ad59fe612232f13dcf1b8358180f510bc97ee9
│   │               ├── 80/
│   │               │   └── c4a4cbd716179311441280d346ac16f88a7ab2a807d9d67e904d9db008899d
│   │               ├── 83/
│   │               │   └── 592017cebc796956c4d9c01e38768d2600acd2991b25d011cbc86a8ac7c8c7
│   │               ├── 84/
│   │               │   └── b1e0eacbf30e2919561e86db5d4f15b41366cd6e1c421514cbf0241c0ead23
│   │               ├── 85/
│   │               │   └── fc8f1d8aaa1881f365e5e03e485dc3ce0f1f31decbe705adc3080b8940277f
│   │               ├── 8f/
│   │               │   └── c1213ea092e22c325fa5ad42f2e3bcae32d7f5f3cef57979a008f427e9d7d0
│   │               ├── 92/
│   │               │   ├── 4fe926ec4cd47e0304801483afc663a1829e779476c492f7be2996fdb7717c
│   │               │   └── d45446618749d74bb3377b0f68eca3c1f4392f9b094ecf71f6b7c11e47421f
│   │               ├── 94/
│   │               │   └── 54c281d58441cd4e68f7e6f853f27334d19bc43f1eaf6f654287cf165f582a
│   │               ├── 95/
│   │               │   └── f626e0e9943cc078b905ce2ba6c08a14cd8b3031c9e12f8aa3f8e8d74ea015
│   │               ├── 98/
│   │               │   ├── 2ce3f1ee993bedb1f3922dc43eeee9246752ccc8902496627f5695ae8de45b
│   │               │   └── b154ebeefb18f0d89106cabf20003ebc5ea1045b8c401c014b8a639e24d30b
│   │               ├── 9b/
│   │               │   └── c4024f9f30d4f17a7689e9224daa9922c1ae7cdb80c160b2f488a07dc4accd
│   │               ├── 9c/
│   │               │   └── ce64096a34a558a31ba7ff9d177d232c0206705337bde319aceb17a3670eb0
│   │               ├── 9d/
│   │               │   └── cfceb9d45812c2f2c5d3d8f7b5105bf20a9d4155b049c26a1092980c814bd6
│   │               ├── 9e/
│   │               │   └── ea847b20a846415aff5ab80539dd2092bc625b52550d83d52d0673561112ff
│   │               ├── 9f/
│   │               │   └── 09412d4907979d035e6548c38ac8ff04ccc98e23cae749e631d2b50c6d57a8
│   │               ├── a1/
│   │               │   └── ab8a89eecbb75b021354dc570a802d76726d522ee29946a3d5b342db30d77f
│   │               ├── a2/
│   │               │   └── 8e2ef91e74d4e0d9af056141b1aa5c6a84d61d339e66103419b15ddf62e9ec
│   │               ├── a5/
│   │               │   └── ce0567a59bbb95a147ad313bdbb5e9a6f80e3b1071ac421f6b3d4183b96d22
│   │               ├── a6/
│   │               │   └── ea9eca2f0fd8b821ed941651a07f433957b83e4deed7e7231cf6f689d8ccf4
│   │               ├── a7/
│   │               │   └── 99cdfd54cbce70aaaaf23faff3911b82bdc0d3d8afc1454a783928c9e097f7
│   │               ├── a8/
│   │               │   └── 45f31917b9b20c7dd5165672407aab2c4bb9db263ad60fad7eb9c11b2b708c
│   │               ├── aa/
│   │               │   └── dc531eb827c1a74688a3a10621186abed6f579f7173fd599fb774d7563e5f0
│   │               ├── ab/
│   │               │   ├── 33b54f032203b8633e2fdde0f9857f0350e262a479cd0e9050d467a519b21b
│   │               │   └── bb62bdd2991c0e0ae466c64f16527e36fbc886947b58a4d474ac03c39936b7
│   │               ├── ac/
│   │               │   └── b418e8347c01680d53a837227020a598007cf23fa79e4991a57cfc392f7891
│   │               ├── ad/
│   │               │   └── 3de1e36946a4311545bc36a4eeec565a8d126a3fd220cf5adc3d64ee6a24d4
│   │               ├── ae/
│   │               │   └── a98b8058482a0b71c9b67d339eb45b3b0e746af96a11cdbfab810c099a84b1
│   │               ├── af/
│   │               │   └── 9bc10db82a427568dca37ac69bd91aa0aeea461a1c2b411c9b895ca2e54aeb
│   │               ├── b1/
│   │               │   └── 6f24b19847d0a130a6132bfe2913fd5ab055cb5d0e8961a1da2ceb2273b42e
│   │               ├── b2/
│   │               │   └── e5bca22395754bc7201e96b2b02289851cce6945b939836f8b35506f65dc1e
│   │               ├── b3/
│   │               │   └── 28d3db6d0c11bed2ccb7065759d8d3f6bbd9428f9cd1eb8ae5d424d3befc20
│   │               ├── b9/
│   │               │   └── 36e833f0aee9829a7dd35393c778ee816d7d2ec3433e7629c9d2513aa329b3
│   │               ├── bd/
│   │               │   └── c8efd44dac060e7c0180014fa21b94d6e19571d49e485271fc67b16b7c4232
│   │               ├── be/
│   │               │   └── 316f2201fe24eb666a2f2a7161fa1bfcddf0176b10a22762b438dc7fa5d6e6
│   │               ├── bf/
│   │               │   └── 6bc0b2ee31345100572fb539a65f9bbb7ae04b3392d53f663e0c9bed14384d
│   │               ├── c0/
│   │               │   └── 9113fb9557c9aff69a9fb0828f6cd9085707003347509662864a5ae54d707b
│   │               ├── c1/
│   │               │   └── 8e3fce589275c09a49f1a4cc7677ad37b290a8c78dbe1646be80feb378da27
│   │               ├── c2/
│   │               │   ├── cc6b84a9f4eb9b6e8b0c003d26650092a3a7bf97c633dfdd28196004e5f120
│   │               │   ├── ef846d9adcc041c4563da65557ef2554f2838ebcc000c3278a7b0603730cd8
│   │               │   └── f659eea73a70a3e18100850751e9eb855f7806a9e8f28f2e6b3821b06ba432
│   │               ├── c3/
│   │               │   ├── 10195511914fa4ee2be29d017309cf6860ad2442004b75baaa2c66f23d7a63
│   │               │   └── ec9d7ef495fabeffc9060deed2b6e7672a232ea1eb077560011151d707a87a
│   │               ├── c4/
│   │               │   └── 75fb16a0a38c10c1dfdabab30c1b77e378d30ee1498bdb8f6399b29145ac1c
│   │               ├── c6/
│   │               │   └── b20534916e2ba117b370e18f5877c70f9277d97b0f9a8e31884c36ecb67968
│   │               ├── c9/
│   │               │   └── d5e20a5f7b3fca081d0e9fefda3ed37bceb84e645a9d71e24adc07baece46b
│   │               ├── cb/
│   │               │   └── 2747846fce151666135aebce8a8af85eb1eea8cdbde7f7e7ea77f795066b00
│   │               ├── cc/
│   │               │   └── cca6c3bfd574eb97bcbac50bcd9a577ae1f9ef049eee6ad1ca713bcf09be0a
│   │               ├── cf/
│   │               │   └── 92a9502650587c6b587bf0bd2fbe8408688be12db457cf57d12d7fa7447406
│   │               ├── d1/
│   │               │   ├── 974bd06596719580558f58eb297118a7afe09a544da9e1eefaa77295f81aa1
│   │               │   └── adf2390a11c4437b01dfbf3a0bdf78750fd0ee85614df683fe95428b8d6199
│   │               ├── d4/
│   │               │   └── 3a555dae8da5d95d957efec151bd184b427167c8ae1856c1a08016b9d57d24
│   │               ├── d5/
│   │               │   └── bd3094d0ad18bb35e581c2994241c11383381cd4bd274ec339b250c609ea6c
│   │               ├── d6/
│   │               │   └── b7bb1d58f549ca44a0764e7fd94e3714f7cbb6049fb24202664de210aacfdd
│   │               ├── d7/
│   │               │   └── 92c6bf5ca0cb6a01484eb838c34af15433bcb0da692b9084a472d9c4b505d9
│   │               ├── d8/
│   │               │   └── 460058dd46e923c304cee7010502aba8c4093fd64832454cd7047c0adc7473
│   │               ├── db/
│   │               │   └── c25cc47c033af87e9e88e49fc3db2da361c878bc8cef3070720fa89ead405c
│   │               ├── dc/
│   │               │   └── fea998fe1fd8b380872a1aece45a0dc84ea6c2a026018414e86ea08222b1b1
│   │               ├── dd/
│   │               │   └── 33d64d5c9484d6871f5b8acd882a074ad1d426584bda62166eb0c77af62b49
│   │               ├── df/
│   │               │   └── b4f236aae87abb1af2c130f9a4ff24d8c53a3013f1eebd24fa995c591a47ae
│   │               ├── e1/
│   │               │   └── 6915de1ee145b4551bf365486a617cad9de4723e8bd4e1108200e9fbcef526
│   │               ├── e3/
│   │               │   └── b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
│   │               ├── e4/
│   │               │   ├── 339f2cff31a3300a09c17c08f21f25d52c1baa04fbe050d72e1de0a2f40cd9
│   │               │   ├── 5357e75c488a7e619aec090ceaff01c1fd600d0fe1877056a63f64d1ec5ab1
│   │               │   └── bd289bc0bbfb364d99dfb54983c08b42ba2a4e667dc40d363533c56c27f214
│   │               ├── e5/
│   │               │   └── 4d3484396d913125c7a386ae59d7ef7bcc69ecf0afcbda0b1fd80e80aa2db2
│   │               ├── e7/
│   │               │   └── 71c382aa34051b00868eff65d922b969dc3bb7b1eaae356637abf78f9be551
│   │               ├── e9/
│   │               │   └── 2c762ee67e5c599d533c1f0abc210d41a8270c2c85b178c08642755fcbf5f7
│   │               ├── ea/
│   │               │   └── df3dfe34d237e72b57a6f65a765e995f6d280ae9df43d31475c6ddd56ab30c
│   │               ├── ec/
│   │               │   └── d92e266253295c8db97f9575c379ae8997ba7f6950f936df68450c1326f935
│   │               ├── ed/
│   │               │   ├── bc97ede5832fc84913b39dc6483c59021402f4de631cca082a5825bba5b22b
│   │               │   └── f867c0ee7664e62c7dbd27fba23467f1652c419dcce1c4ee57c7772dab4e48
│   │               ├── f1/
│   │               │   └── 4de0c2dfa4009076ed6ba8d42c9b22d122562a5d0f63fef83c1d37c980aa05
│   │               ├── f2/
│   │               │   └── 6474473b95c88cb3306339ea2de52245f119f46242683f7a76257ddd70a461
│   │               ├── f6/
│   │               │   └── 5cd8a0bbb88a838309164c51364f7a4aade6eb52086ca1c3c73c4de227ad93
│   │               ├── f8/
│   │               │   └── af3b8919e60de352473986a794bb7f5130ea78933de5f04ae860178f2d24a1
│   │               ├── f9/
│   │               │   ├── 6beea3b5952d170ff7a0a3bf096ba1774e419484af218b83b8f106363f19cf
│   │               │   └── e856f21719585ba00f827f2c44aca692005fd416150b4bd497ffd16d39cb88
│   │               ├── fa/
│   │               │   └── 7e3898b35bd6336f764b2de29f0c1ff11b73239574bd17c491fce466ecaf2d
│   │               └── fc/
│   │                   ├── 5cd15a7922e80358a840029fb84cba57a85bff721a4533671cee889d09c67a
│   │                   └── 7fd42ac2ea9db79760e7459de6ef1c2141001780d192ab516c5d1e23fe17ba
│   ├── Gemfile
│   ├── Gemfile.lock
│   ├── _config.yml
│   ├── _includes/
│   │   ├── context-panel.html
│   │   ├── sidebar.html
│   │   ├── topnav.html
│   │   └── trust-boundary.html
│   ├── _layouts/
│   │   └── default.html
│   ├── _site/
│   │   ├── about/
│   │   │   └── index.html
│   │   ├── assets/
│   │   │   ├── css/
│   │   │   │   └── main.css
│   │   │   ├── data/
│   │   │   │   └── search.json
│   │   │   ├── img/
│   │   │   │   └── favicon.svg
│   │   │   └── js/
│   │   │       └── main.js
│   │   ├── crosswalks/
│   │   │   ├── compare/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── nfpa79-iec60204/
│   │   │   │   └── index.html
│   │   │   ├── standards-decision-workflow/
│   │   │   │   └── index.html
│   │   │   └── ul508a-nec-nfpa79/
│   │   │       └── index.html
│   │   ├── index.html
│   │   ├── industries/
│   │   │   ├── commercial/
│   │   │   │   └── index.html
│   │   │   ├── energy/
│   │   │   │   └── index.html
│   │   │   ├── food-and-beverage/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── marine/
│   │   │   │   └── index.html
│   │   │   ├── medical/
│   │   │   │   └── index.html
│   │   │   ├── nuclear/
│   │   │   │   └── index.html
│   │   │   ├── offshore/
│   │   │   │   └── index.html
│   │   │   ├── petroleum/
│   │   │   │   └── index.html
│   │   │   └── semiconductor/
│   │   │       └── index.html
│   │   ├── lifecycle/
│   │   │   ├── build/
│   │   │   │   └── index.html
│   │   │   ├── commissioning/
│   │   │   │   └── index.html
│   │   │   ├── concept/
│   │   │   │   └── index.html
│   │   │   ├── detailed-design/
│   │   │   │   └── index.html
│   │   │   ├── draft-documentation/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── installation/
│   │   │   │   └── index.html
│   │   │   ├── maintenance/
│   │   │   │   └── index.html
│   │   │   ├── pre-commissioning/
│   │   │   │   └── index.html
│   │   │   ├── risk-assessment/
│   │   │   │   └── index.html
│   │   │   ├── safety-architecture/
│   │   │   │   └── index.html
│   │   │   ├── safety-wiring/
│   │   │   │   └── index.html
│   │   │   └── standards-selection/
│   │   │       └── index.html
│   │   ├── plans/
│   │   │   ├── 2026-03-05-phase2-design.md
│   │   │   ├── 2026-03-05-phase2-implementation.md
│   │   │   ├── 2026-03-06-phase3-functional-safety-design.md
│   │   │   ├── 2026-03-06-phase3-implementation.md
│   │   │   ├── 2026-03-08-decision-workflow-enhancements.md
│   │   │   └── 2026-03-08-nec-page-update.md
│   │   ├── scenarios/
│   │   │   ├── global-machine/
│   │   │   │   └── index.html
│   │   │   ├── index.html
│   │   │   ├── machine-safety-implementation/
│   │   │   │   └── index.html
│   │   │   ├── networked-safety-plc/
│   │   │   │   └── index.html
│   │   │   ├── process-skid/
│   │   │   │   └── index.html
│   │   │   ├── semiconductor-equipment/
│   │   │   │   └── index.html
│   │   │   └── us-industrial-control-panel/
│   │   │       └── index.html
│   │   ├── software-stack/
│   │   │   └── index.html
│   │   └── standards/
│   │       ├── cybersecurity/
│   │       │   ├── iec-62443/
│   │       │   │   └── index.html
│   │       │   └── index.html
│   │       ├── functional-safety/
│   │       │   ├── iec-61508/
│   │       │   │   └── index.html
│   │       │   ├── iec-61511/
│   │       │   │   └── index.html
│   │       │   ├── iec-62061/
│   │       │   │   └── index.html
│   │       │   ├── index.html
│   │       │   ├── iso-12100/
│   │       │   │   └── index.html
│   │       │   └── iso-13849-1/
│   │       │       └── index.html
│   │       ├── index.html
│   │       ├── machinery/
│   │       │   ├── iec-60204-1/
│   │       │   │   └── index.html
│   │       │   └── index.html
│   │       └── us-electrical/
│   │           ├── index.html
│   │           ├── nec/
│   │           │   └── index.html
│   │           ├── nfpa-79/
│   │           │   └── index.html
│   │           └── ul-508a/
│   │               └── index.html
│   ├── about/
│   │   └── index.md
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── data/
│   │   │   └── search.json
│   │   ├── img/
│   │   │   └── favicon.svg
│   │   └── js/
│   │       └── main.js
│   ├── crosswalks/
│   │   ├── compare/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── nfpa79-iec60204/
│   │   │   └── index.md
│   │   ├── standards-decision-workflow/
│   │   │   └── index.md
│   │   └── ul508a-nec-nfpa79/
│   │       └── index.md
│   ├── index.md
│   ├── industries/
│   │   ├── commercial/
│   │   │   └── index.md
│   │   ├── energy/
│   │   │   └── index.md
│   │   ├── food-and-beverage/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── marine/
│   │   │   └── index.md
│   │   ├── medical/
│   │   │   └── index.md
│   │   ├── nuclear/
│   │   │   └── index.md
│   │   ├── offshore/
│   │   │   └── index.md
│   │   ├── petroleum/
│   │   │   └── index.md
│   │   └── semiconductor/
│   │       └── index.md
│   ├── lifecycle/
│   │   ├── build/
│   │   │   └── index.md
│   │   ├── commissioning/
│   │   │   └── index.md
│   │   ├── concept/
│   │   │   └── index.md
│   │   ├── detailed-design/
│   │   │   └── index.md
│   │   ├── draft-documentation/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── installation/
│   │   │   └── index.md
│   │   ├── maintenance/
│   │   │   └── index.md
│   │   ├── pre-commissioning/
│   │   │   └── index.md
│   │   ├── risk-assessment/
│   │   │   └── index.md
│   │   ├── safety-architecture/
│   │   │   └── index.md
│   │   ├── safety-wiring/
│   │   │   └── index.md
│   │   └── standards-selection/
│   │       └── index.md
│   ├── plans/
│   │   ├── 2026-03-05-phase2-design.md
│   │   ├── 2026-03-05-phase2-implementation.md
│   │   ├── 2026-03-06-phase3-functional-safety-design.md
│   │   ├── 2026-03-06-phase3-implementation.md
│   │   ├── 2026-03-08-decision-workflow-enhancements.md
│   │   └── 2026-03-08-nec-page-update.md
│   ├── scenarios/
│   │   ├── global-machine/
│   │   │   └── index.md
│   │   ├── index.md
│   │   ├── machine-safety-implementation/
│   │   │   └── index.md
│   │   ├── networked-safety-plc/
│   │   │   └── index.md
│   │   ├── process-skid/
│   │   │   └── index.md
│   │   ├── semiconductor-equipment/
│   │   │   └── index.md
│   │   └── us-industrial-control-panel/
│   │       └── index.md
│   ├── software-stack/
│   │   └── index.md
│   ├── standards/
│   │   ├── cybersecurity/
│   │   │   ├── iec-62443/
│   │   │   │   └── index.md
│   │   │   └── index.md
│   │   ├── functional-safety/
│   │   │   ├── iec-61508/
│   │   │   │   └── index.md
│   │   │   ├── iec-61511/
│   │   │   │   └── index.md
│   │   │   ├── iec-62061/
│   │   │   │   └── index.md
│   │   │   ├── index.md
│   │   │   ├── iso-12100/
│   │   │   │   └── index.md
│   │   │   └── iso-13849-1/
│   │   │       └── index.md
│   │   ├── index.md
│   │   ├── machinery/
│   │   │   ├── iec-60204-1/
│   │   │   │   └── index.md
│   │   │   └── index.md
│   │   └── us-electrical/
│   │       ├── index.md
│   │       ├── nec/
│   │       │   └── index.md
│   │       ├── nfpa-79/
│   │       │   └── index.md
│   │       └── ul-508a/
│   │           └── index.md
│   └── vendor/
│       └── bundle/
│           └── ruby/
│               └── 2.6.0/
│                   ├── bin/
│                   │   ├── jekyll
│                   │   ├── kramdown
│                   │   ├── listen
│                   │   ├── rougify
│                   │   └── safe_yaml
│                   ├── build_info/
│                   ├── cache/
│                   │   ├── addressable-2.8.9.gem
│                   │   ├── colorator-1.1.0.gem
│                   │   ├── concurrent-ruby-1.3.6.gem
│                   │   ├── em-websocket-0.5.3.gem
│                   │   ├── eventmachine-1.2.7.gem
│                   │   ├── ffi-1.17.3.gem
│                   │   ├── forwardable-extended-2.6.0.gem
│                   │   ├── google-protobuf-3.23.4-arm64-darwin.gem
│                   │   ├── http_parser.rb-0.8.1.gem
│                   │   ├── i18n-1.14.8.gem
│                   │   ├── jekyll-4.3.4.gem
│                   │   ├── jekyll-sass-converter-3.0.0.gem
│                   │   ├── jekyll-seo-tag-2.8.0.gem
│                   │   ├── jekyll-watch-2.2.1.gem
│                   │   ├── kramdown-2.5.2.gem
│                   │   ├── kramdown-parser-gfm-1.1.0.gem
│                   │   ├── liquid-4.0.4.gem
│                   │   ├── listen-3.10.0.gem
│                   │   ├── logger-1.7.0.gem
│                   │   ├── mercenary-0.4.0.gem
│                   │   ├── pathutil-0.16.2.gem
│                   │   ├── public_suffix-5.1.1.gem
│                   │   ├── rb-fsevent-0.11.2.gem
│                   │   ├── rb-inotify-0.11.1.gem
│                   │   ├── rexml-3.4.4.gem
│                   │   ├── rouge-3.30.0.gem
│                   │   ├── safe_yaml-1.0.5.gem
│                   │   ├── sass-embedded-1.58.3-arm64-darwin.gem
│                   │   ├── terminal-table-3.0.2.gem
│                   │   ├── unicode-display_width-2.6.0.gem
│                   │   └── webrick-1.9.2.gem
│                   ├── doc/
│                   ├── extensions/
│                   │   └── universal-darwin-25/
│                   │       └── 2.6.0/
│                   │           ├── eventmachine-1.2.7/
│                   │           │   ├── fastfilereaderext.bundle
│                   │           │   ├── gem.build_complete
│                   │           │   ├── gem_make.out
│                   │           │   ├── mkmf.log
│                   │           │   └── rubyeventmachine.bundle
│                   │           ├── ffi-1.17.3/
│                   │           │   ├── ffi_c.bundle
│                   │           │   ├── gem.build_complete
│                   │           │   ├── gem_make.out
│                   │           │   └── mkmf.log
│                   │           └── http_parser.rb-0.8.1/
│                   │               ├── gem.build_complete
│                   │               ├── gem_make.out
│                   │               └── ruby_http_parser.bundle
│                   ├── gems/
│                   │   ├── addressable-2.8.9/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   └── lib/
│                   │   │       ├── addressable/
│                   │   │       │   ├── idna/
│                   │   │       │   │   ├── native.rb
│                   │   │       │   │   └── pure.rb
│                   │   │       │   ├── idna.rb
│                   │   │       │   ├── template.rb
│                   │   │       │   ├── uri.rb
│                   │   │       │   └── version.rb
│                   │   │       └── addressable.rb
│                   │   ├── colorator-1.1.0/
│                   │   │   ├── Gemfile
│                   │   │   ├── History.markdown
│                   │   │   ├── LICENSE
│                   │   │   ├── README.markdown
│                   │   │   ├── Rakefile
│                   │   │   ├── colorator.gemspec
│                   │   │   └── lib/
│                   │   │       ├── colorator/
│                   │   │       │   └── core_ext.rb
│                   │   │       └── colorator.rb
│                   │   ├── concurrent-ruby-1.3.6/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── ext/
│                   │   │   │   └── concurrent-ruby/
│                   │   │   │       ├── ConcurrentRubyService.java
│                   │   │   │       └── com/
│                   │   │   │           └── concurrent_ruby/
│                   │   │   │               └── ext/
│                   │   │   │                   ├── AtomicReferenceLibrary.java
│                   │   │   │                   ├── JRubyMapBackendLibrary.java
│                   │   │   │                   ├── JavaAtomicBooleanLibrary.java
│                   │   │   │                   ├── JavaAtomicFixnumLibrary.java
│                   │   │   │                   ├── JavaSemaphoreLibrary.java
│                   │   │   │                   ├── SynchronizationLibrary.java
│                   │   │   │                   ├── jsr166e/
│                   │   │   │                   │   ├── ConcurrentHashMap.java
│                   │   │   │                   │   ├── ConcurrentHashMapV8.java
│                   │   │   │                   │   ├── LongAdder.java
│                   │   │   │                   │   ├── Striped64.java
│                   │   │   │                   │   └── nounsafe/
│                   │   │   │                   │       ├── ConcurrentHashMapV8.java
│                   │   │   │                   │       ├── LongAdder.java
│                   │   │   │                   │       └── Striped64.java
│                   │   │   │                   └── jsr166y/
│                   │   │   │                       └── ThreadLocalRandom.java
│                   │   │   └── lib/
│                   │   │       └── concurrent-ruby/
│                   │   │           ├── concurrent/
│                   │   │           │   ├── agent.rb
│                   │   │           │   ├── array.rb
│                   │   │           │   ├── async.rb
│                   │   │           │   ├── atom.rb
│                   │   │           │   ├── atomic/
│                   │   │           │   │   ├── atomic_boolean.rb
│                   │   │           │   │   ├── atomic_fixnum.rb
│                   │   │           │   │   ├── atomic_markable_reference.rb
│                   │   │           │   │   ├── atomic_reference.rb
│                   │   │           │   │   ├── count_down_latch.rb
│                   │   │           │   │   ├── cyclic_barrier.rb
│                   │   │           │   │   ├── event.rb
│                   │   │           │   │   ├── fiber_local_var.rb
│                   │   │           │   │   ├── java_count_down_latch.rb
│                   │   │           │   │   ├── locals.rb
│                   │   │           │   │   ├── lock_local_var.rb
│                   │   │           │   │   ├── mutex_atomic_boolean.rb
│                   │   │           │   │   ├── mutex_atomic_fixnum.rb
│                   │   │           │   │   ├── mutex_count_down_latch.rb
│                   │   │           │   │   ├── mutex_semaphore.rb
│                   │   │           │   │   ├── read_write_lock.rb
│                   │   │           │   │   ├── reentrant_read_write_lock.rb
│                   │   │           │   │   ├── semaphore.rb
│                   │   │           │   │   └── thread_local_var.rb
│                   │   │           │   ├── atomic_reference/
│                   │   │           │   │   ├── atomic_direct_update.rb
│                   │   │           │   │   ├── mutex_atomic.rb
│                   │   │           │   │   └── numeric_cas_wrapper.rb
│                   │   │           │   ├── atomics.rb
│                   │   │           │   ├── collection/
│                   │   │           │   │   ├── copy_on_notify_observer_set.rb
│                   │   │           │   │   ├── copy_on_write_observer_set.rb
│                   │   │           │   │   ├── java_non_concurrent_priority_queue.rb
│                   │   │           │   │   ├── lock_free_stack.rb
│                   │   │           │   │   ├── map/
│                   │   │           │   │   │   ├── mri_map_backend.rb
│                   │   │           │   │   │   ├── non_concurrent_map_backend.rb
│                   │   │           │   │   │   ├── synchronized_map_backend.rb
│                   │   │           │   │   │   └── truffleruby_map_backend.rb
│                   │   │           │   │   ├── non_concurrent_priority_queue.rb
│                   │   │           │   │   ├── ruby_non_concurrent_priority_queue.rb
│                   │   │           │   │   ├── ruby_timeout_queue.rb
│                   │   │           │   │   └── timeout_queue.rb
│                   │   │           │   ├── concern/
│                   │   │           │   │   ├── deprecation.rb
│                   │   │           │   │   ├── dereferenceable.rb
│                   │   │           │   │   ├── logging.rb
│                   │   │           │   │   ├── obligation.rb
│                   │   │           │   │   └── observable.rb
│                   │   │           │   ├── concurrent_ruby.jar
│                   │   │           │   ├── configuration.rb
│                   │   │           │   ├── constants.rb
│                   │   │           │   ├── dataflow.rb
│                   │   │           │   ├── delay.rb
│                   │   │           │   ├── errors.rb
│                   │   │           │   ├── exchanger.rb
│                   │   │           │   ├── executor/
│                   │   │           │   │   ├── abstract_executor_service.rb
│                   │   │           │   │   ├── cached_thread_pool.rb
│                   │   │           │   │   ├── executor_service.rb
│                   │   │           │   │   ├── fixed_thread_pool.rb
│                   │   │           │   │   ├── immediate_executor.rb
│                   │   │           │   │   ├── indirect_immediate_executor.rb
│                   │   │           │   │   ├── java_executor_service.rb
│                   │   │           │   │   ├── java_single_thread_executor.rb
│                   │   │           │   │   ├── java_thread_pool_executor.rb
│                   │   │           │   │   ├── ruby_executor_service.rb
│                   │   │           │   │   ├── ruby_single_thread_executor.rb
│                   │   │           │   │   ├── ruby_thread_pool_executor.rb
│                   │   │           │   │   ├── safe_task_executor.rb
│                   │   │           │   │   ├── serial_executor_service.rb
│                   │   │           │   │   ├── serialized_execution.rb
│                   │   │           │   │   ├── serialized_execution_delegator.rb
│                   │   │           │   │   ├── simple_executor_service.rb
│                   │   │           │   │   ├── single_thread_executor.rb
│                   │   │           │   │   ├── thread_pool_executor.rb
│                   │   │           │   │   └── timer_set.rb
│                   │   │           │   ├── executors.rb
│                   │   │           │   ├── future.rb
│                   │   │           │   ├── hash.rb
│                   │   │           │   ├── immutable_struct.rb
│                   │   │           │   ├── ivar.rb
│                   │   │           │   ├── map.rb
│                   │   │           │   ├── maybe.rb
│                   │   │           │   ├── mutable_struct.rb
│                   │   │           │   ├── mvar.rb
│                   │   │           │   ├── options.rb
│                   │   │           │   ├── promise.rb
│                   │   │           │   ├── promises.rb
│                   │   │           │   ├── re_include.rb
│                   │   │           │   ├── scheduled_task.rb
│                   │   │           │   ├── set.rb
│                   │   │           │   ├── settable_struct.rb
│                   │   │           │   ├── synchronization/
│                   │   │           │   │   ├── abstract_lockable_object.rb
│                   │   │           │   │   ├── abstract_object.rb
│                   │   │           │   │   ├── abstract_struct.rb
│                   │   │           │   │   ├── condition.rb
│                   │   │           │   │   ├── full_memory_barrier.rb
│                   │   │           │   │   ├── jruby_lockable_object.rb
│                   │   │           │   │   ├── lock.rb
│                   │   │           │   │   ├── lockable_object.rb
│                   │   │           │   │   ├── mutex_lockable_object.rb
│                   │   │           │   │   ├── object.rb
│                   │   │           │   │   ├── safe_initialization.rb
│                   │   │           │   │   └── volatile.rb
│                   │   │           │   ├── synchronization.rb
│                   │   │           │   ├── thread_safe/
│                   │   │           │   │   ├── synchronized_delegator.rb
│                   │   │           │   │   ├── util/
│                   │   │           │   │   │   ├── adder.rb
│                   │   │           │   │   │   ├── data_structures.rb
│                   │   │           │   │   │   ├── power_of_two_tuple.rb
│                   │   │           │   │   │   ├── striped64.rb
│                   │   │           │   │   │   ├── volatile.rb
│                   │   │           │   │   │   └── xor_shift_random.rb
│                   │   │           │   │   └── util.rb
│                   │   │           │   ├── timer_task.rb
│                   │   │           │   ├── tuple.rb
│                   │   │           │   ├── tvar.rb
│                   │   │           │   ├── utility/
│                   │   │           │   │   ├── engine.rb
│                   │   │           │   │   ├── monotonic_time.rb
│                   │   │           │   │   ├── native_extension_loader.rb
│                   │   │           │   │   ├── native_integer.rb
│                   │   │           │   │   └── processor_counter.rb
│                   │   │           │   └── version.rb
│                   │   │           ├── concurrent-ruby.rb
│                   │   │           └── concurrent.rb
│                   │   ├── em-websocket-0.5.3/
│                   │   │   ├── .gitignore
│                   │   │   ├── CHANGELOG.rdoc
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENCE
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── em-websocket.gemspec
│                   │   │   ├── examples/
│                   │   │   │   ├── echo.rb
│                   │   │   │   ├── multicast.rb
│                   │   │   │   ├── ping.rb
│                   │   │   │   └── test.html
│                   │   │   ├── lib/
│                   │   │   │   ├── em-websocket/
│                   │   │   │   │   ├── close03.rb
│                   │   │   │   │   ├── close05.rb
│                   │   │   │   │   ├── close06.rb
│                   │   │   │   │   ├── close75.rb
│                   │   │   │   │   ├── connection.rb
│                   │   │   │   │   ├── debugger.rb
│                   │   │   │   │   ├── framing03.rb
│                   │   │   │   │   ├── framing04.rb
│                   │   │   │   │   ├── framing05.rb
│                   │   │   │   │   ├── framing07.rb
│                   │   │   │   │   ├── framing76.rb
│                   │   │   │   │   ├── handler.rb
│                   │   │   │   │   ├── handler03.rb
│                   │   │   │   │   ├── handler05.rb
│                   │   │   │   │   ├── handler06.rb
│                   │   │   │   │   ├── handler07.rb
│                   │   │   │   │   ├── handler08.rb
│                   │   │   │   │   ├── handler13.rb
│                   │   │   │   │   ├── handler75.rb
│                   │   │   │   │   ├── handler76.rb
│                   │   │   │   │   ├── handshake.rb
│                   │   │   │   │   ├── handshake04.rb
│                   │   │   │   │   ├── handshake75.rb
│                   │   │   │   │   ├── handshake76.rb
│                   │   │   │   │   ├── masking04.rb
│                   │   │   │   │   ├── message_processor_03.rb
│                   │   │   │   │   ├── message_processor_06.rb
│                   │   │   │   │   ├── version.rb
│                   │   │   │   │   └── websocket.rb
│                   │   │   │   └── em-websocket.rb
│                   │   │   └── spec/
│                   │   │       ├── helper.rb
│                   │   │       ├── integration/
│                   │   │       │   ├── common_spec.rb
│                   │   │       │   ├── draft03_spec.rb
│                   │   │       │   ├── draft05_spec.rb
│                   │   │       │   ├── draft06_spec.rb
│                   │   │       │   ├── draft13_spec.rb
│                   │   │       │   ├── draft75_spec.rb
│                   │   │       │   ├── draft76_spec.rb
│                   │   │       │   ├── gte_03_examples.rb
│                   │   │       │   └── shared_examples.rb
│                   │   │       └── unit/
│                   │   │           ├── framing_spec.rb
│                   │   │           ├── handshake_spec.rb
│                   │   │           └── masking_spec.rb
│                   │   ├── eventmachine-1.2.7/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── GNU
│                   │   │   ├── LICENSE
│                   │   │   ├── README.md
│                   │   │   ├── docs/
│                   │   │   │   ├── DocumentationGuidesIndex.md
│                   │   │   │   ├── GettingStarted.md
│                   │   │   │   └── old/
│                   │   │   │       ├── ChangeLog
│                   │   │   │       ├── DEFERRABLES
│                   │   │   │       ├── EPOLL
│                   │   │   │       ├── INSTALL
│                   │   │   │       ├── KEYBOARD
│                   │   │   │       ├── LEGAL
│                   │   │   │       ├── LIGHTWEIGHT_CONCURRENCY
│                   │   │   │       ├── PURE_RUBY
│                   │   │   │       ├── RELEASE_NOTES
│                   │   │   │       ├── SMTP
│                   │   │   │       ├── SPAWNED_PROCESSES
│                   │   │   │       └── TODO
│                   │   │   ├── examples/
│                   │   │   │   ├── guides/
│                   │   │   │   │   └── getting_started/
│                   │   │   │   │       ├── 01_eventmachine_echo_server.rb
│                   │   │   │   │       ├── 02_eventmachine_echo_server_that_recognizes_exit_command.rb
│                   │   │   │   │       ├── 03_simple_chat_server.rb
│                   │   │   │   │       ├── 04_simple_chat_server_step_one.rb
│                   │   │   │   │       ├── 05_simple_chat_server_step_two.rb
│                   │   │   │   │       ├── 06_simple_chat_server_step_three.rb
│                   │   │   │   │       ├── 07_simple_chat_server_step_four.rb
│                   │   │   │   │       └── 08_simple_chat_server_step_five.rb
│                   │   │   │   └── old/
│                   │   │   │       ├── ex_channel.rb
│                   │   │   │       ├── ex_queue.rb
│                   │   │   │       ├── ex_tick_loop_array.rb
│                   │   │   │       ├── ex_tick_loop_counter.rb
│                   │   │   │       └── helper.rb
│                   │   │   ├── ext/
│                   │   │   │   ├── .sitearchdir.time
│                   │   │   │   ├── Makefile
│                   │   │   │   ├── binder.cpp
│                   │   │   │   ├── binder.h
│                   │   │   │   ├── binder.o
│                   │   │   │   ├── cmain.cpp
│                   │   │   │   ├── cmain.o
│                   │   │   │   ├── ed.cpp
│                   │   │   │   ├── ed.h
│                   │   │   │   ├── ed.o
│                   │   │   │   ├── em.cpp
│                   │   │   │   ├── em.h
│                   │   │   │   ├── em.o
│                   │   │   │   ├── eventmachine.h
│                   │   │   │   ├── extconf.rb
│                   │   │   │   ├── fastfilereader/
│                   │   │   │   │   ├── .sitearchdir.time
│                   │   │   │   │   ├── Makefile
│                   │   │   │   │   ├── extconf.rb
│                   │   │   │   │   ├── fastfilereaderext.bundle
│                   │   │   │   │   ├── mapper.cpp
│                   │   │   │   │   ├── mapper.h
│                   │   │   │   │   ├── mapper.o
│                   │   │   │   │   ├── rubymain.cpp
│                   │   │   │   │   └── rubymain.o
│                   │   │   │   ├── kb.cpp
│                   │   │   │   ├── kb.o
│                   │   │   │   ├── page.cpp
│                   │   │   │   ├── page.h
│                   │   │   │   ├── page.o
│                   │   │   │   ├── pipe.cpp
│                   │   │   │   ├── pipe.o
│                   │   │   │   ├── project.h
│                   │   │   │   ├── rubyeventmachine.bundle
│                   │   │   │   ├── rubymain.cpp
│                   │   │   │   ├── rubymain.o
│                   │   │   │   ├── ssl.cpp
│                   │   │   │   ├── ssl.h
│                   │   │   │   └── ssl.o
│                   │   │   ├── java/
│                   │   │   │   ├── .classpath
│                   │   │   │   ├── .project
│                   │   │   │   └── src/
│                   │   │   │       └── com/
│                   │   │   │           └── rubyeventmachine/
│                   │   │   │               ├── EmReactor.java
│                   │   │   │               ├── EmReactorException.java
│                   │   │   │               ├── EventableChannel.java
│                   │   │   │               ├── EventableDatagramChannel.java
│                   │   │   │               └── EventableSocketChannel.java
│                   │   │   ├── lib/
│                   │   │   │   ├── em/
│                   │   │   │   │   ├── buftok.rb
│                   │   │   │   │   ├── callback.rb
│                   │   │   │   │   ├── channel.rb
│                   │   │   │   │   ├── completion.rb
│                   │   │   │   │   ├── connection.rb
│                   │   │   │   │   ├── deferrable/
│                   │   │   │   │   │   └── pool.rb
│                   │   │   │   │   ├── deferrable.rb
│                   │   │   │   │   ├── file_watch.rb
│                   │   │   │   │   ├── future.rb
│                   │   │   │   │   ├── iterator.rb
│                   │   │   │   │   ├── messages.rb
│                   │   │   │   │   ├── pool.rb
│                   │   │   │   │   ├── process_watch.rb
│                   │   │   │   │   ├── processes.rb
│                   │   │   │   │   ├── protocols/
│                   │   │   │   │   │   ├── header_and_content.rb
│                   │   │   │   │   │   ├── httpclient.rb
│                   │   │   │   │   │   ├── httpclient2.rb
│                   │   │   │   │   │   ├── line_and_text.rb
│                   │   │   │   │   │   ├── line_protocol.rb
│                   │   │   │   │   │   ├── linetext2.rb
│                   │   │   │   │   │   ├── memcache.rb
│                   │   │   │   │   │   ├── object_protocol.rb
│                   │   │   │   │   │   ├── postgres3.rb
│                   │   │   │   │   │   ├── saslauth.rb
│                   │   │   │   │   │   ├── smtpclient.rb
│                   │   │   │   │   │   ├── smtpserver.rb
│                   │   │   │   │   │   ├── socks4.rb
│                   │   │   │   │   │   ├── stomp.rb
│                   │   │   │   │   │   └── tcptest.rb
│                   │   │   │   │   ├── protocols.rb
│                   │   │   │   │   ├── pure_ruby.rb
│                   │   │   │   │   ├── queue.rb
│                   │   │   │   │   ├── resolver.rb
│                   │   │   │   │   ├── spawnable.rb
│                   │   │   │   │   ├── streamer.rb
│                   │   │   │   │   ├── threaded_resource.rb
│                   │   │   │   │   ├── tick_loop.rb
│                   │   │   │   │   ├── timers.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   ├── eventmachine.rb
│                   │   │   │   ├── fastfilereaderext.bundle
│                   │   │   │   ├── jeventmachine.rb
│                   │   │   │   └── rubyeventmachine.bundle
│                   │   │   ├── rakelib/
│                   │   │   │   ├── package.rake
│                   │   │   │   ├── test.rake
│                   │   │   │   └── test_pure.rake
│                   │   │   └── tests/
│                   │   │       ├── client.crt
│                   │   │       ├── client.key
│                   │   │       ├── dhparam.pem
│                   │   │       ├── em_test_helper.rb
│                   │   │       ├── test_attach.rb
│                   │   │       ├── test_basic.rb
│                   │   │       ├── test_channel.rb
│                   │   │       ├── test_completion.rb
│                   │   │       ├── test_connection_count.rb
│                   │   │       ├── test_connection_write.rb
│                   │   │       ├── test_defer.rb
│                   │   │       ├── test_deferrable.rb
│                   │   │       ├── test_epoll.rb
│                   │   │       ├── test_error_handler.rb
│                   │   │       ├── test_exc.rb
│                   │   │       ├── test_file_watch.rb
│                   │   │       ├── test_fork.rb
│                   │   │       ├── test_futures.rb
│                   │   │       ├── test_handler_check.rb
│                   │   │       ├── test_hc.rb
│                   │   │       ├── test_httpclient.rb
│                   │   │       ├── test_httpclient2.rb
│                   │   │       ├── test_idle_connection.rb
│                   │   │       ├── test_inactivity_timeout.rb
│                   │   │       ├── test_ipv4.rb
│                   │   │       ├── test_ipv6.rb
│                   │   │       ├── test_iterator.rb
│                   │   │       ├── test_kb.rb
│                   │   │       ├── test_line_protocol.rb
│                   │   │       ├── test_ltp.rb
│                   │   │       ├── test_ltp2.rb
│                   │   │       ├── test_many_fds.rb
│                   │   │       ├── test_next_tick.rb
│                   │   │       ├── test_object_protocol.rb
│                   │   │       ├── test_pause.rb
│                   │   │       ├── test_pending_connect_timeout.rb
│                   │   │       ├── test_pool.rb
│                   │   │       ├── test_process_watch.rb
│                   │   │       ├── test_processes.rb
│                   │   │       ├── test_proxy_connection.rb
│                   │   │       ├── test_pure.rb
│                   │   │       ├── test_queue.rb
│                   │   │       ├── test_resolver.rb
│                   │   │       ├── test_running.rb
│                   │   │       ├── test_sasl.rb
│                   │   │       ├── test_send_file.rb
│                   │   │       ├── test_servers.rb
│                   │   │       ├── test_shutdown_hooks.rb
│                   │   │       ├── test_smtpclient.rb
│                   │   │       ├── test_smtpserver.rb
│                   │   │       ├── test_sock_opt.rb
│                   │   │       ├── test_spawn.rb
│                   │   │       ├── test_ssl_args.rb
│                   │   │       ├── test_ssl_dhparam.rb
│                   │   │       ├── test_ssl_ecdh_curve.rb
│                   │   │       ├── test_ssl_extensions.rb
│                   │   │       ├── test_ssl_methods.rb
│                   │   │       ├── test_ssl_protocols.rb
│                   │   │       ├── test_ssl_verify.rb
│                   │   │       ├── test_stomp.rb
│                   │   │       ├── test_system.rb
│                   │   │       ├── test_threaded_resource.rb
│                   │   │       ├── test_tick_loop.rb
│                   │   │       ├── test_timers.rb
│                   │   │       ├── test_ud.rb
│                   │   │       └── test_unbind_reason.rb
│                   │   ├── ffi-1.17.3/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── COPYING
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE
│                   │   │   ├── LICENSE.SPECS
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── Steepfile
│                   │   │   ├── ext/
│                   │   │   │   └── ffi_c/
│                   │   │   │       ├── .sitearchdir.time
│                   │   │   │       ├── AbstractMemory.c
│                   │   │   │       ├── AbstractMemory.h
│                   │   │   │       ├── AbstractMemory.o
│                   │   │   │       ├── ArrayType.c
│                   │   │   │       ├── ArrayType.h
│                   │   │   │       ├── ArrayType.o
│                   │   │   │       ├── Buffer.c
│                   │   │   │       ├── Buffer.o
│                   │   │   │       ├── Call.c
│                   │   │   │       ├── Call.h
│                   │   │   │       ├── Call.o
│                   │   │   │       ├── ClosurePool.c
│                   │   │   │       ├── ClosurePool.h
│                   │   │   │       ├── ClosurePool.o
│                   │   │   │       ├── DynamicLibrary.c
│                   │   │   │       ├── DynamicLibrary.h
│                   │   │   │       ├── DynamicLibrary.o
│                   │   │   │       ├── Function.c
│                   │   │   │       ├── Function.h
│                   │   │   │       ├── Function.o
│                   │   │   │       ├── FunctionInfo.c
│                   │   │   │       ├── FunctionInfo.o
│                   │   │   │       ├── LastError.c
│                   │   │   │       ├── LastError.h
│                   │   │   │       ├── LastError.o
│                   │   │   │       ├── LongDouble.c
│                   │   │   │       ├── LongDouble.h
│                   │   │   │       ├── LongDouble.o
│                   │   │   │       ├── Makefile
│                   │   │   │       ├── MappedType.c
│                   │   │   │       ├── MappedType.h
│                   │   │   │       ├── MappedType.o
│                   │   │   │       ├── MemoryPointer.c
│                   │   │   │       ├── MemoryPointer.h
│                   │   │   │       ├── MemoryPointer.o
│                   │   │   │       ├── MethodHandle.c
│                   │   │   │       ├── MethodHandle.h
│                   │   │   │       ├── MethodHandle.o
│                   │   │   │       ├── Platform.c
│                   │   │   │       ├── Platform.h
│                   │   │   │       ├── Platform.o
│                   │   │   │       ├── Pointer.c
│                   │   │   │       ├── Pointer.h
│                   │   │   │       ├── Pointer.o
│                   │   │   │       ├── Struct.c
│                   │   │   │       ├── Struct.h
│                   │   │   │       ├── Struct.o
│                   │   │   │       ├── StructByValue.c
│                   │   │   │       ├── StructByValue.h
│                   │   │   │       ├── StructByValue.o
│                   │   │   │       ├── StructLayout.c
│                   │   │   │       ├── StructLayout.o
│                   │   │   │       ├── Thread.c
│                   │   │   │       ├── Thread.h
│                   │   │   │       ├── Thread.o
│                   │   │   │       ├── Type.c
│                   │   │   │       ├── Type.h
│                   │   │   │       ├── Type.o
│                   │   │   │       ├── Types.c
│                   │   │   │       ├── Types.h
│                   │   │   │       ├── Types.o
│                   │   │   │       ├── Variadic.c
│                   │   │   │       ├── Variadic.o
│                   │   │   │       ├── compat.h
│                   │   │   │       ├── extconf.h
│                   │   │   │       ├── extconf.rb
│                   │   │   │       ├── ffi.c
│                   │   │   │       ├── ffi.o
│                   │   │   │       ├── ffi_c.bundle
│                   │   │   │       ├── libffi/
│                   │   │   │       │   ├── .allow-ai-service
│                   │   │   │       │   ├── .ci/
│                   │   │   │       │   │   ├── Containerfile.ppc64le
│                   │   │   │       │   │   ├── ar-lib
│                   │   │   │       │   │   ├── bfin-sim.exp
│                   │   │   │       │   │   ├── build-cross-in-container.sh
│                   │   │   │       │   │   ├── build-in-container.sh
│                   │   │   │       │   │   ├── build.sh
│                   │   │   │       │   │   ├── compile
│                   │   │   │       │   │   ├── install.sh
│                   │   │   │       │   │   ├── m32r-sim.exp
│                   │   │   │       │   │   ├── moxie-sim.exp
│                   │   │   │       │   │   ├── msvs-detect
│                   │   │   │       │   │   ├── or1k-sim.exp
│                   │   │   │       │   │   ├── powerpc-eabisim.exp
│                   │   │   │       │   │   ├── site.exp
│                   │   │   │       │   │   ├── unix-noexec.exp
│                   │   │   │       │   │   └── wine-sim.exp
│                   │   │   │       │   ├── .gail-labels
│                   │   │   │       │   ├── .gitattributes
│                   │   │   │       │   ├── .github/
│                   │   │   │       │   │   ├── issue_template.md
│                   │   │   │       │   │   └── workflows/
│                   │   │   │       │   │       ├── build.yml
│                   │   │   │       │   │       ├── emscripten.yml
│                   │   │   │       │   │       ├── label-new-issue.yaml
│                   │   │   │       │   │       └── tarball.yml
│                   │   │   │       │   ├── .gitignore
│                   │   │   │       │   ├── ChangeLog.old
│                   │   │   │       │   ├── LICENSE
│                   │   │   │       │   ├── LICENSE-BUILDTOOLS
│                   │   │   │       │   ├── Makefile.am
│                   │   │   │       │   ├── Makefile.in
│                   │   │   │       │   ├── README.md
│                   │   │   │       │   ├── acinclude.m4
│                   │   │   │       │   ├── autogen.sh
│                   │   │   │       │   ├── compile
│                   │   │   │       │   ├── config.guess
│                   │   │   │       │   ├── config.sub
│                   │   │   │       │   ├── configure
│                   │   │   │       │   ├── configure.ac
│                   │   │   │       │   ├── configure.host
│                   │   │   │       │   ├── doc/
│                   │   │   │       │   │   ├── Makefile.am
│                   │   │   │       │   │   ├── Makefile.in
│                   │   │   │       │   │   ├── libffi.texi
│                   │   │   │       │   │   └── version.texi
│                   │   │   │       │   ├── fficonfig.h.in
│                   │   │   │       │   ├── generate-darwin-source-and-headers.py
│                   │   │   │       │   ├── include/
│                   │   │   │       │   │   ├── Makefile.am
│                   │   │   │       │   │   ├── Makefile.in
│                   │   │   │       │   │   ├── ffi.h.in
│                   │   │   │       │   │   ├── ffi_cfi.h
│                   │   │   │       │   │   ├── ffi_common.h
│                   │   │   │       │   │   └── tramp.h
│                   │   │   │       │   ├── install-sh
│                   │   │   │       │   ├── libffi.map.in
│                   │   │   │       │   ├── libffi.pc.in
│                   │   │   │       │   ├── libffi.xcodeproj/
│                   │   │   │       │   │   └── project.pbxproj
│                   │   │   │       │   ├── libtool-ldflags
│                   │   │   │       │   ├── libtool-version
│                   │   │   │       │   ├── ltmain.sh
│                   │   │   │       │   ├── m4/
│                   │   │   │       │   │   ├── asmcfi.m4
│                   │   │   │       │   │   ├── ax_append_flag.m4
│                   │   │   │       │   │   ├── ax_cc_maxopt.m4
│                   │   │   │       │   │   ├── ax_cflags_warn_all.m4
│                   │   │   │       │   │   ├── ax_check_compile_flag.m4
│                   │   │   │       │   │   ├── ax_compiler_vendor.m4
│                   │   │   │       │   │   ├── ax_configure_args.m4
│                   │   │   │       │   │   ├── ax_enable_builddir.m4
│                   │   │   │       │   │   ├── ax_gcc_archflag.m4
│                   │   │   │       │   │   ├── ax_gcc_x86_cpuid.m4
│                   │   │   │       │   │   ├── ax_prepend_flag.m4
│                   │   │   │       │   │   └── ax_require_defined.m4
│                   │   │   │       │   ├── make_sunver.pl
│                   │   │   │       │   ├── man/
│                   │   │   │       │   │   ├── Makefile.am
│                   │   │   │       │   │   ├── Makefile.in
│                   │   │   │       │   │   ├── ffi.3
│                   │   │   │       │   │   ├── ffi_call.3
│                   │   │   │       │   │   ├── ffi_prep_cif.3
│                   │   │   │       │   │   └── ffi_prep_cif_var.3
│                   │   │   │       │   ├── missing
│                   │   │   │       │   ├── msvc_build/
│                   │   │   │       │   │   └── aarch64/
│                   │   │   │       │   │       ├── Ffi_staticLib.sln
│                   │   │   │       │   │       ├── Ffi_staticLib.vcxproj
│                   │   │   │       │   │       ├── Ffi_staticLib.vcxproj.filters
│                   │   │   │       │   │       ├── Ffi_staticLib.vcxproj.user
│                   │   │   │       │   │       └── aarch64_include/
│                   │   │   │       │   │           ├── ffi.h
│                   │   │   │       │   │           └── fficonfig.h
│                   │   │   │       │   ├── msvcc.sh
│                   │   │   │       │   ├── src/
│                   │   │   │       │   │   ├── aarch64/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   ├── sysv.S
│                   │   │   │       │   │   │   └── win64_armasm.S
│                   │   │   │       │   │   ├── alpha/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   └── osf.S
│                   │   │   │       │   │   ├── arc/
│                   │   │   │       │   │   │   ├── arcompact.S
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   └── ffitarget.h
│                   │   │   │       │   │   ├── arm/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   ├── sysv.S
│                   │   │   │       │   │   │   └── sysv_msvc_arm32.S
│                   │   │   │       │   │   ├── avr32/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── bfin/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── closures.c
│                   │   │   │       │   │   ├── cris/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── csky/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── debug.c
│                   │   │   │       │   │   ├── dlmalloc.c
│                   │   │   │       │   │   ├── frv/
│                   │   │   │       │   │   │   ├── eabi.S
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   └── ffitarget.h
│                   │   │   │       │   │   ├── ia64/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── ia64_flags.h
│                   │   │   │       │   │   │   └── unix.S
│                   │   │   │       │   │   ├── java_raw_api.c
│                   │   │   │       │   │   ├── kvx/
│                   │   │   │       │   │   │   ├── asm.h
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── loongarch64/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── m32r/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── m68k/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── m88k/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── obsd.S
│                   │   │   │       │   │   ├── metag/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── microblaze/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── mips/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── n32.S
│                   │   │   │       │   │   │   └── o32.S
│                   │   │   │       │   │   ├── moxie/
│                   │   │   │       │   │   │   ├── eabi.S
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   └── ffitarget.h
│                   │   │   │       │   │   ├── or1k/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── pa/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffi64.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── hpux32.S
│                   │   │   │       │   │   │   ├── hpux64.S
│                   │   │   │       │   │   │   └── linux.S
│                   │   │   │       │   │   ├── powerpc/
│                   │   │   │       │   │   │   ├── aix.S
│                   │   │   │       │   │   │   ├── aix_closure.S
│                   │   │   │       │   │   │   ├── asm.h
│                   │   │   │       │   │   │   ├── darwin.S
│                   │   │   │       │   │   │   ├── darwin_closure.S
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffi_darwin.c
│                   │   │   │       │   │   │   ├── ffi_linux64.c
│                   │   │   │       │   │   │   ├── ffi_powerpc.h
│                   │   │   │       │   │   │   ├── ffi_sysv.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   ├── linux64.S
│                   │   │   │       │   │   │   ├── linux64_closure.S
│                   │   │   │       │   │   │   ├── ppc_closure.S
│                   │   │   │       │   │   │   ├── sysv.S
│                   │   │   │       │   │   │   └── t-aix
│                   │   │   │       │   │   ├── prep_cif.c
│                   │   │   │       │   │   ├── raw_api.c
│                   │   │   │       │   │   ├── riscv/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── s390/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── sh/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── sh64/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── sysv.S
│                   │   │   │       │   │   ├── sparc/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffi64.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   ├── v8.S
│                   │   │   │       │   │   │   └── v9.S
│                   │   │   │       │   │   ├── tile/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   └── tile.S
│                   │   │   │       │   │   ├── tramp.c
│                   │   │   │       │   │   ├── types.c
│                   │   │   │       │   │   ├── vax/
│                   │   │   │       │   │   │   ├── elfbsd.S
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   └── ffitarget.h
│                   │   │   │       │   │   ├── wasm/
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   └── ffitarget.h
│                   │   │   │       │   │   ├── x86/
│                   │   │   │       │   │   │   ├── asmnames.h
│                   │   │   │       │   │   │   ├── ffi.c
│                   │   │   │       │   │   │   ├── ffi64.c
│                   │   │   │       │   │   │   ├── ffitarget.h
│                   │   │   │       │   │   │   ├── ffiw64.c
│                   │   │   │       │   │   │   ├── internal.h
│                   │   │   │       │   │   │   ├── internal64.h
│                   │   │   │       │   │   │   ├── sysv.S
│                   │   │   │       │   │   │   ├── sysv_intel.S
│                   │   │   │       │   │   │   ├── unix64.S
│                   │   │   │       │   │   │   ├── win64.S
│                   │   │   │       │   │   │   └── win64_intel.S
│                   │   │   │       │   │   └── xtensa/
│                   │   │   │       │   │       ├── ffi.c
│                   │   │   │       │   │       ├── ffitarget.h
│                   │   │   │       │   │       └── sysv.S
│                   │   │   │       │   ├── stamp-h.in
│                   │   │   │       │   └── testsuite/
│                   │   │   │       │       ├── Makefile.am
│                   │   │   │       │       ├── Makefile.in
│                   │   │   │       │       ├── config/
│                   │   │   │       │       │   └── default.exp
│                   │   │   │       │       ├── emscripten/
│                   │   │   │       │       │   ├── build-tests.sh
│                   │   │   │       │       │   ├── build.sh
│                   │   │   │       │       │   ├── conftest.py
│                   │   │   │       │       │   ├── node-tests.sh
│                   │   │   │       │       │   ├── test.html
│                   │   │   │       │       │   └── test_libffi.py
│                   │   │   │       │       ├── lib/
│                   │   │   │       │       │   ├── libffi.exp
│                   │   │   │       │       │   ├── target-libpath.exp
│                   │   │   │       │       │   └── wrapper.exp
│                   │   │   │       │       ├── libffi.bhaible/
│                   │   │   │       │       │   ├── Makefile
│                   │   │   │       │       │   ├── README
│                   │   │   │       │       │   ├── alignof.h
│                   │   │   │       │       │   ├── bhaible.exp
│                   │   │   │       │       │   ├── test-call.c
│                   │   │   │       │       │   ├── test-callback.c
│                   │   │   │       │       │   └── testcases.c
│                   │   │   │       │       ├── libffi.call/
│                   │   │   │       │       │   ├── align_mixed.c
│                   │   │   │       │       │   ├── align_stdcall.c
│                   │   │   │       │       │   ├── bpo_38748.c
│                   │   │   │       │       │   ├── call.exp
│                   │   │   │       │       │   ├── callback.c
│                   │   │   │       │       │   ├── callback2.c
│                   │   │   │       │       │   ├── callback3.c
│                   │   │   │       │       │   ├── callback4.c
│                   │   │   │       │       │   ├── err_bad_typedef.c
│                   │   │   │       │       │   ├── ffitest.h
│                   │   │   │       │       │   ├── float.c
│                   │   │   │       │       │   ├── float1.c
│                   │   │   │       │       │   ├── float2.c
│                   │   │   │       │       │   ├── float3.c
│                   │   │   │       │       │   ├── float4.c
│                   │   │   │       │       │   ├── float_va.c
│                   │   │   │       │       │   ├── longjmp.c
│                   │   │   │       │       │   ├── many.c
│                   │   │   │       │       │   ├── many2.c
│                   │   │   │       │       │   ├── many_double.c
│                   │   │   │       │       │   ├── many_mixed.c
│                   │   │   │       │       │   ├── negint.c
│                   │   │   │       │       │   ├── offsets.c
│                   │   │   │       │       │   ├── overread.c
│                   │   │   │       │       │   ├── pr1172638.c
│                   │   │   │       │       │   ├── promotion.c
│                   │   │   │       │       │   ├── pyobjc_tc.c
│                   │   │   │       │       │   ├── return_dbl.c
│                   │   │   │       │       │   ├── return_dbl1.c
│                   │   │   │       │       │   ├── return_dbl2.c
│                   │   │   │       │       │   ├── return_fl.c
│                   │   │   │       │       │   ├── return_fl1.c
│                   │   │   │       │       │   ├── return_fl2.c
│                   │   │   │       │       │   ├── return_fl3.c
│                   │   │   │       │       │   ├── return_ldl.c
│                   │   │   │       │       │   ├── return_ll.c
│                   │   │   │       │       │   ├── return_ll1.c
│                   │   │   │       │       │   ├── return_sc.c
│                   │   │   │       │       │   ├── return_sl.c
│                   │   │   │       │       │   ├── return_uc.c
│                   │   │   │       │       │   ├── return_ul.c
│                   │   │   │       │       │   ├── s55.c
│                   │   │   │       │       │   ├── strlen.c
│                   │   │   │       │       │   ├── strlen2.c
│                   │   │   │       │       │   ├── strlen3.c
│                   │   │   │       │       │   ├── strlen4.c
│                   │   │   │       │       │   ├── struct1.c
│                   │   │   │       │       │   ├── struct10.c
│                   │   │   │       │       │   ├── struct2.c
│                   │   │   │       │       │   ├── struct3.c
│                   │   │   │       │       │   ├── struct4.c
│                   │   │   │       │       │   ├── struct5.c
│                   │   │   │       │       │   ├── struct6.c
│                   │   │   │       │       │   ├── struct7.c
│                   │   │   │       │       │   ├── struct8.c
│                   │   │   │       │       │   ├── struct9.c
│                   │   │   │       │       │   ├── struct_by_value_2.c
│                   │   │   │       │       │   ├── struct_by_value_3.c
│                   │   │   │       │       │   ├── struct_by_value_3f.c
│                   │   │   │       │       │   ├── struct_by_value_4.c
│                   │   │   │       │       │   ├── struct_by_value_4f.c
│                   │   │   │       │       │   ├── struct_by_value_big.c
│                   │   │   │       │       │   ├── struct_by_value_small.c
│                   │   │   │       │       │   ├── struct_int_float.c
│                   │   │   │       │       │   ├── struct_return_2H.c
│                   │   │   │       │       │   ├── struct_return_8H.c
│                   │   │   │       │       │   ├── uninitialized.c
│                   │   │   │       │       │   ├── va_1.c
│                   │   │   │       │       │   ├── va_2.c
│                   │   │   │       │       │   ├── va_3.c
│                   │   │   │       │       │   ├── va_struct1.c
│                   │   │   │       │       │   ├── va_struct2.c
│                   │   │   │       │       │   ├── va_struct3.c
│                   │   │   │       │       │   └── x32.c
│                   │   │   │       │       ├── libffi.closures/
│                   │   │   │       │       │   ├── closure.exp
│                   │   │   │       │       │   ├── closure_fn0.c
│                   │   │   │       │       │   ├── closure_fn1.c
│                   │   │   │       │       │   ├── closure_fn2.c
│                   │   │   │       │       │   ├── closure_fn3.c
│                   │   │   │       │       │   ├── closure_fn4.c
│                   │   │   │       │       │   ├── closure_fn5.c
│                   │   │   │       │       │   ├── closure_fn6.c
│                   │   │   │       │       │   ├── closure_loc_fn0.c
│                   │   │   │       │       │   ├── closure_simple.c
│                   │   │   │       │       │   ├── cls_12byte.c
│                   │   │   │       │       │   ├── cls_16byte.c
│                   │   │   │       │       │   ├── cls_18byte.c
│                   │   │   │       │       │   ├── cls_19byte.c
│                   │   │   │       │       │   ├── cls_1_1byte.c
│                   │   │   │       │       │   ├── cls_20byte.c
│                   │   │   │       │       │   ├── cls_20byte1.c
│                   │   │   │       │       │   ├── cls_24byte.c
│                   │   │   │       │       │   ├── cls_2byte.c
│                   │   │   │       │       │   ├── cls_3_1byte.c
│                   │   │   │       │       │   ├── cls_3byte1.c
│                   │   │   │       │       │   ├── cls_3byte2.c
│                   │   │   │       │       │   ├── cls_3float.c
│                   │   │   │       │       │   ├── cls_4_1byte.c
│                   │   │   │       │       │   ├── cls_4byte.c
│                   │   │   │       │       │   ├── cls_5_1_byte.c
│                   │   │   │       │       │   ├── cls_5byte.c
│                   │   │   │       │       │   ├── cls_64byte.c
│                   │   │   │       │       │   ├── cls_6_1_byte.c
│                   │   │   │       │       │   ├── cls_6byte.c
│                   │   │   │       │       │   ├── cls_7_1_byte.c
│                   │   │   │       │       │   ├── cls_7byte.c
│                   │   │   │       │       │   ├── cls_8byte.c
│                   │   │   │       │       │   ├── cls_9byte1.c
│                   │   │   │       │       │   ├── cls_9byte2.c
│                   │   │   │       │       │   ├── cls_align_double.c
│                   │   │   │       │       │   ├── cls_align_float.c
│                   │   │   │       │       │   ├── cls_align_longdouble.c
│                   │   │   │       │       │   ├── cls_align_longdouble_split.c
│                   │   │   │       │       │   ├── cls_align_longdouble_split2.c
│                   │   │   │       │       │   ├── cls_align_pointer.c
│                   │   │   │       │       │   ├── cls_align_sint16.c
│                   │   │   │       │       │   ├── cls_align_sint32.c
│                   │   │   │       │       │   ├── cls_align_sint64.c
│                   │   │   │       │       │   ├── cls_align_uint16.c
│                   │   │   │       │       │   ├── cls_align_uint32.c
│                   │   │   │       │       │   ├── cls_align_uint64.c
│                   │   │   │       │       │   ├── cls_dbls_struct.c
│                   │   │   │       │       │   ├── cls_double.c
│                   │   │   │       │       │   ├── cls_double_va.c
│                   │   │   │       │       │   ├── cls_float.c
│                   │   │   │       │       │   ├── cls_longdouble.c
│                   │   │   │       │       │   ├── cls_longdouble_va.c
│                   │   │   │       │       │   ├── cls_many_mixed_args.c
│                   │   │   │       │       │   ├── cls_many_mixed_float_double.c
│                   │   │   │       │       │   ├── cls_multi_schar.c
│                   │   │   │       │       │   ├── cls_multi_sshort.c
│                   │   │   │       │       │   ├── cls_multi_sshortchar.c
│                   │   │   │       │       │   ├── cls_multi_uchar.c
│                   │   │   │       │       │   ├── cls_multi_ushort.c
│                   │   │   │       │       │   ├── cls_multi_ushortchar.c
│                   │   │   │       │       │   ├── cls_pointer.c
│                   │   │   │       │       │   ├── cls_pointer_stack.c
│                   │   │   │       │       │   ├── cls_schar.c
│                   │   │   │       │       │   ├── cls_sint.c
│                   │   │   │       │       │   ├── cls_sshort.c
│                   │   │   │       │       │   ├── cls_struct_va1.c
│                   │   │   │       │       │   ├── cls_uchar.c
│                   │   │   │       │       │   ├── cls_uint.c
│                   │   │   │       │       │   ├── cls_uint_va.c
│                   │   │   │       │       │   ├── cls_ulong_va.c
│                   │   │   │       │       │   ├── cls_ulonglong.c
│                   │   │   │       │       │   ├── cls_ushort.c
│                   │   │   │       │       │   ├── err_bad_abi.c
│                   │   │   │       │       │   ├── ffitest.h
│                   │   │   │       │       │   ├── huge_struct.c
│                   │   │   │       │       │   ├── nested_struct.c
│                   │   │   │       │       │   ├── nested_struct1.c
│                   │   │   │       │       │   ├── nested_struct10.c
│                   │   │   │       │       │   ├── nested_struct11.c
│                   │   │   │       │       │   ├── nested_struct12.c
│                   │   │   │       │       │   ├── nested_struct13.c
│                   │   │   │       │       │   ├── nested_struct2.c
│                   │   │   │       │       │   ├── nested_struct3.c
│                   │   │   │       │       │   ├── nested_struct4.c
│                   │   │   │       │       │   ├── nested_struct5.c
│                   │   │   │       │       │   ├── nested_struct6.c
│                   │   │   │       │       │   ├── nested_struct7.c
│                   │   │   │       │       │   ├── nested_struct8.c
│                   │   │   │       │       │   ├── nested_struct9.c
│                   │   │   │       │       │   ├── problem1.c
│                   │   │   │       │       │   ├── single_entry_structs1.c
│                   │   │   │       │       │   ├── single_entry_structs2.c
│                   │   │   │       │       │   ├── single_entry_structs3.c
│                   │   │   │       │       │   ├── stret_large.c
│                   │   │   │       │       │   ├── stret_large2.c
│                   │   │   │       │       │   ├── stret_medium.c
│                   │   │   │       │       │   ├── stret_medium2.c
│                   │   │   │       │       │   ├── testclosure.c
│                   │   │   │       │       │   ├── unwindtest.cc
│                   │   │   │       │       │   └── unwindtest_ffi_call.cc
│                   │   │   │       │       ├── libffi.complex/
│                   │   │   │       │       │   ├── cls_align_complex.inc
│                   │   │   │       │       │   ├── cls_align_complex_double.c
│                   │   │   │       │       │   ├── cls_align_complex_float.c
│                   │   │   │       │       │   ├── cls_align_complex_longdouble.c
│                   │   │   │       │       │   ├── cls_complex.inc
│                   │   │   │       │       │   ├── cls_complex_double.c
│                   │   │   │       │       │   ├── cls_complex_float.c
│                   │   │   │       │       │   ├── cls_complex_longdouble.c
│                   │   │   │       │       │   ├── cls_complex_struct.inc
│                   │   │   │       │       │   ├── cls_complex_struct_double.c
│                   │   │   │       │       │   ├── cls_complex_struct_float.c
│                   │   │   │       │       │   ├── cls_complex_struct_longdouble.c
│                   │   │   │       │       │   ├── cls_complex_va.inc
│                   │   │   │       │       │   ├── cls_complex_va_double.c
│                   │   │   │       │       │   ├── cls_complex_va_float.c
│                   │   │   │       │       │   ├── cls_complex_va_longdouble.c
│                   │   │   │       │       │   ├── complex.exp
│                   │   │   │       │       │   ├── complex.inc
│                   │   │   │       │       │   ├── complex_defs_double.inc
│                   │   │   │       │       │   ├── complex_defs_float.inc
│                   │   │   │       │       │   ├── complex_defs_longdouble.inc
│                   │   │   │       │       │   ├── complex_double.c
│                   │   │   │       │       │   ├── complex_float.c
│                   │   │   │       │       │   ├── complex_int.c
│                   │   │   │       │       │   ├── complex_longdouble.c
│                   │   │   │       │       │   ├── ffitest.h
│                   │   │   │       │       │   ├── many_complex.inc
│                   │   │   │       │       │   ├── many_complex_double.c
│                   │   │   │       │       │   ├── many_complex_float.c
│                   │   │   │       │       │   ├── many_complex_longdouble.c
│                   │   │   │       │       │   ├── return_complex.inc
│                   │   │   │       │       │   ├── return_complex1.inc
│                   │   │   │       │       │   ├── return_complex1_double.c
│                   │   │   │       │       │   ├── return_complex1_float.c
│                   │   │   │       │       │   ├── return_complex1_longdouble.c
│                   │   │   │       │       │   ├── return_complex2.inc
│                   │   │   │       │       │   ├── return_complex2_double.c
│                   │   │   │       │       │   ├── return_complex2_float.c
│                   │   │   │       │       │   ├── return_complex2_longdouble.c
│                   │   │   │       │       │   ├── return_complex_double.c
│                   │   │   │       │       │   ├── return_complex_float.c
│                   │   │   │       │       │   └── return_complex_longdouble.c
│                   │   │   │       │       ├── libffi.go/
│                   │   │   │       │       │   ├── aa-direct.c
│                   │   │   │       │       │   ├── closure1.c
│                   │   │   │       │       │   ├── ffitest.h
│                   │   │   │       │       │   ├── go.exp
│                   │   │   │       │       │   └── static-chain.h
│                   │   │   │       │       └── libffi.threads/
│                   │   │   │       │           ├── ffitest.h
│                   │   │   │       │           ├── threads.exp
│                   │   │   │       │           └── tsan.c
│                   │   │   │       ├── libffi.bsd.mk
│                   │   │   │       ├── libffi.darwin.mk
│                   │   │   │       ├── libffi.gnu.mk
│                   │   │   │       ├── libffi.mk
│                   │   │   │       ├── libffi.vc.mk
│                   │   │   │       ├── libffi.vc64.mk
│                   │   │   │       ├── rbffi.h
│                   │   │   │       └── rbffi_endian.h
│                   │   │   ├── ffi.gemspec
│                   │   │   ├── lib/
│                   │   │   │   ├── ffi/
│                   │   │   │   │   ├── abstract_memory.rb
│                   │   │   │   │   ├── autopointer.rb
│                   │   │   │   │   ├── buffer.rb
│                   │   │   │   │   ├── callback.rb
│                   │   │   │   │   ├── compat.rb
│                   │   │   │   │   ├── data_converter.rb
│                   │   │   │   │   ├── dynamic_library.rb
│                   │   │   │   │   ├── enum.rb
│                   │   │   │   │   ├── errno.rb
│                   │   │   │   │   ├── ffi.rb
│                   │   │   │   │   ├── function.rb
│                   │   │   │   │   ├── io.rb
│                   │   │   │   │   ├── library.rb
│                   │   │   │   │   ├── library_path.rb
│                   │   │   │   │   ├── managedstruct.rb
│                   │   │   │   │   ├── memorypointer.rb
│                   │   │   │   │   ├── platform/
│                   │   │   │   │   │   ├── aarch64-darwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── aarch64-freebsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── aarch64-freebsd12/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── aarch64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── aarch64-openbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── aarch64-windows/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── arm-freebsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── arm-freebsd12/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── arm-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── hppa1.1-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── hppa2.0-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-cygwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-darwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-freebsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-freebsd12/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-gnu/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-netbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-openbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-solaris/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── i386-windows/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── ia64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── loongarch64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mips-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mips64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mips64el-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mipsel-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mipsisa32r6-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mipsisa32r6el-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mipsisa64r6-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── mipsisa64r6el-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc-aix/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc-darwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc-openbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── powerpc64le-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── riscv64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── s390-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── s390x-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sparc-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sparc-solaris/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sparcv9-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sparcv9-openbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sparcv9-solaris/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── sw_64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-cygwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-darwin/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-dragonflybsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-freebsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-freebsd12/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-haiku/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-linux/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-msys/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-netbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-openbsd/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   ├── x86_64-solaris/
│                   │   │   │   │   │   │   └── types.conf
│                   │   │   │   │   │   └── x86_64-windows/
│                   │   │   │   │   │       └── types.conf
│                   │   │   │   │   ├── platform.rb
│                   │   │   │   │   ├── pointer.rb
│                   │   │   │   │   ├── struct.rb
│                   │   │   │   │   ├── struct_by_reference.rb
│                   │   │   │   │   ├── struct_layout.rb
│                   │   │   │   │   ├── struct_layout_builder.rb
│                   │   │   │   │   ├── tools/
│                   │   │   │   │   │   ├── const_generator.rb
│                   │   │   │   │   │   ├── generator.rb
│                   │   │   │   │   │   ├── generator_task.rb
│                   │   │   │   │   │   └── struct_generator.rb
│                   │   │   │   │   ├── types.rb
│                   │   │   │   │   ├── union.rb
│                   │   │   │   │   ├── variadic.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   ├── ffi.rb
│                   │   │   │   └── ffi_c.bundle
│                   │   │   ├── samples/
│                   │   │   │   ├── getlogin.rb
│                   │   │   │   ├── getpid.rb
│                   │   │   │   ├── gettimeofday.rb
│                   │   │   │   ├── hello.rb
│                   │   │   │   ├── hello_ractor.rb
│                   │   │   │   ├── inotify.rb
│                   │   │   │   ├── pty.rb
│                   │   │   │   ├── qsort.rb
│                   │   │   │   └── qsort_ractor.rb
│                   │   │   └── sig/
│                   │   │       ├── ffi/
│                   │   │       │   ├── abstract_memory.rbs
│                   │   │       │   ├── auto_pointer.rbs
│                   │   │       │   ├── buffer.rbs
│                   │   │       │   ├── data_converter.rbs
│                   │   │       │   ├── dynamic_library.rbs
│                   │   │       │   ├── enum.rbs
│                   │   │       │   ├── errno.rbs
│                   │   │       │   ├── function.rbs
│                   │   │       │   ├── library.rbs
│                   │   │       │   ├── native_type.rbs
│                   │   │       │   ├── platform.rbs
│                   │   │       │   ├── pointer.rbs
│                   │   │       │   ├── struct.rbs
│                   │   │       │   ├── struct_by_reference.rbs
│                   │   │       │   ├── struct_by_value.rbs
│                   │   │       │   ├── struct_layout.rbs
│                   │   │       │   ├── struct_layout_builder.rbs
│                   │   │       │   └── type.rbs
│                   │   │       └── ffi.rbs
│                   │   ├── forwardable-extended-2.6.0/
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE
│                   │   │   ├── Rakefile
│                   │   │   └── lib/
│                   │   │       └── forwardable/
│                   │   │           ├── extended/
│                   │   │           │   └── version.rb
│                   │   │           └── extended.rb
│                   │   ├── google-protobuf-3.23.4-arm64-darwin/
│                   │   │   ├── ext/
│                   │   │   │   └── google/
│                   │   │   │       └── protobuf_c/
│                   │   │   │           ├── convert.c
│                   │   │   │           ├── convert.h
│                   │   │   │           ├── defs.c
│                   │   │   │           ├── defs.h
│                   │   │   │           ├── extconf.rb
│                   │   │   │           ├── map.c
│                   │   │   │           ├── map.h
│                   │   │   │           ├── message.c
│                   │   │   │           ├── message.h
│                   │   │   │           ├── protobuf.c
│                   │   │   │           ├── protobuf.h
│                   │   │   │           ├── repeated_field.c
│                   │   │   │           ├── repeated_field.h
│                   │   │   │           ├── ruby-upb.c
│                   │   │   │           ├── ruby-upb.h
│                   │   │   │           ├── third_party/
│                   │   │   │           │   └── utf8_range/
│                   │   │   │           │       ├── LICENSE
│                   │   │   │           │       ├── naive.c
│                   │   │   │           │       ├── range2-neon.c
│                   │   │   │           │       ├── range2-sse.c
│                   │   │   │           │       └── utf8_range.h
│                   │   │   │           └── wrap_memcpy.c
│                   │   │   └── lib/
│                   │   │       └── google/
│                   │   │           ├── 2.6/
│                   │   │           │   └── protobuf_c.bundle
│                   │   │           ├── 2.7/
│                   │   │           │   └── protobuf_c.bundle
│                   │   │           ├── 3.0/
│                   │   │           │   └── protobuf_c.bundle
│                   │   │           ├── 3.1/
│                   │   │           │   └── protobuf_c.bundle
│                   │   │           ├── 3.2/
│                   │   │           │   └── protobuf_c.bundle
│                   │   │           ├── protobuf/
│                   │   │           │   ├── any_pb.rb
│                   │   │           │   ├── api_pb.rb
│                   │   │           │   ├── descriptor_dsl.rb
│                   │   │           │   ├── descriptor_pb.rb
│                   │   │           │   ├── duration_pb.rb
│                   │   │           │   ├── empty_pb.rb
│                   │   │           │   ├── field_mask_pb.rb
│                   │   │           │   ├── message_exts.rb
│                   │   │           │   ├── plugin_pb.rb
│                   │   │           │   ├── repeated_field.rb
│                   │   │           │   ├── source_context_pb.rb
│                   │   │           │   ├── struct_pb.rb
│                   │   │           │   ├── timestamp_pb.rb
│                   │   │           │   ├── type_pb.rb
│                   │   │           │   ├── well_known_types.rb
│                   │   │           │   └── wrappers_pb.rb
│                   │   │           └── protobuf.rb
│                   │   ├── http_parser.rb-0.8.1/
│                   │   │   ├── .github/
│                   │   │   │   └── workflows/
│                   │   │   │       ├── linux.yml
│                   │   │   │       └── windows.yml
│                   │   │   ├── .gitignore
│                   │   │   ├── .gitmodules
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE-MIT
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── bench/
│                   │   │   │   ├── standalone.rb
│                   │   │   │   └── thin.rb
│                   │   │   ├── ext/
│                   │   │   │   └── ruby_http_parser/
│                   │   │   │       ├── .gitignore
│                   │   │   │       ├── .sitearchdir.time
│                   │   │   │       ├── Makefile
│                   │   │   │       ├── RubyHttpParserService.java
│                   │   │   │       ├── ext_help.h
│                   │   │   │       ├── extconf.rb
│                   │   │   │       ├── org/
│                   │   │   │       │   └── ruby_http_parser/
│                   │   │   │       │       └── RubyHttpParser.java
│                   │   │   │       ├── ruby_http_parser.bundle
│                   │   │   │       ├── ruby_http_parser.c
│                   │   │   │       ├── ruby_http_parser.o
│                   │   │   │       ├── ryah_http_parser.c
│                   │   │   │       ├── ryah_http_parser.h
│                   │   │   │       ├── ryah_http_parser.o
│                   │   │   │       └── vendor/
│                   │   │   │           ├── .gitkeep
│                   │   │   │           ├── http-parser/
│                   │   │   │           │   ├── AUTHORS
│                   │   │   │           │   ├── LICENSE-MIT
│                   │   │   │           │   ├── Makefile
│                   │   │   │           │   ├── README.md
│                   │   │   │           │   ├── bench.c
│                   │   │   │           │   ├── contrib/
│                   │   │   │           │   │   ├── parsertrace.c
│                   │   │   │           │   │   └── url_parser.c
│                   │   │   │           │   ├── http_parser.c
│                   │   │   │           │   ├── http_parser.gyp
│                   │   │   │           │   ├── http_parser.h
│                   │   │   │           │   └── test.c
│                   │   │   │           └── http-parser-java/
│                   │   │   │               ├── AUTHORS
│                   │   │   │               ├── LICENSE-MIT
│                   │   │   │               ├── Makefile
│                   │   │   │               ├── README.md
│                   │   │   │               ├── TODO
│                   │   │   │               ├── build.xml
│                   │   │   │               ├── ext/
│                   │   │   │               │   └── primitives.jar
│                   │   │   │               ├── http_parser.c
│                   │   │   │               ├── http_parser.gyp
│                   │   │   │               ├── http_parser.h
│                   │   │   │               ├── src/
│                   │   │   │               │   ├── Http-parser.java.iml
│                   │   │   │               │   ├── impl/
│                   │   │   │               │   │   └── http_parser/
│                   │   │   │               │   │       ├── FieldData.java
│                   │   │   │               │   │       ├── HTTPCallback.java
│                   │   │   │               │   │       ├── HTTPDataCallback.java
│                   │   │   │               │   │       ├── HTTPErrorCallback.java
│                   │   │   │               │   │       ├── HTTPException.java
│                   │   │   │               │   │       ├── HTTPMethod.java
│                   │   │   │               │   │       ├── HTTPParser.java
│                   │   │   │               │   │       ├── HTTPParserUrl.java
│                   │   │   │               │   │       ├── ParserSettings.java
│                   │   │   │               │   │       ├── ParserType.java
│                   │   │   │               │   │       ├── Util.java
│                   │   │   │               │   │       └── lolevel/
│                   │   │   │               │   │           ├── HTTPCallback.java
│                   │   │   │               │   │           ├── HTTPDataCallback.java
│                   │   │   │               │   │           ├── HTTPErrorCallback.java
│                   │   │   │               │   │           ├── HTTPParser.java
│                   │   │   │               │   │           └── ParserSettings.java
│                   │   │   │               │   └── test/
│                   │   │   │               │       └── http_parser/
│                   │   │   │               │           └── lolevel/
│                   │   │   │               │               ├── Message.java
│                   │   │   │               │               ├── ParseUrl.java
│                   │   │   │               │               ├── Requests.java
│                   │   │   │               │               ├── Responses.java
│                   │   │   │               │               ├── Test.java
│                   │   │   │               │               ├── TestHeaderOverflowError.java
│                   │   │   │               │               ├── TestLoaderNG.java
│                   │   │   │               │               ├── TestNoOverflowLongBody.java
│                   │   │   │               │               ├── UnitTest.java
│                   │   │   │               │               ├── Upgrade.java
│                   │   │   │               │               ├── Url.java
│                   │   │   │               │               ├── Util.java
│                   │   │   │               │               └── WrongContentLength.java
│                   │   │   │               ├── test.c
│                   │   │   │               ├── tests.dumped
│                   │   │   │               ├── tests.utf8
│                   │   │   │               └── tools/
│                   │   │   │                   ├── byte_constants.rb
│                   │   │   │                   ├── const_char.rb
│                   │   │   │                   ├── lowcase.rb
│                   │   │   │                   └── parse_tests.rb
│                   │   │   ├── http_parser.rb.gemspec
│                   │   │   ├── lib/
│                   │   │   │   ├── http/
│                   │   │   │   │   └── parser.rb
│                   │   │   │   ├── http_parser.rb
│                   │   │   │   └── ruby_http_parser.bundle
│                   │   │   └── tasks/
│                   │   │       ├── compile.rake
│                   │   │       ├── fixtures.rake
│                   │   │       ├── spec.rake
│                   │   │       └── submodules.rake
│                   │   ├── i18n-1.14.8/
│                   │   │   ├── MIT-LICENSE
│                   │   │   ├── README.md
│                   │   │   └── lib/
│                   │   │       ├── i18n/
│                   │   │       │   ├── backend/
│                   │   │       │   │   ├── base.rb
│                   │   │       │   │   ├── cache.rb
│                   │   │       │   │   ├── cache_file.rb
│                   │   │       │   │   ├── cascade.rb
│                   │   │       │   │   ├── chain.rb
│                   │   │       │   │   ├── fallbacks.rb
│                   │   │       │   │   ├── flatten.rb
│                   │   │       │   │   ├── gettext.rb
│                   │   │       │   │   ├── interpolation_compiler.rb
│                   │   │       │   │   ├── key_value.rb
│                   │   │       │   │   ├── lazy_loadable.rb
│                   │   │       │   │   ├── memoize.rb
│                   │   │       │   │   ├── metadata.rb
│                   │   │       │   │   ├── pluralization.rb
│                   │   │       │   │   ├── simple.rb
│                   │   │       │   │   └── transliterator.rb
│                   │   │       │   ├── backend.rb
│                   │   │       │   ├── config.rb
│                   │   │       │   ├── exceptions.rb
│                   │   │       │   ├── gettext/
│                   │   │       │   │   ├── helpers.rb
│                   │   │       │   │   └── po_parser.rb
│                   │   │       │   ├── gettext.rb
│                   │   │       │   ├── interpolate/
│                   │   │       │   │   └── ruby.rb
│                   │   │       │   ├── locale/
│                   │   │       │   │   ├── fallbacks.rb
│                   │   │       │   │   ├── tag/
│                   │   │       │   │   │   ├── parents.rb
│                   │   │       │   │   │   ├── rfc4646.rb
│                   │   │       │   │   │   └── simple.rb
│                   │   │       │   │   └── tag.rb
│                   │   │       │   ├── locale.rb
│                   │   │       │   ├── middleware.rb
│                   │   │       │   ├── tests/
│                   │   │       │   │   ├── basics.rb
│                   │   │       │   │   ├── defaults.rb
│                   │   │       │   │   ├── interpolation.rb
│                   │   │       │   │   ├── link.rb
│                   │   │       │   │   ├── localization/
│                   │   │       │   │   │   ├── date.rb
│                   │   │       │   │   │   ├── date_time.rb
│                   │   │       │   │   │   ├── procs.rb
│                   │   │       │   │   │   └── time.rb
│                   │   │       │   │   ├── localization.rb
│                   │   │       │   │   ├── lookup.rb
│                   │   │       │   │   ├── pluralization.rb
│                   │   │       │   │   └── procs.rb
│                   │   │       │   ├── tests.rb
│                   │   │       │   ├── utils.rb
│                   │   │       │   └── version.rb
│                   │   │       └── i18n.rb
│                   │   ├── jekyll-4.3.4/
│                   │   │   ├── .rubocop.yml
│                   │   │   ├── LICENSE
│                   │   │   ├── README.markdown
│                   │   │   ├── exe/
│                   │   │   │   └── jekyll
│                   │   │   ├── lib/
│                   │   │   │   ├── blank_template/
│                   │   │   │   │   ├── _config.yml
│                   │   │   │   │   ├── _layouts/
│                   │   │   │   │   │   └── default.html
│                   │   │   │   │   ├── _sass/
│                   │   │   │   │   │   └── base.scss
│                   │   │   │   │   ├── assets/
│                   │   │   │   │   │   └── css/
│                   │   │   │   │   │       └── main.scss
│                   │   │   │   │   └── index.md
│                   │   │   │   ├── jekyll/
│                   │   │   │   │   ├── cache.rb
│                   │   │   │   │   ├── cleaner.rb
│                   │   │   │   │   ├── collection.rb
│                   │   │   │   │   ├── command.rb
│                   │   │   │   │   ├── commands/
│                   │   │   │   │   │   ├── build.rb
│                   │   │   │   │   │   ├── clean.rb
│                   │   │   │   │   │   ├── doctor.rb
│                   │   │   │   │   │   ├── help.rb
│                   │   │   │   │   │   ├── new.rb
│                   │   │   │   │   │   ├── new_theme.rb
│                   │   │   │   │   │   ├── serve/
│                   │   │   │   │   │   │   ├── live_reload_reactor.rb
│                   │   │   │   │   │   │   ├── livereload_assets/
│                   │   │   │   │   │   │   │   └── livereload.js
│                   │   │   │   │   │   │   ├── mime_types_charset.json
│                   │   │   │   │   │   │   ├── servlet.rb
│                   │   │   │   │   │   │   └── websockets.rb
│                   │   │   │   │   │   └── serve.rb
│                   │   │   │   │   ├── configuration.rb
│                   │   │   │   │   ├── converter.rb
│                   │   │   │   │   ├── converters/
│                   │   │   │   │   │   ├── identity.rb
│                   │   │   │   │   │   ├── markdown/
│                   │   │   │   │   │   │   └── kramdown_parser.rb
│                   │   │   │   │   │   ├── markdown.rb
│                   │   │   │   │   │   └── smartypants.rb
│                   │   │   │   │   ├── convertible.rb
│                   │   │   │   │   ├── deprecator.rb
│                   │   │   │   │   ├── document.rb
│                   │   │   │   │   ├── drops/
│                   │   │   │   │   │   ├── collection_drop.rb
│                   │   │   │   │   │   ├── document_drop.rb
│                   │   │   │   │   │   ├── drop.rb
│                   │   │   │   │   │   ├── excerpt_drop.rb
│                   │   │   │   │   │   ├── jekyll_drop.rb
│                   │   │   │   │   │   ├── site_drop.rb
│                   │   │   │   │   │   ├── static_file_drop.rb
│                   │   │   │   │   │   ├── theme_drop.rb
│                   │   │   │   │   │   ├── unified_payload_drop.rb
│                   │   │   │   │   │   └── url_drop.rb
│                   │   │   │   │   ├── entry_filter.rb
│                   │   │   │   │   ├── errors.rb
│                   │   │   │   │   ├── excerpt.rb
│                   │   │   │   │   ├── external.rb
│                   │   │   │   │   ├── filters/
│                   │   │   │   │   │   ├── date_filters.rb
│                   │   │   │   │   │   ├── grouping_filters.rb
│                   │   │   │   │   │   └── url_filters.rb
│                   │   │   │   │   ├── filters.rb
│                   │   │   │   │   ├── frontmatter_defaults.rb
│                   │   │   │   │   ├── generator.rb
│                   │   │   │   │   ├── hooks.rb
│                   │   │   │   │   ├── inclusion.rb
│                   │   │   │   │   ├── layout.rb
│                   │   │   │   │   ├── liquid_extensions.rb
│                   │   │   │   │   ├── liquid_renderer/
│                   │   │   │   │   │   ├── file.rb
│                   │   │   │   │   │   └── table.rb
│                   │   │   │   │   ├── liquid_renderer.rb
│                   │   │   │   │   ├── log_adapter.rb
│                   │   │   │   │   ├── mime.types
│                   │   │   │   │   ├── page.rb
│                   │   │   │   │   ├── page_excerpt.rb
│                   │   │   │   │   ├── page_without_a_file.rb
│                   │   │   │   │   ├── path_manager.rb
│                   │   │   │   │   ├── plugin.rb
│                   │   │   │   │   ├── plugin_manager.rb
│                   │   │   │   │   ├── profiler.rb
│                   │   │   │   │   ├── publisher.rb
│                   │   │   │   │   ├── reader.rb
│                   │   │   │   │   ├── readers/
│                   │   │   │   │   │   ├── collection_reader.rb
│                   │   │   │   │   │   ├── data_reader.rb
│                   │   │   │   │   │   ├── layout_reader.rb
│                   │   │   │   │   │   ├── page_reader.rb
│                   │   │   │   │   │   ├── post_reader.rb
│                   │   │   │   │   │   ├── static_file_reader.rb
│                   │   │   │   │   │   └── theme_assets_reader.rb
│                   │   │   │   │   ├── regenerator.rb
│                   │   │   │   │   ├── related_posts.rb
│                   │   │   │   │   ├── renderer.rb
│                   │   │   │   │   ├── site.rb
│                   │   │   │   │   ├── static_file.rb
│                   │   │   │   │   ├── stevenson.rb
│                   │   │   │   │   ├── tags/
│                   │   │   │   │   │   ├── highlight.rb
│                   │   │   │   │   │   ├── include.rb
│                   │   │   │   │   │   ├── link.rb
│                   │   │   │   │   │   └── post_url.rb
│                   │   │   │   │   ├── theme.rb
│                   │   │   │   │   ├── theme_builder.rb
│                   │   │   │   │   ├── url.rb
│                   │   │   │   │   ├── utils/
│                   │   │   │   │   │   ├── ansi.rb
│                   │   │   │   │   │   ├── exec.rb
│                   │   │   │   │   │   ├── internet.rb
│                   │   │   │   │   │   ├── platforms.rb
│                   │   │   │   │   │   ├── thread_event.rb
│                   │   │   │   │   │   └── win_tz.rb
│                   │   │   │   │   ├── utils.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   ├── jekyll.rb
│                   │   │   │   ├── site_template/
│                   │   │   │   │   ├── .gitignore
│                   │   │   │   │   ├── 404.html
│                   │   │   │   │   ├── _config.yml
│                   │   │   │   │   ├── _posts/
│                   │   │   │   │   │   └── 0000-00-00-welcome-to-jekyll.markdown.erb
│                   │   │   │   │   ├── about.markdown
│                   │   │   │   │   └── index.markdown
│                   │   │   │   └── theme_template/
│                   │   │   │       ├── CODE_OF_CONDUCT.md.erb
│                   │   │   │       ├── Gemfile
│                   │   │   │       ├── LICENSE.txt.erb
│                   │   │   │       ├── README.md.erb
│                   │   │   │       ├── _layouts/
│                   │   │   │       │   ├── default.html
│                   │   │   │       │   ├── page.html
│                   │   │   │       │   └── post.html
│                   │   │   │       ├── example/
│                   │   │   │       │   ├── _config.yml.erb
│                   │   │   │       │   ├── _post.md
│                   │   │   │       │   ├── index.html
│                   │   │   │       │   └── style.scss
│                   │   │   │       ├── gitignore.erb
│                   │   │   │       └── theme.gemspec.erb
│                   │   │   └── rubocop/
│                   │   │       ├── jekyll/
│                   │   │       │   ├── assert_equal_literal_actual.rb
│                   │   │       │   ├── no_p_allowed.rb
│                   │   │       │   └── no_puts_allowed.rb
│                   │   │       └── jekyll.rb
│                   │   ├── jekyll-sass-converter-3.0.0/
│                   │   │   └── lib/
│                   │   │       ├── jekyll/
│                   │   │       │   ├── converters/
│                   │   │       │   │   ├── sass.rb
│                   │   │       │   │   └── scss.rb
│                   │   │       │   └── source_map_page.rb
│                   │   │       ├── jekyll-sass-converter/
│                   │   │       │   └── version.rb
│                   │   │       └── jekyll-sass-converter.rb
│                   │   ├── jekyll-seo-tag-2.8.0/
│                   │   │   ├── .github/
│                   │   │   │   └── workflows/
│                   │   │   │       ├── ci.yml
│                   │   │   │       ├── release.yml
│                   │   │   │       ├── scripts/
│                   │   │   │       │   ├── memprof
│                   │   │   │       │   └── memprof.rb
│                   │   │   │       └── third-party.yml
│                   │   │   ├── .gitignore
│                   │   │   ├── .rspec
│                   │   │   ├── .rubocop.yml
│                   │   │   ├── .rubocop_todo.yml
│                   │   │   ├── Gemfile
│                   │   │   ├── History.markdown
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── docs/
│                   │   │   │   ├── README.md
│                   │   │   │   ├── _config.yml
│                   │   │   │   ├── _layouts/
│                   │   │   │   │   └── default.html
│                   │   │   │   ├── advanced-usage.md
│                   │   │   │   ├── installation.md
│                   │   │   │   └── usage.md
│                   │   │   ├── jekyll-seo-tag.gemspec
│                   │   │   ├── lib/
│                   │   │   │   ├── jekyll-seo-tag/
│                   │   │   │   │   ├── author_drop.rb
│                   │   │   │   │   ├── drop.rb
│                   │   │   │   │   ├── filters.rb
│                   │   │   │   │   ├── image_drop.rb
│                   │   │   │   │   ├── json_ld.rb
│                   │   │   │   │   ├── json_ld_drop.rb
│                   │   │   │   │   ├── url_helper.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   ├── jekyll-seo-tag.rb
│                   │   │   │   └── template.html
│                   │   │   └── script/
│                   │   │       ├── bootstrap
│                   │   │       ├── cibuild
│                   │   │       ├── release
│                   │   │       └── site
│                   │   ├── jekyll-watch-2.2.1/
│                   │   │   └── lib/
│                   │   │       ├── jekyll/
│                   │   │       │   ├── commands/
│                   │   │       │   │   └── watch.rb
│                   │   │       │   └── watcher.rb
│                   │   │       ├── jekyll-watch/
│                   │   │       │   └── version.rb
│                   │   │       └── jekyll-watch.rb
│                   │   ├── kramdown-2.5.2/
│                   │   │   ├── AUTHORS
│                   │   │   ├── CONTRIBUTERS
│                   │   │   ├── COPYING
│                   │   │   ├── README.md
│                   │   │   ├── VERSION
│                   │   │   ├── bin/
│                   │   │   │   └── kramdown
│                   │   │   ├── data/
│                   │   │   │   └── kramdown/
│                   │   │   │       ├── document.html
│                   │   │   │       └── document.latex
│                   │   │   ├── lib/
│                   │   │   │   ├── kramdown/
│                   │   │   │   │   ├── converter/
│                   │   │   │   │   │   ├── base.rb
│                   │   │   │   │   │   ├── hash_ast.rb
│                   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   ├── kramdown.rb
│                   │   │   │   │   │   ├── latex.rb
│                   │   │   │   │   │   ├── man.rb
│                   │   │   │   │   │   ├── math_engine/
│                   │   │   │   │   │   │   └── mathjax.rb
│                   │   │   │   │   │   ├── remove_html_tags.rb
│                   │   │   │   │   │   ├── syntax_highlighter/
│                   │   │   │   │   │   │   ├── minted.rb
│                   │   │   │   │   │   │   └── rouge.rb
│                   │   │   │   │   │   ├── syntax_highlighter.rb
│                   │   │   │   │   │   └── toc.rb
│                   │   │   │   │   ├── converter.rb
│                   │   │   │   │   ├── document.rb
│                   │   │   │   │   ├── element.rb
│                   │   │   │   │   ├── error.rb
│                   │   │   │   │   ├── options.rb
│                   │   │   │   │   ├── parser/
│                   │   │   │   │   │   ├── base.rb
│                   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   ├── kramdown/
│                   │   │   │   │   │   │   ├── abbreviation.rb
│                   │   │   │   │   │   │   ├── autolink.rb
│                   │   │   │   │   │   │   ├── blank_line.rb
│                   │   │   │   │   │   │   ├── block_boundary.rb
│                   │   │   │   │   │   │   ├── blockquote.rb
│                   │   │   │   │   │   │   ├── codeblock.rb
│                   │   │   │   │   │   │   ├── codespan.rb
│                   │   │   │   │   │   │   ├── emphasis.rb
│                   │   │   │   │   │   │   ├── eob.rb
│                   │   │   │   │   │   │   ├── escaped_chars.rb
│                   │   │   │   │   │   │   ├── extensions.rb
│                   │   │   │   │   │   │   ├── footnote.rb
│                   │   │   │   │   │   │   ├── header.rb
│                   │   │   │   │   │   │   ├── horizontal_rule.rb
│                   │   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   │   ├── html_entity.rb
│                   │   │   │   │   │   │   ├── line_break.rb
│                   │   │   │   │   │   │   ├── link.rb
│                   │   │   │   │   │   │   ├── list.rb
│                   │   │   │   │   │   │   ├── math.rb
│                   │   │   │   │   │   │   ├── paragraph.rb
│                   │   │   │   │   │   │   ├── smart_quotes.rb
│                   │   │   │   │   │   │   ├── table.rb
│                   │   │   │   │   │   │   └── typographic_symbol.rb
│                   │   │   │   │   │   ├── kramdown.rb
│                   │   │   │   │   │   └── markdown.rb
│                   │   │   │   │   ├── parser.rb
│                   │   │   │   │   ├── utils/
│                   │   │   │   │   │   ├── configurable.rb
│                   │   │   │   │   │   ├── entities.rb
│                   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   ├── lru_cache.rb
│                   │   │   │   │   │   ├── string_scanner.rb
│                   │   │   │   │   │   └── unidecoder.rb
│                   │   │   │   │   ├── utils.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── kramdown.rb
│                   │   │   ├── man/
│                   │   │   │   └── man1/
│                   │   │   │       └── kramdown.1
│                   │   │   └── test/
│                   │   │       ├── run_tests.rb
│                   │   │       ├── test_files.rb
│                   │   │       ├── test_location.rb
│                   │   │       ├── test_string_scanner_kramdown.rb
│                   │   │       └── testcases/
│                   │   │           ├── block/
│                   │   │           │   ├── 01_blank_line/
│                   │   │           │   │   ├── spaces.html
│                   │   │           │   │   ├── spaces.text
│                   │   │           │   │   ├── tabs.html
│                   │   │           │   │   └── tabs.text
│                   │   │           │   ├── 02_eob/
│                   │   │           │   │   ├── beginning.html
│                   │   │           │   │   ├── beginning.text
│                   │   │           │   │   ├── end.html
│                   │   │           │   │   ├── end.text
│                   │   │           │   │   ├── middle.html
│                   │   │           │   │   └── middle.text
│                   │   │           │   ├── 03_paragraph/
│                   │   │           │   │   ├── indented.html
│                   │   │           │   │   ├── indented.html.gfm
│                   │   │           │   │   ├── indented.text
│                   │   │           │   │   ├── line_break_last_line.html
│                   │   │           │   │   ├── line_break_last_line.text
│                   │   │           │   │   ├── no_newline_at_end.html
│                   │   │           │   │   ├── no_newline_at_end.text
│                   │   │           │   │   ├── one_para.html
│                   │   │           │   │   ├── one_para.text
│                   │   │           │   │   ├── standalone_image.html
│                   │   │           │   │   ├── standalone_image.text
│                   │   │           │   │   ├── to_kramdown.kramdown
│                   │   │           │   │   ├── to_kramdown.text
│                   │   │           │   │   ├── two_para.html
│                   │   │           │   │   ├── two_para.text
│                   │   │           │   │   ├── with_html_to_native.html
│                   │   │           │   │   ├── with_html_to_native.options
│                   │   │           │   │   └── with_html_to_native.text
│                   │   │           │   ├── 04_header/
│                   │   │           │   │   ├── atx_header.html
│                   │   │           │   │   ├── atx_header.text
│                   │   │           │   │   ├── atx_header_no_newline_at_end.html
│                   │   │           │   │   ├── atx_header_no_newline_at_end.text
│                   │   │           │   │   ├── header_type_offset.html
│                   │   │           │   │   ├── header_type_offset.kramdown
│                   │   │           │   │   ├── header_type_offset.latex
│                   │   │           │   │   ├── header_type_offset.options
│                   │   │           │   │   ├── header_type_offset.text
│                   │   │           │   │   ├── setext_header.html
│                   │   │           │   │   ├── setext_header.text
│                   │   │           │   │   ├── setext_header_no_newline_at_end.html
│                   │   │           │   │   ├── setext_header_no_newline_at_end.text
│                   │   │           │   │   ├── with_auto_id_prefix.html
│                   │   │           │   │   ├── with_auto_id_prefix.options
│                   │   │           │   │   ├── with_auto_id_prefix.text
│                   │   │           │   │   ├── with_auto_id_stripping.html
│                   │   │           │   │   ├── with_auto_id_stripping.options
│                   │   │           │   │   ├── with_auto_id_stripping.text
│                   │   │           │   │   ├── with_auto_ids.html
│                   │   │           │   │   ├── with_auto_ids.options
│                   │   │           │   │   ├── with_auto_ids.text
│                   │   │           │   │   ├── with_header_links.html
│                   │   │           │   │   ├── with_header_links.options
│                   │   │           │   │   ├── with_header_links.text
│                   │   │           │   │   ├── with_line_break.html
│                   │   │           │   │   └── with_line_break.text
│                   │   │           │   ├── 05_blockquote/
│                   │   │           │   │   ├── indented.html
│                   │   │           │   │   ├── indented.text
│                   │   │           │   │   ├── lazy.html
│                   │   │           │   │   ├── lazy.text
│                   │   │           │   │   ├── nested.html
│                   │   │           │   │   ├── nested.text
│                   │   │           │   │   ├── no_newline_at_end.html
│                   │   │           │   │   ├── no_newline_at_end.text
│                   │   │           │   │   ├── very_long_line.html
│                   │   │           │   │   ├── very_long_line.text
│                   │   │           │   │   ├── with_code_blocks.html
│                   │   │           │   │   └── with_code_blocks.text
│                   │   │           │   ├── 06_codeblock/
│                   │   │           │   │   ├── disable-highlighting.html
│                   │   │           │   │   ├── disable-highlighting.options
│                   │   │           │   │   ├── disable-highlighting.text
│                   │   │           │   │   ├── error.html
│                   │   │           │   │   ├── error.text
│                   │   │           │   │   ├── guess_lang_css_class.html
│                   │   │           │   │   ├── guess_lang_css_class.options
│                   │   │           │   │   ├── guess_lang_css_class.text
│                   │   │           │   │   ├── highlighting-minted-with-opts.latex
│                   │   │           │   │   ├── highlighting-minted-with-opts.options
│                   │   │           │   │   ├── highlighting-minted-with-opts.text
│                   │   │           │   │   ├── highlighting-minted.latex
│                   │   │           │   │   ├── highlighting-minted.options
│                   │   │           │   │   ├── highlighting-minted.text
│                   │   │           │   │   ├── highlighting-opts.html
│                   │   │           │   │   ├── highlighting-opts.options
│                   │   │           │   │   ├── highlighting-opts.text
│                   │   │           │   │   ├── highlighting.html
│                   │   │           │   │   ├── highlighting.options
│                   │   │           │   │   ├── highlighting.text
│                   │   │           │   │   ├── issue_gh45.html
│                   │   │           │   │   ├── issue_gh45.test
│                   │   │           │   │   ├── lazy.html
│                   │   │           │   │   ├── lazy.text
│                   │   │           │   │   ├── no_newline_at_end.html
│                   │   │           │   │   ├── no_newline_at_end.text
│                   │   │           │   │   ├── no_newline_at_end_1.html
│                   │   │           │   │   ├── no_newline_at_end_1.text
│                   │   │           │   │   ├── normal.html
│                   │   │           │   │   ├── normal.text
│                   │   │           │   │   ├── rouge/
│                   │   │           │   │   │   ├── disabled.html
│                   │   │           │   │   │   ├── disabled.options
│                   │   │           │   │   │   ├── disabled.text
│                   │   │           │   │   │   ├── multiple.html
│                   │   │           │   │   │   ├── multiple.options
│                   │   │           │   │   │   ├── multiple.text
│                   │   │           │   │   │   ├── simple.html
│                   │   │           │   │   │   ├── simple.options
│                   │   │           │   │   │   └── simple.text
│                   │   │           │   │   ├── tilde_syntax.html
│                   │   │           │   │   ├── tilde_syntax.text
│                   │   │           │   │   ├── whitespace.html
│                   │   │           │   │   ├── whitespace.text
│                   │   │           │   │   ├── with_blank_line.html
│                   │   │           │   │   ├── with_blank_line.text
│                   │   │           │   │   ├── with_eob_marker.html
│                   │   │           │   │   ├── with_eob_marker.text
│                   │   │           │   │   ├── with_ial.html
│                   │   │           │   │   ├── with_ial.text
│                   │   │           │   │   ├── with_lang_in_fenced_block.html
│                   │   │           │   │   ├── with_lang_in_fenced_block.options
│                   │   │           │   │   ├── with_lang_in_fenced_block.text
│                   │   │           │   │   ├── with_lang_in_fenced_block_any_char.html
│                   │   │           │   │   ├── with_lang_in_fenced_block_any_char.options
│                   │   │           │   │   ├── with_lang_in_fenced_block_any_char.text
│                   │   │           │   │   ├── with_lang_in_fenced_block_name_with_dash.html
│                   │   │           │   │   ├── with_lang_in_fenced_block_name_with_dash.options
│                   │   │           │   │   └── with_lang_in_fenced_block_name_with_dash.text
│                   │   │           │   ├── 07_horizontal_rule/
│                   │   │           │   │   ├── error.html
│                   │   │           │   │   ├── error.text
│                   │   │           │   │   ├── normal.html
│                   │   │           │   │   ├── normal.text
│                   │   │           │   │   ├── sepspaces.html
│                   │   │           │   │   ├── sepspaces.text
│                   │   │           │   │   ├── septabs.html
│                   │   │           │   │   └── septabs.text
│                   │   │           │   ├── 08_list/
│                   │   │           │   │   ├── brackets_in_item.latex
│                   │   │           │   │   ├── brackets_in_item.text
│                   │   │           │   │   ├── escaping.html
│                   │   │           │   │   ├── escaping.text
│                   │   │           │   │   ├── item_ial.html
│                   │   │           │   │   ├── item_ial.text
│                   │   │           │   │   ├── lazy.html
│                   │   │           │   │   ├── lazy.text
│                   │   │           │   │   ├── lazy_and_nested.html
│                   │   │           │   │   ├── lazy_and_nested.text
│                   │   │           │   │   ├── list_and_hr.html
│                   │   │           │   │   ├── list_and_hr.text
│                   │   │           │   │   ├── list_and_others.html
│                   │   │           │   │   ├── list_and_others.text
│                   │   │           │   │   ├── mixed.html
│                   │   │           │   │   ├── mixed.text
│                   │   │           │   │   ├── nested.html
│                   │   │           │   │   ├── nested.text
│                   │   │           │   │   ├── nested_compact.kramdown
│                   │   │           │   │   ├── nested_compact.text
│                   │   │           │   │   ├── other_first_element.html
│                   │   │           │   │   ├── other_first_element.text
│                   │   │           │   │   ├── simple_ol.html
│                   │   │           │   │   ├── simple_ol.text
│                   │   │           │   │   ├── simple_ul.html
│                   │   │           │   │   ├── simple_ul.text
│                   │   │           │   │   ├── single_item.html
│                   │   │           │   │   ├── single_item.text
│                   │   │           │   │   ├── special_cases.html
│                   │   │           │   │   └── special_cases.text
│                   │   │           │   ├── 09_html/
│                   │   │           │   │   ├── cdata_section.html
│                   │   │           │   │   ├── cdata_section.text
│                   │   │           │   │   ├── comment.html
│                   │   │           │   │   ├── comment.text
│                   │   │           │   │   ├── content_model/
│                   │   │           │   │   │   ├── deflists.html
│                   │   │           │   │   │   ├── deflists.options
│                   │   │           │   │   │   ├── deflists.text
│                   │   │           │   │   │   ├── tables.html
│                   │   │           │   │   │   ├── tables.options
│                   │   │           │   │   │   └── tables.text
│                   │   │           │   │   ├── html5_attributes.html
│                   │   │           │   │   ├── html5_attributes.text
│                   │   │           │   │   ├── html_after_block.html
│                   │   │           │   │   ├── html_after_block.text
│                   │   │           │   │   ├── html_and_codeblocks.html
│                   │   │           │   │   ├── html_and_codeblocks.options
│                   │   │           │   │   ├── html_and_codeblocks.text
│                   │   │           │   │   ├── html_and_headers.html
│                   │   │           │   │   ├── html_and_headers.text
│                   │   │           │   │   ├── html_to_native/
│                   │   │           │   │   │   ├── code.html
│                   │   │           │   │   │   ├── code.text
│                   │   │           │   │   │   ├── comment.html
│                   │   │           │   │   │   ├── comment.text
│                   │   │           │   │   │   ├── emphasis.html
│                   │   │           │   │   │   ├── emphasis.text
│                   │   │           │   │   │   ├── entity.html
│                   │   │           │   │   │   ├── entity.text
│                   │   │           │   │   │   ├── header.html
│                   │   │           │   │   │   ├── header.options
│                   │   │           │   │   │   ├── header.text
│                   │   │           │   │   │   ├── list_dl.html
│                   │   │           │   │   │   ├── list_dl.text
│                   │   │           │   │   │   ├── list_ol.html
│                   │   │           │   │   │   ├── list_ol.text
│                   │   │           │   │   │   ├── list_ul.html
│                   │   │           │   │   │   ├── list_ul.text
│                   │   │           │   │   │   ├── options
│                   │   │           │   │   │   ├── paragraph.html
│                   │   │           │   │   │   ├── paragraph.text
│                   │   │           │   │   │   ├── table_normal.html
│                   │   │           │   │   │   ├── table_normal.text
│                   │   │           │   │   │   ├── table_simple.html
│                   │   │           │   │   │   ├── table_simple.text
│                   │   │           │   │   │   ├── typography.html
│                   │   │           │   │   │   └── typography.text
│                   │   │           │   │   ├── invalid_html_1.html
│                   │   │           │   │   ├── invalid_html_1.text
│                   │   │           │   │   ├── invalid_html_2.html
│                   │   │           │   │   ├── invalid_html_2.text
│                   │   │           │   │   ├── markdown_attr.html
│                   │   │           │   │   ├── markdown_attr.text
│                   │   │           │   │   ├── not_parsed.html
│                   │   │           │   │   ├── not_parsed.text
│                   │   │           │   │   ├── parse_as_raw.html
│                   │   │           │   │   ├── parse_as_raw.htmlinput
│                   │   │           │   │   ├── parse_as_raw.options
│                   │   │           │   │   ├── parse_as_raw.text
│                   │   │           │   │   ├── parse_as_span.html
│                   │   │           │   │   ├── parse_as_span.htmlinput
│                   │   │           │   │   ├── parse_as_span.options
│                   │   │           │   │   ├── parse_as_span.text
│                   │   │           │   │   ├── parse_block_html.html
│                   │   │           │   │   ├── parse_block_html.options
│                   │   │           │   │   ├── parse_block_html.text
│                   │   │           │   │   ├── processing_instruction.html
│                   │   │           │   │   ├── processing_instruction.text
│                   │   │           │   │   ├── simple.html
│                   │   │           │   │   ├── simple.options
│                   │   │           │   │   ├── simple.text
│                   │   │           │   │   ├── standalone_image_in_div.htmlinput
│                   │   │           │   │   ├── standalone_image_in_div.text
│                   │   │           │   │   ├── table.kramdown
│                   │   │           │   │   ├── table.text
│                   │   │           │   │   ├── textarea.html
│                   │   │           │   │   ├── textarea.text
│                   │   │           │   │   ├── xml.html
│                   │   │           │   │   └── xml.text
│                   │   │           │   ├── 10_ald/
│                   │   │           │   │   ├── simple.html
│                   │   │           │   │   └── simple.text
│                   │   │           │   ├── 11_ial/
│                   │   │           │   │   ├── auto_id_and_ial.html
│                   │   │           │   │   ├── auto_id_and_ial.options
│                   │   │           │   │   ├── auto_id_and_ial.text
│                   │   │           │   │   ├── nested.html
│                   │   │           │   │   ├── nested.text
│                   │   │           │   │   ├── simple.html
│                   │   │           │   │   └── simple.text
│                   │   │           │   ├── 12_extension/
│                   │   │           │   │   ├── comment.html
│                   │   │           │   │   ├── comment.text
│                   │   │           │   │   ├── ignored.html
│                   │   │           │   │   ├── ignored.text
│                   │   │           │   │   ├── nomarkdown.html
│                   │   │           │   │   ├── nomarkdown.kramdown
│                   │   │           │   │   ├── nomarkdown.latex
│                   │   │           │   │   ├── nomarkdown.text
│                   │   │           │   │   ├── options.html
│                   │   │           │   │   ├── options.text
│                   │   │           │   │   ├── options2.html
│                   │   │           │   │   ├── options2.text
│                   │   │           │   │   ├── options3.html
│                   │   │           │   │   └── options3.text
│                   │   │           │   ├── 13_definition_list/
│                   │   │           │   │   ├── auto_ids.html
│                   │   │           │   │   ├── auto_ids.text
│                   │   │           │   │   ├── definition_at_beginning.html
│                   │   │           │   │   ├── definition_at_beginning.text
│                   │   │           │   │   ├── deflist_ial.html
│                   │   │           │   │   ├── deflist_ial.text
│                   │   │           │   │   ├── item_ial.html
│                   │   │           │   │   ├── item_ial.text
│                   │   │           │   │   ├── multiple_terms.html
│                   │   │           │   │   ├── multiple_terms.text
│                   │   │           │   │   ├── no_def_list.html
│                   │   │           │   │   ├── no_def_list.text
│                   │   │           │   │   ├── para_wrapping.html
│                   │   │           │   │   ├── para_wrapping.text
│                   │   │           │   │   ├── separated_by_eob.html
│                   │   │           │   │   ├── separated_by_eob.text
│                   │   │           │   │   ├── simple.html
│                   │   │           │   │   ├── simple.text
│                   │   │           │   │   ├── styled_terms.html
│                   │   │           │   │   ├── styled_terms.text
│                   │   │           │   │   ├── too_much_space.html
│                   │   │           │   │   ├── too_much_space.text
│                   │   │           │   │   ├── with_blocks.html
│                   │   │           │   │   └── with_blocks.text
│                   │   │           │   ├── 14_table/
│                   │   │           │   │   ├── empty_tag_in_cell.html
│                   │   │           │   │   ├── empty_tag_in_cell.options
│                   │   │           │   │   ├── empty_tag_in_cell.text
│                   │   │           │   │   ├── errors.html
│                   │   │           │   │   ├── errors.text
│                   │   │           │   │   ├── escaping.html
│                   │   │           │   │   ├── escaping.text
│                   │   │           │   │   ├── footer.html
│                   │   │           │   │   ├── footer.text
│                   │   │           │   │   ├── header.html
│                   │   │           │   │   ├── header.text
│                   │   │           │   │   ├── no_table.html
│                   │   │           │   │   ├── no_table.text
│                   │   │           │   │   ├── simple.html
│                   │   │           │   │   ├── simple.text
│                   │   │           │   │   ├── table_with_footnote.html
│                   │   │           │   │   ├── table_with_footnote.latex
│                   │   │           │   │   └── table_with_footnote.text
│                   │   │           │   ├── 15_math/
│                   │   │           │   │   ├── gh_128.html
│                   │   │           │   │   ├── gh_128.text
│                   │   │           │   │   ├── no_engine.html
│                   │   │           │   │   ├── no_engine.options
│                   │   │           │   │   ├── no_engine.text
│                   │   │           │   │   ├── normal.html
│                   │   │           │   │   └── normal.text
│                   │   │           │   └── 16_toc/
│                   │   │           │       ├── no_toc.html
│                   │   │           │       ├── no_toc.text
│                   │   │           │       ├── toc_exclude.html
│                   │   │           │       ├── toc_exclude.options
│                   │   │           │       ├── toc_exclude.text
│                   │   │           │       ├── toc_levels.html
│                   │   │           │       ├── toc_levels.options
│                   │   │           │       ├── toc_levels.text
│                   │   │           │       ├── toc_with_footnotes.html
│                   │   │           │       ├── toc_with_footnotes.options
│                   │   │           │       ├── toc_with_footnotes.text
│                   │   │           │       ├── toc_with_links.html
│                   │   │           │       ├── toc_with_links.options
│                   │   │           │       └── toc_with_links.text
│                   │   │           ├── cjk-line-break.html
│                   │   │           ├── cjk-line-break.options
│                   │   │           ├── cjk-line-break.text
│                   │   │           ├── encoding.html
│                   │   │           ├── encoding.text
│                   │   │           ├── man/
│                   │   │           │   ├── example.man
│                   │   │           │   ├── example.text
│                   │   │           │   ├── heading-name-dash-description.man
│                   │   │           │   ├── heading-name-dash-description.text
│                   │   │           │   ├── heading-name-description.man
│                   │   │           │   ├── heading-name-description.text
│                   │   │           │   ├── heading-name-section-description.man
│                   │   │           │   ├── heading-name-section-description.text
│                   │   │           │   ├── heading-name-section.man
│                   │   │           │   ├── heading-name-section.text
│                   │   │           │   ├── heading-name.man
│                   │   │           │   ├── heading-name.text
│                   │   │           │   ├── sections.man
│                   │   │           │   ├── sections.text
│                   │   │           │   ├── text-escaping.man
│                   │   │           │   └── text-escaping.text
│                   │   │           └── span/
│                   │   │               ├── 01_link/
│                   │   │               │   ├── empty.html
│                   │   │               │   ├── empty.text
│                   │   │               │   ├── empty_title.htmlinput
│                   │   │               │   ├── empty_title.text
│                   │   │               │   ├── image_in_a.html
│                   │   │               │   ├── image_in_a.text
│                   │   │               │   ├── imagelinks.html
│                   │   │               │   ├── imagelinks.text
│                   │   │               │   ├── inline.html
│                   │   │               │   ├── inline.text
│                   │   │               │   ├── latex_escaping.latex
│                   │   │               │   ├── latex_escaping.text
│                   │   │               │   ├── link_defs.html
│                   │   │               │   ├── link_defs.text
│                   │   │               │   ├── link_defs_with_ial.html
│                   │   │               │   ├── link_defs_with_ial.text
│                   │   │               │   ├── links_with_angle_brackets.html
│                   │   │               │   ├── links_with_angle_brackets.text
│                   │   │               │   ├── reference.html
│                   │   │               │   ├── reference.options
│                   │   │               │   └── reference.text
│                   │   │               ├── 02_emphasis/
│                   │   │               │   ├── empty.html
│                   │   │               │   ├── empty.text
│                   │   │               │   ├── errors.html
│                   │   │               │   ├── errors.text
│                   │   │               │   ├── nesting.html
│                   │   │               │   ├── nesting.text
│                   │   │               │   ├── normal.html
│                   │   │               │   ├── normal.options
│                   │   │               │   └── normal.text
│                   │   │               ├── 03_codespan/
│                   │   │               │   ├── empty.html
│                   │   │               │   ├── empty.text
│                   │   │               │   ├── errors.html
│                   │   │               │   ├── errors.text
│                   │   │               │   ├── highlighting-minted.latex
│                   │   │               │   ├── highlighting-minted.options
│                   │   │               │   ├── highlighting-minted.text
│                   │   │               │   ├── highlighting.html
│                   │   │               │   ├── highlighting.text
│                   │   │               │   ├── normal-css-class.html
│                   │   │               │   ├── normal-css-class.options
│                   │   │               │   ├── normal-css-class.text
│                   │   │               │   ├── normal.html
│                   │   │               │   ├── normal.text
│                   │   │               │   └── rouge/
│                   │   │               │       ├── disabled.html
│                   │   │               │       ├── disabled.options
│                   │   │               │       ├── disabled.text
│                   │   │               │       ├── simple.html
│                   │   │               │       ├── simple.options
│                   │   │               │       └── simple.text
│                   │   │               ├── 04_footnote/
│                   │   │               │   ├── backlink_inline.html
│                   │   │               │   ├── backlink_inline.options
│                   │   │               │   ├── backlink_inline.text
│                   │   │               │   ├── backlink_text.html
│                   │   │               │   ├── backlink_text.options
│                   │   │               │   ├── backlink_text.text
│                   │   │               │   ├── definitions.html
│                   │   │               │   ├── definitions.latex
│                   │   │               │   ├── definitions.text
│                   │   │               │   ├── footnote_link_text.html
│                   │   │               │   ├── footnote_link_text.options
│                   │   │               │   ├── footnote_link_text.text
│                   │   │               │   ├── footnote_nr.html
│                   │   │               │   ├── footnote_nr.latex
│                   │   │               │   ├── footnote_nr.options
│                   │   │               │   ├── footnote_nr.text
│                   │   │               │   ├── footnote_prefix.html
│                   │   │               │   ├── footnote_prefix.options
│                   │   │               │   ├── footnote_prefix.text
│                   │   │               │   ├── inside_footnote.html
│                   │   │               │   ├── inside_footnote.text
│                   │   │               │   ├── markers.html
│                   │   │               │   ├── markers.latex
│                   │   │               │   ├── markers.options
│                   │   │               │   ├── markers.text
│                   │   │               │   ├── placement.html
│                   │   │               │   ├── placement.options
│                   │   │               │   ├── placement.text
│                   │   │               │   ├── regexp_problem.html
│                   │   │               │   ├── regexp_problem.options
│                   │   │               │   ├── regexp_problem.text
│                   │   │               │   ├── without_backlink.html
│                   │   │               │   ├── without_backlink.options
│                   │   │               │   └── without_backlink.text
│                   │   │               ├── 05_html/
│                   │   │               │   ├── across_lines.html
│                   │   │               │   ├── across_lines.text
│                   │   │               │   ├── button.html
│                   │   │               │   ├── button.text
│                   │   │               │   ├── invalid.html
│                   │   │               │   ├── invalid.text
│                   │   │               │   ├── link_with_mailto.html
│                   │   │               │   ├── link_with_mailto.text
│                   │   │               │   ├── mark_element.html
│                   │   │               │   ├── mark_element.text
│                   │   │               │   ├── markdown_attr.html
│                   │   │               │   ├── markdown_attr.text
│                   │   │               │   ├── normal.html
│                   │   │               │   ├── normal.text
│                   │   │               │   ├── raw_span_elements.html
│                   │   │               │   ├── raw_span_elements.text
│                   │   │               │   ├── xml.html
│                   │   │               │   └── xml.text
│                   │   │               ├── abbreviations/
│                   │   │               │   ├── abbrev.html
│                   │   │               │   ├── abbrev.text
│                   │   │               │   ├── abbrev_defs.html
│                   │   │               │   ├── abbrev_defs.text
│                   │   │               │   ├── abbrev_in_html.html
│                   │   │               │   ├── abbrev_in_html.text
│                   │   │               │   ├── in_footnote.html
│                   │   │               │   └── in_footnote.text
│                   │   │               ├── autolinks/
│                   │   │               │   ├── url_links.html
│                   │   │               │   └── url_links.text
│                   │   │               ├── escaped_chars/
│                   │   │               │   ├── normal.html
│                   │   │               │   └── normal.text
│                   │   │               ├── extension/
│                   │   │               │   ├── comment.html
│                   │   │               │   ├── comment.text
│                   │   │               │   ├── ignored.html
│                   │   │               │   ├── ignored.text
│                   │   │               │   ├── nomarkdown.html
│                   │   │               │   ├── nomarkdown.text
│                   │   │               │   ├── options.html
│                   │   │               │   └── options.text
│                   │   │               ├── ial/
│                   │   │               │   ├── simple.html
│                   │   │               │   └── simple.text
│                   │   │               ├── line_breaks/
│                   │   │               │   ├── normal.html
│                   │   │               │   ├── normal.latex
│                   │   │               │   └── normal.text
│                   │   │               ├── math/
│                   │   │               │   ├── no_engine.html
│                   │   │               │   ├── no_engine.options
│                   │   │               │   ├── no_engine.text
│                   │   │               │   ├── normal.html
│                   │   │               │   └── normal.text
│                   │   │               └── text_substitutions/
│                   │   │                   ├── entities.html
│                   │   │                   ├── entities.options
│                   │   │                   ├── entities.text
│                   │   │                   ├── entities_as_char.html
│                   │   │                   ├── entities_as_char.options
│                   │   │                   ├── entities_as_char.text
│                   │   │                   ├── entities_as_input.html
│                   │   │                   ├── entities_as_input.options
│                   │   │                   ├── entities_as_input.text
│                   │   │                   ├── entities_numeric.html
│                   │   │                   ├── entities_numeric.options
│                   │   │                   ├── entities_numeric.text
│                   │   │                   ├── entities_symbolic.html
│                   │   │                   ├── entities_symbolic.options
│                   │   │                   ├── entities_symbolic.text
│                   │   │                   ├── greaterthan.html
│                   │   │                   ├── greaterthan.text
│                   │   │                   ├── lowerthan.html
│                   │   │                   ├── lowerthan.text
│                   │   │                   ├── typography.html
│                   │   │                   ├── typography.options
│                   │   │                   ├── typography.text
│                   │   │                   ├── typography_subst.html
│                   │   │                   ├── typography_subst.latex
│                   │   │                   ├── typography_subst.options
│                   │   │                   └── typography_subst.text
│                   │   ├── kramdown-parser-gfm-1.1.0/
│                   │   │   ├── CONTRIBUTERS
│                   │   │   ├── COPYING
│                   │   │   ├── VERSION
│                   │   │   ├── lib/
│                   │   │   │   ├── kramdown/
│                   │   │   │   │   └── parser/
│                   │   │   │   │       ├── gfm/
│                   │   │   │   │       │   └── options.rb
│                   │   │   │   │       └── gfm.rb
│                   │   │   │   └── kramdown-parser-gfm.rb
│                   │   │   └── test/
│                   │   │       ├── test_files.rb
│                   │   │       └── testcases/
│                   │   │           ├── atx_header.html
│                   │   │           ├── atx_header.text
│                   │   │           ├── backticks_syntax.html
│                   │   │           ├── backticks_syntax.options
│                   │   │           ├── backticks_syntax.text
│                   │   │           ├── codeblock_fenced.html
│                   │   │           ├── codeblock_fenced.options
│                   │   │           ├── codeblock_fenced.text
│                   │   │           ├── hard_line_breaks.html
│                   │   │           ├── hard_line_breaks.text
│                   │   │           ├── hard_line_breaks_off.html
│                   │   │           ├── hard_line_breaks_off.options
│                   │   │           ├── hard_line_breaks_off.text
│                   │   │           ├── header_ids.html
│                   │   │           ├── header_ids.options
│                   │   │           ├── header_ids.text
│                   │   │           ├── header_ids_with_prefix.html
│                   │   │           ├── header_ids_with_prefix.options
│                   │   │           ├── header_ids_with_prefix.text
│                   │   │           ├── no_typographic.html
│                   │   │           ├── no_typographic.options
│                   │   │           ├── no_typographic.text
│                   │   │           ├── paragraph_end-disabled.html
│                   │   │           ├── paragraph_end-disabled.options
│                   │   │           ├── paragraph_end-disabled.text
│                   │   │           ├── paragraph_end.html
│                   │   │           ├── paragraph_end.text
│                   │   │           ├── strikethrough.html
│                   │   │           ├── strikethrough.text
│                   │   │           ├── task_list.html
│                   │   │           ├── task_list.text
│                   │   │           ├── two_para_hard_line_breaks.html
│                   │   │           └── two_para_hard_line_breaks.text
│                   │   ├── liquid-4.0.4/
│                   │   │   ├── History.md
│                   │   │   ├── LICENSE
│                   │   │   ├── README.md
│                   │   │   ├── lib/
│                   │   │   │   ├── liquid/
│                   │   │   │   │   ├── block.rb
│                   │   │   │   │   ├── block_body.rb
│                   │   │   │   │   ├── condition.rb
│                   │   │   │   │   ├── context.rb
│                   │   │   │   │   ├── document.rb
│                   │   │   │   │   ├── drop.rb
│                   │   │   │   │   ├── errors.rb
│                   │   │   │   │   ├── expression.rb
│                   │   │   │   │   ├── extensions.rb
│                   │   │   │   │   ├── file_system.rb
│                   │   │   │   │   ├── forloop_drop.rb
│                   │   │   │   │   ├── i18n.rb
│                   │   │   │   │   ├── interrupts.rb
│                   │   │   │   │   ├── lexer.rb
│                   │   │   │   │   ├── locales/
│                   │   │   │   │   │   └── en.yml
│                   │   │   │   │   ├── parse_context.rb
│                   │   │   │   │   ├── parse_tree_visitor.rb
│                   │   │   │   │   ├── parser.rb
│                   │   │   │   │   ├── parser_switching.rb
│                   │   │   │   │   ├── profiler/
│                   │   │   │   │   │   └── hooks.rb
│                   │   │   │   │   ├── profiler.rb
│                   │   │   │   │   ├── range_lookup.rb
│                   │   │   │   │   ├── resource_limits.rb
│                   │   │   │   │   ├── standardfilters.rb
│                   │   │   │   │   ├── strainer.rb
│                   │   │   │   │   ├── tablerowloop_drop.rb
│                   │   │   │   │   ├── tag.rb
│                   │   │   │   │   ├── tags/
│                   │   │   │   │   │   ├── assign.rb
│                   │   │   │   │   │   ├── break.rb
│                   │   │   │   │   │   ├── capture.rb
│                   │   │   │   │   │   ├── case.rb
│                   │   │   │   │   │   ├── comment.rb
│                   │   │   │   │   │   ├── continue.rb
│                   │   │   │   │   │   ├── cycle.rb
│                   │   │   │   │   │   ├── decrement.rb
│                   │   │   │   │   │   ├── for.rb
│                   │   │   │   │   │   ├── if.rb
│                   │   │   │   │   │   ├── ifchanged.rb
│                   │   │   │   │   │   ├── include.rb
│                   │   │   │   │   │   ├── increment.rb
│                   │   │   │   │   │   ├── raw.rb
│                   │   │   │   │   │   ├── table_row.rb
│                   │   │   │   │   │   └── unless.rb
│                   │   │   │   │   ├── template.rb
│                   │   │   │   │   ├── tokenizer.rb
│                   │   │   │   │   ├── utils.rb
│                   │   │   │   │   ├── variable.rb
│                   │   │   │   │   ├── variable_lookup.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── liquid.rb
│                   │   │   └── test/
│                   │   │       ├── fixtures/
│                   │   │       │   └── en_locale.yml
│                   │   │       ├── integration/
│                   │   │       │   ├── assign_test.rb
│                   │   │       │   ├── blank_test.rb
│                   │   │       │   ├── block_test.rb
│                   │   │       │   ├── capture_test.rb
│                   │   │       │   ├── context_test.rb
│                   │   │       │   ├── document_test.rb
│                   │   │       │   ├── drop_test.rb
│                   │   │       │   ├── error_handling_test.rb
│                   │   │       │   ├── filter_test.rb
│                   │   │       │   ├── hash_ordering_test.rb
│                   │   │       │   ├── output_test.rb
│                   │   │       │   ├── parse_tree_visitor_test.rb
│                   │   │       │   ├── parsing_quirks_test.rb
│                   │   │       │   ├── render_profiling_test.rb
│                   │   │       │   ├── security_test.rb
│                   │   │       │   ├── standard_filter_test.rb
│                   │   │       │   ├── tags/
│                   │   │       │   │   ├── break_tag_test.rb
│                   │   │       │   │   ├── continue_tag_test.rb
│                   │   │       │   │   ├── for_tag_test.rb
│                   │   │       │   │   ├── if_else_tag_test.rb
│                   │   │       │   │   ├── include_tag_test.rb
│                   │   │       │   │   ├── increment_tag_test.rb
│                   │   │       │   │   ├── raw_tag_test.rb
│                   │   │       │   │   ├── standard_tag_test.rb
│                   │   │       │   │   ├── statements_test.rb
│                   │   │       │   │   ├── table_row_test.rb
│                   │   │       │   │   └── unless_else_tag_test.rb
│                   │   │       │   ├── template_test.rb
│                   │   │       │   ├── trim_mode_test.rb
│                   │   │       │   └── variable_test.rb
│                   │   │       ├── test_helper.rb
│                   │   │       └── unit/
│                   │   │           ├── block_unit_test.rb
│                   │   │           ├── condition_unit_test.rb
│                   │   │           ├── context_unit_test.rb
│                   │   │           ├── file_system_unit_test.rb
│                   │   │           ├── i18n_unit_test.rb
│                   │   │           ├── lexer_unit_test.rb
│                   │   │           ├── parser_unit_test.rb
│                   │   │           ├── regexp_unit_test.rb
│                   │   │           ├── strainer_unit_test.rb
│                   │   │           ├── tag_unit_test.rb
│                   │   │           ├── tags/
│                   │   │           │   ├── case_tag_unit_test.rb
│                   │   │           │   ├── for_tag_unit_test.rb
│                   │   │           │   └── if_tag_unit_test.rb
│                   │   │           ├── template_unit_test.rb
│                   │   │           ├── tokenizer_unit_test.rb
│                   │   │           └── variable_unit_test.rb
│                   │   ├── listen-3.10.0/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── CONTRIBUTING.md
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── bin/
│                   │   │   │   └── listen
│                   │   │   └── lib/
│                   │   │       ├── listen/
│                   │   │       │   ├── adapter/
│                   │   │       │   │   ├── base.rb
│                   │   │       │   │   ├── bsd.rb
│                   │   │       │   │   ├── config.rb
│                   │   │       │   │   ├── darwin.rb
│                   │   │       │   │   ├── linux.rb
│                   │   │       │   │   ├── polling.rb
│                   │   │       │   │   └── windows.rb
│                   │   │       │   ├── adapter.rb
│                   │   │       │   ├── backend.rb
│                   │   │       │   ├── change.rb
│                   │   │       │   ├── cli.rb
│                   │   │       │   ├── directory.rb
│                   │   │       │   ├── error.rb
│                   │   │       │   ├── event/
│                   │   │       │   │   ├── config.rb
│                   │   │       │   │   ├── loop.rb
│                   │   │       │   │   ├── processor.rb
│                   │   │       │   │   └── queue.rb
│                   │   │       │   ├── file.rb
│                   │   │       │   ├── fsm.rb
│                   │   │       │   ├── listener/
│                   │   │       │   │   └── config.rb
│                   │   │       │   ├── listener.rb
│                   │   │       │   ├── logger.rb
│                   │   │       │   ├── monotonic_time.rb
│                   │   │       │   ├── options.rb
│                   │   │       │   ├── queue_optimizer.rb
│                   │   │       │   ├── record/
│                   │   │       │   │   ├── entry.rb
│                   │   │       │   │   └── symlink_detector.rb
│                   │   │       │   ├── record.rb
│                   │   │       │   ├── silencer/
│                   │   │       │   │   └── controller.rb
│                   │   │       │   ├── silencer.rb
│                   │   │       │   ├── thread.rb
│                   │   │       │   └── version.rb
│                   │   │       └── listen.rb
│                   │   ├── logger-1.7.0/
│                   │   │   ├── .document
│                   │   │   ├── .rdoc_options
│                   │   │   ├── BSDL
│                   │   │   ├── COPYING
│                   │   │   ├── README.md
│                   │   │   └── lib/
│                   │   │       ├── logger/
│                   │   │       │   ├── errors.rb
│                   │   │       │   ├── formatter.rb
│                   │   │       │   ├── log_device.rb
│                   │   │       │   ├── period.rb
│                   │   │       │   ├── severity.rb
│                   │   │       │   └── version.rb
│                   │   │       └── logger.rb
│                   │   ├── mercenary-0.4.0/
│                   │   │   ├── .gitignore
│                   │   │   ├── .rspec
│                   │   │   ├── .rubocop.yml
│                   │   │   ├── .rubocop_todo.yml
│                   │   │   ├── .travis.yml
│                   │   │   ├── Gemfile
│                   │   │   ├── History.markdown
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── examples/
│                   │   │   │   ├── help_dialogue.rb
│                   │   │   │   ├── logging.rb
│                   │   │   │   └── trace.rb
│                   │   │   ├── lib/
│                   │   │   │   ├── mercenary/
│                   │   │   │   │   ├── command.rb
│                   │   │   │   │   ├── option.rb
│                   │   │   │   │   ├── presenter.rb
│                   │   │   │   │   ├── program.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── mercenary.rb
│                   │   │   ├── mercenary.gemspec
│                   │   │   ├── script/
│                   │   │   │   ├── bootstrap
│                   │   │   │   ├── cibuild
│                   │   │   │   ├── console
│                   │   │   │   ├── examples
│                   │   │   │   └── fmt
│                   │   │   └── spec/
│                   │   │       ├── command_spec.rb
│                   │   │       ├── option_spec.rb
│                   │   │       ├── presenter_spec.rb
│                   │   │       ├── program_spec.rb
│                   │   │       └── spec_helper.rb
│                   │   ├── pathutil-0.16.2/
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE
│                   │   │   ├── Rakefile
│                   │   │   └── lib/
│                   │   │       ├── pathutil/
│                   │   │       │   ├── helpers.rb
│                   │   │       │   └── version.rb
│                   │   │       └── pathutil.rb
│                   │   ├── public_suffix-5.1.1/
│                   │   │   ├── .yardopts
│                   │   │   ├── 2.0-Upgrade.md
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── SECURITY.md
│                   │   │   ├── data/
│                   │   │   │   └── list.txt
│                   │   │   └── lib/
│                   │   │       ├── public_suffix/
│                   │   │       │   ├── domain.rb
│                   │   │       │   ├── errors.rb
│                   │   │       │   ├── list.rb
│                   │   │       │   ├── rule.rb
│                   │   │       │   └── version.rb
│                   │   │       └── public_suffix.rb
│                   │   ├── rb-fsevent-0.11.2/
│                   │   │   ├── .gitignore
│                   │   │   ├── Gemfile
│                   │   │   ├── Guardfile
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── bin/
│                   │   │   │   └── fsevent_watch
│                   │   │   ├── ext/
│                   │   │   │   ├── LICENSE
│                   │   │   │   ├── fsevent_watch/
│                   │   │   │   │   ├── FSEventsFix.c
│                   │   │   │   │   ├── FSEventsFix.h
│                   │   │   │   │   ├── TSICTString.c
│                   │   │   │   │   ├── TSICTString.h
│                   │   │   │   │   ├── cli.c
│                   │   │   │   │   ├── cli.h
│                   │   │   │   │   ├── common.h
│                   │   │   │   │   ├── compat.c
│                   │   │   │   │   ├── compat.h
│                   │   │   │   │   ├── defines.h
│                   │   │   │   │   ├── main.c
│                   │   │   │   │   ├── signal_handlers.c
│                   │   │   │   │   └── signal_handlers.h
│                   │   │   │   └── rakefile.rb
│                   │   │   ├── lib/
│                   │   │   │   ├── otnetstring.rb
│                   │   │   │   ├── rb-fsevent/
│                   │   │   │   │   ├── fsevent.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── rb-fsevent.rb
│                   │   │   └── rb-fsevent.gemspec
│                   │   ├── rb-inotify-0.11.1/
│                   │   │   ├── .github/
│                   │   │   │   └── workflows/
│                   │   │   │       └── test.yaml
│                   │   │   ├── .gitignore
│                   │   │   ├── .yardopts
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE.md
│                   │   │   ├── README.md
│                   │   │   ├── lib/
│                   │   │   │   ├── rb-inotify/
│                   │   │   │   │   ├── errors.rb
│                   │   │   │   │   ├── event.rb
│                   │   │   │   │   ├── native/
│                   │   │   │   │   │   └── flags.rb
│                   │   │   │   │   ├── native.rb
│                   │   │   │   │   ├── notifier.rb
│                   │   │   │   │   ├── version.rb
│                   │   │   │   │   └── watcher.rb
│                   │   │   │   └── rb-inotify.rb
│                   │   │   ├── rb-inotify.gemspec
│                   │   │   └── spec/
│                   │   │       ├── inotify_spec.rb
│                   │   │       ├── notifier_spec.rb
│                   │   │       └── spec_helper.rb
│                   │   ├── rexml-3.4.4/
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── NEWS.md
│                   │   │   ├── README.md
│                   │   │   ├── doc/
│                   │   │   │   └── rexml/
│                   │   │   │       ├── context.rdoc
│                   │   │   │       ├── tasks/
│                   │   │   │       │   ├── rdoc/
│                   │   │   │       │   │   ├── child.rdoc
│                   │   │   │       │   │   ├── document.rdoc
│                   │   │   │       │   │   ├── element.rdoc
│                   │   │   │       │   │   ├── node.rdoc
│                   │   │   │       │   │   └── parent.rdoc
│                   │   │   │       │   └── tocs/
│                   │   │   │       │       ├── child_toc.rdoc
│                   │   │   │       │       ├── document_toc.rdoc
│                   │   │   │       │       ├── element_toc.rdoc
│                   │   │   │       │       ├── master_toc.rdoc
│                   │   │   │       │       ├── node_toc.rdoc
│                   │   │   │       │       └── parent_toc.rdoc
│                   │   │   │       └── tutorial.rdoc
│                   │   │   └── lib/
│                   │   │       ├── rexml/
│                   │   │       │   ├── attlistdecl.rb
│                   │   │       │   ├── attribute.rb
│                   │   │       │   ├── cdata.rb
│                   │   │       │   ├── child.rb
│                   │   │       │   ├── comment.rb
│                   │   │       │   ├── doctype.rb
│                   │   │       │   ├── document.rb
│                   │   │       │   ├── dtd/
│                   │   │       │   │   ├── attlistdecl.rb
│                   │   │       │   │   ├── dtd.rb
│                   │   │       │   │   ├── elementdecl.rb
│                   │   │       │   │   ├── entitydecl.rb
│                   │   │       │   │   └── notationdecl.rb
│                   │   │       │   ├── element.rb
│                   │   │       │   ├── encoding.rb
│                   │   │       │   ├── entity.rb
│                   │   │       │   ├── formatters/
│                   │   │       │   │   ├── default.rb
│                   │   │       │   │   ├── pretty.rb
│                   │   │       │   │   └── transitive.rb
│                   │   │       │   ├── functions.rb
│                   │   │       │   ├── instruction.rb
│                   │   │       │   ├── light/
│                   │   │       │   │   └── node.rb
│                   │   │       │   ├── namespace.rb
│                   │   │       │   ├── node.rb
│                   │   │       │   ├── output.rb
│                   │   │       │   ├── parent.rb
│                   │   │       │   ├── parseexception.rb
│                   │   │       │   ├── parsers/
│                   │   │       │   │   ├── baseparser.rb
│                   │   │       │   │   ├── lightparser.rb
│                   │   │       │   │   ├── pullparser.rb
│                   │   │       │   │   ├── sax2parser.rb
│                   │   │       │   │   ├── streamparser.rb
│                   │   │       │   │   ├── treeparser.rb
│                   │   │       │   │   ├── ultralightparser.rb
│                   │   │       │   │   └── xpathparser.rb
│                   │   │       │   ├── quickpath.rb
│                   │   │       │   ├── rexml.rb
│                   │   │       │   ├── sax2listener.rb
│                   │   │       │   ├── security.rb
│                   │   │       │   ├── source.rb
│                   │   │       │   ├── streamlistener.rb
│                   │   │       │   ├── text.rb
│                   │   │       │   ├── undefinednamespaceexception.rb
│                   │   │       │   ├── validation/
│                   │   │       │   │   ├── relaxng.rb
│                   │   │       │   │   ├── validation.rb
│                   │   │       │   │   └── validationexception.rb
│                   │   │       │   ├── xmldecl.rb
│                   │   │       │   ├── xmltokens.rb
│                   │   │       │   ├── xpath.rb
│                   │   │       │   └── xpath_parser.rb
│                   │   │       └── rexml.rb
│                   │   ├── rouge-3.30.0/
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE
│                   │   │   ├── bin/
│                   │   │   │   └── rougify
│                   │   │   ├── lib/
│                   │   │   │   ├── rouge/
│                   │   │   │   │   ├── cli.rb
│                   │   │   │   │   ├── demos/
│                   │   │   │   │   │   ├── abap
│                   │   │   │   │   │   ├── actionscript
│                   │   │   │   │   │   ├── ada
│                   │   │   │   │   │   ├── apache
│                   │   │   │   │   │   ├── apex
│                   │   │   │   │   │   ├── apiblueprint
│                   │   │   │   │   │   ├── applescript
│                   │   │   │   │   │   ├── armasm
│                   │   │   │   │   │   ├── augeas
│                   │   │   │   │   │   ├── awk
│                   │   │   │   │   │   ├── batchfile
│                   │   │   │   │   │   ├── bbcbasic
│                   │   │   │   │   │   ├── bibtex
│                   │   │   │   │   │   ├── biml
│                   │   │   │   │   │   ├── bpf
│                   │   │   │   │   │   ├── brainfuck
│                   │   │   │   │   │   ├── brightscript
│                   │   │   │   │   │   ├── bsl
│                   │   │   │   │   │   ├── c
│                   │   │   │   │   │   ├── ceylon
│                   │   │   │   │   │   ├── cfscript
│                   │   │   │   │   │   ├── clean
│                   │   │   │   │   │   ├── clojure
│                   │   │   │   │   │   ├── cmake
│                   │   │   │   │   │   ├── cmhg
│                   │   │   │   │   │   ├── coffeescript
│                   │   │   │   │   │   ├── common_lisp
│                   │   │   │   │   │   ├── conf
│                   │   │   │   │   │   ├── console
│                   │   │   │   │   │   ├── coq
│                   │   │   │   │   │   ├── cpp
│                   │   │   │   │   │   ├── crystal
│                   │   │   │   │   │   ├── csharp
│                   │   │   │   │   │   ├── css
│                   │   │   │   │   │   ├── csvs
│                   │   │   │   │   │   ├── cuda
│                   │   │   │   │   │   ├── cypher
│                   │   │   │   │   │   ├── cython
│                   │   │   │   │   │   ├── d
│                   │   │   │   │   │   ├── dafny
│                   │   │   │   │   │   ├── dart
│                   │   │   │   │   │   ├── datastudio
│                   │   │   │   │   │   ├── diff
│                   │   │   │   │   │   ├── digdag
│                   │   │   │   │   │   ├── docker
│                   │   │   │   │   │   ├── dot
│                   │   │   │   │   │   ├── ecl
│                   │   │   │   │   │   ├── eex
│                   │   │   │   │   │   ├── eiffel
│                   │   │   │   │   │   ├── elixir
│                   │   │   │   │   │   ├── elm
│                   │   │   │   │   │   ├── email
│                   │   │   │   │   │   ├── epp
│                   │   │   │   │   │   ├── erb
│                   │   │   │   │   │   ├── erlang
│                   │   │   │   │   │   ├── escape
│                   │   │   │   │   │   ├── factor
│                   │   │   │   │   │   ├── fluent
│                   │   │   │   │   │   ├── fortran
│                   │   │   │   │   │   ├── freefem
│                   │   │   │   │   │   ├── fsharp
│                   │   │   │   │   │   ├── gdscript
│                   │   │   │   │   │   ├── ghc-cmm
│                   │   │   │   │   │   ├── ghc-core
│                   │   │   │   │   │   ├── gherkin
│                   │   │   │   │   │   ├── glsl
│                   │   │   │   │   │   ├── go
│                   │   │   │   │   │   ├── gradle
│                   │   │   │   │   │   ├── graphql
│                   │   │   │   │   │   ├── groovy
│                   │   │   │   │   │   ├── hack
│                   │   │   │   │   │   ├── haml
│                   │   │   │   │   │   ├── handlebars
│                   │   │   │   │   │   ├── haskell
│                   │   │   │   │   │   ├── haxe
│                   │   │   │   │   │   ├── hcl
│                   │   │   │   │   │   ├── hlsl
│                   │   │   │   │   │   ├── hocon
│                   │   │   │   │   │   ├── hql
│                   │   │   │   │   │   ├── html
│                   │   │   │   │   │   ├── http
│                   │   │   │   │   │   ├── hylang
│                   │   │   │   │   │   ├── idlang
│                   │   │   │   │   │   ├── idris
│                   │   │   │   │   │   ├── igorpro
│                   │   │   │   │   │   ├── ini
│                   │   │   │   │   │   ├── io
│                   │   │   │   │   │   ├── irb
│                   │   │   │   │   │   ├── irb_output
│                   │   │   │   │   │   ├── isabelle
│                   │   │   │   │   │   ├── isbl
│                   │   │   │   │   │   ├── j
│                   │   │   │   │   │   ├── janet
│                   │   │   │   │   │   ├── java
│                   │   │   │   │   │   ├── javascript
│                   │   │   │   │   │   ├── jinja
│                   │   │   │   │   │   ├── jsl
│                   │   │   │   │   │   ├── json
│                   │   │   │   │   │   ├── json-doc
│                   │   │   │   │   │   ├── jsonnet
│                   │   │   │   │   │   ├── jsp
│                   │   │   │   │   │   ├── jsx
│                   │   │   │   │   │   ├── julia
│                   │   │   │   │   │   ├── kotlin
│                   │   │   │   │   │   ├── lasso
│                   │   │   │   │   │   ├── lean
│                   │   │   │   │   │   ├── liquid
│                   │   │   │   │   │   ├── literate_coffeescript
│                   │   │   │   │   │   ├── literate_haskell
│                   │   │   │   │   │   ├── livescript
│                   │   │   │   │   │   ├── llvm
│                   │   │   │   │   │   ├── lua
│                   │   │   │   │   │   ├── lustre
│                   │   │   │   │   │   ├── lutin
│                   │   │   │   │   │   ├── m68k
│                   │   │   │   │   │   ├── magik
│                   │   │   │   │   │   ├── make
│                   │   │   │   │   │   ├── markdown
│                   │   │   │   │   │   ├── mason
│                   │   │   │   │   │   ├── mathematica
│                   │   │   │   │   │   ├── matlab
│                   │   │   │   │   │   ├── meson
│                   │   │   │   │   │   ├── minizinc
│                   │   │   │   │   │   ├── moonscript
│                   │   │   │   │   │   ├── mosel
│                   │   │   │   │   │   ├── msgtrans
│                   │   │   │   │   │   ├── mxml
│                   │   │   │   │   │   ├── nasm
│                   │   │   │   │   │   ├── nesasm
│                   │   │   │   │   │   ├── nginx
│                   │   │   │   │   │   ├── nial
│                   │   │   │   │   │   ├── nim
│                   │   │   │   │   │   ├── nix
│                   │   │   │   │   │   ├── objective_c
│                   │   │   │   │   │   ├── objective_cpp
│                   │   │   │   │   │   ├── ocaml
│                   │   │   │   │   │   ├── ocl
│                   │   │   │   │   │   ├── openedge
│                   │   │   │   │   │   ├── opentype_feature_file
│                   │   │   │   │   │   ├── pascal
│                   │   │   │   │   │   ├── perl
│                   │   │   │   │   │   ├── php
│                   │   │   │   │   │   ├── plaintext
│                   │   │   │   │   │   ├── plist
│                   │   │   │   │   │   ├── plsql
│                   │   │   │   │   │   ├── pony
│                   │   │   │   │   │   ├── postscript
│                   │   │   │   │   │   ├── powershell
│                   │   │   │   │   │   ├── praat
│                   │   │   │   │   │   ├── prolog
│                   │   │   │   │   │   ├── prometheus
│                   │   │   │   │   │   ├── properties
│                   │   │   │   │   │   ├── protobuf
│                   │   │   │   │   │   ├── puppet
│                   │   │   │   │   │   ├── python
│                   │   │   │   │   │   ├── q
│                   │   │   │   │   │   ├── qml
│                   │   │   │   │   │   ├── r
│                   │   │   │   │   │   ├── racket
│                   │   │   │   │   │   ├── reasonml
│                   │   │   │   │   │   ├── rego
│                   │   │   │   │   │   ├── rescript
│                   │   │   │   │   │   ├── robot_framework
│                   │   │   │   │   │   ├── ruby
│                   │   │   │   │   │   ├── rust
│                   │   │   │   │   │   ├── sas
│                   │   │   │   │   │   ├── sass
│                   │   │   │   │   │   ├── scala
│                   │   │   │   │   │   ├── scheme
│                   │   │   │   │   │   ├── scss
│                   │   │   │   │   │   ├── sed
│                   │   │   │   │   │   ├── shell
│                   │   │   │   │   │   ├── sieve
│                   │   │   │   │   │   ├── slice
│                   │   │   │   │   │   ├── slim
│                   │   │   │   │   │   ├── smalltalk
│                   │   │   │   │   │   ├── smarty
│                   │   │   │   │   │   ├── sml
│                   │   │   │   │   │   ├── solidity
│                   │   │   │   │   │   ├── sparql
│                   │   │   │   │   │   ├── sqf
│                   │   │   │   │   │   ├── sql
│                   │   │   │   │   │   ├── ssh
│                   │   │   │   │   │   ├── stan
│                   │   │   │   │   │   ├── stata
│                   │   │   │   │   │   ├── supercollider
│                   │   │   │   │   │   ├── swift
│                   │   │   │   │   │   ├── systemd
│                   │   │   │   │   │   ├── syzlang
│                   │   │   │   │   │   ├── syzprog
│                   │   │   │   │   │   ├── tap
│                   │   │   │   │   │   ├── tcl
│                   │   │   │   │   │   ├── terraform
│                   │   │   │   │   │   ├── tex
│                   │   │   │   │   │   ├── toml
│                   │   │   │   │   │   ├── tsx
│                   │   │   │   │   │   ├── ttcn3
│                   │   │   │   │   │   ├── tulip
│                   │   │   │   │   │   ├── turtle
│                   │   │   │   │   │   ├── twig
│                   │   │   │   │   │   ├── typescript
│                   │   │   │   │   │   ├── vala
│                   │   │   │   │   │   ├── vb
│                   │   │   │   │   │   ├── vcl
│                   │   │   │   │   │   ├── velocity
│                   │   │   │   │   │   ├── verilog
│                   │   │   │   │   │   ├── vhdl
│                   │   │   │   │   │   ├── viml
│                   │   │   │   │   │   ├── vue
│                   │   │   │   │   │   ├── wollok
│                   │   │   │   │   │   ├── xml
│                   │   │   │   │   │   ├── xojo
│                   │   │   │   │   │   ├── xpath
│                   │   │   │   │   │   ├── xquery
│                   │   │   │   │   │   ├── yaml
│                   │   │   │   │   │   ├── yang
│                   │   │   │   │   │   └── zig
│                   │   │   │   │   ├── formatter.rb
│                   │   │   │   │   ├── formatters/
│                   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   ├── html_inline.rb
│                   │   │   │   │   │   ├── html_legacy.rb
│                   │   │   │   │   │   ├── html_line_highlighter.rb
│                   │   │   │   │   │   ├── html_line_table.rb
│                   │   │   │   │   │   ├── html_linewise.rb
│                   │   │   │   │   │   ├── html_pygments.rb
│                   │   │   │   │   │   ├── html_table.rb
│                   │   │   │   │   │   ├── null.rb
│                   │   │   │   │   │   ├── terminal256.rb
│                   │   │   │   │   │   ├── terminal_truecolor.rb
│                   │   │   │   │   │   └── tex.rb
│                   │   │   │   │   ├── guesser.rb
│                   │   │   │   │   ├── guessers/
│                   │   │   │   │   │   ├── disambiguation.rb
│                   │   │   │   │   │   ├── filename.rb
│                   │   │   │   │   │   ├── glob_mapping.rb
│                   │   │   │   │   │   ├── mimetype.rb
│                   │   │   │   │   │   ├── modeline.rb
│                   │   │   │   │   │   ├── source.rb
│                   │   │   │   │   │   └── util.rb
│                   │   │   │   │   ├── lexer.rb
│                   │   │   │   │   ├── lexers/
│                   │   │   │   │   │   ├── abap.rb
│                   │   │   │   │   │   ├── actionscript.rb
│                   │   │   │   │   │   ├── ada.rb
│                   │   │   │   │   │   ├── apache/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── apache.rb
│                   │   │   │   │   │   ├── apex.rb
│                   │   │   │   │   │   ├── apiblueprint.rb
│                   │   │   │   │   │   ├── apple_script.rb
│                   │   │   │   │   │   ├── armasm.rb
│                   │   │   │   │   │   ├── augeas.rb
│                   │   │   │   │   │   ├── awk.rb
│                   │   │   │   │   │   ├── batchfile.rb
│                   │   │   │   │   │   ├── bbcbasic.rb
│                   │   │   │   │   │   ├── bibtex.rb
│                   │   │   │   │   │   ├── biml.rb
│                   │   │   │   │   │   ├── bpf.rb
│                   │   │   │   │   │   ├── brainfuck.rb
│                   │   │   │   │   │   ├── brightscript.rb
│                   │   │   │   │   │   ├── bsl.rb
│                   │   │   │   │   │   ├── c.rb
│                   │   │   │   │   │   ├── ceylon.rb
│                   │   │   │   │   │   ├── cfscript.rb
│                   │   │   │   │   │   ├── clean.rb
│                   │   │   │   │   │   ├── clojure.rb
│                   │   │   │   │   │   ├── cmake.rb
│                   │   │   │   │   │   ├── cmhg.rb
│                   │   │   │   │   │   ├── coffeescript.rb
│                   │   │   │   │   │   ├── common_lisp.rb
│                   │   │   │   │   │   ├── conf.rb
│                   │   │   │   │   │   ├── console.rb
│                   │   │   │   │   │   ├── coq.rb
│                   │   │   │   │   │   ├── cpp.rb
│                   │   │   │   │   │   ├── crystal.rb
│                   │   │   │   │   │   ├── csharp.rb
│                   │   │   │   │   │   ├── css.rb
│                   │   │   │   │   │   ├── csvs.rb
│                   │   │   │   │   │   ├── cuda.rb
│                   │   │   │   │   │   ├── cypher.rb
│                   │   │   │   │   │   ├── cython.rb
│                   │   │   │   │   │   ├── d.rb
│                   │   │   │   │   │   ├── dafny.rb
│                   │   │   │   │   │   ├── dart.rb
│                   │   │   │   │   │   ├── datastudio.rb
│                   │   │   │   │   │   ├── diff.rb
│                   │   │   │   │   │   ├── digdag.rb
│                   │   │   │   │   │   ├── docker.rb
│                   │   │   │   │   │   ├── dot.rb
│                   │   │   │   │   │   ├── ecl.rb
│                   │   │   │   │   │   ├── eex.rb
│                   │   │   │   │   │   ├── eiffel.rb
│                   │   │   │   │   │   ├── elixir.rb
│                   │   │   │   │   │   ├── elm.rb
│                   │   │   │   │   │   ├── email.rb
│                   │   │   │   │   │   ├── epp.rb
│                   │   │   │   │   │   ├── erb.rb
│                   │   │   │   │   │   ├── erlang.rb
│                   │   │   │   │   │   ├── escape.rb
│                   │   │   │   │   │   ├── factor.rb
│                   │   │   │   │   │   ├── fluent.rb
│                   │   │   │   │   │   ├── fortran.rb
│                   │   │   │   │   │   ├── freefem.rb
│                   │   │   │   │   │   ├── fsharp.rb
│                   │   │   │   │   │   ├── gdscript.rb
│                   │   │   │   │   │   ├── ghc_cmm.rb
│                   │   │   │   │   │   ├── ghc_core.rb
│                   │   │   │   │   │   ├── gherkin/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── gherkin.rb
│                   │   │   │   │   │   ├── glsl.rb
│                   │   │   │   │   │   ├── go.rb
│                   │   │   │   │   │   ├── gradle.rb
│                   │   │   │   │   │   ├── graphql.rb
│                   │   │   │   │   │   ├── groovy.rb
│                   │   │   │   │   │   ├── hack.rb
│                   │   │   │   │   │   ├── haml.rb
│                   │   │   │   │   │   ├── handlebars.rb
│                   │   │   │   │   │   ├── haskell.rb
│                   │   │   │   │   │   ├── haxe.rb
│                   │   │   │   │   │   ├── hcl.rb
│                   │   │   │   │   │   ├── hlsl.rb
│                   │   │   │   │   │   ├── hocon.rb
│                   │   │   │   │   │   ├── hql.rb
│                   │   │   │   │   │   ├── html.rb
│                   │   │   │   │   │   ├── http.rb
│                   │   │   │   │   │   ├── hylang.rb
│                   │   │   │   │   │   ├── idlang.rb
│                   │   │   │   │   │   ├── idris.rb
│                   │   │   │   │   │   ├── igorpro.rb
│                   │   │   │   │   │   ├── ini.rb
│                   │   │   │   │   │   ├── io.rb
│                   │   │   │   │   │   ├── irb.rb
│                   │   │   │   │   │   ├── isabelle.rb
│                   │   │   │   │   │   ├── isbl/
│                   │   │   │   │   │   │   └── builtins.rb
│                   │   │   │   │   │   ├── isbl.rb
│                   │   │   │   │   │   ├── j.rb
│                   │   │   │   │   │   ├── janet.rb
│                   │   │   │   │   │   ├── java.rb
│                   │   │   │   │   │   ├── javascript.rb
│                   │   │   │   │   │   ├── jinja.rb
│                   │   │   │   │   │   ├── jsl.rb
│                   │   │   │   │   │   ├── json.rb
│                   │   │   │   │   │   ├── json_doc.rb
│                   │   │   │   │   │   ├── jsonnet.rb
│                   │   │   │   │   │   ├── jsp.rb
│                   │   │   │   │   │   ├── jsx.rb
│                   │   │   │   │   │   ├── julia.rb
│                   │   │   │   │   │   ├── kotlin.rb
│                   │   │   │   │   │   ├── lasso/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── lasso.rb
│                   │   │   │   │   │   ├── lean.rb
│                   │   │   │   │   │   ├── liquid.rb
│                   │   │   │   │   │   ├── literate_coffeescript.rb
│                   │   │   │   │   │   ├── literate_haskell.rb
│                   │   │   │   │   │   ├── livescript.rb
│                   │   │   │   │   │   ├── llvm/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── llvm.rb
│                   │   │   │   │   │   ├── lua/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── lua.rb
│                   │   │   │   │   │   ├── lustre.rb
│                   │   │   │   │   │   ├── lutin.rb
│                   │   │   │   │   │   ├── m68k.rb
│                   │   │   │   │   │   ├── magik.rb
│                   │   │   │   │   │   ├── make.rb
│                   │   │   │   │   │   ├── markdown.rb
│                   │   │   │   │   │   ├── mason.rb
│                   │   │   │   │   │   ├── mathematica/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── mathematica.rb
│                   │   │   │   │   │   ├── matlab/
│                   │   │   │   │   │   │   ├── builtins.rb
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── matlab.rb
│                   │   │   │   │   │   ├── meson.rb
│                   │   │   │   │   │   ├── minizinc.rb
│                   │   │   │   │   │   ├── moonscript.rb
│                   │   │   │   │   │   ├── mosel.rb
│                   │   │   │   │   │   ├── msgtrans.rb
│                   │   │   │   │   │   ├── mxml.rb
│                   │   │   │   │   │   ├── nasm.rb
│                   │   │   │   │   │   ├── nesasm.rb
│                   │   │   │   │   │   ├── nginx.rb
│                   │   │   │   │   │   ├── nial.rb
│                   │   │   │   │   │   ├── nim.rb
│                   │   │   │   │   │   ├── nix.rb
│                   │   │   │   │   │   ├── objective_c/
│                   │   │   │   │   │   │   └── common.rb
│                   │   │   │   │   │   ├── objective_c.rb
│                   │   │   │   │   │   ├── objective_cpp.rb
│                   │   │   │   │   │   ├── ocaml/
│                   │   │   │   │   │   │   └── common.rb
│                   │   │   │   │   │   ├── ocaml.rb
│                   │   │   │   │   │   ├── ocl.rb
│                   │   │   │   │   │   ├── openedge.rb
│                   │   │   │   │   │   ├── opentype_feature_file.rb
│                   │   │   │   │   │   ├── pascal.rb
│                   │   │   │   │   │   ├── perl.rb
│                   │   │   │   │   │   ├── php/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── php.rb
│                   │   │   │   │   │   ├── plain_text.rb
│                   │   │   │   │   │   ├── plist.rb
│                   │   │   │   │   │   ├── plsql.rb
│                   │   │   │   │   │   ├── pony.rb
│                   │   │   │   │   │   ├── postscript.rb
│                   │   │   │   │   │   ├── powershell.rb
│                   │   │   │   │   │   ├── praat.rb
│                   │   │   │   │   │   ├── prolog.rb
│                   │   │   │   │   │   ├── prometheus.rb
│                   │   │   │   │   │   ├── properties.rb
│                   │   │   │   │   │   ├── protobuf.rb
│                   │   │   │   │   │   ├── puppet.rb
│                   │   │   │   │   │   ├── python.rb
│                   │   │   │   │   │   ├── q.rb
│                   │   │   │   │   │   ├── qml.rb
│                   │   │   │   │   │   ├── r.rb
│                   │   │   │   │   │   ├── racket.rb
│                   │   │   │   │   │   ├── reasonml.rb
│                   │   │   │   │   │   ├── rego.rb
│                   │   │   │   │   │   ├── rescript.rb
│                   │   │   │   │   │   ├── robot_framework.rb
│                   │   │   │   │   │   ├── ruby.rb
│                   │   │   │   │   │   ├── rust.rb
│                   │   │   │   │   │   ├── sas.rb
│                   │   │   │   │   │   ├── sass/
│                   │   │   │   │   │   │   └── common.rb
│                   │   │   │   │   │   ├── sass.rb
│                   │   │   │   │   │   ├── scala.rb
│                   │   │   │   │   │   ├── scheme.rb
│                   │   │   │   │   │   ├── scss.rb
│                   │   │   │   │   │   ├── sed.rb
│                   │   │   │   │   │   ├── shell.rb
│                   │   │   │   │   │   ├── sieve.rb
│                   │   │   │   │   │   ├── slice.rb
│                   │   │   │   │   │   ├── slim.rb
│                   │   │   │   │   │   ├── smalltalk.rb
│                   │   │   │   │   │   ├── smarty.rb
│                   │   │   │   │   │   ├── sml.rb
│                   │   │   │   │   │   ├── solidity.rb
│                   │   │   │   │   │   ├── sparql.rb
│                   │   │   │   │   │   ├── sqf/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── sqf.rb
│                   │   │   │   │   │   ├── sql.rb
│                   │   │   │   │   │   ├── ssh.rb
│                   │   │   │   │   │   ├── stan.rb
│                   │   │   │   │   │   ├── stata.rb
│                   │   │   │   │   │   ├── supercollider.rb
│                   │   │   │   │   │   ├── swift.rb
│                   │   │   │   │   │   ├── systemd.rb
│                   │   │   │   │   │   ├── syzlang.rb
│                   │   │   │   │   │   ├── syzprog.rb
│                   │   │   │   │   │   ├── tap.rb
│                   │   │   │   │   │   ├── tcl.rb
│                   │   │   │   │   │   ├── terraform.rb
│                   │   │   │   │   │   ├── tex.rb
│                   │   │   │   │   │   ├── toml.rb
│                   │   │   │   │   │   ├── tsx.rb
│                   │   │   │   │   │   ├── ttcn3.rb
│                   │   │   │   │   │   ├── tulip.rb
│                   │   │   │   │   │   ├── turtle.rb
│                   │   │   │   │   │   ├── twig.rb
│                   │   │   │   │   │   ├── typescript/
│                   │   │   │   │   │   │   └── common.rb
│                   │   │   │   │   │   ├── typescript.rb
│                   │   │   │   │   │   ├── vala.rb
│                   │   │   │   │   │   ├── varnish.rb
│                   │   │   │   │   │   ├── vb.rb
│                   │   │   │   │   │   ├── velocity.rb
│                   │   │   │   │   │   ├── verilog.rb
│                   │   │   │   │   │   ├── vhdl.rb
│                   │   │   │   │   │   ├── viml/
│                   │   │   │   │   │   │   └── keywords.rb
│                   │   │   │   │   │   ├── viml.rb
│                   │   │   │   │   │   ├── vue.rb
│                   │   │   │   │   │   ├── wollok.rb
│                   │   │   │   │   │   ├── xml.rb
│                   │   │   │   │   │   ├── xojo.rb
│                   │   │   │   │   │   ├── xpath.rb
│                   │   │   │   │   │   ├── xquery.rb
│                   │   │   │   │   │   ├── yaml.rb
│                   │   │   │   │   │   ├── yang.rb
│                   │   │   │   │   │   └── zig.rb
│                   │   │   │   │   ├── plugins/
│                   │   │   │   │   │   └── redcarpet.rb
│                   │   │   │   │   ├── regex_lexer.rb
│                   │   │   │   │   ├── template_lexer.rb
│                   │   │   │   │   ├── tex_theme_renderer.rb
│                   │   │   │   │   ├── text_analyzer.rb
│                   │   │   │   │   ├── theme.rb
│                   │   │   │   │   ├── themes/
│                   │   │   │   │   │   ├── base16.rb
│                   │   │   │   │   │   ├── bw.rb
│                   │   │   │   │   │   ├── colorful.rb
│                   │   │   │   │   │   ├── github.rb
│                   │   │   │   │   │   ├── gruvbox.rb
│                   │   │   │   │   │   ├── igor_pro.rb
│                   │   │   │   │   │   ├── magritte.rb
│                   │   │   │   │   │   ├── molokai.rb
│                   │   │   │   │   │   ├── monokai.rb
│                   │   │   │   │   │   ├── monokai_sublime.rb
│                   │   │   │   │   │   ├── pastie.rb
│                   │   │   │   │   │   ├── thankful_eyes.rb
│                   │   │   │   │   │   └── tulip.rb
│                   │   │   │   │   ├── token.rb
│                   │   │   │   │   ├── util.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── rouge.rb
│                   │   │   └── rouge.gemspec
│                   │   ├── safe_yaml-1.0.5/
│                   │   │   ├── .gitignore
│                   │   │   ├── .travis.yml
│                   │   │   ├── CHANGES.md
│                   │   │   ├── Gemfile
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── bin/
│                   │   │   │   └── safe_yaml
│                   │   │   ├── bundle_install_all_ruby_versions.sh
│                   │   │   ├── lib/
│                   │   │   │   ├── safe_yaml/
│                   │   │   │   │   ├── deep.rb
│                   │   │   │   │   ├── libyaml_checker.rb
│                   │   │   │   │   ├── load.rb
│                   │   │   │   │   ├── parse/
│                   │   │   │   │   │   ├── date.rb
│                   │   │   │   │   │   ├── hexadecimal.rb
│                   │   │   │   │   │   └── sexagesimal.rb
│                   │   │   │   │   ├── psych_handler.rb
│                   │   │   │   │   ├── psych_resolver.rb
│                   │   │   │   │   ├── resolver.rb
│                   │   │   │   │   ├── safe_to_ruby_visitor.rb
│                   │   │   │   │   ├── store.rb
│                   │   │   │   │   ├── syck_hack.rb
│                   │   │   │   │   ├── syck_node_monkeypatch.rb
│                   │   │   │   │   ├── syck_resolver.rb
│                   │   │   │   │   ├── transform/
│                   │   │   │   │   │   ├── to_boolean.rb
│                   │   │   │   │   │   ├── to_date.rb
│                   │   │   │   │   │   ├── to_float.rb
│                   │   │   │   │   │   ├── to_integer.rb
│                   │   │   │   │   │   ├── to_nil.rb
│                   │   │   │   │   │   ├── to_symbol.rb
│                   │   │   │   │   │   └── transformation_map.rb
│                   │   │   │   │   ├── transform.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── safe_yaml.rb
│                   │   │   ├── run_specs_all_ruby_versions.sh
│                   │   │   ├── safe_yaml.gemspec
│                   │   │   └── spec/
│                   │   │       ├── exploit.1.9.2.yaml
│                   │   │       ├── exploit.1.9.3.yaml
│                   │   │       ├── issue48.txt
│                   │   │       ├── issue49.yml
│                   │   │       ├── libyaml_checker_spec.rb
│                   │   │       ├── psych_resolver_spec.rb
│                   │   │       ├── resolver_specs.rb
│                   │   │       ├── safe_yaml_spec.rb
│                   │   │       ├── spec_helper.rb
│                   │   │       ├── store_spec.rb
│                   │   │       ├── support/
│                   │   │       │   └── exploitable_back_door.rb
│                   │   │       ├── syck_resolver_spec.rb
│                   │   │       ├── transform/
│                   │   │       │   ├── base64_spec.rb
│                   │   │       │   ├── to_date_spec.rb
│                   │   │       │   ├── to_float_spec.rb
│                   │   │       │   ├── to_integer_spec.rb
│                   │   │       │   └── to_symbol_spec.rb
│                   │   │       └── yaml_spec.rb
│                   │   ├── sass-embedded-1.58.3-arm64-darwin/
│                   │   │   ├── LICENSE
│                   │   │   ├── README.md
│                   │   │   ├── ext/
│                   │   │   │   └── sass/
│                   │   │   │       ├── embedded.rb
│                   │   │   │       ├── embedded_sass_pb.rb
│                   │   │   │       └── sass_embedded/
│                   │   │   │           ├── dart-sass-embedded
│                   │   │   │           └── src/
│                   │   │   │               ├── LICENSE
│                   │   │   │               ├── dart
│                   │   │   │               └── dart-sass-embedded.snapshot
│                   │   │   └── lib/
│                   │   │       ├── sass/
│                   │   │       │   ├── compile_error.rb
│                   │   │       │   ├── compile_result.rb
│                   │   │       │   ├── embedded/
│                   │   │       │   │   ├── async.rb
│                   │   │       │   │   ├── channel.rb
│                   │   │       │   │   ├── compiler.rb
│                   │   │       │   │   ├── dispatcher.rb
│                   │   │       │   │   ├── host/
│                   │   │       │   │   │   ├── function_registry.rb
│                   │   │       │   │   │   ├── importer_registry.rb
│                   │   │       │   │   │   ├── logger_registry.rb
│                   │   │       │   │   │   └── value_protofier.rb
│                   │   │       │   │   ├── host.rb
│                   │   │       │   │   ├── protofier.rb
│                   │   │       │   │   ├── structifier.rb
│                   │   │       │   │   ├── varint.rb
│                   │   │       │   │   └── version.rb
│                   │   │       │   ├── embedded.rb
│                   │   │       │   ├── logger/
│                   │   │       │   │   ├── silent.rb
│                   │   │       │   │   ├── source_location.rb
│                   │   │       │   │   └── source_span.rb
│                   │   │       │   ├── script_error.rb
│                   │   │       │   ├── value/
│                   │   │       │   │   ├── argument_list.rb
│                   │   │       │   │   ├── boolean.rb
│                   │   │       │   │   ├── color.rb
│                   │   │       │   │   ├── function.rb
│                   │   │       │   │   ├── fuzzy_math.rb
│                   │   │       │   │   ├── list.rb
│                   │   │       │   │   ├── map.rb
│                   │   │       │   │   ├── null.rb
│                   │   │       │   │   ├── number/
│                   │   │       │   │   │   └── unit.rb
│                   │   │       │   │   ├── number.rb
│                   │   │       │   │   └── string.rb
│                   │   │       │   └── value.rb
│                   │   │       └── sass-embedded.rb
│                   │   ├── terminal-table-3.0.2/
│                   │   │   ├── .github/
│                   │   │   │   └── workflows/
│                   │   │   │       └── ci.yml
│                   │   │   ├── .gitignore
│                   │   │   ├── Gemfile
│                   │   │   ├── History.rdoc
│                   │   │   ├── LICENSE.txt
│                   │   │   ├── Manifest
│                   │   │   ├── README.md
│                   │   │   ├── Rakefile
│                   │   │   ├── Todo.rdoc
│                   │   │   ├── examples/
│                   │   │   │   ├── data.csv
│                   │   │   │   ├── examples.rb
│                   │   │   │   ├── examples_unicode.rb
│                   │   │   │   ├── issue100.rb
│                   │   │   │   ├── issue111.rb
│                   │   │   │   ├── issue118.rb
│                   │   │   │   ├── issue95.rb
│                   │   │   │   ├── show_csv_table.rb
│                   │   │   │   └── strong_separator.rb
│                   │   │   ├── lib/
│                   │   │   │   ├── terminal-table/
│                   │   │   │   │   ├── cell.rb
│                   │   │   │   │   ├── import.rb
│                   │   │   │   │   ├── row.rb
│                   │   │   │   │   ├── separator.rb
│                   │   │   │   │   ├── style.rb
│                   │   │   │   │   ├── table.rb
│                   │   │   │   │   ├── table_helper.rb
│                   │   │   │   │   ├── util.rb
│                   │   │   │   │   └── version.rb
│                   │   │   │   └── terminal-table.rb
│                   │   │   └── terminal-table.gemspec
│                   │   ├── unicode-display_width-2.6.0/
│                   │   │   ├── CHANGELOG.md
│                   │   │   ├── MIT-LICENSE.txt
│                   │   │   ├── README.md
│                   │   │   ├── data/
│                   │   │   │   └── display_width.marshal.gz
│                   │   │   └── lib/
│                   │   │       └── unicode/
│                   │   │           ├── display_width/
│                   │   │           │   ├── constants.rb
│                   │   │           │   ├── index.rb
│                   │   │           │   ├── no_string_ext.rb
│                   │   │           │   └── string_ext.rb
│                   │   │           └── display_width.rb
│                   │   └── webrick-1.9.2/
│                   │       ├── Gemfile
│                   │       ├── LICENSE.txt
│                   │       ├── README.md
│                   │       ├── Rakefile
│                   │       ├── lib/
│                   │       │   ├── webrick/
│                   │       │   │   ├── accesslog.rb
│                   │       │   │   ├── cgi.rb
│                   │       │   │   ├── compat.rb
│                   │       │   │   ├── config.rb
│                   │       │   │   ├── cookie.rb
│                   │       │   │   ├── htmlutils.rb
│                   │       │   │   ├── httpauth/
│                   │       │   │   │   ├── authenticator.rb
│                   │       │   │   │   ├── basicauth.rb
│                   │       │   │   │   ├── digestauth.rb
│                   │       │   │   │   ├── htdigest.rb
│                   │       │   │   │   ├── htgroup.rb
│                   │       │   │   │   ├── htpasswd.rb
│                   │       │   │   │   └── userdb.rb
│                   │       │   │   ├── httpauth.rb
│                   │       │   │   ├── httpproxy.rb
│                   │       │   │   ├── httprequest.rb
│                   │       │   │   ├── httpresponse.rb
│                   │       │   │   ├── https.rb
│                   │       │   │   ├── httpserver.rb
│                   │       │   │   ├── httpservlet/
│                   │       │   │   │   ├── abstract.rb
│                   │       │   │   │   ├── cgi_runner.rb
│                   │       │   │   │   ├── cgihandler.rb
│                   │       │   │   │   ├── erbhandler.rb
│                   │       │   │   │   ├── filehandler.rb
│                   │       │   │   │   └── prochandler.rb
│                   │       │   │   ├── httpservlet.rb
│                   │       │   │   ├── httpstatus.rb
│                   │       │   │   ├── httputils.rb
│                   │       │   │   ├── httpversion.rb
│                   │       │   │   ├── log.rb
│                   │       │   │   ├── server.rb
│                   │       │   │   ├── ssl.rb
│                   │       │   │   ├── utils.rb
│                   │       │   │   └── version.rb
│                   │       │   └── webrick.rb
│                   │       ├── sig/
│                   │       │   ├── accesslog.rbs
│                   │       │   ├── cgi.rbs
│                   │       │   ├── compat.rbs
│                   │       │   ├── config.rbs
│                   │       │   ├── cookie.rbs
│                   │       │   ├── htmlutils.rbs
│                   │       │   ├── httpauth/
│                   │       │   │   ├── authenticator.rbs
│                   │       │   │   ├── basicauth.rbs
│                   │       │   │   ├── digestauth.rbs
│                   │       │   │   ├── htdigest.rbs
│                   │       │   │   ├── htgroup.rbs
│                   │       │   │   ├── htpasswd.rbs
│                   │       │   │   └── userdb.rbs
│                   │       │   ├── httpauth.rbs
│                   │       │   ├── httpproxy.rbs
│                   │       │   ├── httprequest.rbs
│                   │       │   ├── httpresponse.rbs
│                   │       │   ├── https.rbs
│                   │       │   ├── httpserver.rbs
│                   │       │   ├── httpservlet/
│                   │       │   │   ├── abstract.rbs
│                   │       │   │   ├── cgi_runner.rbs
│                   │       │   │   ├── cgihandler.rbs
│                   │       │   │   ├── erbhandler.rbs
│                   │       │   │   ├── filehandler.rbs
│                   │       │   │   └── prochandler.rbs
│                   │       │   ├── httpservlet.rbs
│                   │       │   ├── httpstatus.rbs
│                   │       │   ├── httputils.rbs
│                   │       │   ├── httpversion.rbs
│                   │       │   ├── log.rbs
│                   │       │   ├── manifest.yaml
│                   │       │   ├── server.rbs
│                   │       │   ├── ssl.rbs
│                   │       │   ├── utils.rbs
│                   │       │   └── version.rbs
│                   │       └── webrick.gemspec
│                   └── specifications/
│                       ├── addressable-2.8.9.gemspec
│                       ├── colorator-1.1.0.gemspec
│                       ├── concurrent-ruby-1.3.6.gemspec
│                       ├── em-websocket-0.5.3.gemspec
│                       ├── eventmachine-1.2.7.gemspec
│                       ├── ffi-1.17.3.gemspec
│                       ├── forwardable-extended-2.6.0.gemspec
│                       ├── google-protobuf-3.23.4-arm64-darwin.gemspec
│                       ├── http_parser.rb-0.8.1.gemspec
│                       ├── i18n-1.14.8.gemspec
│                       ├── jekyll-4.3.4.gemspec
│                       ├── jekyll-sass-converter-3.0.0.gemspec
│                       ├── jekyll-seo-tag-2.8.0.gemspec
│                       ├── jekyll-watch-2.2.1.gemspec
│                       ├── kramdown-2.5.2.gemspec
│                       ├── kramdown-parser-gfm-1.1.0.gemspec
│                       ├── liquid-4.0.4.gemspec
│                       ├── listen-3.10.0.gemspec
│                       ├── logger-1.7.0.gemspec
│                       ├── mercenary-0.4.0.gemspec
│                       ├── pathutil-0.16.2.gemspec
│                       ├── public_suffix-5.1.1.gemspec
│                       ├── rb-fsevent-0.11.2.gemspec
│                       ├── rb-inotify-0.11.1.gemspec
│                       ├── rexml-3.4.4.gemspec
│                       ├── rouge-3.30.0.gemspec
│                       ├── safe_yaml-1.0.5.gemspec
│                       ├── sass-embedded-1.58.3-arm64-darwin.gemspec
│                       ├── terminal-table-3.0.2.gemspec
│                       ├── unicode-display_width-2.6.0.gemspec
│                       └── webrick-1.9.2.gemspec
├── lifecycle-build-page.png
├── main.py
├── planning/
│   ├── 2026-03-05_12-08-09_project-folder-organization-plan.md
│   ├── 2026-03-05_12-22-49_reorg-execution-report.md
│   ├── backups/
│   │   └── pre_move_snapshot_2026-03-05_12-08-09.tgz
│   └── manifests/
│       ├── post_move_checksums.txt
│       ├── post_move_git_status.txt
│       ├── post_move_manifest.txt
│       ├── pre_move_checksums.txt
│       ├── pre_move_git_status.txt
│       └── pre_move_manifest.txt
├── project_state/
│   ├── change_log.md
│   ├── environment.md
│   ├── how_to.md
│   └── project_state.md
├── pyproject.toml
├── rag -> control-standards/rag
├── tools/
│   ├── README.md
│   ├── fix_ai_boundaries.py
│   ├── generate_rag_index.py
│   ├── generate_standards_overview.py
│   ├── project_automator.py
│   ├── setup_hooks.sh
│   ├── validate_ai_boundaries.py
│   └── validate_reorg.sh
└── uv.lock
```
<!-- AUTO-GENERATED TREE END -->
