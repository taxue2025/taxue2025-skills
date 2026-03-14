# Taxue2025 Skills

<p align="center">
  <a href="./README.md">中文</a> | <a href="./README_EN.md">English</a>
</p>

A collection of AI Skills by Taxue —— High-efficiency skill library for Claude Code and other AI coding assistants.

## Project Overview

This project contains a series of carefully designed AI Skills to enhance AI assistants' capabilities in specific domains. Each Skill follows **Drucker's effectiveness principles** and **Anthropic's iterative design patterns**, ensuring high-quality output triggered at the right time.

## Core Skills

### 1. Ultimate Problem Solver

**Version**: v5.1

Direct, executable problem solutions without fluff.

**Use Cases**:
- Technical debugging
- Decision making
- Process optimization
- Learning path planning

**Key Features**:
- Six-element output structure (Why/Ideal Solution/Specific Actions/Immediately Usable/Prerequisites/Next Steps)
- Debug mode (technical issues)
- Change mode (file/Skill operations)
- Automatic routing to other Skills

[View Details](skills/ultimate-problem-solver/SKILL.md)

---

### 2. Philosophical Companion

A deep conversation partner that helps you find accurate names for vague feelings and hidden choices in repetitive scripts.

**Use Cases**:
- Existential inquiry
- Psychological pattern recognition
- Value clarification
- Inner exploration

**Key Features**:
- Six-stage dialogue flow (Opening → Positioning → Pattern Recognition → Clarification → Expansion → Closure)
- Five conversational positions (Emotional Holding/Value Clarification/Script Revelation/Anchoring Specifics/Returning Power)
- Intelligent boundaries with Ultimate Problem Solver
- Safety boundaries and referral mechanisms

[View Details](skills/哲思伙伴/SKILL.md)

---

### 3. Skill Designer

High-impact AI Skill design framework based on Drucker's effectiveness + Anthropic's validation patterns.

**Use Cases**:
- Creating new Skills
- Improving existing Skills
- Encoding repeatable workflows
- Standardizing Agent behavior

**Key Features**:
- Three-layer progressive disclosure (YAML/Body/References)
- Design-Test-Review-Improve cycle
- Four design patterns (Expert/Coordinator/Converter/Advisor)
- Baseline testing for value validation

[View Details](skills/skill设计师/SKILL.md)

---

### 4. Expert Roundtable

Activate multi-expert roundtable discussion system when users face complex problems requiring multi-dimensional perspectives.

**Use Cases**:
- Strategic decisions, investment judgment, organizational management
- AI system design, content direction, proposal review
- Skill design review, philosophical/life choice exploration

**Key Features**:
- Four resident experts: Drucker (Management), Munger (Inverse Thinking), Sun Tzu (Strategy), Ulrich (Organization)
- Five discussion modes (Single Expert/Roundtable Convergence/Conclusion Reception/System Optimization/Open-ended Inquiry)
- Pass mechanism: Experts self-judge if they have unique perspectives
- Conclusion output with clear responsibility attribution

[View Details](skills/expert-roundtable/SKILL.md)

---

### 5. Organization Designer

Compile purposes into positions, positions into skills, and solutions into reusable assets.

**Use Cases**:
- Designing new positions, new skills, new Agent responsibilities
- Solidifying repeatable workflows
- Standardizing Agent behavior
- Compiling roundtable conclusions into executable systems

**Key Features**:
- Six-step compilation process (Purpose Definition → Delivery Standards → Boundary Definition → Collaboration Interface → Acceptance Protocol → Iteration Triggers)
- Dual template output for JD and skill
- Based on Drucker's Management by Objectives and Ulrich's organizational capability building

[View Details](skills/skill-org/SKILL.md)

## Design Philosophy

### Drucker's Effectiveness Principle

> "Efficiency is doing things right; effectiveness is doing the right things."

Each Skill is validated through three questions before creation:
1. Does it matter? (Will it affect results if not done?)
2. Can the Agent do it without the Skill? (Baseline test)
3. Will it be used more than 5 times? (Reuse frequency)

### Anthropic Iteration Pattern

