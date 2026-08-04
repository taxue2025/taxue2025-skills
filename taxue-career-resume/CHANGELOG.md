# Changelog

## v3.1.0（2026-08-04）

补齐产出层：母版 → 多版本投递 → 独立 HTML 打印 PDF。

- 新增 `assets/master-template.json`：简历母版字段骨架
- 新增 `assets/resume-template.html`：打印友好独立 HTML（零外部依赖、A4、`@media print`）
- 新增 `scripts/render_resume.py`：母版 + 可选 custom.json → resume.html + resume.txt（ATS 纯文本）+ 页数估算
- 新增 `references/master-versioning.md`：工作区目录约定、派生流程、版本不可变、维护操作
- 模式 A/B/D 落点统一到母版/版本（不再只产出散装文本）
- 定向投递优化接入 custom.json 裁剪/排序/覆盖 + jd_resume_match 质检

## v3.0（2026-08-03）

- 求职技能库整合：并入 job-navigator / interview-coach / resume-builder / resume-auditor / job-hunter-pro 精华
- 方法论与 references 见子技能目录（单一真源）
