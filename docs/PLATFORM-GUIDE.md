# 平台适配指南

## 1. 先区分三件事

1. **Skill 格式兼容**：平台能否读取 `SKILL.md`；
2. **图片工具可用**：平台是否真正具备文生图、参考生图或图片编辑工具；
3. **最终画质**：取决于规划模型、图片模型、提示遵循、中文渲染与长宽比能力。

因此，“支持本 Skill”不等于所有平台会生成完全相同的图片。

## 2. Codex

### 推荐方式

- 把完整目录作为项目打开；或把 `SKILL.md` 安装到 Codex Skill 目录；
- 确认当前环境存在图片生成工具；
- 让 Codex顺序生成 A、B、C 三案，核验文件名和文字真值稿。

### 适合原因

Codex适合完成多步骤规划、文件管理、顺序生图、重命名和局部修改。当前作者实测中，整体理解、提问准确性和构图质量较稳定。

官方参考：

- OpenAI Developers：<https://developers.openai.com/>
- GPT Image 2：<https://developers.openai.com/api/docs/models/gpt-image-2>

## 3. WorkBuddy / CodeBuddy

### Skill 安装

CodeBuddy 官方 Skills 结构以 `SKILL.md` 为核心，可以放在项目级 `.codebuddy/skills/` 或用户级 Skill 目录。WorkBuddy / CodeBuddy 也支持 MCP 与自定义模型。

### 推荐配置

- 规划环节选择较强的推理或通用模型；
- 关闭容易造成不可控路由的 Auto 模式，或至少核对最终调用的图片模型；
- 三案逐张生成，不并行；
- 追求更高出图质量时，通过 MCP、连接器或 API 工具封装接入真正的图像生成模型。

### GPT Image 2 的正确接入理解

GPT Image 2 提供图像生成与图像编辑端点。WorkBuddy 的普通自定义聊天模型配置通常面向 `/chat/completions`，不应简单把 GPT Image 2 当作普通聊天模型。更稳妥的方式是：

1. 创建或安装一个图片生成 MCP / connector；
2. 在工具内部调用 OpenAI `gpt-image-2` 的图像生成或编辑接口；
3. 将该能力暴露给 WorkBuddy Agent；
4. 由黑板报 Skill 负责策划和提示词，图片工具负责真正成图。

官方参考：

- WorkBuddy / CodeBuddy Skills：<https://www.workbuddy.ai/docs/zh/ide/Features/Skills>
- WorkBuddy 模型配置：<https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model>
- CodeBuddy MCP：<https://www.workbuddy.ai/docs/zh/ide/User-guide/MCP>
- GPT Image 2：<https://developers.openai.com/api/docs/models/gpt-image-2>

## 4. 千问办公 / 千问工作台

### 推荐方式

- 在具备多模态生成或图片生成能力的工作台中使用；
- 能上传文件时上传 `SKILL.md`；
- 不能上传时，使用 `dist/WEB-QUICK-PROMPT.md`；
- 明确要求超宽真实黑板、中文真值稿和顺序生成三案。

千问办公官方定位为整合多模态生成的一站式生产力平台。Qwen Image 系列对复杂布局、多行文字和中文渲染较有优势。作者实测中，千问工作台整体结果可用。

官方参考：

- 千问办公：<https://help.aliyun.com/zh/qwenwork/>
- Qwen Image：<https://help.aliyun.com/zh/model-studio/qwen-image>
- 千问文生图：<https://help.aliyun.com/zh/model-studio/text-to-image>

## 5. 豆包工作模式

### 推荐方式

- 当前工作模式必须具备图片生成能力；
- 若能选择图像模型，优先使用较新的 Seedream / 豆包图像创作能力；
- 若只支持文本对话，使用快速提示词生成设计简报，再切换图片入口；
- 每轮成图后继续使用 Skill 的三项反馈闭环进行局部修改。

作者实测豆包工作模式可以完成此类任务，但产品入口、路由模型与权限可能随版本变化，因此 README 只宣称“可用”，不保证与 Codex 或千问获得相同画质。

官方参考：

- 火山引擎豆包图像创作能力：<https://www.volcengine.com/sem>

## 6. TRAE

TRAE 可使用 `SKILL.md` 形式的 Skill。建议导入完整目录；实际成图能力取决于当前 Agent 是否配置图片工具、MCP 或外部 API。

- 有图片工具：执行完整三案；
- 没有图片工具：进入策划模式；
- 若使用外部图片 API，应把它封装成可调用工具，而不是要求语言模型自行“想象已生成”。

官方 Skill 页面：<https://docs.trae.ai/ide/skills?_lang=zh>

## 7. Claude Code

Claude Code 可以加载 Skill；但整图生成通常需要额外 MCP 或外部图像工具。将 Skill 与图像工具分开理解：

- Skill 负责领域知识、流程和图像提示；
- MCP / API 工具负责图片生成与编辑。

## 8. Kimi / Kimi Code

- 支持 Skill 或文件读取时使用 `SKILL.md`；
- 网页端需要先启用图片插件或进入图片生成入口；
- 无图片工具时使用策划模式或快速提示词。

## 9. 推荐等级

### 完整体验

- Codex + 可用图片工具
- 强 Agent + GPT Image 2 / Qwen Image / Seedream 等实际图片工具

### 低门槛可用

- 千问办公 / 千问工作台图片能力
- 豆包工作模式图片能力
- WorkBuddy 内置图片路由

### 条件支持

- TRAE、Claude Code、Kimi Code：需要确认图片工具或 MCP
- 普通网页聊天：需要手动切换图片模式
