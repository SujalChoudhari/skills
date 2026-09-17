#!/usr/bin/env python3
"""Generate lowercase compatibility entrypoints from canonical SKILL.md files."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    (ROOT / "storyscope" / "SKILL.md", ROOT / "storyscope" / "skill.md"),
    (ROOT / "unslop-ui" / "SKILL.md", ROOT / "unslop-ui" / "skill.md"),
)

for canonical, compatibility in PAIRS:
    if not canonical.is_file():
        raise SystemExit(f"missing canonical entrypoint: {canonical}")
    shutil.copyfile(canonical, compatibility)
    print(f"synced {compatibility.relative_to(ROOT)}")
