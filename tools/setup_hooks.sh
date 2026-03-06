#!/bin/bash
# Setup Git Hooks for Project Automation

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOOK_DIR="$PROJECT_ROOT/.git/hooks"
PRE_COMMIT="$HOOK_DIR/pre-commit"

echo "Installing Project Automator Hook..."

# Create the pre-commit hook
cat > "$PRE_COMMIT" << 'EOF'
#!/bin/bash
echo "🤖 Running Project Automator..."
python3 tools/project_automator.py
git add STRUCTURE_SUMMARY.md project_state/change_log.md
EOF

# Make it executable
chmod +x "$PRE_COMMIT"

echo "✅ Hook installed!"
echo "   The project structure will now auto-update"
echo "   and project_state/change_log.md will be staged with each commit"
echo "   every time you run 'git commit'."
