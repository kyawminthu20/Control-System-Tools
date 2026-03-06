#!/bin/bash
# Setup Git Hooks for Project Automation

HOOK_DIR="../.git/hooks"
PRE_COMMIT="$HOOK_DIR/pre-commit"

echo "Installing Project Automator Hook..."

# Create the pre-commit hook
cat > "$PRE_COMMIT" << 'EOF'
#!/bin/bash
echo "🤖 Running Project Automator..."
python3 tools/project_automator.py
git add STRUCTURE_SUMMARY.md general_change_log.md
EOF

# Make it executable
chmod +x "$PRE_COMMIT"

echo "✅ Hook installed!"
echo "   The project structure and change log will now auto-update"
echo "   every time you run 'git commit'."