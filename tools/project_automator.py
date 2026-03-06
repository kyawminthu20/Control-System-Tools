#!/usr/bin/env python3
"""
Project Automator "Skill"
Purpose: Automatically maintain project structure documentation and aggregate change logs.
Acts as a local MCP (Model Context Protocol) to keep the repository self-documenting.
"""

import os
import datetime
import re

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRUCTURE_FILE = os.path.join(PROJECT_ROOT, "STRUCTURE_SUMMARY.md")
LOG_FILE = os.path.join(PROJECT_ROOT, "general_change_log.md")

IGNORE_DIRS = {'.git', '__pycache__', '.DS_Store', '.idea', 'venv', 'node_modules'}
IGNORE_FILES = {'.DS_Store'}

def generate_tree(dir_path, prefix=""):
    """Generates a visual tree structure of the directory."""
    tree_str = ""
    try:
        contents = sorted([x for x in os.listdir(dir_path) 
                          if x not in IGNORE_DIRS and x not in IGNORE_FILES])
        
        pointers = [("├── ", "│   ")] * (len(contents) - 1) + [("└── ", "    ")]
        
        for pointer, content in zip(pointers, contents):
            path = os.path.join(dir_path, content)
            is_last = pointer[0] == "└── "
            
            # Handle Symlinks
            if os.path.islink(path):
                target = os.readlink(path)
                tree_str += f"{prefix}{pointer[0]}{content} -> {target}\n"
                continue
                
            if os.path.isdir(path):
                tree_str += f"{prefix}{pointer[0]}{content}/\n"
                tree_str += generate_tree(path, prefix + pointer[1])
            else:
                tree_str += f"{prefix}{pointer[0]}{content}\n"
                
    except PermissionError:
        pass
        
    return tree_str

def update_structure_summary():
    """Updates the STRUCTURE_SUMMARY.md file with the current tree, preserving manual content."""
    print("🔍 Scanning project structure...")
    tree_output = generate_tree(PROJECT_ROOT)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the automated section with markers
    START_MARKER = "<!-- AUTO-GENERATED TREE START -->"
    END_MARKER = "<!-- AUTO-GENERATED TREE END -->"
    
    auto_section = f"{START_MARKER}\n## Directory Tree\n**Last Auto-Updated:** {timestamp}\n\n```text\n{tree_output}```\n{END_MARKER}"
    
    if os.path.exists(STRUCTURE_FILE):
        with open(STRUCTURE_FILE, 'r') as f:
            content = f.read()
        
        if START_MARKER in content and END_MARKER in content:
            # Regex to replace the content between markers
            pattern = re.compile(f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL)
            new_content = pattern.sub(auto_section, content)
            print(f"✅ Updated existing tree in {os.path.basename(STRUCTURE_FILE)}")
        else:
            # If markers don't exist, insert after the main header to keep it visible
            if "# Folder Structure Summary" in content:
                # Insert after the first header block
                lines = content.splitlines()
                # Find first blank line after header to insert
                insert_idx = 1
                for i, line in enumerate(lines):
                    if i > 0 and line.strip() == "":
                        insert_idx = i + 1
                        break
                lines.insert(insert_idx, "\n" + auto_section + "\n")
                new_content = "\n".join(lines)
                print(f"✅ Inserted new tree section into {os.path.basename(STRUCTURE_FILE)}")
            else:
                # Fallback: Append to end
                new_content = content + "\n\n" + auto_section
                print(f"✅ Appended tree to {os.path.basename(STRUCTURE_FILE)}")
    else:
        # Create new file
        new_content = f"# Folder Structure Summary\n\n{auto_section}\n"
        print(f"✅ Created {os.path.basename(STRUCTURE_FILE)}")
    
    with open(STRUCTURE_FILE, 'w') as f:
        f.write(new_content)

def scan_for_generation_summaries():
    """Scans for GENERATION_SUMMARY.md files and returns their content."""
    summaries = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        if "GENERATION_SUMMARY.md" in files:
            path = os.path.join(root, "GENERATION_SUMMARY.md")
            rel_path = os.path.relpath(path, PROJECT_ROOT)
            
            with open(path, 'r') as f:
                content = f.read()
                
            # Extract key info using regex
            date_match = re.search(r'\*\*Generated:\*\* ([\d-]+)', content)
            status_match = re.search(r'\*\*Status:\*\* (.+)', content)
            title_match = re.search(r'# (.+)', content)
            
            if date_match and title_match:
                summaries.append({
                    'date': date_match.group(1),
                    'title': title_match.group(1),
                    'status': status_match.group(1) if status_match else "Unknown",
                    'source': rel_path
                })
    return summaries

def update_general_log():
    """Updates general_change_log.md with new findings."""
    print("🔍 Aggregating distributed logs...")
    
    if not os.path.exists(LOG_FILE):
        print(f"⚠️ {LOG_FILE} not found. Skipping log aggregation.")
        return

    with open(LOG_FILE, 'r') as f:
        current_log = f.read()

    summaries = scan_for_generation_summaries()
    new_entries = []

    for summary in summaries:
        # Simple check to see if this source is already mentioned for this date
        # A more robust check would parse the markdown structure
        check_str = f"Source:** `{summary['source']}`"
        if check_str not in current_log:
            entry = f"\n### {summary['date']}: {summary['title']}\n"
            entry += f"**Type:** Automated Aggregation\n"
            entry += f"**Source:** `{summary['source']}`\n"
            entry += f"**Status:** {summary['status']}\n"
            entry += f"- **Action:** Detected new generation summary file.\n"
            new_entries.append(entry)

    if new_entries:
        # Append new entries before the "Upcoming Priorities" section if it exists
        if "## Upcoming Priorities" in current_log:
            parts = current_log.split("## Upcoming Priorities")
            updated_log = parts[0] + "".join(new_entries) + "\n## Upcoming Priorities" + parts[1]
        else:
            updated_log = current_log + "\n## Recent Auto-Detected Changes\n" + "".join(new_entries)
            
        with open(LOG_FILE, 'w') as f:
            f.write(updated_log)
        print(f"✅ Added {len(new_entries)} new entries to {os.path.basename(LOG_FILE)}")
    else:
        print("✨ No new distributed logs found.")

if __name__ == "__main__":
    update_structure_summary()
    update_general_log()