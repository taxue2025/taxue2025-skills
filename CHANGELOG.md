# CHANGELOG

## v2.6（2026-06）

### 触发边界
- 全部 24 个 Skill 增加 DO NOT use when 边界声明
- 相邻 Skill 触发词互斥检查，防止误触发

### 原创案例
- taxue-solve、taxue-content、taxue-calm 嵌入原创案例库
- 每个案例标注要点，看完即懂

### 条件路由
- 所有 Skill 的下游协作增加具体触发条件
- 从「你可能需要 XX」升级为「如果你现在卡在 XX，下一步是 YY」

### 自诊断
- taxue-skill 支持以自身为诊断目标
- 完整六维诊断 + 自动修复

### 统一语言规则
- 全部 Skill 增加语言规则：中文遵循《中文文案排版指北》

### 结构优化
- 移除 taxue-style-replicator（第三方账号依赖）
- 清理 `/ming`、`/zaoren` 等外部引用
- 技能总数：24

---

## v2.5（2026-06）

- 文档体系重构
- 完整技能表（26 个 Skill，分 5 层）
- 工作流联动图
- 状态管理体系（progress / restore / decision）
- 设计哲学 + 哲学锚点
