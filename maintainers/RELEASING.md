# 维护者发布流程

1. 更新 `VERSION`、`SKILL.md` 元数据和 `CHANGELOG.md`。
2. 生成并核验发布物：

   ```bash
   python3 tools/build_portable.py
   python3 tools/build_release.py
   python3 tools/validate_package.py
   python3 -m unittest discover -s tests
   ```

3. 确认仓库无密钥、个人绝对路径、学生数据、私人材料和图片文件。
4. 通过 Pull Request 合并后创建版本标签与 GitHub Release。
5. 上传标准 ZIP、教师完整单文件和 `dist/WEB-QUICK-PROMPT.md`。

构建工具只从 `VERSION` 和根目录 `SKILL.md` 读取版本与内容。不要手工维护教师单文件或修改 ZIP 内文件。
