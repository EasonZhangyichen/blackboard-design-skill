# 贡献指南

感谢你改进 Blackboard Design Skill。

## 提交问题

请先搜索现有 Issue，再使用对应模板。问题描述应包含学段、主题、载体、实际结果和预期结果。平台兼容性反馈还应说明 Skill 导入方式、图片工具是否可用和实际调用的图像模型。请勿上传学生个人信息、未脱敏的学校材料、密钥或版权不清的参考图片与完整作品。

## 提交修改

1. 从 `main` 创建独立分支。
2. 保持修改范围清楚，不混入无关重构。
3. 修改运行逻辑时同步更新 `SKILL.md` 或对应 `references/`，并在 `evals/test-cases.yaml` 补充场景，在 `evals/rubric.md` 记录评测标准；评测结果应说明用例、得分、失败项和使用的平台能力。
4. 运行：

   ```bash
   python3 tools/validate_package.py
   python3 -m unittest discover -s tests
   python3 tools/build_portable.py --check
   ```

5. 提交 Pull Request，说明动机、变更和验证结果。

`dist/blackboard-design-skill-portable-*.md` 与发布 ZIP 是生成物，不应手工修改。维护者负责版本、发布包、标签和 Release。
