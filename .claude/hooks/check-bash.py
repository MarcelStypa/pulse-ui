#!/usr/bin/env python3
"""PreToolUse hook (Bash): enforce commit rules from docs/git-and-commits.md.

Blocks (exit 2): non-conventional commit subjects, --no-verify, force-push.
Reads the hook JSON from stdin. Fails open on parse problems.
"""
import json
import re
import sys

CC = re.compile(
    r"^(feat|fix|docs|refactor|test|build|ci|chore|perf|revert)"
    r"(\([a-z0-9._/-]+\))?!?: \S.{0,70}$"
)

def block(msg):
    print(f"BLOCKED by repo policy: {msg}", file=sys.stderr)
    sys.exit(2)

try:
    cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
except Exception:
    sys.exit(0)

if re.search(r"\bgit\b.*\b(commit|push)\b.*--no-verify|\bgit\b.*\bcommit\b.*\s-n\b", cmd):
    block("do not skip hooks (--no-verify); fix the failing check instead")

if re.search(r"\bgit\s+push\b.*(--force\b|\s-f\b|--force-with-lease)", cmd):
    block("force-push is not allowed (docs/git-and-commits.md)")

if re.search(r"\bgit\s+commit\b", cmd) and "--amend" not in cmd:
    m = re.search(r"""-m\s+(?:"\$\(cat <<'?EOF'?\s*\n)?["']?([^\n"']+)""", cmd)
    if m:
        subject = m.group(1).strip()
        if not CC.match(subject):
            block(
                f"commit subject {subject!r} is not a Conventional Commit "
                "(type(scope): subject, max 72 chars). See docs/git-and-commits.md"
            )
sys.exit(0)
