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

### 简历产出层（taxue-career-resume v3.1.0）
```
建母版 master.json
  → 按 JD 写 versions/日期_公司_岗位/custom.json
  → python3 scripts/render_resume.py master/master.json --custom .../custom.json --out .../resume.html
  → 浏览器打开 HTML → 打印 PDF；resume.txt 过 ATS
  → python3 scripts/jd_resume_match.py jd.txt resume.txt
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

| Skill | 功能 | 触发示例 | 版本 |
|-------|------|---------|------|
| taxue | 入口路由 | /taxue | v2.13 |
| taxue-solve | 解法引擎 | 「怎么办」 | v3.2 |
| taxue-breakdown | 任务拆解 | 「帮我拆一下」 | v3.1 |
| taxue-learn | 学习方法 | 「怎么学」 | v2.8 |
| taxue-content | 内容创作 | 「写一篇」 | v3.1 |
| taxue-insight | 本质洞察 | 「本质是什么」 | v3.0 |
| taxue-roundtable | 决策圆桌 | 「多角度看看」 | v3.1 |
| taxue-build | 系统构建 | 「固化流程」 | v2.8 |
| taxue-calm | 情绪解码 | 「好焦虑」 | v3.1 |
| taxue-relate | 关系沟通 | 「怎么谈」 | v3.2 |
| taxue-speak | 说话练习 | 「说话紧张」 | v2.8 |
| taxue-business | 商业判断 | 「这个生意能不能做」 | v3.1 |
| taxue-career | 职业入口 | 「找工作」 | v3.1.0 |
| taxue-save | 状态存档 | 「保存进度」 | v3.2 |
| taxue-material | 素材管理 | 「素材库」 | v2.8 |
| taxue-skill | Skill 工程 | 「优化skill」 | v2.8 |
| taxue-upgrade | 版本管理 | 「升级」 | v2.8 |
| taxue-industry | 行业认知 | 「了解XX行业」 | v1.2 |
| taxue-job-search | 岗位搜索 | 「搜招聘」 | v2.2 |
| taxue-career-direction | 方向诊断 | 「不知道做什么」 | v3.1.0 |
| taxue-career-resume | 简历/JD + 产出层 | 「帮我看看简历」「简历母版」 | v3.1.0 |
| taxue-career-channel | 渠道策略 | 「在哪投」 | v3.1.0 |
| taxue-career-interview | 面试准备 | 「面试」 | v3.1.0 |
| taxue-career-offer | Offer决策 | 「选Offer」 | v3.1.0 |
| taxue-career-onboard | 入职指南 | 「刚入职」 | v3.1.0 |
| taxue-career-fail | 失败复盘 | 「总是被拒」 | v3.1.0 |
