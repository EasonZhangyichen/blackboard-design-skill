# Changelog

本项目的重要变更记录在此文件中。

## [Unreleased]

## [0.7.3] - 2026-08-27

- 恢复经真实测试表现稳定的 v0.7.1 完整自包含运行正文，不再要求运行前读取 `references/`。
- 保留 v0.7.2 的开源工程、品牌、MIT License、CI、社区文档和 Release 架构。
- 跨平台小学、初中和高中实测显示，模块化运行可能出现内容减少、构图模块化和结果海报化，因此重新以完整单文件作为唯一运行真源。
- 教师单文件与根目录 `SKILL.md` 完全一致；标准 ZIP 使用同一运行文件，只附带许可证和 OpenAI 展示配置。
- 保留跨学段主题、唯一文件命名、能力握手、图片模型不绑定、真实宽板、二轮反馈、重路由、隐私与事实准确性规则。
- 加固发行链路：CI 明确检查版本化单文件已被 Git 跟踪且内容最新，升级到 Node 24 运行时的官方 Actions，并加入自动 Release、发行说明和 SHA-256 校验文件。

## [0.7.2] - 2026-08-27

- 将标准 Skill 名称统一为 `blackboard-design-skill`，补齐 MIT、版本、仓库和维护者元数据。
- 将主 `SKILL.md` 收敛为标准入口，并把详细规则拆入四份一级参考文档。
- 增加由标准版自动生成的 Portable 单文件和固定顶层目录的标准发布 ZIP。
- 明确图片工具由宿主平台提供，不强制绑定 GPT Image 2 或其他指定模型。
- 增加 OpenAI 可选展示信息、品牌声明、隐私说明和开源社区文件。
- 增加版本一致性、YAML、官方规范、发布包、敏感信息与图片文件检查。

## [0.7.1] - 2026-08-26

- 明确核心价值观、学生素养与五育、节气、传统文化、红色精神和纪念主题均可跨学段出现。
- 明确学段路由改变认知入口、标题语言、正文深度、核心意象与行动连接。
- 将用户或学校指定的育人方向、关键词、人物与事件纳入共享设计核心。
- 增加跨学段转译示例、平台说明与 MIT License。

## [0.7.0]

- 引入柔性图像语法、任务类型路由、五类育人素养和小初高学段路由。
- 增加真实宽黑板契约、同题三案、观看距离检查与二轮反馈闭环。

## [0.6.1]

- 建立单文件自包含、载体路由、唯一文件名和学段切换重路由。

[Unreleased]: https://github.com/EasonZhangyichen/blackboard-design-skill/compare/v0.7.3...HEAD
[0.7.3]: https://github.com/EasonZhangyichen/blackboard-design-skill/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/EasonZhangyichen/blackboard-design-skill/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/EasonZhangyichen/blackboard-design-skill/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/EasonZhangyichen/blackboard-design-skill/releases/tag/v0.7.0
[0.6.1]: https://github.com/EasonZhangyichen/blackboard-design-skill/releases/tag/v0.6.1
