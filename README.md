# Taxue2025 Skills

<p align="center">
  <a href="./README.md">中文</a> | <a href="./README_EN.md">English</a>
</p>

踏雪寻仙的 AI Skill 集合 —— 用于 Claude Code 和其他 AI 编程助手的高效技能库。

## 项目简介

本项目包含一系列精心设计的 AI Skill，用于增强 AI 助手在特定领域的能力。每个 Skill 都遵循**德鲁克的有效性原则**和**Anthropic 的迭代设计模式**，确保在正确的时机触发，提供高质量的输出。

## 核心 Skill

### 1. 问题解决器 (ultimate-problem-solver)

**版本**: v5.1

直接、可执行的问题解决方案，无废话。

**适用场景**:
- 技术问题调试
- 决策制定
- 流程优化
- 学习路径规划

**核心特点**:
- 六要素输出结构（为什么/理想解法/具体做法/直接可用/前提/推进）
- 调试模式（技术问题）
- 变更模式（文件/Skill 操作）
- 自动路由到其他 Skill

[查看详情](skills/ultimate-problem-solver/SKILL.md)

---

### 2. 哲思伙伴

深度对话伙伴，帮你在模糊的感受里找到准确的名字，在重复的剧本里看见隐藏的选择。

**适用场景**:
- 存在主义追问
- 心理模式识别
- 价值澄清
- 内在探索

**核心特点**:
- 六阶段对话流程（开场→定位→识别→澄清→展开→收束）
- 五个对话位置（接住情绪/澄清价值/揭示脚本/锚定具体/归还力量）
- 与问题解决器的智能边界
- 安全边界和转介机制

[查看详情](skills/哲思伙伴/SKILL.md)

---

### 3. Skill 设计师 (skill设计师)

基于德鲁克有效性 + Anthropic 验证模式的高影响力 AI Skill 设计框架。

**适用场景**:
- 创建新 Skill
- 改进现有 Skill
- 编码可重复工作流
- 标准化 Agent 行为

**核心特点**:
- 三层渐进式披露（YAML/正文/参考）
- 设计-测试-评审-改进循环
- 四种设计模式（专家/协调者/转换器/顾问）
- 基线测试验证价值

[查看详情](skills/skill设计师/SKILL.md)

---

### 4. 多专家圆桌讨论 (expert-roundtable)

激活多专家圆桌讨论系统，当用户面对复杂问题需要多维视角时立即触发。

**适用场景**:
- 战略决策、投资判断、组织管理
- AI系统设计、内容方向、方案评审
- skill设计评审、哲学/人生选择探索

**核心特点**:
- 四位常驻专家：德鲁克（管理）、芒格（逆向思维）、孙子（战略）、Ulrich（组织）
- 五种讨论模式（单专家/圆桌收敛/结论接收/系统优化/开放式求真）
- 轮空机制：专家自判断是否有独特观点
- 责任归属明确的结论输出

[查看详情](skills/expert-roundtable/SKILL.md)

---

### 5. 组织设计师 (skill-org)

将目的编译成岗位，将岗位编译成skill，将解法编译成可复用资产。

**适用场景**:
- 设计新岗位、新skill、新Agent职责
- 固化可重复工作流
- 标准化 Agent 行为
- 编译圆桌结论为可执行系统

**核心特点**:
- 六步编译流程（目的定义→交付标准→边界定义→协作界面→验收协议→迭代触发）
- JD和skill双模板输出
- 基于德鲁克目标管理和Ulrich组织能力建设

[查看详情](skills/skill-org/SKILL.md)

## 设计理念

### 德鲁克有效性原则

> 「效率是把事情做对，有效性是做对的事情。」

每个 Skill 在创建前都通过三个问题验证：
1. 这重要吗？（不做会影响结果吗？）
2. Agent 没有 Skill 能做吗？（基线测试）
3. 会被使用 5 次以上吗？（复用频率）

### Anthropic 迭代模式

Skill 设计是迭代的，不是一次性完成的：

