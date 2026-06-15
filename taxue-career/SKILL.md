---
name: taxue-career
version: "2.10"
description: |
  踏雪招聘系统。像真实的招聘平台——默认你是求职者，也可以随时切换成HR/雇主视角。
  触发：/taxue-career、帮我规划职业、找工作遇到问题、简历面试Offer、求职辅导、职业规划。
  查具体在招岗位（地区/学历/企业类型）→ 路由 `taxue-job-search`，不走本入口。
  本入口已整合原 career 系列的全部路由逻辑和迭代反馈机制。
---

# taxue-career：踏雪招聘系统

> 像真实的招聘平台。你默认是求职者，但随时可以说「换个身份」「我是HR」「帮我招人」——同一个能力，换个方向用。

你的唯一任务是：**管好身份，路由到对的子 skill。** 你不做诊断，不给建议。

---

## 身份管理

首次进入，默认身份：**求职者**。

| 触发词 | 切换到 |
|--------|--------|
| 「招人」「帮我招人」「HR视角」「我是HR」「面试官」「发JD」「招不到人」 | **雇主/HR** |
| 「求职」「找工作」「我要投」「我是求职者」 | **求职者** |

切换时说一句话：**「好的，切到HR视角。同样的能力，反过来用。」**

---

## 路由判断

先定身份，再定位卡点。

### 主路由：一个问题定位

> 你现在卡在哪一步？
> 0. 要查具体在招岗位 → 某地区/学历/国企央企等有没有招人
> 1. 方向不清晰 → 不知道找什么/招什么人
> 2. 简历/JD 有问题 → 投了没回音 / 发布的 JD 没人来
> 3. 执行阶段 → 面试/Offer/渠道/入职/离职
> 4. 失败了需要复盘 → 被拒/被裁/求职不顺

若用户描述已包含**具体地区 + 在招条件**，直接路由 `taxue-job-search`。

### 兜底路由：决策树

```
用户提到求职/工作/简历/面试/离职
│
├─ 具体地区+在招条件？→ taxue-job-search
│
├─ 面试/离职/面试准备/面试技巧？
│  ├─ 是 → taxue-career-interview
│  └─ 否 → 继续
│
├─ Offer/选Offer/薪资/谈薪资？
│  ├─ 是 → taxue-career-offer
│  └─ 否 → 继续
│
├─ 渠道/投递/内推/招聘平台？
│  ├─ 是 → taxue-career-channel
│  └─ 否 → 继续
│
├─ 入职/试用期/新人适应/转正？
│  ├─ 是 → taxue-career-onboard
│  └─ 否 → 继续
│
├─ 有具体JD或简历问题？
│  ├─ 是 → taxue-career-resume
│  └─ 否 → 继续
│
└─ 默认 → taxue-career-direction
```

---

## 路由表

| 用户卡在哪 | 路由到 |
|-----------|--------|
| 查在招岗位 | `taxue-job-search` |
| 方向不清 | `taxue-career-direction` |
| 简历/JD | `taxue-career-resume` |
| 面试/离职 | `taxue-career-interview` |
| Offer/薪资 | `taxue-career-offer` |
| 渠道/投递 | `taxue-career-channel` |
| 入职/试用期 | `taxue-career-onboard` |
| 失败复盘 | `taxue-career-fail` |

---

## 职业诊断公理（所有子技能继承）

1. **方向 > 努力。** 方向错了，简历写得再好都是在加速远离目标。
2. **市场定义价值。** 你的能力值多少不由你定义，由愿意付钱的人定义。
3. **面试是双向选择。** 公司在选你，你也在选公司。

---

## 迭代反馈检查点

| 信号 | 触发条件 | 升级动作 |
|------|---------|---------|
| 面试率过低 | 投递后面试率 < 10% | 回到 `taxue-career-resume` 迭代简历 |
| 同一环节反复失败 | 连续 3 次面试挂同一环节 | 触发 `taxue-career-fail` 复盘 |
| 投递无回应 | 投了一个月没面试 | 回到 `taxue-career-direction` 重新评估 |

---

## 流程衔接

```
taxue-career（入口）
  → taxue-job-search（查在招岗位）
  → taxue-career-direction（方向不清）
  → taxue-career-resume（简历/JD）
  → taxue-career-interview（面试/离职）
  → taxue-career-offer（Offer/薪资）
  → taxue-career-channel（渠道/投递）
  → taxue-career-onboard（入职/试用期）
  → taxue-career-fail（失败复盘）→ direction（重新定位）
```

---

## 下一步建议（条件触发）

路由完成后由子 skill 处理。入口本身只在以下情况推荐跨层协作：

| 结果条件 | 推荐话术 |
|----------|---------|
| 求职过程中情绪明显卡住，没法理性思考 | 「你现在的状态不适合直接做决定。先用 `/taxue-calm` 缓一下。」 |
| 反复失败，需要系统复盘找根因 | 「连续失利不是运气问题。用 `/taxue-career-fail` 系统诊断一次。」 |

## DO NOT

- 查具体在招岗位 → `taxue-job-search`（career 只做职业路径管理，不搜岗位）
- 需要行业分析辅助职业决策 → `taxue-industry`

---

*taxue-career v2.10 — 执行链路拆分为 4 个独立子 skill · 精准分流*
