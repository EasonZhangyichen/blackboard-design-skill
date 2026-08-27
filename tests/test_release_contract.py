from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import unittest
from zipfile import ZipFile

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "blackboard-design-skill"
BRAND_ASSET = "assets/wechat-official-account.jpg"
BRAND_ASSET_SHA256 = "1fcdab09d012580b4a6923d12cc7590346d745c039615ce9641145064d02a2d9"
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
    "弱模型必带的负面约束",
    "文字真值稿",
    "图中文字核验",
    "想替换什么",
    "重大变化必须重新路由",
    "局部放大与可打印素材",
    "150—300字设计理念",
    "合规与准确",
    "交付前质量门",
)
FULL_RUNTIME_SECTIONS = (
    "## 1. 核心任务",
    "## 3. 当前能力判断",
    "## 6. 先判断任务类型",
    "## 8. 主题转译",
    "## 9. 学段路由：画面、标题、正文和育人价值共同进阶",
    "## 12. 真实板面视觉契约",
    "## 13. 柔性构图语法",
    "## 14. 标题语法",
    "## 15. 正文与文字流线",
    "## 19. 同题三案",
    "## 20. 图片生成执行协议",
    "## 21. 结果优先与默认反馈闭环",
    "## 23. 第二阶段：局部放大与可打印素材",
    "## 26. 交付前质量门",
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
        self.assertEqual(version, "0.7.3")

        skill = ROOT / "SKILL.md"
        frontmatter = read_frontmatter(skill)
        self.assertEqual(frontmatter["name"], SKILL_NAME)
        self.assertEqual(frontmatter["license"], "MIT")
        self.assertEqual(frontmatter["metadata"]["author"], "奕思 Geek&Chalk")
        self.assertEqual(frontmatter["metadata"]["version"], version)
        self.assertEqual(
            frontmatter["metadata"]["repository"],
            "https://github.com/EasonZhangyichen/blackboard-design-skill",
        )
        self.assertIn("Agent Skills", frontmatter["compatibility"])
        self.assertLessEqual(len(str(frontmatter["description"])), 1024)
        self.assertTrue(all(isinstance(value, str) for value in frontmatter["metadata"].values()))
        skill_text = skill.read_text(encoding="utf-8")
        self.assertGreater(len(skill_text.splitlines()), 500)
        self.assertNotIn("## 参考文件加载规则", skill_text)
        self.assertNotIn("references/", skill_text)
        for section in FULL_RUNTIME_SECTIONS:
            self.assertIn(section, skill_text)
        for marker in CORE_MARKERS:
            self.assertIn(marker, skill_text)
        self.assertIn("不要求所有平台或模型使用某个指定图片模型", skill_text)
        self.assertIn("学生姓名", skill_text)

    def test_portable_and_standard_release_are_generated(self) -> None:
        subprocess.run(["python3", "tools/build_portable.py"], cwd=ROOT, check=True)
        subprocess.run(["python3", "tools/build_release.py"], cwd=ROOT, check=True)

        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        portable = ROOT / "dist" / f"blackboard-design-skill-v{version}.md"
        archive = ROOT / "dist" / f"blackboard-design-skill-v{version}.zip"
        portable_text = portable.read_text(encoding="utf-8")
        portable_frontmatter = read_frontmatter(portable)

        self.assertEqual(portable_frontmatter["name"], SKILL_NAME)
        self.assertEqual(portable_text, (ROOT / "SKILL.md").read_text(encoding="utf-8"))

        with ZipFile(archive) as release:
            names = release.namelist()
        self.assertEqual(
            names,
            [
                f"{SKILL_NAME}/SKILL.md",
                f"{SKILL_NAME}/LICENSE",
                f"{SKILL_NAME}/agents/openai.yaml",
            ],
        )

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

    def test_official_account_brand_entry_is_exact_and_documented(self) -> None:
        asset = ROOT / BRAND_ASSET
        self.assertTrue(asset.is_file(), BRAND_ASSET)
        self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), BRAND_ASSET_SHA256)

        for relative in ("README.md", "BRAND.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(BRAND_ASSET, text)
            self.assertIn("公众号留言", text)

        code_of_conduct = (ROOT / "CODE_OF_CONDUCT.md").read_text(encoding="utf-8")
        self.assertNotIn("GitHub 私信", code_of_conduct)
        self.assertIn("公众号留言", code_of_conduct)

        security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("README 或 BRAND.md 中的公众号", security)
        self.assertIn("不要在公众号留言中提交", security)

        subprocess.run(["python3", "tools/build_release.py"], cwd=ROOT, check=True)
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        archive = ROOT / "dist" / f"blackboard-design-skill-v{version}.zip"
        with ZipFile(archive) as release:
            names = release.namelist()
        self.assertFalse(any("wechat-official-account" in name for name in names))


if __name__ == "__main__":
    unittest.main()
