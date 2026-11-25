#!/usr/bin/env python3
"""PreToolUse hook (Write/Edit): block writing secret-like files.

Blocks (exit 2) .env*, *.tfvars, *.tfstate, *.pem, *.key unless they are
*.example files. See docs/security.md. Fails open on parse problems.
"""
import json
import re
import sys

try:
    path = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
except Exception:
    sys.exit(0)

name = path.rsplit("/", 1)[-1]
if name.endswith((".example", ".sample", ".template")):
    sys.exit(0)

if re.match(r"^\.env(\..*)?$", name) or re.search(r"\.(tfvars|tfstate|pem|key)(\.backup)?$", name):
    print(
        f"BLOCKED by repo policy: {name} looks like a secret file. "
        "Write a *.example file with placeholders instead (docs/security.md).",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
