# Workspace Structure Summary

Use this file as a tree reference for the whole workspace. The primary narrative lives in [README.md](/Users/kyawminthu/Dev/Control System Tools/README.md) and [PROJECT_STARTUP_CONTEXT.md](/Users/kyawminthu/Dev/Control System Tools/PROJECT_STARTUP_CONTEXT.md).

<!-- AUTO-GENERATED TREE START -->
## Directory Tree
**Last Auto-Updated:** 2026-03-05 20:25:07

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
├── .gitignore
├── .mcp.json
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
├── AGENTS.md
├── CLAUDE.md
├── PRE_MIGRATION_CHECK.sh
├── PROJECT_STARTUP_CONTEXT.md
├── README.md
├── STRUCTURE_SUMMARY.md
├── archive/
│   ├── MIGRATION_GUIDE.md
│   ├── MIGRATION_READY.md
│   └── MIGRATION_SCRIPT.sh
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
│   │   │   │   ├── functional_safety/
│   │   │   │   │   ├── iec_61508/
│   │   │   │   │   ├── iec_61511/
│   │   │   │   │   ├── iec_62061/
│   │   │   │   │   ├── iso_12100/
│   │   │   │   │   └── iso_13849_1/
│   │   │   │   │       └── file_structure.md
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
│       │   ├── diagrams/
│       │   ├── experiments/
│       │   ├── mermaid_diagrams_to_reference.md
│       │   ├── mini_machine_safety_design_v2_project_status.md
│       │   ├── scratch_notes/
│       │   ├── standards_web_page_design_prompt_v1.md
│       │   ├── standards_web_page_design_prompt_v3.md
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
├── general_change_log.md
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
