# 维护者发布流程

1. 更新 `VERSION`、`SKILL.md` 元数据和 `CHANGELOG.md`。
2. 生成并核验发布物：

   ```bash
   python3 tools/build_portable.py --check
   python3 tools/validate_package.py
   python3 -m unittest discover -s tests
   python3 tools/build_release.py
   python3 tools/build_checksums.py
   ```

3. 确认仓库无密钥、个人绝对路径、学生数据、私人材料和未批准图片。
4. 通过 Pull Request 合并到 `main`。当 `VERSION` 发生变化时，`.github/workflows/release.yml` 会自动：
   - 创建对应的 `v<version>` 标签与 GitHub Release；
   - 上传标准 ZIP、教师完整单文件、`WEB-QUICK-PROMPT.md` 与 `SHA256SUMS.txt`；
   - 从 `CHANGELOG.md` 提取当前版本说明。
5. 发布完成后人工核验 Release 标题、标签、四个附件、校验值和下载链接。需要重跑时使用 Release 工作流的 `workflow_dispatch`；工作流会覆盖同名附件并更新版本说明，不创建重复 Release。

构建工具只从 `VERSION` 和根目录 `SKILL.md` 读取版本与内容。不要手工维护教师单文件、校验文件或修改 ZIP 内文件。
