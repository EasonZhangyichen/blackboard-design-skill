# 分发方式

本项目采用一套标准源码、三种使用入口：

1. 标准 Agent Skill ZIP：供支持目录式 Skill 的平台导入；
2. Portable 单文件：供只能上传单个文档的平台使用；
3. 网页快速提示词：供已进入图片生成模式的网页产品使用。

标准 ZIP 固定以 `blackboard-design-skill/` 为顶层目录，只包含 `SKILL.md`、`LICENSE`、`references/` 和 `agents/`。Portable 文件由同一套标准源码生成，不能独立编辑。

正式版本应同时提供：

- GitHub 仓库主页；
- 标准 ZIP；
- Portable 单文件；
- `WEB-QUICK-PROMPT.md`；
- 对应版本说明。

对外介绍必须区分 Skill 格式兼容、图片工具可用性和实际图像模型质量，不承诺不同平台获得完全相同的结果。