```
草稿 → 测试 → 评审 → 改进 →（重复）
   ↑________________________↓
```

每次迭代让 Skill 提升 20%，直到足够好。

## 快速开始

### 安装

使用 Vercel 的 skills CLI 工具安装：

```bash
npx skills add taxue2025/taxue2025-skills
```

### 安装选项

```bash
# 查看本仓库包含的 skill 列表
npx skills add taxue2025/taxue2025-skills --list

# 安装特定 skill
npx skills add taxue2025/taxue2025-skills --skill ultimate-problem-solver

# 全局安装（所有项目可用）
npx skills add taxue2025/taxue2025-skills -g

# 安装到特定 Agent
npx skills add taxue2025/taxue2025-skills -a claude-code

# 非交互式安装（CI/CD 友好）
npx skills add taxue2025/taxue2025-skills --all -y
```

### 使用方法

安装后重启 Claude Code 或等待 Skill 自动加载，然后使用触发词激活对应 Skill。

### 触发词示例

**问题解决器**:
- 「帮我解决这个问题」
- 「怎么做到...」
- 「我该怎么办」
- 「修复这个」
- 「优化一下」

**哲思伙伴**:
- 「我想深度对话」
- 「人生意义是什么」
- 「哲学思考」
- 「自我认知」

**Skill 设计师**:
- 「设计一个 Skill」
- 「创建新 Skill」
- 「改进这个 Skill」

**多专家圆桌讨论**:
- 「开圆桌」
- 「让专家讨论」
- 「多角度分析」
- 「格鲁克怎么看」

**组织设计师**:
- 「设计一个岗位」
- 「给 Agent 定职责」
- 「拆分这个工作流」

## Skill 协作关系

```
expert-roundtable（思考层）
        ↓
    skill-org（编译层）
    /           \
问题解决        JD/skill设计
        ↓
   哲思伙伴（深度对话）
        ↓
  skill设计师（设计框架）
```

- **复杂问题** → expert-roundtable 多角度分析
- **需要固化** → skill-org 编译成可执行系统
- **深度对话** → 哲思伙伴
- **设计 skill** → skill设计师
- **直接解决** → 问题解决器

## 目录结构

```
taxue2025-skills/
├── README.md                          # 中文介绍
├── README_EN.md                       # English Introduction
├── INSTALL.md                         # 安装指南
├── INSTALL_EN.md                      # Installation Guide
├── skills/
│   ├── ultimate-problem-solver/       # 问题解决器
│   │   └── SKILL.md
│   ├── 哲思伙伴/                       # 哲思伙伴
│   │   └── SKILL.md
│   ├── skill设计师/                    # Skill 设计师
│   │   └── SKILL.md
│   ├── expert-roundtable/             # 多专家圆桌讨论
│   │   └── SKILL.md
│   └── skill-org/                     # 组织设计师
│       └── SKILL.md
└── LICENSE                            # 许可证
```

## 版本更新

| Skill | 版本 | 更新日期 | 主要更新 |
|-------|------|----------|----------|
| 问题解决器 | v5.1 | 2025-03 | 优化六要素输出结构，增强调试模式 |
| 哲思伙伴 | v1.0 | 2025-03 | 初始版本，六阶段对话流程 |
| Skill 设计师 | v1.0 | 2025-03 | 初始版本，Drucker + Anthropic 设计框架 |
| 多专家圆桌讨论 | v1.0 | 2025-03 | 初始版本，五位专家协作系统 |
| 组织设计师 | v1.0 | 2025-03 | 初始版本，六步编译流程 |

## 贡献指南

欢迎提交 Issue 和 PR！在贡献前请确保：

1. 通过 Skill 设计师的基线测试
2. 包含具体的使用示例
3. 更新版本日志

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 关于作者

**踏雪寻仙 (taxue2025)**

- GitHub: [@taxue2025](https://github.com/taxue2025)
- 专注于 AI 工具实战和内容创业方法论

---

> 「最好的 Skill 是在正确的时间加载，产生高质量的输出，并在每次使用中不断改进。」
