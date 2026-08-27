#!/usr/bin/env python3
"""Validate source metadata, release structure, privacy, and generated files."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
from zipfile import ZipFile

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "blackboard-design-skill"
REFERENCES = {
    "pedagogy-and-stages.md",
    "image-grammar.md",
    "generation-protocol.md",
    "writing-and-compliance.md",
}
TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".txt", ".toml", ""}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg"}
CORE_MARKERS = (
    "用尽可能少的问题",
    "required_focus",
    "主题可以跨学段",
    "任务类型",
    "育人素养",
    "载体路由",
    "3.3:1—4:1",
    "柔性构图",
    "标题语法",
    "中文文风",
    "5米",
    "可绘制性",
    "A_recommended_",
    "B_enhanced_",
    "C_simplified_",
    "每次图片调用都完整写入",
    "通用负面约束",
    "文字真值稿",
    "图中文字核验",
    "想替换什么",
    "重新执行路由",
    "局部放大与可打印素材",
    "150—300字设计理念",
    "准确性、版权与符号",
    "交付前质量门",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        fail("SKILL.md must begin with YAML frontmatter")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        fail("SKILL.md frontmatter must be a mapping")
    return data, text


def repository_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__", ".venv"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not ignored_parts.intersection(path.relative_to(ROOT).parts)
    ]


def validate_metadata() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    metadata, skill_text = parse_frontmatter(ROOT / "SKILL.md")
    if metadata.get("name") != SKILL_NAME:
        fail(f"Skill name must be {SKILL_NAME}")
    if metadata.get("license") != "MIT":
        fail("Skill license must be MIT")
    description = metadata.get("description")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        fail("Skill description must contain 1-1024 characters")
    values = metadata.get("metadata")
    if not isinstance(values, dict) or not all(isinstance(value, str) for value in values.values()):
        fail("Skill metadata values must be strings")
    if values.get("version") != version:
        fail("VERSION and Skill metadata version differ")
    if len(skill_text.splitlines()) > 500:
        fail("SKILL.md exceeds 500 lines")

    references = ROOT / "references"
    actual = {path.name for path in references.iterdir() if path.is_file()}
    if actual != REFERENCES:
        fail(f"references must contain exactly: {', '.join(sorted(REFERENCES))}")
    if any(path.is_dir() for path in references.iterdir()):
        fail("references must not contain nested directories")
    for filename in REFERENCES:
        if f"references/{filename}" not in skill_text:
            fail(f"SKILL.md does not link references/{filename}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"v{version}" not in readme or f"[{version}]" not in changelog:
        fail("Current version is inconsistent in README or CHANGELOG")


def validate_yaml() -> None:
    required = [ROOT / "agents/openai.yaml", ROOT / "evals/test-cases.yaml"]
    required.extend((ROOT / ".github").rglob("*.yml"))
    required.extend((ROOT / ".github").rglob("*.yaml"))
    for path in required:
        yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_repository_hygiene() -> None:
    forbidden_path_fragments = (
        "/" + "Users/",
        "/" + "home/",
        "/" + "workspace/",
        "/" + "mnt/data/",
    )
    secret_patterns = (
        re.compile(r"gh" + r"p_[A-Za-z0-9]{20,}"),
        re.compile(r"sk" + r"-[A-Za-z0-9]{20,}"),
        re.compile(r"AK" + r"IA[0-9A-Z]{16}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    )
    files = repository_files()
    env_files = [path for path in files if path.name == ".env" or path.name.startswith(".env.")]
    if env_files:
        fail("Environment files are not allowed")
    images = [path for path in files if path.suffix.lower() in IMAGE_SUFFIXES]
    if images:
        fail("Image files are not allowed in this release candidate")

    for path in files:
        if path == Path(__file__).resolve() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(fragment in text for fragment in forbidden_path_fragments):
            fail(f"Local absolute path found in {path.relative_to(ROOT)}")
        if any(pattern.search(text) for pattern in secret_patterns):
            fail(f"Possible secret found in {path.relative_to(ROOT)}")


def validate_generated_files() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    result = subprocess.run(
        [sys.executable, "tools/build_portable.py", "--check"],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        fail("Portable distribution is stale")
    portable = ROOT / "dist" / f"blackboard-design-skill-portable-v{version}.md"
    portable_text = portable.read_text(encoding="utf-8")
    for marker in CORE_MARKERS:
        if marker not in portable_text:
            fail(f"Portable distribution is missing core rule: {marker}")

    release_result = subprocess.run(
        [sys.executable, "tools/build_release.py"],
        cwd=ROOT,
        check=False,
    )
    if release_result.returncode:
        fail("Standard release archive could not be built")
    archive_path = ROOT / "dist" / f"{SKILL_NAME}-v{version}.zip"
    allowed = {"SKILL.md", "LICENSE", "references", "agents"}
    with ZipFile(archive_path) as archive:
        names = archive.namelist()
    if not names or any(not name.startswith(f"{SKILL_NAME}/") for name in names):
        fail("Standard release archive has an invalid top-level directory")
    for name in names:
        relative = Path(name).relative_to(SKILL_NAME)
        if relative.parts[0] not in allowed:
            fail(f"Unexpected file in standard release archive: {relative}")


def main() -> int:
    try:
        validate_metadata()
        validate_yaml()
        validate_repository_hygiene()
        validate_generated_files()
    except (AssertionError, FileNotFoundError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
