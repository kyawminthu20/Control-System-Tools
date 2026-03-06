#!/usr/bin/env python3
"""
AI Boundary Validator "Skill"
Purpose: Enforce AI safety rules by scanning the RAG directory for forbidden content.
Acts as a security gate to prevent sensitive data leakage into AI context.
"""

import os
import sys

# Configuration
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Prioritize the new canonical path, fallback to symlink/legacy
RAG_DIR = os.path.join(PROJECT_ROOT, "control-standards", "rag")
if not os.path.exists(RAG_DIR):
    RAG_DIR = os.path.join(PROJECT_ROOT, "rag")

# Rules
REQUIRED_HEADER = "AI_READ_ACCESS: ALLOWED"
FORBIDDEN_KEYWORDS = [
    "CONFIDENTIAL", 
    "INTERNAL ONLY", 
    "DO NOT UPLOAD", 
    "DRAFT ONLY",
    "NO-AI"
]

def validate_file(filepath):
    """Checks a single file for compliance rules."""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Check 1: Header presence (only for markdown files)
        if filepath.endswith('.md'):
            # Check first 1000 chars for the permission tag
            header_chunk = content[:1000]
            if REQUIRED_HEADER not in header_chunk:
                issues.append(f"Missing required permission tag: '{REQUIRED_HEADER}'")

        # Check 2: Forbidden keywords (Global check)
        for keyword in FORBIDDEN_KEYWORDS:
            if keyword in content:
                issues.append(f"Contains forbidden keyword: '{keyword}'")
                
    except Exception as e:
        issues.append(f"Could not read file: {str(e)}")
        
    return issues

def main():
    print(f"🛡️  Scanning RAG directory for AI safety: {os.path.relpath(RAG_DIR, PROJECT_ROOT)}")
    
    violation_count = 0
    file_count = 0
    
    for root, dirs, files in os.walk(RAG_DIR):
        for file in files:
            if file.endswith('.md') or file.endswith('.yaml') or file.endswith('.txt'):
                file_count += 1
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, PROJECT_ROOT)
                
                issues = validate_file(path)
                
                if issues:
                    violation_count += 1
                    print(f"\n❌ Violation in: {rel_path}")
                    for issue in issues:
                        print(f"   - {issue}")
    
    print("\n" + "="*40)
    if violation_count > 0:
        print(f"⛔ FAILED: Found {violation_count} files with safety violations.")
        print(f"   Scanned {file_count} files.")
        sys.exit(1)
    else:
        print(f"✅ PASSED: All {file_count} RAG files comply with AI safety boundaries.")
        sys.exit(0)

if __name__ == "__main__":
    main()