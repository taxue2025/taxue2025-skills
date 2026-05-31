# 踏雪问题解决系统（Taxue Problem Solving System）

> 把任何模糊的问题，变成可执行的行动。

不是工具箱，是工作流。26 个 Skill 覆盖问题解决、学习、创作、情绪、关系、职业、商业全领域。

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                      /taxue（入口）                           │
│         「听你说什么，送到对的地方。只做路由，不做分析。」       │
└───────────────────────┬─────────────────────────────────────┘
                        ↓
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    ↓      ↓      ↓      ↓      ↓      ↓      ↓
 ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
 │solve│ │break│ │learn│ │cont │ │ins  │ │round│ │build│
 │解决掉│ │拆任务│ │学习 │ │内容 │ │洞察 │ │圆桌 │ │系统 │
 └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
    │       │       │       │       │       │       │
    └───────┴───────┴───────┴───────┴───────┴───────┘
                        ↓
              ┌──────────────────┐
              │  深度场景层       │
              │ calm / relate /  │
              │ speak / business │
              │ save / career    │
              └──────────────────┘
```

---

## 技能详情

| 技能 | 别名 | 职责 | 触发场景 |
|------|------|------|----------|
| **taxue** | `/taxue` | 入口路由 | 自动推断意图，路由到正确 Skill |
| **taxue-solve** | `/solve` | 解法引擎 | 问题清晰，需要具体解法 |
| **taxue-breakdown** | `/breakdown` | 任务拆解 | 事情太多、无从下手 |
| **taxue-learn** | `/learn` | 学习方法 | 想学新东西、学了记不住 |
| **taxue-content** | `/content` | 内容创作 | 写文章、做脚本、出内容 |
| **taxue-insight** | `/insight` | 本质洞察 | 想看透本质、底层逻辑 |
| **taxue-roundtable** | `/roundtable` | 决策圆桌 | 复杂决策拿不定主意 |
| **taxue-calm** | `/calm` | 情绪解码 | 焦虑、内耗、崩溃 |
| **taxue-relate** | `/relate` | 关系沟通 | 冲突、谈判、边界 |
| **taxue-speak** | `/speak` | 说话练习 | 表达不好、紧张 |
| **taxue-business** | `/business` | 商业诊断 | 商业模式判断 |
| **taxue-save** | `/save` | 状态存档 | 保存进度、继续上次 |
| **taxue-career** | `/career` | 职场入口 | 任何职业问题 |
| **taxue-build** | `/build` | 系统构建 | 问题重复出现 |
| **taxue-upgrade** | `/upgrade` | 版本管理 | 升级 Skill 到最新版 |

---

## 工作流联动

### 解决主线
```
solve（出方案了）→ breakdown（拆步骤）→ build（固化为 Skill）
```

### 情绪 → 行动线
```
calm（解码情绪，找到问题）→ solve（解决具体问题）
calm（关系问题）→ relate（沟通策略）
```

### 职业线
```
career → direction → resume → channel → interview → offer → onboard
```

### 持续积累线
```
solve 有结论 → save 存档 → 下次 restore 恢复 → 继续
```

### 学习线
```
learn 选课题 → 四步内化 → 实践遇阻 → solve
```

---

## 核心原则

1. **先澄清，后解决** —— 问题不清，答案无用
2. **够用就好，不要完美** —— 有限理性，追求当前够用的方案
3. **推动行动，不给建议** —— 不说「你可以考虑」，说「第一步做 X」
4. **能固化，不复述** —— 重复的问题写成 Skill，一次建设长期受益

---

## 安装

```bash
npx skills add taxueseek/taxueskills
```

或直接在 Claude Code 中配置后使用：

```bash
git clone https://github.com/taxueseek/taxueskills ~/.claude/skills/taxue
```

---

## 文件结构

```
taxue/
├── SKILL.md           # 入口路由 + 自动意图识别
├── README.md          # 本文件（体系总览）

子 skill（平级目录）：
taxue-solve/          # 问题解决
taxue-breakdown/      # 任务拆解
taxue-learn/          # 学习方法
taxue-content/        # 内容创作
taxue-insight/        # 本质洞察
taxue-roundtable/     # 决策圆桌
taxue-calm/           # 情绪解码
taxue-relate/         # 关系沟通
taxue-speak/          # 说话练习
taxue-business/       # 商业诊断
taxue-save/           # 状态存档
taxue-career/         # 职场入口（含 7 个子 Skill）
taxue-build/          # 系统构建
taxue-upgrade/        # 版本管理
```

---

## 质量自检

每个 Skill 在输出前必须检查：

- [ ] 是否只解决一个主要矛盾？
- [ ] 输出是否直接可用？
- [ ] 用户今天能不能开始做？
- [ ] 是否留了余地让用户参与？

---

## 版本

- 系统版本：**v2.5**
- 最后更新：2026-06
- 核心原则：德鲁克有效性 + 西蒙有限理性 + 杜威实用主义
