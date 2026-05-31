# Changelog

## v2.5 → v2.5

### 文档体系重构（2026-06）

此版本更新了完整的文档体系，后续更新在 CHANGELOG 中记版本差异。

---

## v2.3（2026-04）— 文档体系重构

## v2.5（2026-06）— 文档体系重构

### 概述

本次更新是 Taxue Skills 的文档体系大重构。参考 dbskill 的文档风格，建立了完整的技能索引、工作流联动图、设计哲学体系，并补全了长期缺失的文档内容。原有 SKILL.md 逻辑不变，新增和完善的是**文档层**。

### 新增文件

| 文件 | 说明 |
|------|------|
| `README.md` | 仓库级完整文档，含技能表、联动图、架构图、哲学锚点、版本历史 |
| `CHANGELOG.md` | 本文件 — 完整的版本变更记录 |
| `.agents/skills/taxue/README.md` | 本地安装版 README，同步更新为新风格 |

### 文档变化

- **README.md**（根级）：从零创建，参考 dbskill 的文档结构：
  - 完整技能表（26 个 Skill，分 5 层）
  - 工作流联动图：核心解决线 / 内容线 / 情绪线 / 职业线 / 积累线 / 学习线
  - 状态管理体系（progress / restore / decision 三模式）
  - 设计哲学（6 位哲学家的映射）
  - 架构图（多层路由）
  - 常见使用路径表
  - 版本历史

- **`.agents/skills/taxue/README.md`**：全面重写
  - 移除过时的 `/think` / `/search` 引用（已不存在）
  - 补充完整技能表（15 个核心技能）
  - 增加工作流联动关系
  - 更新架构图匹配当前体系

- **`.agents/skills/taxue/SKILL.md`**：路由表补全
  - 新增 6 个缺失技能的路由规则
  - 新增 10 条流程衔接
  - 更新「超出能力时」提示
  - 版本号 v2.2 → v2.3

### 技能清单核对

| 技能 | 路由表 | README | 说明 |
|------|--------|--------|------|
| taxue (入口) | ✅ | ✅ | — |
| taxue-solve | ✅ | ✅ | — |
| taxue-breakdown | ✅ | ✅ | — |
| taxue-learn | ✅ | ✅ | — |
| taxue-content | ✅ | ✅ | — |
| taxue-insight | ✅ | ✅ | — |
| taxue-roundtable | ✅ | ✅ | — |
| taxue-calm | ✅ | ✅ | — |
| taxue-relate | ✅ | ✅ | — |
| taxue-speak | ✅ | ✅ | — |
| taxue-business | ✅ | ✅ | — |
| taxue-save | ✅ | ✅ | — |
| taxue-career | ✅ | ✅ | — |
| taxue-build | ✅ | ✅ | — |
| taxue-upgrade | ✅ | ✅ | — |
| taxue-material | ✅ | ✅ | 新增路由 |
| taxue-skill | ✅ | ✅ | 新增路由 |
| taxue-weread | ✅ | ✅ | 新增路由 |
| taxue-jimin-citrus-method | ✅ | ✅ | 新增路由 |
| taxue-peizhe-allocator-method | ✅ | ✅ | 新增路由 |
| taxue-style-replicator | ✅ | ✅ | 新增路由 |
| taxue-career-fail | ✅ | ✅ | 新增路由 |

### 备份

全量备份已保存至 `.taxue-backups/current/`（26 个技能目录）。
现有备份 `.taxue-backups/pre-optimization-20260517/` 保持不变。

---

## v2.2（2026-04）

- 新增格莱斯信号检测
- 精确信号词表
- 完整流程衔接
- 状态管理三合一（save / restore / archive 合并）

## v2.1（2025-12）

- 双模式设计：极速版 + 专业版
- 自动意图识别
- 智能路由

## v2.0（2025-09）

- 从 skill 集合升级为问题解决系统
- 统一入口 `/taxue`
- 哲学锚点体系引入
