# TaxueSkills

> **把任何模糊的问题，变成可执行的行动。**

踏雪问题解决系统。不是工具箱，是工作流和思维模型。26 个 Skill 覆盖问题消解、任务拆解、学习方法、内容创作、本质洞察、情绪处理、关系沟通、商业判断、行业认知、职业规划全流程。

可在 Claude Code、Codex、Cursor、Grok Build 等任意支持 Skill 的 Agent 上使用。

**最新更新：v3.3**

**v3.3 更新（2026-06-15）**：7 个子 Skill 内容升级。taxue-insight 从 v2.9 升级至 v3.0，新增四视角路由（本质/结构/共情/历史），穿透分类再下判断。taxue-roundtable 从 v2.8 升级至 v5.1，全面重写为多模式讨论引擎（并行判断/质询/辩论/多轮深挖），引入 10 角色库、把握加权、深度引擎。taxue-relate 从 v3.1 升级至 v3.2，新增谈判关系、场景化脚本、风险预判、「绝对不要说」禁忌表。taxue-solve 从 v3.1 升级至 v3.2，新增「剥壳看结构」步骤，方案模板从 4 元素扩展至 6 元素（理想态+推进）。taxue-breakdown 移除模板输出，简化反模式。taxue-speak 重构为单步直接路由。主入口新增 references/shared-rules.md 共享规则文件。

**EN: v3.3 (2026-06-15)** — 7 sub-skills upgraded. taxue-insight v2.9→v3.0 with 4-perspective routing (essence/structure/empathy/history). taxue-roundtable v2.8→v5.1 complete rewrite as a multi-mode discussion engine (parallel/jury/debate/deep-dive) with 10-role library, confidence weighting, and 4 depth engines. taxue-relate v3.1→v3.2 adding negotiation mode, scenario-specific scripts, risk pre-assessment, and a "never say" ban list. taxue-solve v3.1→v3.2 adding a "peel the shell" step and expanding the solution template from 4 to 6 elements. taxue-breakdown removes template output and simplifies anti-patterns. taxue-speak restructured to single-step direct routing. New references/shared-rules.md extracted from the main router.

---

## 快速开始

输入 `/taxue`，描述你遇到的问题。系统自动识别场景，路由到对的 Skill。

**三种最常见的用法：**

```
/taxue 我不知道该怎么办              → 自动路由到 taxue-solve，帮你消解问题
/taxue 事情太多，帮我拆一下           → 自动路由到 taxue-breakdown，拆成可执行的步骤
/taxue 帮我写一篇关于XX的文章         → 自动路由到 taxue-content，选题诊断 + 创作
```

**不用记 Skill 名称。** 说人话就行。系统听你说什么，送到对的地方。

---

## 安装

#### Claude Code

```bash
claude plugin marketplace add taxueseek/taxueskills
claude plugin install taxue@taxue-skills
```

#### 通用安装方式（适用于 Codex / Claude Code / Cursor）

```bash
npx -y skills add taxueseek/taxueskills -g --all
```

#### Grok Build

```bash
npx -y skills add taxueseek/taxueskills -g --all
```

安装后 skill 文件在 `~/.claude/skills/` 目录下，每个子 Skill 一个独立目录。

---

## 更新

#### Claude Code 插件市场安装的用户

```bash
claude plugin marketplace update taxue-skills
claude plugin update taxue@taxue-skills
/reload-plugins
```

#### 通过 `npx skills add` 安装的用户

重新运行一次同样的命令即可。安装和更新用的是同一条命令：

```bash
npx -y skills add taxueseek/taxueskills -g --all
```

#### 手动更新

```bash
cd ~/.claude/skills && git clone https://github.com/taxueseek/taxueskills.git temp-taxue && cp -r temp-taxue/taxue* . && rm -rf temp-taxue
```

---

## 技能表（26 个）

### 核心解决层

