# Blackboard Design Skill｜黑板报整图生成

由奕思 Geek&Chalk 推出的教师 Agent Skill，用于设计中国大陆小学、初中和高中的真实黑板报、班级主题板报、拼贴黑板与软板展板。

当前版本：**v0.7.3｜完整自包含运行恢复版**。项目仍处于公开测试阶段。

## 公众号

<img src="assets/wechat-official-account.jpg" alt="奕思 Geek&Chalk 微信公众号二维码" width="220">

项目使用意见与反馈，可在公众号留言。

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

1. 下载 `blackboard-design-skill-v0.7.3.md`；
2. 把这个文件上传到 Codex、WorkBuddy、千问工作台、豆包、Kimi 或其他支持文件读取的 AI；
3. 告诉 AI：“请加载这个黑板报 Skill，并为〔学段〕设计〔主题〕黑板报，板面采用〔传统黑板／黑板加剪贴／软板〕。”
4. 当前会话需要具备图片生成能力；只有文字能力时，Skill 会输出完整方案与生图提示词。

教师单文件、标准 ZIP 和仓库根目录 `SKILL.md` 使用同一份完整运行规则，不需要额外加载 `references/`。

## 快速开始

### 标准 Agent Skill 包

从 [Releases](https://github.com/EasonZhangyichen/blackboard-design-skill/releases) 下载 `blackboard-design-skill-v0.7.3.zip`，导入支持 Agent Skills 目录或 ZIP 的平台。标准 ZIP 包含完整 `SKILL.md`、许可证和 OpenAI 展示配置。

### 教师完整单文件

下载 `blackboard-design-skill-v0.7.3.md`。它与仓库根目录 `SKILL.md` 内容完全一致，适合只能上传一个文件的平台，也是面向普通教师的首选传播物。

### 网页图片模式

复制 [`dist/WEB-QUICK-PROMPT.md`](dist/WEB-QUICK-PROMPT.md) 到已经启用图片生成能力的网页会话。

示例：

> 使用黑板报 Skill，为高一设计“古韵传薪火 经典启新思”主题黑板报，采用传统手绘黑板，一键生成。

### Release 完整性校验

每个正式 Release 同时提供 `SHA256SUMS.txt`。下载发行文件后，可核对文件是否与发布版本一致：

```bash
# Linux
sha256sum -c SHA256SUMS.txt

# macOS
shasum -a 256 -c SHA256SUMS.txt
```

### 通过 GitHub 仓库地址安装

部分 Agent 可以读取或安装 GitHub 仓库，但这不是所有平台的通用能力。只有在平台明确支持“从仓库／URL安装 Skill”或能够克隆仓库时，才适合直接发送仓库地址。

- 支持仓库安装：让 Agent 读取仓库根目录 `SKILL.md`；
- 只支持上传文件：使用教师完整单文件；
- 支持 ZIP 导入：使用标准 Release ZIP；
- 普通网页聊天：先进入图片生成模式，再使用完整单文件或网页快速提示词。

不要只发送仓库首页并假设所有 AI 都会递归读取、安装和启用图片工具。

## 平台适配

需要区分三件事：平台能否读取 Skill 格式、当前会话是否真正提供图片工具、最终图像模型的质量。兼容 Skill 不代表一定能够成图，也不代表不同平台会获得相同画质。

| 平台类型 | Skill 使用 | 成图条件 |
|---|---|---|
| Codex、Claude Code、TRAE 等 Agent | 导入标准包或完整目录 | 当前 Agent 具备图片生成或编辑工具 |
| WorkBuddy / CodeBuddy 等工作台 | 导入 Skill；可按个人环境配置模型或工具 | 内置图片能力、MCP、连接器或外部图像 API 可用 |
| 千问、豆包、Kimi 等网页产品 | 上传完整单文件或使用快速提示词 | 先进入平台的图片生成入口 |

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
├── assets/
├── agents/openai.yaml
├── dist/
├── docs/
├── evals/
├── maintainers/
├── tests/
├── tools/
├── BRAND.md
├── PRIVACY.md
└── LICENSE
```

标准发布 ZIP 只包含 `SKILL.md`、`LICENSE` 和 `agents/openai.yaml`。教师单文件与 ZIP 均从根目录 `SKILL.md` 构建，三种入口使用同一套完整运行逻辑。v0.7.2 的模块化参考文档保留在 `docs/modular-v0.7.2/`，不作为运行前提。

## 验证与构建

```bash
python3 tools/build_portable.py --check
python3 tools/validate_package.py
python3 -m unittest discover -s tests
python3 tools/build_release.py
python3 tools/build_checksums.py
```

CI 会运行 Agent Skills 官方参考验证器、YAML 解析、版本一致性、敏感信息、批准图片和发行契约检查，并分别验证标准包与教师完整单文件。`main` 分支中的 `VERSION` 变化会触发受控 Release 工作流，生成版本标签、发布说明、发行附件与 SHA-256 校验文件。

## 贡献

提交问题或改进前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。安全问题请按 [`SECURITY.md`](SECURITY.md) 私下报告；参与者应遵守 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)。

## 品牌与独立项目声明

“奕思 Geek&Chalk”是本项目的发布者标识。第三方修改版本不得暗示获得官方背书。本项目是独立开源项目，与文中提及的平台和模型提供方不存在官方隶属或背书关系。详见 [`BRAND.md`](BRAND.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。
