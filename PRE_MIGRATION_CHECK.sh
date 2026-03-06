#!/bin/bash
#
# Pre-Migration Check Script
# Purpose: Verify environment before running migration
# Date: 2026-01-15
#

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Pre-Migration Environment Check${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Paths
OLD_RAG="/Users/kyawminthu/Dev/tools/rag"
NEW_RAG="/Users/kyawminthu/Dev/tools/control-standards/rag"

PASS_COUNT=0
WARN_COUNT=0
FAIL_COUNT=0

check_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((PASS_COUNT++))
}

check_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    ((WARN_COUNT++))
}

check_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    ((FAIL_COUNT++))
}

echo -e "${BLUE}Checking Directories...${NC}"
echo ""

# Check OLD RAG exists
if [ -d "$OLD_RAG" ]; then
    check_pass "OLD RAG directory exists: $OLD_RAG"
else
    check_fail "OLD RAG directory NOT found: $OLD_RAG"
fi

# Check NEW RAG exists
if [ -d "$NEW_RAG" ]; then
    check_pass "NEW RAG directory exists: $NEW_RAG"
else
    check_fail "NEW RAG directory NOT found: $NEW_RAG"
fi

echo ""
echo -e "${BLUE}Checking OLD RAG Contents...${NC}"
echo ""

# Check OLD standards
if [ -d "$OLD_RAG/standards_intelligence" ]; then
    check_pass "OLD has standards_intelligence/"

    # Count standards
    OLD_STANDARDS_COUNT=$(find "$OLD_RAG/standards_intelligence" -maxdepth 1 -type d | wc -l | tr -d ' ')
    echo -e "  ${BLUE}→${NC} Found $OLD_STANDARDS_COUNT directories in OLD standards_intelligence"
else
    check_warn "OLD missing standards_intelligence/"
fi

# Check OLD tools
OLD_TOOLS=(
    "audit_tool"
    "business_metrics_profit_engine"
    "design_package_generator"
    "ip_library_licensing"
    "knowledge_platform"
    "retainer_support_engine"
    "ul508a_panel_automation"
)

for tool in "${OLD_TOOLS[@]}"; do
    if [ -d "$OLD_RAG/$tool" ]; then
        check_pass "OLD has $tool/"
    else
        check_warn "OLD missing $tool/"
    fi
done

echo ""
echo -e "${BLUE}Checking NEW RAG Contents...${NC}"
echo ""

# Check NEW standards
if [ -d "$NEW_RAG/standards_intelligence" ]; then
    check_pass "NEW has standards_intelligence/"

    # Count standards
    NEW_STANDARDS_COUNT=$(find "$NEW_RAG/standards_intelligence" -maxdepth 1 -type d | wc -l | tr -d ' ')
    echo -e "  ${BLUE}→${NC} Found $NEW_STANDARDS_COUNT directories in NEW standards_intelligence"

    # Check for overlap matrices
    if [ -d "$NEW_RAG/standards_intelligence/_overlap_matrix" ]; then
        OVERLAP_COUNT=$(find "$NEW_RAG/standards_intelligence/_overlap_matrix" -name "*.md" -o -name "*.yaml" | wc -l | tr -d ' ')
        check_pass "NEW has overlap matrices ($OVERLAP_COUNT files)"
    else
        check_warn "NEW missing overlap matrices"
    fi

    # Check for overlap notes
    if [ -d "$NEW_RAG/standards_intelligence/_overlap_notes" ]; then
        NOTES_COUNT=$(find "$NEW_RAG/standards_intelligence/_overlap_notes" -name "*.md" -o -name "*.yaml" | wc -l | tr -d ' ')
        check_pass "NEW has overlap notes ($NOTES_COUNT files)"
    else
        check_warn "NEW missing overlap notes"
    fi
else
    check_fail "NEW missing standards_intelligence/"
fi

# Check NEW modules
NEW_MODULES=(
    "commissioning_checklists"
    "design_framework"
    "training_modules"
    "troubleshooting_engine"
)

for module in "${NEW_MODULES[@]}"; do
    if [ -d "$NEW_RAG/$module" ]; then
        check_pass "NEW has $module/"
    else
        check_warn "NEW missing $module/"
    fi
done

echo ""
echo -e "${BLUE}Checking File Counts...${NC}"
echo ""

OLD_FILE_COUNT=$(find "$OLD_RAG" -type f | wc -l | tr -d ' ')
NEW_FILE_COUNT=$(find "$NEW_RAG" -type f | wc -l | tr -d ' ')

echo -e "  OLD RAG total files: ${BLUE}$OLD_FILE_COUNT${NC}"
echo -e "  NEW RAG total files: ${BLUE}$NEW_FILE_COUNT${NC}"

if [ "$NEW_FILE_COUNT" -gt "$OLD_FILE_COUNT" ]; then
    check_pass "NEW has more files than OLD (includes new overlap matrices/notes)"
elif [ "$NEW_FILE_COUNT" -eq "$OLD_FILE_COUNT" ]; then
    check_warn "NEW and OLD have same file count"
else
    check_warn "NEW has fewer files than OLD (expected if overlap matrices not in OLD)"
fi

echo ""
echo -e "${BLUE}Checking Disk Space...${NC}"
echo ""

REQUIRED_SPACE_MB=100
AVAILABLE_SPACE_KB=$(df -k /Users/kyawminthu/Dev/tools | tail -1 | awk '{print $4}')
AVAILABLE_SPACE_MB=$((AVAILABLE_SPACE_KB / 1024))

echo -e "  Available space: ${BLUE}${AVAILABLE_SPACE_MB}MB${NC}"
echo -e "  Required space: ${BLUE}${REQUIRED_SPACE_MB}MB${NC}"

if [ "$AVAILABLE_SPACE_MB" -gt "$REQUIRED_SPACE_MB" ]; then
    check_pass "Sufficient disk space available"
else
    check_fail "Insufficient disk space"
fi

echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}           Check Results Summary${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

echo -e "  ${GREEN}PASS:${NC} $PASS_COUNT"
echo -e "  ${YELLOW}WARN:${NC} $WARN_COUNT"
echo -e "  ${RED}FAIL:${NC} $FAIL_COUNT"
echo ""

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo -e "${RED}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║              CRITICAL ISSUES FOUND                     ║${NC}"
    echo -e "${RED}║         DO NOT RUN MIGRATION SCRIPT YET                ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}Please resolve FAIL items before migrating.${NC}"
    exit 1
elif [ "$WARN_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║              WARNINGS DETECTED                         ║${NC}"
    echo -e "${YELLOW}║    Review warnings before running migration            ║${NC}"
    echo -e "${YELLOW}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Migration can proceed, but review warnings above.${NC}"
    exit 0
else
    echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║           ALL CHECKS PASSED                            ║${NC}"
    echo -e "${GREEN}║       READY FOR MIGRATION                              ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Environment is ready. You can now run:${NC}"
    echo -e "${BLUE}  ./MIGRATION_SCRIPT.sh${NC}"
    exit 0
fi