| 斜杠命令 | 功能 | 自然语言触发 | 版本 |
|---------|------|-------------|------|
| `/taxue` | 主入口，自动路由 | 「/t」「卡住了」「迷茫」「纠结」 | v2.13 |
| `/taxue-solve` | 解法引擎，5层消解漏斗 | 「怎么办」「卡住了」「帮我理一下思路」 | v3.2 |
| `/taxue-breakdown` | 任务拆解，拆到最小执行单位 | 「帮我拆一下」「事情太多」「步骤」「排期」 | v3.1 |
| `/taxue-learn` | 学习方法论，四步内化法 | 「怎么学」「怎么入门」「学了记不住」 | v2.8 |
| `/taxue-content` | 内容创作，从选题到终稿 | 「写一篇」「帮我创作」「小红书」「公众号」 | v3.1 |
| `/taxue-insight` | 本质洞察，穿透表象 | 「本质是什么」「看透」「第一性原理」 | **v3.0** |
| `/taxue-roundtable` | 多视角碰撞，暴露盲区 | 「多角度看看」「开圆桌」「讨论一下」 | **v5.1** |
| `/taxue-build` | 系统构建，经验变工具 | 「固化流程」「写个skill」「标准化」 | v2.8 |

### 深度场景层

| 斜杠命令 | 功能 | 自然语言触发 | 版本 |
|---------|------|-------------|------|
| `/taxue-calm` | 情绪管理，把情绪转化为问题 | 「好焦虑」「内耗」「心态崩了」「睡不着」 | v3.1 |
| `/taxue-relate` | 关系沟通，利益结构分析 | 「怎么谈」「冲突」「谈判」「边界」 | **v3.2** |
| `/taxue-speak` | 说话练习，四种法则 | 「说话紧张」「汇报不流畅」「说不清楚」 | v2.8 |
| `/taxue-business` | 商业判断，三问定生死 | 「这个生意能不能做」「商业模式」 | v3.1 |
| `/taxue-industry` | 行业认知引擎 | 「了解XX行业」「行业调研」「行业分析」 | v1.2 |

### 职业发展层

| 斜杠命令 | 功能 | 版本 |
|---------|------|------|
| `/taxue-career` | 职场入口，自动路由到职业子 Skill | v2.10 |
| `/taxue-career-direction` | 方向诊断 | v2.8 |
| `/taxue-career-resume` | 简历/JD 诊断 | v2.8 |
| `/taxue-career-channel` | 渠道策略 | v2.8 |
| `/taxue-career-interview` | 面试/离职 | v2.8 |
| `/taxue-career-offer` | Offer 决策与薪资谈判 | v2.8 |
| `/taxue-career-onboard` | 入职前 90 天生存指南 | v2.8 |
| `/taxue-career-fail` | 失败复盘 | v3.1 |
| `/taxue-job-search` | 岗位搜索引擎 | v2.2 |

### 工具与基建

| 斜杠命令 | 功能 | 版本 |
|---------|------|------|
| `/taxue-save` | 状态存档（进度/恢复/决策记录）| v3.2 |
| `/taxue-material` | 素材管理 | v2.8 |
| `/taxue-skill` 或 `/txs` | Skill 诊断 + 优化 + 自诊断 | v2.8 |
| `/taxue-upgrade` | 版本管理，一键升级 | v2.8 |

---

## 工作流联动

Skill 之间通过入口自动推荐下一步。不需要记住该用什么——系统帮你判断。

```
solve（出方案了）→ breakdown（拆成可执行步骤）→ build（经验固化）

content 需要选题 → insight 看透本质 → content 出终稿 → material 积累素材

calm（情绪解码）→ solve（解决具体问题）→ relate（如涉及关系）

career → direction → resume → channel → interview → offer → onboard
                                             ↓（失败时）
                                       career-fail → direction
```

---

## 单独使用子 Skill

