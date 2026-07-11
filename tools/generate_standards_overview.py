import os
import re
import datetime
from pathlib import Path

# --- CONFIGURATION ---
# Resolve relative to this file so the script works on any checkout location
ROOT_DIR = Path(__file__).resolve().parent.parent / "control-standards" / "rag"
OUTPUT_FILE = ROOT_DIR / "VERSION_OVERVIEW.md"

def get_file_description(file_path):
    """
    Reads the file to find a human-readable title.
    Prioritizes:
    1. 'title:' or 'description:' fields (YAML/Frontmatter)
    2. First Markdown Header (# Title)
    3. First non-empty text line
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(2048) # Read first 2KB only for efficiency
            
        # Check for YAML/Frontmatter title
        yaml_match = re.search(r'^(?:title|description):\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
        if yaml_match:
            return yaml_match.group(1).strip().strip('"\'')

        # Check for Markdown H1
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()

        # Fallback: First non-empty line that isn't a separator
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith(('---', '```', '|')):
                return line
                
        return "Configuration or Data File"
    except Exception as e:
        return f"Error reading file"

def generate_overview():
    if not ROOT_DIR.exists():
        print(f"❌ Error: Directory not found: {ROOT_DIR}")
        return

    print(f"Scanning {ROOT_DIR}...")
    
    lines = [
        "# Authoritative Standards Overview",
        "",
        "**AI_READ_ACCESS: ALLOWED**",
        "**CONTENT_CLASS: RAG_APPROVED**",
        "**Status:** Auto-generated Reference",
        "",
        "**Auto-generated Summary**",
        "This document explains the contents of the standards library in simple language.",
        ""
    ]

    # Walk the directory tree
    for root, dirs, files in os.walk(ROOT_DIR):
        # Filter hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files.sort()
        dirs.sort()

        rel_path = Path(root).relative_to(ROOT_DIR)
        
        # Filter for relevant text files
        relevant_files = [f for f in files if f.endswith(('.md', '.yaml', '.yml', '.txt')) and f != OUTPUT_FILE.name]
        
        if not relevant_files:
            continue

        # Create Section Header based on folder path
        if str(rel_path) == ".":
            lines.append("## 📂 Root Directory")
        else:
            # Convert "standards_intelligence/us/nfpa79" -> "Standards Intelligence > Us > Nfpa79"
            readable_path = str(rel_path).replace(os.sep, ' > ').replace('_', ' ').title()
            lines.append(f"## 📂 {readable_path}")

        # Create Table
        lines.append("| File | Last Modified | Description |")
        lines.append("| :--- | :--- | :--- |")

        for filename in relevant_files:
            file_path = Path(root) / filename
            desc = get_file_description(file_path)
            # Escape pipes to prevent breaking markdown table
            desc = desc.replace('|', '-')
            
            mod_time = datetime.datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
            lines.append(f"| `{filename}` | {mod_time} | {desc} |")
        
        lines.append("") # Spacing

    # Write the file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"✅ Success! Overview generated at:\n{OUTPUT_FILE}")
    except PermissionError:
        print(f"❌ Error: Permission denied writing to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_overview()
