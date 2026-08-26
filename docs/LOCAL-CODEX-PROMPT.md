# 交给本地 Codex 的完整任务提示词

请在当前目录对“黑板报整图生成 Skill v0.7.1”执行一次发布前检查，并推送到我的 GitHub 私有仓库。

## 目标

- GitHub 账号：`EasonZhangyichen`
- 仓库名：`blackboard-design-skill`
- 初始可见性：`private`
- 默认分支：`main`
- 不得改为 public
- 不得上传 API Key、Token、个人隐私文件或未列入仓库的图片资产

## 执行步骤

1. 阅读根目录 `SKILL.md`、`README.md`、`CHANGELOG.md`、`LICENSE` 和 `docs/` 下发布说明。
2. 确认核心版本均为 `v0.7.1`，不存在 `v0.7.0` 发行文件残留。
3. 运行：

   ```bash
   python3 scripts/validate_package.py
   python3 scripts/build_release.py
   ```

4. 检查：
   - 根目录必须包含 `SKILL.md` 和 `LICENSE`；
   - 主包不得包含普通参考图片；
   - 不得出现 `/workspace/`、`/mnt/data/` 等不可移植路径；
   - 不得包含 `.env`、API Key、Token 或本地缓存；
   - `dist/blackboard-design-skill-v0.7.1.zip` 成功生成。
5. 检查 `gh auth status`。如果没有登录，只提示我完成 `gh auth login`，不要把任何凭证写入文件。
6. 如果当前目录还不是 Git 仓库：
   - `git init -b main`
   - 检查本地 Git 用户名和邮箱；缺失时先告诉我，不要编造邮箱。
7. `git add .`，提交信息：

   ```text
   feat: release blackboard design skill v0.7.1
   ```

8. 检查 GitHub 上是否已经存在 `EasonZhangyichen/blackboard-design-skill`：
   - 不存在：使用 `gh repo create ... --private --source . --remote origin --push` 创建；
   - 已存在：确认它属于我且为 private，再设置 remote 并推送；
   - 不得覆盖其他同名仓库或强推。
9. 推送 `main` 分支。
10. 最后返回：
    - 仓库 URL；
    - 仓库可见性；
    - 当前 commit SHA；
    - 验证脚本结果；
    - Release ZIP 路径；
    - MIT License 是否存在且内容完整。

## 禁止事项

- 不要把仓库设为 public；
- 不要创建 GitHub Release；
- 不要修改或移除 MIT License；
- 不要上传参考案例图片；
- 不要修改 Skill 的产品逻辑，除非验证脚本发现确定性错误；