每个子 Skill 都可以**独立使用**，不需要经过 `/taxue` 入口。直接用斜杠命令或自然语言触发即可。

**推荐场景：**

- 你明确知道问题类型 → 直接用子 Skill，跳过入口路由，更快
- 你在某个 Skill 工作流中 → 子 Skill 会自动推荐下一步，不需要回入口
- 你只想用某一个功能 → 直接调用，不需要加载整个系统

**示例：**

```
/taxue-solve 我想做副业但不知道做什么
/taxue-insight 为什么大多数人努力了还是没有结果
/taxue-calm 最近总是焦虑得睡不着
/taxue-breakdown 帮我拆解这个月的目标
/taxue-content 帮我写一篇关于AI时代职业选择的文章
/taxue-business 这个社群项目能不能做
/taxue-relate 怎么跟合伙人谈股权分配
/taxue-speak 下周要做述职汇报，我紧张
/taxue-career-resume 帮我看看这份简历
/taxue-save 保存这次讨论的结论
```

---

## 设计哲学

1. **先澄清，后解决**：80% 的纠结是因为问题本身有问题
2. **够用就好**：追求当前最有效的一步，不追求完美
3. **推动行动**：不说「你可以考虑」，说「第一步做 X」
4. **能固化则不复述**：重复的问题写成 Skill
5. **入口做减法**：入口只管路由，能力下沉到子 Skill

| 哲学家 | 映射 |
|--------|------|
| 亚里士多德「第一性原理」 | 剥离表象，找到底层机制 |
| 杜威「实用主义」 | 不能推动行动的思考都是空转 |
| 德鲁克「有效性」 | 对谁有价值？ |
| 阿德勒「目的论」 | 情绪在保护你避开什么？ |
| 芒格「格栅思维」 | 单一视角必然盲视 |
| 维特根斯坦「语言审查」 | 说不清的概念等于伪概念 |

---

## 版本历史

| 版本 | 更新 | 日期 |
|------|------|------|
| **v3.3** | 7 个子 Skill 内容升级：insight v3.0（四视角路由）、roundtable v5.1（多模式讨论引擎重写）、relate v3.2（谈判+场景脚本）、solve v3.2（剥壳+六元素）、breakdown 简化和 speak 重构。主入口新增 shared-rules.md。 | 2026-06-15 |
| v3.2 | 7 个子 Skill 升级至 v3.1，taxue-save v3.2，主入口 v2.13，冲突消解规则细化，对话信号检测增强 | 2026-06 |
| v3.1 | taxue-save 记忆时效分层（永久/周期/一次性），patterns.md 半衰期字段 | 2026-06 |
| v3.0 | 7 个子 Skill 输出风格重构，对话信号全局检测，消解前置拦截，连招建议 | 2026-06 |
| v2.12 | 入口参考文件索引，渐进式信息披露 | 2026-06-08 |
| v2.11 | 输出风格三层化，9 个独立人格声线 | 2026-06-08 |
| v2.10 | 路由表重构为 17 级优先级，冲突消解规则 | 2026-06-05 |
| v2.9 | 新增 taxue-industry（行业认知引擎）、路由表扩展、默会知识注入 | 2026-06 |
| v2.8 | 6 个子 Skill 升级，新增反模式声明、案例外移、描述去边界化 | 2026-06 |
| v2.7 | 入口纯路由化，能力下沉，入口瘦身 95 行，推理轮次 3-5 → 1 | 2026-06 |
| v2.6 | 触发边界、原创案例、条件路由、自诊断、统一语言规则 | 2026-06 |
| v2.5 | 文档体系重构，完整技能表，工作流联动图 | 2026-06 |

更完整的历史变更，见 [GitHub Releases](https://github.com/taxueseek/taxueskills/releases)。

---

## 许可证

MIT License

---

> 好的 Skill 不是让 AI 变得更复杂，而是让复杂的事情变得简单。
> 输入 `/taxue`，开始。
