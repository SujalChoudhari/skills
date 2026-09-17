#!/usr/bin/env python3
"""Validate the portable skill layout and the Unslop UI regression fixture."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_frontmatter(path: Path) -> None:
    text = read(path)
    assert text.startswith("---\n"), f"{path}: frontmatter must start at byte 0"
    match = re.search(r"\n---\n", text[4:])
    assert match, f"{path}: frontmatter closing marker missing"
    frontmatter = text[4 : match.start() + 4]
    fields = dict(
        re.findall(r"(?m)^([a-z][a-z0-9_-]*):\s*(.+)$", frontmatter)
    )
    for field in ("name", "description"):
        assert field in fields, f"{path}: missing {field}"
    description = fields["description"].strip().strip('"')
    assert len(description) <= 60, f"{path}: description exceeds 60 characters"
    assert description.endswith("."), f"{path}: description must end with a period"
    assert re.fullmatch(r"[a-z0-9-]+", fields["name"].strip()), (
        f"{path}: invalid skill name"
    )


for skill_dir in (ROOT / "storyscope", ROOT / "unslop-ui"):
    canonical = skill_dir / "SKILL.md"
    alias = skill_dir / "skill.md"
    validate_frontmatter(canonical)
    assert alias.is_file() and not alias.is_symlink(), (
        f"{alias}: expected generated compatibility file"
    )
    assert read(alias) == read(canonical), f"{alias}: run scripts/sync_entrypoints.py"

unslop = read(ROOT / "unslop-ui" / "SKILL.md")
for phrase in (
    "AUDIT -> BOUND -> CHANGE -> VERIFY",
    "auxiliary-text pass",
    "No evidence is `BLOCKED`",
    "MEANINGFUL",
    "REDUNDANT",
    "GENERIC",
    "references/audit-report-template.md",
):
    assert phrase.lower() in unslop.lower(), f"unslop skill missing {phrase!r}"

checklist = read(ROOT / "unslop-ui" / "references" / "anti-slop-checklist.md")
numbered = [int(value) for value in re.findall(r"(?m)^(\d+)\. ", checklist)]
assert numbered == list(range(1, 101)), "anti-slop checklist must contain 1..100"

fixture = read(ROOT / "unslop-ui" / "references" / "adversarial-fixture.md")
for phrase in (
    "Build better",
    "Powerful tools",
    "Designed for you",
    "Updated 17 September 2026",
    "Required findings",
):
    assert phrase in fixture, f"fixture missing {phrase!r}"

print("frontmatter=ok")
print("canonical_entrypoints=ok")
print("lowercase_aliases=ok")
print("unslop_procedure=ok")
print("checklist_items=100")
print("adversarial_fixture=ok")
