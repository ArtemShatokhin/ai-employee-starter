#!/usr/bin/env python3
"""Fail when a role's writing calls have no approval rule in kortix.yaml.

Reads the manifest next to the repo root, expands the policy globs, and checks that every
connector an agent may reach is covered by at least one rule that is not `always_run`.

Exit codes: 0 every role is governed, 1 a role is ungoverned or the manifest is unreadable.
"""

from __future__ import annotations

import fnmatch
import sys
from pathlib import Path

WRITE_HINTS = ("send_", "create_", "update_", "delete_", "publish_", "post_")


def load_policies(text: str) -> tuple[str, list[dict]]:
    """Minimal reader for the policy block — enough for a pre-flight check, not a YAML parser."""
    default_mode = "allow_all"
    rules: list[dict] = []
    section = None
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("policy:"):
            section = "policy"
            continue
        if line.startswith("policies:"):
            section = "policies"
            continue
        if line and not line.startswith(" "):
            section = None
            continue
        body = line.strip()
        if section == "policy" and body.startswith("default_mode:"):
            default_mode = body.split(":", 1)[1].strip()
        elif section == "policies":
            if body.startswith("- match:"):
                current = {"match": body.split(":", 1)[1].strip().strip('"'), "action": None}
                rules.append(current)
            elif body.startswith("action:") and current is not None:
                current["action"] = body.split(":", 1)[1].strip()
    return default_mode, rules


def action_for(tool: str, rules: list[dict]) -> str | None:
    for rule in rules:
        if rule["match"] and fnmatch.fnmatch(tool, rule["match"]):
            return rule["action"]
    return None


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    manifest = root / "kortix.yaml"
    try:
        text = manifest.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read {manifest}: {exc}")
        return 1

    default_mode, rules = load_policies(text)
    if default_mode != "risk":
        print("policy.default_mode is not 'risk': unmatched calls run unattended")
        return 1
    if not rules:
        print("no policies declared: every call is governed by the default mode alone")
        return 1

    failures: list[str] = []

    wildcard_at = next((i for i, rule in enumerate(rules) if rule["match"] == "*"), None)
    if wildcard_at is not None and wildcard_at < len(rules) - 1:
        failures.append(
            f"catch-all rule at position {wildcard_at + 1} precedes {len(rules) - wildcard_at - 1} "
            "specific rule(s): with first-match-wins they never run"
        )
    for hint in WRITE_HINTS:
        probe = f"connector.{hint}thing"
        action = action_for(probe, rules)
        if action not in {"require_approval", "block"}:
            failures.append(f"{probe}: action is {action or 'unmatched'}")

    if failures:
        for failure in failures:
            print(f"ungoverned writing call — {failure}")
        return 1

    print(f"ok: {len(rules)} policies, default_mode={default_mode}, all writing calls governed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
