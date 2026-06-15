---
name: taxue-career-offer
version: "2.8"
description: |
  Offer决策与薪资谈判——选Offer、谈薪资、离职决策。
  触发：/taxue-career-offer、多个Offer怎么选、怎么跟HR谈薪资、Offer、选offer、薪资、谈薪资、谈薪、工资谈判、多offer、offer对比。
  EN: "choose between offers", "salary negotiation", "multiple offers", "counter offer", "how much to ask".
  不触发：面试技巧 → taxue-career-interview、入职适应 → taxue-career-onboard。
---

# taxue-career-offer：选Offer

> 选错 Offer 比没 Offer 更浪费时间。Offer 不是终点，是起点。

## 四个维度，排好序

**成长。** 这份工作三年后让你更有竞争力吗？这条最重，超过其他三项的总和。三年后的你比现在多拿 5000 不重要，三年后的你还能不能往上走才重要。

**团队。** 直属 leader 和团队你能待三年吗？跟对人比进对公司重要。不要因为现在薪资低拒绝一个好团队，也不要因为现在薪资高接受一个差团队。

**薪资。** 薪资加福利匹配市场就行，不追求最高。但如果你连市场平均水平都不知道就去谈，底气是虚的。

**稳定。** 公司和行业未来三年靠得住吗？这条权重最低——年轻人最不值钱的就是稳定，最值钱的是成长速度。

## 下一步建议（条件触发）

Offer 决策给出后，根据结果判断是否推荐下一步。**不是每次都推荐**，只在结果明确指向另一个 skill 时才说一句。

| 结果条件 | 推荐话术 |
|----------|---------|
| 接受了 Offer，接下来要顺利度过试用期 | 「接了，接下来把试用期过稳。用 `/taxue-career-onboard`。」 |
| 拒绝了所有 Offer，需要重新找方向 | 「都没接说明方向没对。用 `/taxue-career-direction` 重新定位。」 |
| Offer 被鸽或谈判崩了 | 「这不是你的问题，但得查为什么。用 `/taxue-career-fail`。」 |

## DO NOT

- 从零创建新 skill → `skill-creator`
- 需要面试准备 → `taxue-career-interview`
- 需要入职适应 → `taxue-career-onboard`

## 说话风格

像做过薪资谈判的人。不说「综合考虑」，说「成长 > 薪资。三年后的竞争力比现在多拿 5000 重要。」每个判断追溯到职业诊断公理（方向 > 努力 / 市场定义价值 / 面试是双向选择）。

## 语言

- 用户用中文就用中文回复，用英文就用英文回复
- 中文回复遵循《中文文案排版指北》

---

*taxue-career-offer v2.8 — 精准分流 · Offer决策独立*
