# Blackboard Design Skill｜黑板报整图生成 Skill

面向中国大陆小学、初中和高中教师的自包含式 `SKILL.md`。输入学段、主题与板面形式后，Skill 会完成育人命题转译、中文标题与正文、柔性字图构图、同题三案、局部修改和可打印局部素材。

当前版本：**v0.7.1｜跨学段主题兼容与发行校准版**

## 本版微调

- 明确社会主义核心价值观、学生素养与五育、节气、中华优秀传统文化、红色精神、重大节日、传统节日和革命纪念日等主题都可以跨学段出现；
- 学段路由只改变认知入口、标题语言、正文深度、核心意象与行动连接，不把主题限定给某一年龄段；
- 用户或学校指定的价值方向、关键词、人物与事件会进入三案的共享设计核心；
- 保持 v0.7.0 的柔性构图、真实宽板、同题三案、结果优先和二轮修改闭环；
- 增加平台适配、传播方式和私有 GitHub 发布指南。

## 最快使用方式

### 1. 支持 Agent Skills 的平台

将整个目录导入平台，或只安装根目录 `SKILL.md`，然后直接说：

> 使用黑板报 Skill，为高一设计“古韵传薪火 经典启新思”主题黑板报，传统手绘黑板，一键生成。

### 2. 只能上传单文件的平台或 Skill 社区

上传根目录 `SKILL.md`。它是完整、自包含的核心发行物，不依赖参考图或附加资料。

### 3. 普通网页图片模式

先进入平台的图片生成模式，再使用 `dist/WEB-QUICK-PROMPT.md`。普通文字聊天没有图片工具时，只能输出策划和生图提示词。

## 应该传播哪个文件

| 使用对象 | 推荐交付 |
|---|---|
| Skill 社区、小红书 Skill 分享、普通教师 | `SKILL.md` + GitHub 仓库链接 |
| Codex、Claude Code、TRAE、CodeBuddy 等 Agent 用户 | 完整 Release ZIP 或克隆仓库 |
| 千问、豆包、Kimi 等网页图片模式 | `WEB-QUICK-PROMPT.md`；支持文件上传时也可附 `SKILL.md` |
| 开发者和贡献者 | GitHub 仓库 |

不要只对 AI 说“读取这个 GitHub 仓库”。部分平台不会递归读取仓库。公开后应优先提供：

1. GitHub 仓库主页；
2. 根目录 `SKILL.md` 的直接文件链接；
3. Release ZIP；
4. 网页图片模式快速提示词。

详见 `docs/PUBLISHING.md`。

## 平台适配概览

| 平台 | Skill 读取 | 整图生成 | 建议 |
|---|---|---|---|
| Codex | 原生适合 | 具备图像工具时完整执行 | 当前推荐的完整体验入口 |
| WorkBuddy / CodeBuddy | 支持 `SKILL.md`、MCP 与自定义模型 | 取决于实际图片工具和最终路由模型 | 使用较强规划模型；如追求更高画质，通过 MCP/连接器接入 GPT Image 2 等真正的图片生成工具 |
| 千问办公 / 千问工作台 | 可读取任务材料，整合多模态能力 | 进入图片生成能力后可用 | Qwen Image 对复杂布局和中文文字较友好，作者实测效果较好 |
| 豆包工作模式 | 可使用核心 Skill 或快速提示词 | 开启图像生成、Seedream 或相应工具时可用 | 作者实测可用；实际质量取决于产品路由与当前模型 |
| TRAE | 支持 Skill | 取决于图片工具、MCP 或 API | 适合完整目录导入 |
| Claude Code | 支持 Skill | 需要外部图片工具或 MCP | 无图片工具时自动退化为策划模式 |
| Kimi / Kimi Code | 可读取 Skill 或提示词 | 取决于图片插件或工具 | 网页端先进入图片生成入口 |

**兼容 Skill 格式不等于所有平台会产生相同画质。**规划模型、图片模型、工具权限、长宽比支持和中文文字渲染都会影响结果。

### WorkBuddy 接入 GPT Image 2 的注意点

WorkBuddy / CodeBuddy 官方支持 Skills、模型配置与 MCP。GPT Image 2 是图像生成与编辑模型，使用图像生成或编辑端点。更稳妥的方式是通过 MCP、连接器或一个 API 工具封装把 GPT Image 2 暴露为“图片生成工具”，而不是只把它配置成普通对话模型。

详见 `docs/PLATFORM-GUIDE.md`。

## 仓库结构

```text
blackboard-design-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE-DECISION.md
├── .gitignore
├── dist/
│   ├── WEB-QUICK-PROMPT.md
│   └── blackboard-design-SKILL-v0.7.1.md
├── docs/
│   ├── IMAGE-GRAMMAR-v1.1.md
│   ├── PLATFORM-GUIDE.md
│   ├── PUBLISHING.md
│   ├── PUBLISH-TO-GITHUB.md
│   └── LOCAL-CODEX-PROMPT.md
├── evals/
│   ├── test-cases.yaml
│   └── rubric.md
└── scripts/
    ├── validate_package.py
    ├── build_release.py
    └── publish_private.sh
```

## 验证与打包

```bash
python3 scripts/validate_package.py
python3 scripts/build_release.py
```

## GitHub 发布

当前建议先创建 **private** 仓库，完成复核与实测后再改为 public。完整步骤见：

- `docs/PUBLISH-TO-GITHUB.md`
- `docs/LOCAL-CODEX-PROMPT.md`

## 为什么主包不附普通参考图

1. 核心 Skill 必须单文件独立工作；
2. 一般参考图会形成不必要的审美锚定；
3. 图片存在来源、版权和质量分层问题；
4. 案例更适合内部蒸馏、回归评测和未来精选 Showcase。

未来只有达到作者认可的审美上限、来源清楚且有展示权限的“黄金案例”，才适合放入单独的 `showcase/`，且仍不作为运行依赖。

## 许可证

公开发布前请阅读 `LICENSE-DECISION.md`。在没有正式 `LICENSE` 之前，仓库虽然可以公开查看，但不应宣传为已经完成开源授权。
