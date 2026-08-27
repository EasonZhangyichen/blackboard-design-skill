from __future__ import annotations

from pathlib import Path
import subprocess
import unittest
from zipfile import ZipFile

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "blackboard-design-skill"
REFERENCE_FILES = (
    "pedagogy-and-stages.md",
    "image-grammar.md",
    "generation-protocol.md",
    "writing-and-compliance.md",
)
PORTABLE_ANCHORS = (
    "portable-reference-pedagogy-and-stages",
    "portable-reference-image-grammar",
    "portable-reference-generation-protocol",
    "portable-reference-writing-and-compliance",
)
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


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    prefix, raw, _ = text.split("---", 2)
    if prefix.strip():
        raise AssertionError(f"{path} does not begin with YAML frontmatter")
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise AssertionError(f"Invalid frontmatter in {path}")
    return data


class PublicReleaseContractTests(unittest.TestCase):
    def test_standard_skill_structure_and_metadata(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, "0.7.2")

        skill = ROOT / "SKILL.md"
        frontmatter = read_frontmatter(skill)
        self.assertEqual(frontmatter["name"], SKILL_NAME)
        self.assertEqual(frontmatter["license"], "MIT")
        self.assertEqual(frontmatter["metadata"]["version"], version)
        self.assertLessEqual(len(str(frontmatter["description"])), 1024)
        self.assertTrue(all(isinstance(value, str) for value in frontmatter["metadata"].values()))
        skill_text = skill.read_text(encoding="utf-8")
        self.assertLessEqual(len(skill_text.splitlines()), 500)
        self.assertIn("## 参考文件加载规则", skill_text)

        for filename in REFERENCE_FILES:
            reference = ROOT / "references" / filename
            self.assertTrue(reference.is_file(), filename)
            self.assertIn(f"references/{filename}", skill_text)

    def test_portable_and_standard_release_are_generated(self) -> None:
        subprocess.run(["python3", "tools/build_portable.py"], cwd=ROOT, check=True)
        subprocess.run(["python3", "tools/build_release.py"], cwd=ROOT, check=True)

        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        portable = ROOT / "dist" / f"blackboard-design-skill-portable-v{version}.md"
        archive = ROOT / "dist" / f"blackboard-design-skill-v{version}.zip"
        portable_text = portable.read_text(encoding="utf-8")
        portable_frontmatter = read_frontmatter(portable)

        self.assertEqual(portable_frontmatter["name"], SKILL_NAME)
        self.assertIn("Portable 单文件说明", portable_text)
        self.assertNotIn("(references/", portable_text)
        for anchor in PORTABLE_ANCHORS:
            self.assertIn(f'id="{anchor}"', portable_text)
            self.assertIn(f"](#{anchor})", portable_text)
        for marker in CORE_MARKERS:
            self.assertIn(marker, portable_text)

        with ZipFile(archive) as release:
            names = release.namelist()
        self.assertTrue(names)
        self.assertTrue(all(name.startswith(f"{SKILL_NAME}/") for name in names))
        allowed = {"SKILL.md", "LICENSE", "references", "agents"}
        for name in names:
            relative = Path(name).relative_to(SKILL_NAME)
            self.assertIn(relative.parts[0], allowed)

    def test_public_project_files_exist(self) -> None:
        required = (
            "BRAND.md",
            "CONTRIBUTING.md",
            "SECURITY.md",
            "PRIVACY.md",
            "CODE_OF_CONDUCT.md",
            "agents/openai.yaml",
            ".github/CODEOWNERS",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/feature_request.yml",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/workflows/validate.yml",
        )
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
