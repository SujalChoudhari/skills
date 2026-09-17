#!/usr/bin/env python3
"""Validate the portable Unslop UI skill's enforcement contract."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "unslop-ui" / "skill.md"
CHECKLIST = ROOT / "unslop-ui" / "references" / "anti-slop-checklist.md"
FIXTURE = ROOT / "unslop-ui" / "references" / "adversarial-fixture.md"

skill = SKILL.read_text(encoding="utf-8")
checklist = CHECKLIST.read_text(encoding="utf-8")
fixture = FIXTURE.read_text(encoding="utf-8")

assert skill.startswith("---\n"), "skill frontmatter is missing"
assert "## Mandatory audit gate" in skill
assert "## Auxiliary-text detection algorithm" in skill
assert "AUDIT GATE" in skill
assert "No evidence means `BLOCKED`" in skill
assert "Do not edit before the gate is complete" in skill

required_terms = (
    "eyebrow",
    "kicker",
    "overline",
    "subtitle",
    "supportingText",
    "MEANINGFUL",
    "REDUNDANT",
    "GENERIC",
    "DECORATIVE",
    "UNCLEAR",
)
for term in required_terms:
    assert term.lower() in skill.lower(), f"skill missing {term!r}"

numbers = [int(value) for value in re.findall(r"(?m)^(\d+)\. ", checklist)]
assert numbers == list(range(1, 101)), "checklist must contain items 1 through 100"

for term in (
    "Build better",
    "Powerful tools",
    "Designed for you",
    "Updated 17 September 2026",
    "Required findings",
):
    assert term in fixture, f"fixture missing {term!r}"

print("skill_frontmatter=ok")
print("mandatory_audit_gate=ok")
print("auxiliary_text_algorithm=ok")
print("checklist_items=100")
print("adversarial_fixture=ok")