Skill design is iterative, not one-time:

```
Draft → Test → Review → Improve → (Repeat)
   ↑________________________↓
```

Each iteration improves the Skill by 20% until it's good enough.

## Quick Start

### Installation

Install using Vercel's skills CLI tool:

```bash
npx skills add taxue2025/taxue2025-skills
```

### Installation Options

```bash
# List skills in this repository
npx skills add taxue2025/taxue2025-skills --list

# Install specific skill
npx skills add taxue2025/taxue2025-skills --skill ultimate-problem-solver

# Global installation (available across all projects)
npx skills add taxue2025/taxue2025-skills -g

# Install to specific Agent
npx skills add taxue2025/taxue2025-skills -a claude-code

# Non-interactive installation (CI/CD friendly)
npx skills add taxue2025/taxue2025-skills --all -y
```

### Usage

After installation, restart Claude Code or wait for Skills to auto-load, then use trigger words to activate corresponding Skills.

### Trigger Word Examples

**Ultimate Problem Solver**:
- "Help me solve this problem"
- "How to do..."
- "What should I do"
- "Fix this"
- "Optimize this"

**Philosophical Companion**:
- "I want a deep conversation"
- "What is the meaning of life"
- "Philosophical thinking"
- "Self-awareness"

**Skill Designer**:
- "Design a Skill"
- "Create a new Skill"
- "Improve this Skill"

**Expert Roundtable**:
- "Start a roundtable"
- "Let experts discuss"
- "Multi-angle analysis"
- "What would Drucker say"

**Organization Designer**:
- "Design a position"
- "Define Agent responsibilities"
- "Break down this workflow"

## Skill Collaboration Relationships

```
Expert Roundtable (Thinking Layer)
        ↓
    Skill-Org (Compilation Layer)
    /           \
Problem Solving   JD/Skill Design
        ↓
   Philosophical Companion (Deep Dialogue)
        ↓
  Skill Designer (Design Framework)
```

- **Complex Problems** → Expert Roundtable for multi-angle analysis
- **Need Solidification** → Skill-Org to compile into executable systems
- **Deep Dialogue** → Philosophical Companion
- **Design Skill** → Skill Designer
- **Direct Solution** → Ultimate Problem Solver

## Directory Structure

```
taxue2025-skills/
├── README.md                          # Chinese Introduction
├── README_EN.md                       # English Introduction
├── INSTALL.md                         # Installation Guide (Chinese)
├── INSTALL_EN.md                      # Installation Guide (English)
├── skills/
│   ├── ultimate-problem-solver/       # Ultimate Problem Solver
│   │   └── SKILL.md
│   ├── 哲思伙伴/                       # Philosophical Companion
│   │   └── SKILL.md
│   ├── skill设计师/                    # Skill Designer
│   │   └── SKILL.md
│   ├── expert-roundtable/             # Expert Roundtable
│   │   └── SKILL.md
│   └── skill-org/                     # Organization Designer
│       └── SKILL.md
└── LICENSE                            # License
```

## Version Updates

| Skill | Version | Update Date | Major Updates |
|-------|---------|-------------|---------------|
| Ultimate Problem Solver | v5.1 | 2025-03 | Optimized six-element output structure, enhanced debug mode |
| Philosophical Companion | v1.0 | 2025-03 | Initial version, six-stage dialogue flow |
| Skill Designer | v1.0 | 2025-03 | Initial version, Drucker + Anthropic design framework |
| Expert Roundtable | v1.0 | 2025-03 | Initial version, five-expert collaboration system |
| Organization Designer | v1.0 | 2025-03 | Initial version, six-step compilation process |

## Contributing

Issues and PRs are welcome! Before contributing, please ensure:

1. Pass the Skill Designer's baseline test
2. Include specific usage examples
3. Update version logs

## License

MIT License - See [LICENSE](LICENSE) file for details

## About the Author

**Taxue (taxue2025)**

- GitHub: [@taxue2025](https://github.com/taxue2025)
- Focused on AI tool practice and content entrepreneurship methodology

---

> "The best Skill loads at the right time, produces high-quality output, and continuously improves with each use."
