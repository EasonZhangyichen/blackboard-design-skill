# 分发方式

本项目采用一个完整运行真源、三种使用入口：

1. 标准 Agent Skill ZIP：供支持目录式 Skill 的平台导入；
2. 教师完整单文件：供只能上传单个文档的平台使用；
3. 网页快速提示词：供已进入图片生成模式的网页产品使用。

标准 ZIP 固定以 `blackboard-design-skill/` 为顶层目录，只包含 `SKILL.md`、`LICENSE` 和 `agents/openai.yaml`。教师完整单文件与根目录 `SKILL.md` 完全一致，不能独立编辑。

正式版本同时提供：

- GitHub 仓库主页；
- `blackboard-design-skill-v<version>.zip`；
- `blackboard-design-skill-v<version>.md`；
- `WEB-QUICK-PROMPT.md`；
- `SHA256SUMS.txt`；
- 对应版本说明。

`main` 分支中的 `VERSION` 变化会触发自动 Release 工作流。工作流在重新执行验证后创建或更新对应版本标签和 Release，并上传四个发行附件。维护者发布后仍需人工核验附件、说明和下载链接。

对外介绍必须区分 Skill 格式兼容、图片工具可用性和实际图像模型质量，不承诺不同平台获得完全相同的结果。
