---
name: skill-designer
description: Skill 设计师。快速评估一个 skill 值不值得做，然后帮你做出来。当用户说「设计一个 skill」、「这个功能值得做成 skill 吗」、「改进这个 skill」、「skill design」、「design a skill」、「improve this skill」时触发。专注于 skill 的价值评估和迭代优化。从零开始设计完整的 JD 或组织架构用 skill-org，复杂问题分析用 expert-roundtable。
---

# Skill 设计师

设计有用的 skill，不设计没人用的 skill。

---

## 先问三个问题（Drucker 过滤）

动手之前，回答：

没有这个 skill，结果会变差吗？不会就不做。

这个 skill 会被用5次以上吗？一次性任务不需要 skill。

Claude 直接回答不了这个问题吗？能直接回答就不需要 skill。

三个问题都过了，再往下走。

---

## Skill 的三层结构

```
Level 1（YAML frontmatter）：触发机制，始终加载
Level 2（SKILL.md body）：执行指令，触发时加载，控制在 500 行以内
Level 3（references/）：深度参考，按需读取
```

最重要的是 Level 1。Description 写不好，skill 永远不会触发。

---

## Description 怎么写

Description 决定 skill 什么时候加载。写法：

```yaml
description: |
  [一句话说清楚这个 skill 做什么]
  
  Use when:
  - 「[触发词1]」
  - 「[触发词2]」
  （至少10个，覆盖精确表达和模糊表达）
  
  Use for:
  - [具体场景1]
  - [具体场景2]
  
  Use other skills for:
  - [相邻场景] → [用哪个 skill]
```

写完之后测试：列出10个查询（5个应该触发，5个不应该），确认准确率超过90%。

---

## Skill Body 怎么写

Examples 比规则有效10倍。先写例子，再写规则。

```markdown
## 示例

输入：[真实的用户请求，要具体，带背景]
输出：[理想的响应]
```

好例子的三个标准：具体（有真实场景）、现实（用户真的会这样说）、边缘（覆盖容易混淆的情况）。

---

## 迭代循环

```
草稿 → 测试3个案例 → 用户看输出 → 改进 → 重复
```

每轮迭代目标：让 skill 在测试案例上的通过率提升20%。

三个测试案例：理想输入（happy path）、边界输入（edge case）、近似输入（near-miss，容易触发但不应该触发的）。

---

## 常见问题

| 问题 | 症状 | 修法 |
|------|------|------|
| 触发太宽 | 不相关的请求也触发 | 缩窄 description，加「Use other skills for」 |
| 触发太窄 | 明显应该触发但没触发 | 补充触发词，覆盖模糊表达 |
| 输出格式不对 | 结构乱 | 加具体的输出模板或示例 |
| 什么都想做 | Skill 越来越大 | 拆分，每个 skill 只做一件事 |

---

## 与 skill-org 的分工

skill-org 负责从目的出发，设计完整的组织架构和 JD，然后把 JD 编译成 skill 文件。

skill-designer 负责快速评估和迭代已有 skill，专注于触发精度和输出质量。

有现成的 skill 需要改进用这里。从零设计一套 Agent 分工体系用 skill-org。
