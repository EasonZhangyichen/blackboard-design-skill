# 使用本地 Codex 推送到私有 GitHub 仓库

目标仓库建议：

```text
EasonZhangyichen/blackboard-design-skill
```

初始可见性：`private`

## 一、准备

### 1. 解压完整仓库包

把 `blackboard-design-skill-v0.7.1.zip` 解压到本地工作目录，例如：

```bash
cd ~/Projects
unzip ~/Downloads/blackboard-design-skill-v0.7.1.zip
cd blackboard-design-v0.7.1
```

### 2. 确认 Git 与 GitHub CLI

```bash
git --version
gh --version
```

macOS 没有 `gh` 时：

```bash
brew install gh
```

### 3. 登录 GitHub

```bash
gh auth login
gh auth status
```

建议选择：

- GitHub.com
- HTTPS
- 使用浏览器登录

## 二、让本地 Codex 执行

把 `docs/LOCAL-CODEX-PROMPT.md` 的完整内容发给本地 Codex，并让它在仓库根目录执行。

Codex 应完成：

1. 检查文件和版本；
2. 运行验证脚本；
3. 运行 Release 打包脚本；
4. 检查 Git 状态和敏感信息；
5. 初始化 `main` 分支；
6. 创建首次提交；
7. 创建 private GitHub 仓库；
8. 推送到 `origin/main`；
9. 返回仓库地址、commit SHA 和验证结果。

## 三、手动命令备用方案

```bash
python3 scripts/validate_package.py
python3 scripts/build_release.py

git init -b main

git config user.name "EasonZhangyichen"
# 把下一行替换为你的真实 GitHub 邮箱或 noreply 邮箱
git config user.email "YOUR_GITHUB_EMAIL"

git add .
git commit -m "feat: release blackboard design skill v0.7.1"

gh repo create EasonZhangyichen/blackboard-design-skill \
  --private \
  --description "Portable Agent Skill for generating age-appropriate Chinese school blackboard designs" \
  --source . \
  --remote origin \
  --push
```

如果仓库已经存在：

```bash
git remote add origin https://github.com/EasonZhangyichen/blackboard-design-skill.git
git push -u origin main
```

## 四、推送后检查

```bash
gh repo view EasonZhangyichen/blackboard-design-skill --web

git status
git log --oneline -1
git remote -v
```

检查 GitHub 页面：

- 仓库显示为 Private；
- 根目录直接可见 `SKILL.md`；
- README 正常渲染；
- ZIP、图片、密钥或本地路径没有被误提交；
- `python3 scripts/validate_package.py` 通过。

## 五、公开前必须完成

1. 确定 `LICENSE`；
2. 删除或处理 `LICENSE-DECISION.md`；
3. 确认无 API Key、邮箱、真实学校隐私材料；
4. 完成至少四个平台回归测试；
5. 创建标签与 Release。

创建 Release：

```bash
git tag v0.7.1
git push origin v0.7.1

gh release create v0.7.1 \
  dist/blackboard-design-skill-v0.7.1.zip \
  SKILL.md \
  dist/WEB-QUICK-PROMPT.md \
  --title "Blackboard Design Skill v0.7.1" \
  --notes "跨学段主题兼容与发行校准版。详见 CHANGELOG.md。"
```

## 六、确认后改为 Public

只有在你本人确认后执行：

```bash
gh repo edit EasonZhangyichen/blackboard-design-skill \
  --visibility public \
  --accept-visibility-change-consequences
```

执行后重新打开仓库确认可见性。
