# TaxueSkills

A decision-making and problem-solving skill collection for AI agents. **26 skills** covering problem dissection, task breakdown, learning methods, content creation, insight, emotional regulation, relationship communication, business judgment, industry analysis, and career planning.

Works with Claude Code, Codex, Cursor, Grok Build, and any agent platform that supports local skill loading.

<a id="top"></a>
[中文](#cn-section) | [English](#en-section)

---

<a id="cn-section"></a>
## 中文版

### 这是什么

踏雪问题解决系统。不是工具箱，是工作流和思维模型。**26 个 Skill** 覆盖问题消解、任务拆解、学习方法、内容创作、本质洞察、情绪处理、关系沟通、商业判断、行业认知、职业规划全流程。

可在 Claude Code、Codex、Cursor、Zcode、WorkBuddy 、Grok Build 等任意支持 Skill 的 Agent 上使用。

**最新版本：v3.4.1**（2026-07-12）— 主入口瘦身 + 路由准确性优化。

### v3.4.1 更新

#### 主入口重写（演绎引擎）

- **taxue 从路由器升级为决策触发器**：核心定位从"只做路由"改为"目标 + 约束 + 调度"三位一体的第一性原理框架
- **演绎引擎替代固定模板**：不再依赖固定句式输出，每次根据情境自由组织语言。像老手从多个角度看问题，不标注视角标题
- **默会知识优先**：能自己推的不靠追问。每个问题必须是为了缩小判断范围，不是为了收集信息本身
- **连招无缝衔接**：结尾自然衔接到下一段旅程，指令织在句子里。不单独成段推荐，不暴露分流感
- **导航前推不回头**：判断给完往前走，不给"选择题"，用户如果要拐弯他自己会说

#### 说话规则优化

- 删除了固定输出格式模板（"先跑 /xxx，再往下聊" 属于机械句式）
- 新增原则：对话不停留在「等选择」上、不暴露内部结构（视角A/B/C 类标题）
- 新增原则：一个人从多个角度看问题，输出自然流畅不分段

#### 行为准则（DO NOT）增强

- 不等待选择——判断给完往前走，不要问「你想先走哪条」
- 不暴露内部结构——用户看不到分段标题

### v3.4 更新

#### 路由性能优化（主入口瘦身）

- **主入口从 193 行降到 118 行（-39%）**，冷启动 token 减半，路由速度提升
- 成长日志外迁到 `taxue/CHANGELOG.md`，主入口只留指针，不占路由上下文
- 输出风格节压缩为指针 + 声线分化表，完整规则在 `references/shared-rules.md` 按需加载
- 7 个子 skill 的风格引用从「主入口语气表」改为 `shared-rules.md`，消除三处重复维护

#### 路由准确性优化（description 补触发词）

- **离线基准 Top-1 从 90.2%（37/41）提升**，泛化测试通过
- 4 个子 skill 补口语化触发词
  - `taxue-relate`：补职场关系词（老板针对我/领导挑毛病/排挤/同事关系等）
  - `taxue-solve`：补决策词（该不该辞职/走还是留等）
  - `taxue-insight`：补结论验证词（结论成立吗/站得住脚吗等）
  - `taxue-material`：补素材缺失词（找不到好句子/写东西没素材等）
- `taxue-career-offer`：补「该不该接受offer」精确匹配

#### patterns.md grep 精确化

- 主入口 grep 指令改为 `grep -E` 精确匹配「适用：」行，消除 `grep taxue` 命中所有 taxue-xxx 的污染

### v3.3 更新内容

#### 路由优化（主入口）

- **伪问题拦截**：空泛的「怎么赚钱」→ 重路由 `taxue-business`；空泛的「怎么消除焦虑」→ 重路由 `taxue-calm`，不再卡在入口空转
- **信息不足拦截增强**：抽象的「有没有什么方法」「该不该」→ 先追问具体上下文再路由，预计减少 30% 误路由
- 新增 `references/shared-rules.md`，统一语言规则、输出风格三层结构、对话信号检测，所有子 skill 继承

#### 子 Skill 内容升级（7 个）

| Skill | 版本 | 变更 |
|-------|------|------|
| **taxue-insight** | v2.9 → **v3.0** | 四视角路由：本质/结构/共情/历史。不同问题用不同视角，不再一刀切冷断言。共情视角先命名感受，结构视角拆利益链，历史视角留余地。 |
| **taxue-roundtable** | v2.8 → **v3.1** | 全面重写为多模式讨论引擎。4 种模式（并行判断/质询/辩论/多轮深挖），10 角色库 + 7 议题推荐组合，把握加权（0-10），立场追踪，轮空三问，钢人原则。 |
| **taxue-relate** | v3.1 → **v3.2** | 新增谈判关系（明牌利益交换）。场景化脚本（老板/谈判/伴侣不同语气）。风险预判：「最坏/兜底/不说的代价」。「绝对不要说」禁忌表（5 条 AI 味废话）。 |
| **taxue-solve** | v3.1 → **v3.2** | 新增「剥壳看结构」步骤——去数字去情绪看关系结构。方案模板从 4 元素扩展至 6 元素（新增理想态 + 推进）。 |
| **taxue-breakdown** | v3.1 | 移除模板输出，简化反模式 |
| **taxue-business** | v3.1 | 新增「高频假设错误」节、反模式第 4 条 |
| **taxue-speak** | v2.8 | 重构为单步直接路由，框架定义外移 |

### 技能列表

#### 核心解决层

| 斜杠命令 | 功能 | 触发示例 | 版本 |
|---------|------|---------|------|
| `/taxue` | 主入口，自动路由 | 「/t」「卡住了」「迷茫」 | v2.13 |
| `/taxue-solve` | 解法引擎，5 层消解漏斗 | 「怎么办」「卡住了」「帮我理一下」 | v3.2 |
| `/taxue-breakdown` | 任务拆解 | 「帮我拆一下」「事情太多」 | v3.1 |
| `/taxue-learn` | 学习方法，四步内化 | 「怎么学」「学了记不住」 | v2.8 |
| `/taxue-content` | 内容创作，选题到终稿 | 「写一篇」「小红书」「公众号」 | v3.1 |
| `/taxue-insight` | 本质洞察，穿透表象 | 「本质是什么」「看透」「第一性原理」 | **v3.0** |
| `/taxue-roundtable` | 多视角碰撞，暴露盲区 | 「多角度看看」「开圆桌」 | **v3.1** |
| `/taxue-build` | 系统构建，经验变工具 | 「固化流程」「写个skill」 | v2.8 |

#### 深度场景层

| 斜杠命令 | 功能 | 触发示例 | 版本 |
|---------|------|---------|------|
| `/taxue-calm` | 情绪管理 | 「好焦虑」「内耗」「心态崩了」 | v3.1 |
| `/taxue-relate` | 关系沟通 | 「怎么谈」「冲突」「谈判」 | **v3.2** |
| `/taxue-speak` | 说话练习 | 「说话紧张」「汇报不流畅」 | v2.8 |
| `/taxue-business` | 商业判断 | 「这个生意能不能做」 | v3.1 |
| `/taxue-industry` | 行业认知 | 「了解XX行业」「行业调研」 | v1.2 |

#### 职业发展层

| 斜杠命令 | 功能 | 版本 |
|---------|------|------|
| `/taxue-career` | 职场入口，自动路由 | v2.10 |
| `/taxue-career-direction` | 方向诊断 | v2.8 |
| `/taxue-career-resume` | 简历/JD 诊断 | v2.8 |
| `/taxue-career-channel` | 渠道策略 | v2.8 |
| `/taxue-career-interview` | 面试/离职 | v2.8 |
| `/taxue-career-offer` | Offer 决策与薪资谈判 | v2.8 |
| `/taxue-career-onboard` | 入职前 90 天 | v2.8 |
| `/taxue-career-fail` | 失败复盘 | v3.1 |
| `/taxue-job-search` | 岗位搜索引擎 | v2.2 |

#### 工具与基建

| 斜杠命令 | 功能 | 版本 |
|---------|------|------|
| `/taxue-save` | 状态存档（进度/恢复/决策记录）| v3.2 |
| `/taxue-material` | 素材管理 | v2.8 |
| `/taxue-skill` / `/txs` | Skill 诊断 + 优化 | v2.8 |
| `/taxue-upgrade` | 版本管理，一键升级 | v2.8 |

### 工作流联动

```
solve → breakdown → build
content → insight → content → material
calm → solve → relate
career → direction → resume → channel → interview → offer → onboard
                                                      ↓（失败时）
                                                career-fail → direction
```

### 快速开始

```bash
# 安装
npx -y skills add taxueseek/taxueskills -g --all

# 或手动安装
cd ~/.claude/skills
git clone https://github.com/taxueseek/taxueskills.git temp
cp -r temp/taxue* . && rm -rf temp
```

**用法：**
```
/taxue 两个工作不知道选哪个
/taxue-insight 为什么大多数人努力还是没有结果
/taxue-calm 最近总是焦虑得睡不着
/taxue-breakdown 帮我拆解这个月的目标
/taxue-business 这个社群项目能不能做
/taxue-relate 怎么跟合伙人谈股权分配
/taxue-speak 下周要述职汇报，我紧张
/taxue-save 保存这次讨论的结论
```

### 设计哲学

1. **先澄清，后解决**：80% 的纠结是因为问题本身有问题
2. **够用就好**：追求当前最有效的一步，不追求完美
3. **推动行动**：不说「你可以考虑」，说「第一步做 X」
4. **能固化则不复述**：重复的问题写成 Skill
5. **入口做减法**：入口只管路由，能力下沉到子 Skill

### 版本历史

| 版本 | 更新 | 日期 |
|------|------|------|
| **v3.4.1** | 主入口瘦身（193→118 行，token 减半）。4 个子 skill description 补触发词，基准 Top-1 90.2%→100%。patterns.md grep 精确化。 | 2026-07-06 |
| **v3.3** | 路由优化（伪问题+信息不足拦截）。7 个子 Skill 升级：insight v3.0（四视角路由）、roundtable v3.1（多模式讨论引擎重写）、relate v3.2、solve v3.2、breakdown/business/speak 改进。shared-rules.md 抽取。 | 2026-06-15 |
| v3.2 | 7 个子 Skill 升级至 v3.1，save v3.2（记忆时效分层），主入口 v2.13 | 2026-06 |
| v3.1 | save v3.1 记忆时效分层（永久/周期/一次性） | 2026-06 |
| v3.0 | 7 个子 Skill 输出风格重构，对话信号全局检测，消解前置，连招建议 | 2026-06 |
| v2.12 | 入口参考文件索引，渐进式信息披露 | 2026-06-08 |
| v2.11 | 输出风格三层化，9 个独立人格声线 | 2026-06-08 |
| v2.10 | 17 级优先级路由表，冲突消解规则 | 2026-06-05 |
| v2.9 | 新增行业认知引擎，路由扩展 | 2026-06 |
| v2.8 | 6 个子 Skill 升级，反模式声明，案例外移 | 2026-06 |
| v2.7 | 入口纯路由化，130→35 行，3-5→1 轮推理 | 2026-06 |

### License

MIT License

---

<a id="en-section"></a>
## English

### What This Repo Does

TaxueSkills turns fuzzy, overwhelming questions into executable actions. Instead of giving you generic advice, it routes your problem to the right cognitive tool—whether you need to think through a decision, break down a complex task, write better content, or navigate a difficult conversation.

**Latest release: v3.4.1** (2026-07-12) — Main entry slimming + routing accuracy optimization.

### v3.4.1 Update

#### Main Entry Rewrite (Deduction Engine)

- **taxue upgraded from router to decision trigger**: Core positioning changed from "routing only" to a first-principles framework of "Goal + Constraint + Scheduling"
- **Deduction engine replaces fixed templates**: No longer relies on fixed sentence patterns. Language freely organized based on context each time. Like an expert viewing from multiple angles without labeling perspectives
- **Tacit knowledge first**: Don't ask what you can deduce yourself. Every question must serve to narrow the judgment, not just collect information
- **Seamless combo chaining**: Ending naturally flows into the next leg of the journey. Command reference woven in sentences. No standalone recommendation paragraphs, no routing exposure
- **Forward navigation, no looping back**: After judgment, move forward. No multiple-choice menus. User will speak up if they want to turn

#### Speaking Rules Optimization

- Removed fixed output format templates ("run /xxx first" type mechanical phrasing)
- New principle: Conversations don't pause at "waiting for choice"; no internal structure exposure (perspective A/B/C headers)
- New principle: One person viewing from multiple angles, output flows naturally without sectioning

#### DO NOT Section Enhanced

- Don't wait for choice — after judgment, move forward, never ask "which one do you want"
- Don't expose internal structure — no visible section headers

### v3.4 Changelog

#### Routing Performance Optimization (Main Entry Slimming)

- **Main entry reduced from 193 to 118 lines (-39%)**, cold-start tokens halved, routing speed improved
- Changelog moved to `taxue/CHANGELOG.md`, main entry keeps only a pointer, no longer consuming routing context
- Output style section compressed to pointer + voice differentiation table; full rules in `references/shared-rules.md`, loaded on demand
- 7 sub-skills' style references switched from "main entry tone table" to `shared-rules.md`, eliminating three redundant maintenance points

#### Routing Accuracy Optimization (Description Trigger Words)

- **Offline benchmark Top-1 improved from 90.2% (37/41) to 100% (41/41)**, generalization test 4/4 passed
- 4 sub-skills received colloquial trigger words, fixing 4 misses:
  - `taxue-relate`: Added workplace relationship terms (boss targeting me / leader nitpicking / exclusion / colleague relations, etc.)
  - `taxue-solve`: Added decision terms (should I quit / stay or leave, etc.)
  - `taxue-insight`: Added conclusion validation terms (does this conclusion hold / is this judgment correct, etc.)
  - `taxue-material`: Added material scarcity terms (can't find good sentences / no material for writing, etc.)
- `taxue-career-offer`: Added "should I accept this offer" exact match

#### patterns.md grep Precision

- Main entry grep command changed to `grep -E` exact match on "适用：" lines, eliminating `grep taxue` pollution that matched all taxue-xxx entries

### v3.3 Changelog

#### Routing optimization (taxue main router)

- **Pseudo-question detection added**: Empty "how to make money" questions now route directly to `taxue-business`; vague "how to stop anxiety" routes to `taxue-calm` — no more getting stuck in the generic router
- **Vague input detection enhanced**: Abstract "methods", "tips", "should I" questions without context now trigger a clarification prompt before routing, reducing misrouted sessions by an estimated 30%
- New `references/shared-rules.md` extracted from the main router — shared language rules, output style, and conversation signal detection now live in a single reference file inherited by all sub-skills

#### Sub-skill upgrades (7 skills)

| Skill | Version | What Changed |
|-------|---------|-------------|
| **taxue-insight** | v2.9 → **v3.0** | 4-perspective routing: essence/structure/empathy/history. No more one-size-fits-all cold assertions—picks the right lens before judging. Empathy mode names emotions first, structure mode maps interest chains, history mode leaves room for nuance. |
| **taxue-roundtable** | v2.8 → **v3.1** | Complete rewrite as a multi-mode discussion engine. 4 modes (parallel judgment / cross-examination / debate / deep-dive), 10-character role library + 7 recommended combos, confidence-weighted conclusions (0-10), position-tracking, skip-three-questions filter, steel-man principle. |
| **taxue-relate** | v3.1 → **v3.2** | New negotiation relationship type with explicit exchange terms. Scenario-aware scripting (boss/negotiation/partner — different tone for each). Risk pre-assessment: "worst case, fallback, cost of silence." "Never say" ban list (5 AI-sounding platitudes). |
| **taxue-solve** | v3.1 → **v3.2** | New "peel the shell" step that strips numbers and emotions to reveal the underlying structural pattern — turns "this answer" into "a portable framework." Solution template expanded from 4 to 6 elements (added ideal state + next-step prompt). |
| **taxue-breakdown** | v3.1 | Removed template output section. Simplified anti-patterns from 3 to 2. |
| **taxue-business** | v3.1 | Added "frequent assumption errors" section (3 common cognitive traps). New anti-pattern: "answering invalid questions." |
| **taxue-speak** | v2.8 | Restructured from multi-step process to single-step direct routing. Framework definitions moved to references. |

### Included Skills

#### Core Problem-Solving Layer

| Command | Purpose | Natural Triggers |
|---------|---------|-----------------|
| `/taxue` | Main router — auto-routes to the right skill | "/t", "I'm stuck", "what should I do" |
| `/taxue-solve` | Problem-dissection engine, 5-level validation funnel | "What do I do?", "I'm stuck", "help me think" |
| `/taxue-breakdown` | Task breakdown to actionable steps | "Break this down", "too many things to do" |
| `/taxue-learn` | Learning methodology, 4-step internalization | "How do I learn X?", "can't remember" |
| `/taxue-content` | Content creation, from topic to final draft | "Write an article about X", "Xiaohongshu" |
| `/taxue-insight` | Essence insight, see through the surface | "What's the essence?", "see through", "first principles" |
| `/taxue-roundtable` | Multi-perspective collision, expose blind spots | "Multiple angles", "roundtable", "discuss" |
| `/taxue-build` | System builder, turn experience into repeatable tools | "Standardize this", "create a skill" |

#### Depth Scenario Layer

| Command | Purpose | Natural Triggers |
|---------|---------|-----------------|
| `/taxue-calm` | Emotional regulation, turn emotions into problems | "Anxious", "overthinking", "can't sleep" |
| `/taxue-relate` | Relationship communication, interest-structure analysis | "How to negotiate", "conflict", "boundaries" |
| `/taxue-speak` | Speaking practice, 4 frameworks | "Nervous speaking", "presentation anxiety" |
| `/taxue-business` | Business judgment, 3-question viability test | "Can this business work?", "business model" |
| `/taxue-industry` | Industry understanding engine | "Understand X industry", "industry research" |

#### Career Development Layer

| Command | Purpose |
|---------|---------|
| `/taxue-career` | Career entry — auto-routes to career sub-skills |
| `/taxue-career-direction` | Direction diagnosis |
| `/taxue-career-resume` | Resume / JD review |
| `/taxue-career-channel` | Channel strategy |
| `/taxue-career-interview` | Interview prep & resignation |
| `/taxue-career-offer` | Offer decision & salary negotiation |
| `/taxue-career-onboard` | First 90 days survival guide |
| `/taxue-career-fail` | Failure postmortem |
| `/taxue-job-search` | Job search engine |

#### Tools & Infrastructure

| Command | Purpose |
|---------|---------|
| `/taxue-save` | State save/resume/decision log |
| `/taxue-material` | Content library management |
| `/taxue-skill` or `/txs` | Skill diagnosis & optimization |
| `/taxue-upgrade` | Version management, one-click update |

### Workflow Integration

```
solve → breakdown → build
content → insight → content → material
calm → solve → relate
career → direction → resume → channel → interview → offer → onboard
                                                      ↓ (on failure)
                                                career-fail → direction
```

### Quick Start

```bash
# Installation via npx (works for Codex, Claude Code, Cursor, Grok Build)
npx -y skills add taxueseek/taxueskills -g --all

# Or manual install
cd ~/.claude/skills
git clone https://github.com/taxueseek/taxueskills.git temp
cp -r temp/taxue* . && rm -rf temp
```

**Usage:**
```
/taxue I'm stuck choosing between two jobs
/taxue-insight Why do most people work hard but still struggle?
/taxue-calm I've been anxious and can't sleep
/taxue-breakdown Help me break down this month's goals
/taxue-business Can this community project work?
/taxue-relate How do I negotiate equity with my co-founder?
```

### Requirements

- Any agent that supports local SKILL.md loading
- No external dependencies for core skills
- Web search + web fetch for `taxue-industry`

### Design Philosophy

1. **Clarify first, solve second** — 80% of confusion is a poorly-formed problem
2. **Good enough** — the most effective next step, not perfection
3. **Push action** — never "you could consider", always "step one: do X"
4. **Codify or repeat** — recurring problems become Skills
5. **Entry does less** — routing only, capability lives in sub-skills

### Version History

| Version | Highlights | Date |
|---------|-----------|------|
| **v3.4.1** | Main entry slimming (193→118 lines, tokens halved). 4 sub-skill descriptions received trigger words, benchmark Top-1 90.2%→100%. patterns.md grep precision. | 2026-07-06 |
| **v3.3** | Routing optimization (pseudo-question + vague input detection). 7 sub-skill upgrades: insight v3.0 (4-perspective routing), roundtable v3.1 (multi-mode engine), relate v3.2, solve v3.2, breakup/business/speak improvements. shared-rules.md extracted. | 2026-06-15 |
| v3.2 | 7 sub-skills to v3.1, save v3.2 (memory tiering), main router v2.13, conflict resolution refinement | 2026-06 |
| v3.1 | save v3.1 memory tiering (permanent/periodic/one-shot), patterns.md half-life fields | 2026-06 |
| v3.0 | 7 sub-skills output style rewrite, global conversation signal detection, pre-filtering layer, combo suggestion | 2026-06 |
| v2.12 | Entry reference index, progressive information disclosure | 2026-06-08 |
| v2.11 | 3-layer output style, 9 persona voices | 2026-06-08 |
| v2.10 | 17-level priority routing table, conflict resolution (P013) | 2026-06-05 |
| v2.9 | New industry skill, routing expansion, tacit knowledge injection | 2026-06 |
| v2.8 | 6 sub-skills upgraded, anti-pattern declarations, cases externalized | 2026-06 |
| v2.7 | Entry pure-routing, 130→35 lines, 3-5→1 reasoning round | 2026-06 |

### License

MIT License

---

> A good skill doesn't make AI more complex — it makes complex things simple.
> Type `/taxue` and begin.
>
> 好的 Skill 不是让 AI 变得更复杂，而是让复杂的事情变得简单。
> 输入 `/taxue`，开始。
