#!/usr/bin/env python3
"""Build Markdown release notes from the current CHANGELOG section."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def changelog_section(current: str) -> str:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    heading = f"## [{current}]"
    start = changelog.find(heading)
    if start < 0:
        raise SystemExit(f"Missing {heading} in CHANGELOG.md")
    remainder = changelog[start:]
    next_heading = remainder.find("\n## [", len(heading))
    return (remainder if next_heading < 0 else remainder[:next_heading]).strip()


def render() -> str:
    current = version()
    parts = (
        f"# Blackboard Design Skill v{current}",
        "面向中国大陆小学、初中和高中教师的黑板报整图生成 Skill，由 **奕思 Geek&Chalk** 维护。",
        changelog_section(current),
        "\n".join(
            (
                "## 下载建议",
                "",
                f"- 普通教师：下载 `blackboard-design-skill-v{current}.md`；",
                f"- Agent / 技术用户：下载 `blackboard-design-skill-v{current}.zip`；",
                "- 网页图片模式：使用 `WEB-QUICK-PROMPT.md`；",
                "- 完整性校验：下载 `SHA256SUMS.txt`。",
            )
        ),
        "不同平台最终画质取决于实际规划模型、图片模型和工具权限。",
    )
    return "\n\n".join(parts) + "\n"


def main() -> int:
    destination = ROOT / "dist" / "RELEASE_NOTES.md"
    destination.write_text(render(), encoding="utf-8")
    print(f"Built {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
