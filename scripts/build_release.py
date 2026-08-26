from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.7.1"
OUTPUT = ROOT / "dist" / f"blackboard-design-skill-v{VERSION}.zip"

EXCLUDED_PARTS = {".git", "__pycache__", ".DS_Store"}
EXCLUDED_FILES = {OUTPUT.resolve()}


def should_include(path: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in path.parts):
        return False
    if path.resolve() in EXCLUDED_FILES:
        return False
    return path.is_file()


with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as archive:
    for path in sorted(ROOT.rglob("*")):
        if should_include(path):
            archive.write(path, Path(ROOT.name) / path.relative_to(ROOT))

print(f"Created: {OUTPUT}")
