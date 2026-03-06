#!/bin/bash

PROJECT_ROOT=$(dirname "$(dirname "$0")")
cd "$PROJECT_ROOT" || exit 1

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASS_COUNT=0
FAIL_COUNT=0

_check() {
    local condition=$1
    local message=$2
    if eval "$condition"; then
        echo -e "${GREEN}PASS:${NC} $message"
        ((PASS_COUNT++))
    else
        echo -e "${RED}FAIL:${NC} $message"
        ((FAIL_COUNT++))
    fi
}

check_file_exists() { _check "[ -f \"$1\" ]" "File exists: $1"; }
check_dir_exists() { _check "[ -d \"$1\" ]" "Directory exists: $1"; }
check_dir_missing() { _check "[ ! -d \"$1\" ]" "Directory removed: $1"; }
check_symlink_target() { _check "[ -L \"$1\" ] && [ \"$(readlink "$1")\" = \"$2\" ] && [ -e \"$1\" ]" "Symlink points to $2: $1"; }
check_script_runs() { _check "python3 \"$1\" >/dev/null" "Script runs successfully: $1"; }

check_file_pattern() {
    local pattern=$1
    local message=$2
    if ls $pattern 1> /dev/null 2>&1; then
        echo -e "${GREEN}PASS:${NC} $message"
        ((PASS_COUNT++))
    else
        echo -e "${RED}FAIL:${NC} $message"
        ((FAIL_COUNT++))
    fi
}

check_pre_artifacts() {
    echo -e "\n${YELLOW}--- Verifying Pre-Move Artifacts ---${NC}"
    check_file_exists "planning/manifests/pre_move_manifest.txt"
    check_file_exists "planning/manifests/pre_move_checksums.txt"
    check_file_exists "planning/manifests/pre_move_git_status.txt"
    check_file_pattern "planning/backups/pre_move_snapshot_*.tgz" "Pre-move snapshot exists"
}

check_post_phase2() {
    echo -e "\n${YELLOW}--- Verifying Post-Phase 2: Consolidation ---${NC}"
    check_dir_missing "change_management"
    check_dir_missing "archive"
    check_dir_missing "drafts"
    check_dir_missing "drafts_DO_NOT_READ"
    check_dir_missing "exports"
    check_dir_missing "templates"

    check_dir_exists "control-standards/governance"
    check_dir_exists "control-standards/archive"
    check_dir_exists "control-standards/work"
    check_dir_exists "control-standards/work/general"
    check_dir_exists "control-standards/work/design"
    check_dir_exists "control-standards/restricted"
    check_dir_exists "control-standards/restricted/legacy_drafts"
    check_dir_exists "control-standards/restricted/do_not_read"
    check_dir_exists "control-standards/exports"
    check_dir_exists "control-standards/exports/legacy_root"
    check_dir_exists "control-standards/templates"
}

check_post_phase3() {
    echo -e "\n${YELLOW}--- Verifying Post-Phase 3: Standards Reorg ---${NC}"
    local SI="control-standards/rag/standards_intelligence"
    check_dir_exists "$SI/us/nec"
    check_dir_exists "$SI/us/nfpa79"
    check_dir_exists "$SI/us/ul_508a"
    check_dir_exists "$SI/international/machinery/iec_60204_1"
    check_dir_exists "$SI/international/functional_safety/iso_13849_1"
    check_dir_exists "$SI/international/functional_safety/iso_12100"
    check_dir_exists "$SI/international/functional_safety/iec_62061"
    check_dir_exists "$SI/international/functional_safety/iec_61508"
    check_dir_exists "$SI/international/functional_safety/iec_61511"
    check_dir_exists "$SI/crosswalks/overlap_matrix"
    check_dir_exists "$SI/crosswalks/overlap_notes"

    check_dir_missing "$SI/nec"
    check_dir_missing "$SI/nfpa79"
    check_dir_missing "$SI/ul_508a"
    check_dir_missing "$SI/iec_60204_1"
    check_dir_missing "$SI/_overlap_matrix"
    check_dir_missing "$SI/_overlap_notes"
}

check_post_phase5() {
    echo -e "\n${YELLOW}--- Verifying Compatibility State ---${NC}"
    check_symlink_target "rag" "control-standards/rag"
}

check_deliverables() {
    echo -e "\n${YELLOW}--- Verifying Reorg Deliverables ---${NC}"
    check_file_pattern "planning/*_project-folder-organization-plan.md" "Organization plan exists"
    check_file_pattern "planning/*_reorg-execution-report.md" "Execution report exists"
    check_file_exists "planning/manifests/post_move_manifest.txt"
    check_file_exists "planning/manifests/post_move_checksums.txt"
    check_file_exists "planning/manifests/post_move_git_status.txt"
    check_file_exists "README.md"
    check_file_exists "control-standards/README.md"
    check_file_exists "control-standards/QUICK_START.md"
    check_file_exists "control-standards/STRUCTURE_SUMMARY.md"
}

main() {
    case "$1" in
        pre-check) check_pre_artifacts ;;
        post-check-p2) check_post_phase2 ;;
        post-check-p3) check_post_phase3 ;;
        post-check-p5) check_post_phase5 ;;
        deliverables) check_deliverables ;;
        all)
            check_pre_artifacts
            check_deliverables
            check_post_phase2
            check_post_phase3
            check_post_phase5
            echo -e "\n${YELLOW}--- Running Supporting Scripts ---${NC}"
            check_script_runs "tools/project_automator.py"
            check_script_runs "tools/validate_ai_boundaries.py"
            ;;
        *)
            echo "Usage: $0 {pre-check|post-check-p2|post-check-p3|post-check-p5|deliverables|all}"
            exit 1
            ;;
    esac

    echo -e "\n${YELLOW}--- Summary ---${NC}"
    echo -e "Total Checks: $((PASS_COUNT + FAIL_COUNT))"
    echo -e "${GREEN}Passed: $PASS_COUNT${NC}"
    echo -e "${RED}Failed: $FAIL_COUNT${NC}"

    if [ "$FAIL_COUNT" -gt 0 ]; then
        exit 1
    fi
}

main "$@"
