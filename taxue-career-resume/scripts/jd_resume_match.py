#!/usr/bin/env python3
"""JD ↔ 简历匹配评分器。

实现 taxue-career「定向投递优化」三步中的第二步「匹配度自检」：
- 输入：JD 文本 + 简历文本
- 输出：硬性门槛命中、关键词覆盖率、匹配度评分、缺什么

用法：
  python3 jd_resume_match.py jd.txt resume.txt          # 文本评分
  python3 jd_resume_match.py jd.txt resume.txt --json   # JSON 输出
  python3 jd_resume_match.py jd.txt resume.txt --ci     # 大小写不敏感（默认开）

注意：脚本做机械匹配（关键词/技能/数字），语义匹配（经历相关性）仍需 LLM 判断。
"""

import argparse
import json
import re
import sys

# 常见硬性门槛信号（学历/年限/证书/语言）
HARD_GATES = [
    r"本科", r"硕士", r"博士", r"大专",
    r"\d+\s*年.*经验", r"经验.*\d+\s*年",
    r"CET-?6", r"英语.*流利", r"口语.*流利",
    r"PMP", r"CPA", r"CFA", r"法律职业资格", r"执业医师",
]

# 常见技能关键词（扩展可按需添加）
SKILL_KEYWORDS = [
    "Python", "Java", "Go", "C\\+\\+", "Rust", "JavaScript", "TypeScript",
    "React", "Vue", "Node", "SQL", "MySQL", "PostgreSQL", "Redis", "MongoDB",
    "Docker", "Kubernetes", "K8s", "AWS", "Azure", "GCP", "Linux",
    "TensorFlow", "PyTorch", "机器学习", "深度学习", "NLP", "大模型", "LLM",
    "数据分析", "数据挖掘", "ETL", "Hadoop", "Spark", "Flink",
    "产品设计", "原型", "Axure", "Figma", "PRD", "项目管理", "敏捷", "Scrum",
    "市场营销", "增长", "SEO", "SEM", "新媒体", "内容运营", "用户运营",
    "财务分析", "审计", "成本控制", "预算", "投资分析", "尽职调查",
]


def extract_jd_features(jd_text: str) -> dict:
    """从 JD 提取：硬性门槛、技能关键词、职责动词。"""
    hard_hits = []
    for pattern in HARD_GATES:
        if re.search(pattern, jd_text):
            hard_hits.append(pattern)

    skills = []
    for kw in SKILL_KEYWORDS:
        if re.search(kw, jd_text, re.IGNORECASE):
            skills.append(kw)

    return {"hard_gates": hard_hits, "skills": skills}


def score(jd_text: str, resume_text: str, case_insensitive: bool = True) -> dict:
    flags = re.IGNORECASE if case_insensitive else 0
    features = extract_jd_features(jd_text)
    resume_lower = resume_text.lower()

    # 硬性门槛命中
    hard_missing = []
    for gate in features["hard_gates"]:
        if not re.search(gate, resume_text, flags):
            hard_missing.append(gate)

    # 技能关键词覆盖率
    skill_present = []
    skill_missing = []
    for kw in features["skills"]:
        if re.search(kw, resume_text, flags):
            skill_present.append(kw)
        else:
            skill_missing.append(kw)

    skill_coverage = len(skill_present) / len(features["skills"]) if features["skills"] else 0

    # 量化指标检测（简历里有多少「数字 + 提升/降低/规模」）
    quant_patterns = [
        r"\d+\s*%", r"提升\s*\d+", r"降低\s*\d+", r"增长\s*\d+",
        r"\d+\s*(万|亿|人|个|家|倍)", r"从\s*\d+.*到\s*\d+",
    ]
    quant_hits = 0
    for p in quant_patterns:
        if re.search(p, resume_text):
            quant_hits += 1

    # 综合评分：硬性门槛（40%）+ 技能覆盖（40%）+ 量化（20%）
    gate_score = 1.0 if not hard_missing else max(0.2, 1.0 - 0.4 * len(hard_missing))
    skill_score = skill_coverage
    quant_score = min(1.0, quant_hits / 3)
    total = gate_score * 0.4 + skill_score * 0.4 + quant_score * 0.2

    verdict = "✅ 强烈推荐投递" if total >= 0.8 else (
        "⚠️ 建议补充匹配后再投" if total >= 0.5 else "❌ 匹配度低，先调整方向"
    )

    return {
        "hard_gates_total": len(features["hard_gates"]),
        "hard_gates_missing": hard_missing,
        "skills_total": len(features["skills"]),
        "skills_present": skill_present,
        "skills_missing": skill_missing,
        "skill_coverage": round(skill_coverage * 100),
        "quant_hits": quant_hits,
        "match_score": round(total * 100),
        "verdict": verdict,
    }


def main():
    ap = argparse.ArgumentParser(description="JD ↔ 简历匹配评分器")
    ap.add_argument("jd", help="JD 文件路径")
    ap.add_argument("resume", help="简历文件路径")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    ap.add_argument("--no-ci", action="store_true", help="大小写敏感")
    args = ap.parse_args()

    with open(args.jd, encoding="utf-8") as f:
        jd_text = f.read()
    with open(args.resume, encoding="utf-8") as f:
        resume_text = f.read()

    result = score(jd_text, resume_text, case_insensitive=not args.no_ci)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"硬性门槛: 命中 {result['hard_gates_total'] - len(result['hard_gates_missing'])}/{result['hard_gates_total']}")
    if result["hard_gates_missing"]:
        print(f"  ❌ 缺失: {', '.join(result['hard_gates_missing'])}")
    print(f"技能关键词: 覆盖 {result['skill_coverage']}% ({len(result['skills_present'])}/{result['skills_total']})")
    if result["skills_missing"]:
        print(f"  ⚠️ 缺: {', '.join(result['skills_missing'][:10])}")
    print(f"量化指标: {result['quant_hits']} 处")
    print(f"匹配度: {result['match_score']}/100 | {result['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
