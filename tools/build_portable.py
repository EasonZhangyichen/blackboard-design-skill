#!/usr/bin/env python3
"""Build the versioned single-file distribution from the runtime source."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def output_path() -> Path:
    return ROOT / "dist" / f"blackboard-design-skill-v{version()}.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when the committed single-file distribution differs from SKILL.md",
    )
    args = parser.parse_args()
    source = (ROOT / "SKILL.md").read_bytes()
    destination = output_path()

    if args.check:
        if not destination.is_file() or destination.read_bytes() != source:
            print(f"Single-file distribution is stale: {destination.relative_to(ROOT)}")
            return 1
        print(f"Single-file distribution is current: {destination.relative_to(ROOT)}")
        return 0

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(source)
    print(f"Built {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
