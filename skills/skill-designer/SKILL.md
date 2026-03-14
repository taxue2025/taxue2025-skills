---
name: skill-designer
description: |
  Design high-impact AI skills using Drucker's effectiveness + Anthropic's proven patterns.

  Use when:
  - "design a skill"
  - "create a new skill"
  - "improve this skill"
  - "skill design"
  - "skill designer"
  - "设计 skill"
  - "创建 skill"
  - "改进 skill"

  Use for:
  - Encoding repeatable workflows
  - Standardizing agent behavior
  - Creating skill templates

  Use other skills for:
  - Complex problem analysis → expert-roundtable
  - Direct problem solving → ultimate-problem-solver
  - JD/skill design → skill-org
---

# Skill 设计师

Design effective skills.

**System**: Drucker's Effectiveness + Anthropic's Iteration

---

## First Principles

### 1. Drucker: Do the Right Thing
```
Skill Value = Importance × Quality × Frequency
```

Ask before designing:
- [ ] Does this matter? (Drucker: "Would it affect results if not done?")
- [ ] Can agent do this without skill? (Baseline test)
- [ ] Will this be used 5+ times? (Reuse frequency)

### 2. Anthropic: Iterate to Quality

Skill design is **iterative**, not one-shot:

```
Draft → Test → Review → Improve → (repeat)
        ↑________________________↓
```

Each iteration makes the skill 20% better. Stop when good enough.

### 3. Claude: Structure for Understanding

**Progressive Disclosure** (Anthropic pattern):

| Level | When Loaded | Content |
|-------|-------------|---------|
| 1 (YAML) | Always | Triggers + core purpose |
| 2 (Body) | When matched | Instructions + examples |
| 3 (Refs) | On demand | Deep docs + templates |

---

## The Critical Few

### Most Important: Description (Level 1)

**Description decides if skill loads**. Get this right:

```yaml
---
name: skill-name
description: |
  [What it does] + [When to use it]
  
  Use when:
  - "[trigger phrase 1]"
  - "[trigger phrase 2]"
  (10+ specific phrases)
  
  Use for:
  - [Specific use case 1]
  - [Specific use case 2]
  
  Use other tools for:
  - [Adjacent case 1] → [Alternative]
---
```

**Test description** (Anthropic method):
1. Write 10 test queries (5 should trigger, 5 should not)
2. Check which trigger the skill
3. Adjust until 90%+ accuracy

### Most Important: Examples (Level 2)

**Examples teach better than rules**. Provide 2-4:

```xml
<examples>
  <example>
    <input>[Exact user request]</input>
    <output>[Desired response]</output>
  </example>
</examples>
```

**Good example criteria** (Anthropic):
- **Specific**: Real filenames, real data
- **Realistic**: User actually says this
- **Near-miss**: Edge case that could confuse

### Most Important: Baseline (Drucker Validation)

**Prove skill adds value**:

```markdown
## Baseline Test

**Task**: [Same input]

**Without skill**: [Output + quality score 1-5]
**With skill**: [Output + quality score 1-5]
**Improvement**: [Specific gain]
```

If no clear improvement → Don't create the skill.

---

## The Design Loop

### Step 1: Draft (10 min)

**Minimal viable skill**:
```yaml
---
name: [name]
description: |
  [What + when]
  
  Use when:
  - "[trigger]"
  
  Use for:
  - [use case]
---

# [Name]

## Purpose
[One sentence]

## Examples
[2 concrete cases]

## Process
[XML workflow if complex]
```

**Don't over-engineer**. Start simple, iterate.

### Step 2: Test (10 min)

**Run 3 test cases**:
1. **Happy path**: Ideal input
2. **Edge case**: Boundary input  
3. **Near-miss**: Similar but different

**Check**:
- [ ] Skill triggers correctly
- [ ] Output matches expectation
- [ ] Quality > 4/5

### Step 3: Review (Critical - Anthropic Key Insight)

**Show output to user before declaring done**:

```markdown
## Test Results

**Case 1**: [Input] → [Output]
**Case 2**: [Input] → [Output]
**Case 3**: [Input] → [Output]

Review questions:
1. What meets expectations?
2. What needs improvement? (Specific)
3. Any missing scenarios?
```

**Collect feedback → Record → Iterate**

### Step 4: Improve (10 min)

**Improve based on feedback**:
- False trigger? → Narrow description
- Missed trigger? → Add phrases
- Wrong output? → Add examples
- Wrong format? → Clarify XML structure

**Then**: Go to Step 2 (Test again)

**Stop when**: 3 tests pass + user satisfied

---

## Design Patterns

Choose based on problem:

| Pattern | Problem | Test |
|---------|---------|------|
| **Specialist** | Deep expertise | "Does this require domain knowledge?" |
| **Coordinator** | Multi-step | "Does this have handoffs between steps?" |
| **Transformer** | Format conversion | "Is this input → output mapping?" |
| **Advisor** | Recommendation | "Is this choosing between options?" |

---

## Anti-Patterns

| Pattern | Symptom | Fix |
|---------|---------|-----|
| **Kitchen Sink** | Does everything | Split, use parameters |
| **Black Box** | No progress visibility | Add state tracking |
| **Crystal Ball** | Assumes unknown info | Request explicitly |
| **Permafrost** | Never updated | Design for iteration |

---

## Example

```yaml
---
name: data-analyst
description: |
  Analyze datasets to extract insights and recommendations.
  
  Use when:
  - "analyze this data"
  - "what insights from this spreadsheet"
  - "help me understand these numbers"
  
  Use for:
  - Trend identification
  - Statistical summaries
  - Actionable recommendations
  
  Use other tools for:
  - Data visualization → Use chart-generator
  - Predictive modeling → Use ml-predictor
---

# Data Analyst

## Purpose
Transform raw data into actionable insights.

## Process

<workflow>
  <step>Explore: Load → Stats → Quality check</step>
  <step>Analyze: Apply methods per question type</step>
  <step>Synthesize: Key findings + confidence</step>
  <step>Recommend: 2-3 specific actions</step>
</workflow>

## Examples

### Example 1: Sales Trend
**Input**: "Q1-Q4 sales trend?"
**Process**: YoY growth + seasonality
**Output**: Executive summary with 3 recommendations

### Example 2: Churn Analysis
**Input**: "Why are customers leaving?"
**Process**: Cohort analysis + feature correlation
**Output**: Root causes + intervention plan

## Constraints

- Request raw data when possible
- Flag small samples (n<30)
- Distinguish correlation/causation
- Express uncertainty
```

---

## Quick Checklist

**Before**:
- [ ] Passes Drucker's 3 questions
- [ ] Baseline shows clear gap
- [ ] Pattern selected

**Draft**:
- [ ] Description with 5+ triggers
- [ ] 2-4 concrete examples
- [ ] XML structure if complex

**Test**:
- [ ] 3 cases (happy/edge/near-miss)
- [ ] 90%+ trigger accuracy
- [ ] Quality > 4/5

**Review**:
- [ ] User seen output
- [ ] Feedback recorded
- [ ] Improvements made

**Iterate**: Until 3 tests pass.

---

## Philosophy

> "The best skill is one that loads at the right time, produces quality output, 
> and improves with each use." — Anthropic + Drucker

**Design for**:
- Right problem (Drucker)
- Right time (Description accuracy)
- Right way (Iteration)

**Avoid**:
- Perfect first draft
- Complex evals
- Design without testing
