#!/usr/bin/env python3
"""Build SHA-256 checksums for the public release assets."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def release_assets() -> tuple[Path, ...]:
    current = version()
    return (
        ROOT / "dist" / f"blackboard-design-skill-v{current}.md",
        ROOT / "dist" / f"blackboard-design-skill-v{current}.zip",
        ROOT / "dist" / "WEB-QUICK-PROMPT.md",
    )


def main() -> int:
    assets = release_assets()
    missing = [path for path in assets if not path.is_file()]
    if missing:
        names = ", ".join(path.relative_to(ROOT).as_posix() for path in missing)
        raise SystemExit(f"Missing release assets: {names}")

    lines = [f"{sha256(path.read_bytes()).hexdigest()}  {path.name}" for path in assets]
    destination = ROOT / "dist" / "SHA256SUMS.txt"
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Built {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
