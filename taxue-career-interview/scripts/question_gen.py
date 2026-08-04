#!/usr/bin/env python3
"""面试题目生成器。

输入岗位/JD 的技能关键词，按 interview-coach 的题目分类体系生成题目。
- 技术面：DS-Algo / Network / OS / Database / Lang-Runtime / Framework / Arch-Design / Scenario / Coding
- 行为面：Behavior-Project / Team / Conflict / Fail / Plan / Leadership
- 系统设计：SD-Overall / Scale / Data / Realworld

用法：
  python3 question_gen.py --jd jd.txt                # 从 JD 提取技能并出题
  python3 question_gen.py --skills "Python React SQL" # 直接指定技能
  python3 question_gen.py --jd jd.txt --round tech    # 只出技术面
  python3 question_gen.py --jd jd.txt --count 10 --json
"""

import argparse
import json
import re
import sys

# 技能 → 分类路由
SKILL_ROUTE = {
    "Python": ["Lang-Runtime", "Coding"],
    "Java": ["Lang-Runtime", "Coding"],
    "Go": ["Lang-Runtime", "Coding"],
    "JavaScript": ["Lang-Runtime", "Framework"],
    "TypeScript": ["Lang-Runtime", "Framework"],
    "React": ["Framework", "Lang-Runtime"],
    "Vue": ["Framework"],
    "SQL": ["Database", "Coding"],
    "MySQL": ["Database"],
    "PostgreSQL": ["Database"],
    "Redis": ["Database", "Framework"],
    "MongoDB": ["Database"],
    "Docker": ["Framework", "Arch-Design"],
    "Kubernetes": ["Framework", "Arch-Design"],
    "AWS": ["Arch-Design", "Scenario"],
    "Linux": ["OS"],
    "网络": ["Network"],
    "TCP": ["Network"],
    "HTTP": ["Network"],
    "微服务": ["Arch-Design"],
    "高并发": ["Arch-Design", "Scenario"],
    "分布式": ["Arch-Design", "SD-Scale"],
    "消息队列": ["Framework", "Arch-Design"],
    "Kafka": ["Framework", "Arch-Design"],
    "机器学习": ["DS-Algo", "Lang-Runtime"],
    "大模型": ["DS-Algo", "Scenario"],
}

# 每类别的题目模板
TECH_QUESTIONS = {
    "DS-Algo": [
        "讲一个你最近解决的算法题，复杂度是多少？",
        "数组和链表的区别？什么场景用哪个？",
        "如何设计一个 LRU 缓存？",
    ],
    "Network": [
        "从输入 URL 到页面渲染，发生了什么？",
        "TCP 三次握手和四次挥手？为什么需要？",
        "HTTPS 和 HTTP 的区别？TLS 握手过程？",
    ],
    "OS": [
        "进程和线程的区别？协程呢？",
        "什么是死锁？如何避免？",
        "虚拟内存是什么？页面置换算法？",
    ],
    "Database": [
        "索引为什么用 B+ 树？",
        "事务的 ACID 是什么？隔离级别呢？",
        "分库分表的策略？什么时候需要？",
    ],
    "Lang-Runtime": [
        "垃圾回收机制怎么工作的？",
        "闭包是什么？有什么坑？",
        "值传递和引用传递的区别？",
    ],
    "Framework": [
        "讲一下你用的框架的核心原理？",
        "这个框架的性能瓶颈在哪？怎么排查？",
        "对比另一个同类框架，你会怎么选？",
    ],
    "Arch-Design": [
        "设计一个高可用的系统，你会怎么考虑？",
        "微服务拆分的原则？拆错会怎样？",
        "如何做容量评估和限流降级？",
    ],
    "Scenario": [
        "线上服务突然变慢，怎么排查？",
        "数据库连接池被打满，怎么处理？",
        "用户反馈数据不一致，怎么定位？",
    ],
    "Coding": [
        "手写：反转链表 / 实现一个 Promise / 二分查找",
        "手写：两个有序数组的中位数",
        "手写：实现一个线程安全的单例",
    ],
}

BEHAVIOR_QUESTIONS = {
    "Behavior-Project": "讲一个你最有成就感的项目？你的角色和贡献是什么？",
    "Behavior-Team": "讲一次和同事协作解决难题的经历？",
    "Behavior-Conflict": "讲一次你和同事意见分歧，最后怎么解决的？",
    "Behavior-Fail": "讲一次你失败的经历？学到了什么？",
    "Behavior-Plan": "你未来 3-5 年的职业规划？",
    "Behavior-Leadership": "讲一次你主动牵头推动事情的经历？",
}

SD_QUESTIONS = {
    "SD-Overall": "设计一个 XX 系统，从需求到架构讲一遍？",
    "SD-Scale": "如果这个系统要支撑 10 倍流量，怎么改造？",
    "SD-Data": "这个系统的数据存储怎么设计？一致性怎么保证？",
    "SD-Realworld": "复现一个你熟悉的真实系统（如短视频推荐/电商订单），讲架构？",
}


def extract_skills(jd_text: str) -> list:
    """从 JD 提取技能关键词（匹配 SKILL_ROUTE 的 key）。"""
    found = []
    for kw in SKILL_ROUTE:
        if re.search(kw, jd_text, re.IGNORECASE):
            found.append(kw)
    return found


def generate(skills: list, round_type: str = "all", count: int = 10) -> list:
    """按分类体系生成题目。"""
    # 技术面分类：从技能路由聚合
    tech_cats = []
    for s in skills:
        for cat in SKILL_ROUTE.get(s, []):
            if cat not in tech_cats:
                tech_cats.append(cat)

    # 行为面固定 1-2 题
    behavior_pool = list(BEHAVIOR_QUESTIONS.keys())
    # 系统设计在 round=all 或 design 时出 1 题
    sd_cats = list(SD_QUESTIONS.keys())

    questions = []
    if round_type in ("all", "tech"):
        for cat in tech_cats[:count]:
            templates = TECH_QUESTIONS.get(cat, [])
            if templates:
                questions.append({"category": cat, "question": templates[0]})
    if round_type in ("all", "behavior"):
        for cat in behavior_pool[:2]:
            questions.append({"category": cat, "question": BEHAVIOR_QUESTIONS[cat]})
    if round_type in ("all", "design"):
        questions.append({"category": "SD-Overall", "question": SD_QUESTIONS["SD-Overall"]})

    return questions[:count]


def main():
    ap = argparse.ArgumentParser(description="面试题目生成器")
    ap.add_argument("--jd", help="JD 文件路径（自动提取技能）")
    ap.add_argument("--skills", help="直接指定技能（空格分隔）")
    ap.add_argument("--round", choices=["all", "tech", "behavior", "design"], default="all")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.skills:
        skills = [s.strip() for s in args.skills.split() if s.strip()]
    elif args.jd:
        with open(args.jd, encoding="utf-8") as f:
            skills = extract_skills(f.read())
        if not skills:
            print("⚠️ JD 中未识别到技能关键词，请用 --skills 手动指定")
            skills = []
    else:
        print("需提供 --jd 或 --skills")
        return 1

    questions = generate(skills, args.round, args.count)

    if args.json:
        print(json.dumps({"skills": skills, "questions": questions}, ensure_ascii=False, indent=2))
        return 0

    print(f"识别技能: {', '.join(skills) if skills else '无'}")
    print(f"生成题目: {len(questions)} 道")
    print("---")
    for i, q in enumerate(questions, 1):
        print(f"{i}. [{q['category']}] {q['question']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
