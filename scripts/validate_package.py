from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
DIST_SKILL = ROOT / "dist" / "blackboard-design-SKILL-v0.7.1.md"
TESTS = ROOT / "evals" / "test-cases.yaml"
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
    ROOT / "LICENSE",
    DIST_SKILL,
    ROOT / "dist" / "WEB-QUICK-PROMPT.md",
    ROOT / "docs" / "IMAGE-GRAMMAR-v1.1.md",
    ROOT / "docs" / "PLATFORM-GUIDE.md",
    ROOT / "docs" / "PUBLISHING.md",
    ROOT / "docs" / "PUBLISH-TO-GITHUB.md",
    ROOT / "docs" / "LOCAL-CODEX-PROMPT.md",
    TESTS,
    ROOT / "evals" / "rubric.md",
    ROOT / "scripts" / "build_release.py",
    ROOT / "scripts" / "publish_private.sh",
]

errors: list[str] = []

for path in REQUIRED_FILES:
    if not path.exists():
        errors.append(f"缺少发行文件：{path.relative_to(ROOT)}")

if not SKILL.exists():
    errors.append("缺少 SKILL.md")
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md 缺少 YAML frontmatter")
    parts = text.split("---", 2)
    frontmatter = parts[1] if len(parts) >= 3 else ""
    for field in ("name:", "description:"):
        if field not in frontmatter:
            errors.append(f"frontmatter 缺少 {field}")

    forbidden = [
        r"/workspace/",
        r"/mnt/data/",
        r"必须读取外部案例",
        r"依赖参考图片",
        r"固定标题区.*固定正文区",
    ]
    for pattern in forbidden:
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            errors.append(f"发现不可移植、外部依赖或回退式固定骨架内容：{pattern}")

    required = [
        "v0.7.1（跨学段主题兼容与发行校准版）",
        "任务类型",
        "育人素养",
        "视觉锚点",
        "画面走势",
        "标题姿态",
        "文字流线",
        "流线长卷",
        "主景环绕",
        "题字驱动",
        "双叙事",
        "手绘视觉特刊",
        "模块软板",
        "3.3:1—4:1",
        "主题可以跨学段",
        "required_focus",
        "社会主义核心价值观",
        "学生素养",
        "节气",
        "中华优秀传统文化",
        "红色精神",
        "重大节日",
        "传统节日",
        "革命纪念日",
        "想替换什么",
        "哪些地方不满意",
        "哪些部分希望保留",
        "A_recommended_",
        "B_enhanced_",
        "C_simplified_",
    ]
    for item in required:
        if item not in text:
            errors.append(f"缺少关键规则：{item}")

    if DIST_SKILL.exists() and DIST_SKILL.read_text(encoding="utf-8") != text:
        errors.append("dist/blackboard-design-SKILL-v0.7.1.md 与根目录 SKILL.md 不一致")

if TESTS.exists():
    tests_text = TESTS.read_text(encoding="utf-8")
    for item in ("0.7.1", "社会主义核心价值观", "革命纪念日", "跨学段"):
        if item not in tests_text:
            errors.append(f"回归测试缺少：{item}")

image_suffixes = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg"}
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in image_suffixes:
        errors.append(f"主发行包不应默认包含图片：{path.relative_to(ROOT)}")

# Only CHANGELOG may retain historical release mentions.
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".sh"}:
        continue
    if path.name in {"CHANGELOG.md", "validate_package.py"}:
        continue
    body = path.read_text(encoding="utf-8", errors="replace")
    if "blackboard-design-SKILL-v0.7.0" in body or "blackboard-design-skill-v0.7.0.zip" in body:
        errors.append(f"发现旧发行文件名残留：{path.relative_to(ROOT)}")

if errors:
    print("Blackboard Design Skill package validation: FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Blackboard Design Skill package validation: OK")
print("核心结构、跨学段主题转译、柔性图像语法、反馈闭环、发行文件和无图片依赖检查通过。")
