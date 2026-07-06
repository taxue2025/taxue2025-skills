---
name: taxue-material
version: "2.8"
description: |
  从个人创作资产库里检索并注入高质量素材、金句、案例。Retrieve and inject high-quality material from the personal content library.

  When to use / 适用场景: 整理素材、调用素材库、金句、案例库、找点灵感、有什么素材、好的素材、引用、积累素材。、找不到好句子、写东西没素材、写的时候没灵感、没有好句子、缺素材
  EN: "need inspiration", "looking for quotes", "content library", "find examples", "writing material", "reference material".
  Not for / 不适用: 写文章本身 → taxue-content、学写作方法 → taxue-learn、素材库管理/入库 → taxue-material-library。
---

# taxue-material：素材库

> 最好的素材不是找出来的，是攒出来的。

你的任务：从素材库中检索、注入高质量素材到用户的创作中。

---

## 素材类型

| 类型 | 内容 | 适用场景 |
|------|------|---------|
| 金句 | 精炼的、有冲击力的短句 | 标题、开头、结尾、社交媒体 |
| 洞见 | 深度分析的结论 | 文章核心观点、视频脚本 |
| 案例 | 真实经历的案例 | 论证、讲故事 |
| 方法论 | 可复用的思维框架 | 教程、分析文章 |

---

## 工作流程

1. **识别需求**：用户需要什么类型的素材？
2. **检索素材**：从素材库对应区域检索
3. **注入创作**：把素材融入用户的内容
4. **标注来源**：标注素材来源

---

## 下一步建议（条件触发）

素材给出后，根据结果判断是否推荐下一步。**不是每次都推荐**，只在结果明确指向另一个 skill 时才说一句。

| 结果条件 | 推荐话术 |
|----------|---------|
| 拿到素材了，接下来要写进内容里 | 「素材有了，开始写。用 `/taxue-content`。」 |
| 找不到好素材，根源是话题没看透 | 「素材少是因为没挖透。用 `/taxue-insight` 先看本质。」 |

---

## DO NOT

- 需要创作内容 → `taxue-content`（material 只管素材，content 管创作）
- 需要管理素材库本身 → `taxue-material-library`（本 skill 是活化器，不是管理器）
---

*taxue-material v2.8*
