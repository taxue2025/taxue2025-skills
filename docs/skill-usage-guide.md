# Taxue Skills 使用引导

## 快速开始

输入 `/taxue`，描述你遇到的问题。系统自动识别场景，路由到对的 Skill。

**三种最常见的用法：**

```
/taxue 我不知道该怎么办              → 自动路由到 taxue-solve
/taxue 事情太多，帮我拆一下           → 自动路由到 taxue-breakdown
/taxue 帮我写一篇关于XX的文章         → 自动路由到 taxue-content
```

**不用记 Skill 名称。** 说人话就行。

## 典型工作流

### 解决问题
```
卡住了 → /taxue → taxue-solve（消解漏斗验证问题）→ taxue-breakdown（拆成步骤）
```

### 内容创作
```
有选题 → /taxue → taxue-content（选题门禁 + 见感思行 + 质量诊断）→ taxue-material（存素材）
```

### 情绪处理
```
好焦虑 → /taxue → taxue-calm（情绪解码）→ 找到具体问题 → taxue-solve（解决）
```

### 职业路径
```
找工作 → /taxue → taxue-career → direction → resume → channel → interview → offer → onboard
```

## 状态管理

复杂问题不会在一次会话中完成。使用存档功能：

```
「保存进度」→ 存档当前状态
「继续上次」→ 恢复上次状态
「记录这个决策」→ 记录关键决策供复盘
```

存档默认放在 `~/.taxue/sessions/`，每个项目隔离。

## Skill 列表

| Skill | 功能 | 触发示例 |
|-------|------|---------|
| taxue | 入口路由 | /taxue |
| taxue-solve | 解法引擎 | 「怎么办」 |
| taxue-breakdown | 任务拆解 | 「帮我拆一下」 |
| taxue-learn | 学习方法 | 「怎么学」 |
| taxue-content | 内容创作 | 「写一篇」 |
| taxue-insight | 本质洞察 | 「本质是什么」 |
| taxue-roundtable | 决策圆桌 | 「多角度看看」 |
| taxue-build | 系统构建 | 「固化流程」 |
| taxue-calm | 情绪解码 | 「好焦虑」 |
| taxue-relate | 关系沟通 | 「怎么谈」 |
| taxue-speak | 说话练习 | 「说话紧张」 |
| taxue-business | 商业判断 | 「这个生意能不能做」 |
| taxue-career | 职业入口 | 「找工作」 |
| taxue-save | 状态存档 | 「保存进度」 |
| taxue-material | 素材管理 | 「素材库」 |
| taxue-skill | Skill 工程 | 「优化skill」 |
| taxue-upgrade | 版本管理 | 「升级」 |
| taxue-industry | 行业认知 | 「了解XX行业」 |
| taxue-job-search | 岗位搜索 | 「搜招聘」 |
