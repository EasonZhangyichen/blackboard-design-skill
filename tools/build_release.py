#!/usr/bin/env python3
"""Build the deterministic standard Agent Skill release archive."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "blackboard-design-skill"
FILES = (
    Path("SKILL.md"),
    Path("LICENSE"),
    Path("agents/openai.yaml"),
)


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def add_file(archive: ZipFile, relative: Path) -> None:
    info = ZipInfo(f"{SKILL_NAME}/{relative.as_posix()}")
    info.date_time = (2026, 1, 1, 0, 0, 0)
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, (ROOT / relative).read_bytes())


def main() -> int:
    destination = ROOT / "dist" / f"{SKILL_NAME}-v{version()}.zip"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w") as archive:
        for relative in FILES:
            add_file(archive, relative)
    print(f"Built {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
