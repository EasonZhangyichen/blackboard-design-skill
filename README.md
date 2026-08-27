# Blackboard Design Skill｜黑板报整图生成

由奕思 Geek&Chalk 推出的教师 Agent Skill，用于设计中国大陆小学、初中和高中的真实黑板报、班级主题板报、拼贴黑板与软板展板。

当前版本：**v0.7.2｜公开发布工程加固版（Public Release Candidate）**。项目仍处于公开测试阶段。

## 核心能力

- 将主题、固定标题和学校要求转译为适合当前学段的育人命题；
- 先建立中文文字真值稿，再组织标题、正文与图像；
- 使用视觉锚点、主要走势、标题姿态和文字流线完成柔性构图；
- 默认提供A推荐主案、B风格强化案、C简化实操案；
- 支持完整成图、局部修改和选案后的可打印局部素材；
- 当前环境没有图片工具时，自动退化为三案简报与自包含提示词，不假装已经成图。

## 学段与载体

| 学段 | 主要表达 |
|---|---|
| 小学低段 | 具体生活、温暖短句、易描画或易剪贴的元素 |
| 小学高段 | 事实、故事与行动结合，场景和模块并用 |
| 初中 | 少年感、真实问题、责任选择与清楚阅读路径 |
| 高中 | 历史与现实判断、字图共生、长卷或视觉特刊 |

支持三类载体：传统手绘黑板、黑板加卡纸剪贴、软板／展板。主题可以跨学段，变化的是认知入口、文案深度、意象和行动连接。

## A/B/C 三案

- **A｜推荐主案**：内容、审美、阅读性与可实施性最均衡。
- **B｜风格强化案**：加强题字、构图、色彩或材料语言，仍然可落地。
- **C｜简化实操案**：保留主题与主要走势，减少非必要细节，便于现实绘制。

三案共享主题、育人命题与文字核心，差异不是简单换色或换边框。

## 普通教师最简单的使用方式

多数教师不需要学习 GitHub，也不需要理解仓库结构。

1. 下载 `blackboard-design-skill-portable-v0.7.2.md`；
2. 把这个文件上传到 Codex、WorkBuddy、千问工作台、豆包、Kimi 或其他支持文件读取的 AI；
3. 告诉 AI：“请加载这个黑板报 Skill，并为〔学段〕设计〔主题〕黑板报，板面采用〔传统黑板／黑板加剪贴／软板〕。”
4. 当前会话需要具备图片生成能力；只有文字能力时，Skill 会输出完整方案与生图提示词。

**不要把根目录185行的 `SKILL.md` 单独发给只支持单文件的平台。**它是标准目录包的入口，需要同时读取 `references/`。单文件传播应使用 Portable 文件。

## 快速开始

### 标准 Agent Skill 包

从 [Releases](https://github.com/EasonZhangyichen/blackboard-design-skill/releases) 下载 `blackboard-design-skill-v0.7.2.zip`，导入支持 Agent Skills 目录或 ZIP 的平台。标准 ZIP 包含主 `SKILL.md`、四份专业参考规则、许可证和 OpenAI 展示配置。

### Portable 单文件

下载 `blackboard-design-skill-portable-v0.7.2.md`。它由标准版自动构建，已经内嵌全部专业规则，适合只能上传一个文件的平台，也是面向普通教师的首选传播物。

### 网页图片模式

复制 [`dist/WEB-QUICK-PROMPT.md`](dist/WEB-QUICK-PROMPT.md) 到已经启用图片生成能力的网页会话。

示例：

> 使用黑板报 Skill，为高一设计“古韵传薪火 经典启新思”主题黑板报，采用传统手绘黑板，一键生成。

### 通过 GitHub 仓库地址安装

部分 Agent 可以读取或安装 GitHub 仓库，但这不是所有平台的通用能力。只有在平台明确支持“从仓库／URL安装 Skill”或能够克隆仓库时，才适合直接发送仓库地址。

- 支持仓库安装：可让 Agent 读取仓库根目录 `SKILL.md` 与 `references/`；
- 只支持上传文件：使用 Portable 单文件；
- 支持 ZIP 导入：使用标准 Release ZIP；
- 普通网页聊天：先进入图片生成模式，再使用 Portable 或网页快速提示词。

不要只发送仓库首页并假设所有 AI 都会递归读取、安装和启用图片工具。

## 平台适配

需要区分三件事：平台能否读取 Skill 格式、当前会话是否真正提供图片工具、最终图像模型的质量。兼容 Skill 不代表一定能够成图，也不代表不同平台会获得相同画质。

| 平台类型 | Skill 使用 | 成图条件 |
|---|---|---|
| Codex、Claude Code、TRAE 等 Agent | 导入标准包或完整目录 | 当前 Agent 具备图片生成或编辑工具 |
| WorkBuddy / CodeBuddy 等工作台 | 导入 Skill；可按个人环境配置模型或工具 | 内置图片能力、MCP、连接器或外部图像 API 可用 |
| 千问、豆包、Kimi 等网页产品 | 上传 Portable 文件或使用快速提示词 | 先进入平台的图片生成入口 |

本 Skill 不强制使用 GPT Image 2 或任何指定图片模型。模型与工具配置属于使用者和宿主平台的选择。详见 [`docs/PLATFORM-GUIDE.md`](docs/PLATFORM-GUIDE.md)。

## 已知限制

- 中文长文在生成图片中可能出现错字，最终抄写以文字真值稿为准。
- 超宽比例、参考图编辑和局部修字能力取决于宿主工具。
- 历史、法治、安全、科学、纪念日期和引文等事实内容需要可靠来源；无法核实时应省略。
- 不同平台的规划模型、图像模型与权限会造成结果差异。

## 隐私

上传真实黑板、学生作品或学校材料前，请移除学生姓名、学号、联系方式、人脸和其他可识别信息。本项目不需要收集个人数据，也不应把用户材料加入公开仓库。详见 [`PRIVACY.md`](PRIVACY.md)。

## 项目结构

```text
blackboard-design-skill/
├── SKILL.md
├── references/
├── agents/openai.yaml
├── dist/
├── docs/
├── evals/
├── tests/
├── tools/
├── BRAND.md
├── PRIVACY.md
└── LICENSE
```

标准发布 ZIP 只包含运行所需的 `SKILL.md`、`LICENSE`、`references/` 和 `agents/`。Portable 单文件与 ZIP 均由构建工具生成，不单独维护。

## 验证与构建

```bash
python3 tools/validate_package.py
python3 -m unittest discover -s tests
python3 tools/build_portable.py
python3 tools/build_release.py
```

CI 还会运行 Agent Skills 官方参考验证器、YAML 解析、版本一致性、敏感信息和图片文件检查，并分别验证标准包与 Portable 单文件。

## 贡献

提交问题或改进前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。安全问题请按 [`SECURITY.md`](SECURITY.md) 私下报告；参与者应遵守 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)。

## 品牌与独立项目声明

“奕思 Geek&Chalk”是本项目的发布者标识。第三方修改版本不得暗示获得官方背书。本项目是独立开源项目，与文中提及的平台和模型提供方不存在官方隶属或背书关系。详见 [`BRAND.md`](BRAND.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。
