# Taxue2025 Skills

踏雪寻仙的 AI Skill 集合 —— 用于 Claude Code 和其他 AI 编程助手的高效技能库。

## 项目简介

本项目包含一系列精心设计的 AI Skill，用于增强 AI 助手在特定领域的能力。每个 Skill 都遵循德鲁克的有效性原则和 Anthropic 的迭代设计模式，确保在正确的时机触发，提供高质量的输出。

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

## 目录结构

```
taxue2025-skills/
├── README.md                          # 项目介绍
├── skills/
│   ├── ultimate-problem-solver/       # 问题解决器
│   │   └── SKILL.md
│   ├── 哲思伙伴/                       # 哲思伙伴
│   │   └── SKILL.md
│   └── skill设计师/                    # Skill 设计师
│       └── SKILL.md
└── LICENSE                            # 许可证
```

## 安装方法

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

## 使用方法

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

## 版本更新

| Skill | 版本 | 更新日期 | 主要更新 |
|-------|------|----------|----------|
| 问题解决器 | v5.1 | 2025-03 | 优化六要素输出结构，增强调试模式 |
| 哲思伙伴 | v1.0 | 2025-03 | 初始版本，六阶段对话流程 |
| Skill 设计师 | v1.0 | 2025-03 | 初始版本，Drucker + Anthropic 设计框架 |

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
