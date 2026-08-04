#!/usr/bin/env python3
"""render_resume.py — 简历母版渲染器（taxue-career-resume 产出层）

把结构化母版 JSON 渲染为独立 HTML（打印友好、ATS 可解析），
同时输出纯文本版本供 ATS 自检。

用法：
    python3 render_resume.py master.json [--custom custom.json] [--out resume.html]

- master.json   母版数据（字段见 assets/master-template.json）
- custom.json   定制配置（可选）：order / exclude / overrides，见下方示例
- --out         输出 HTML 路径；同目录自动生成同名 .txt（ATS 纯文本）

定制配置示例（custom.json）：
{
  "order": ["summary", "skills", "experience", "education", "certifications"],
  "exclude": {"experience": ["e3"], "projects": ["p1"]},
  "overrides": {
    "meta": {"title": "后端工程师（Java/Go）"},
    "summary": "针对本 JD 重写的价值主张……",
    "skills": {"hard": ["Java", "Spring", "Go"], "soft": ["跨团队协作"]}
  }
}

不传 custom.json 时，输出母版全量版（作为基准版本）。
"""

import argparse
import html
import json
import os
import sys
import textwrap

SECTION_ORDER_DEFAULT = [
    "summary", "skills", "experience", "projects",
    "education", "certifications", "languages",
]

SECTION_TITLES = {
    "summary": "个人简介",
    "skills": "专业技能",
    "experience": "工作经历",
    "projects": "项目经历",
    "education": "教育背景",
    "certifications": "证书与荣誉",
    "languages": "语言能力",
}


def esc(value):
    return html.escape(str(value), quote=True)


def load_json(path):
    if not path or not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_overrides(master, overrides):
    """按 overrides 覆盖母版字段（浅合并 skills，其余直接替换）。"""
    data = json.loads(json.dumps(master))  # deep copy
    if not overrides:
        return data
    if "meta" in overrides:
        data["meta"] = {**data.get("meta", {}), **overrides["meta"]}
    if "summary" in overrides:
        data["summary"] = overrides["summary"]
    if "skills" in overrides:
        data["skills"] = {**data.get("skills", {}), **overrides["skills"]}
    for key in ("experience", "projects", "education", "certifications", "languages"):
        if key in overrides:
            data[key] = overrides[key]
    return data


def apply_exclude(data, exclude):
    for key, ids in (exclude or {}).items():
        if key not in data or not isinstance(data[key], list):
            continue
        data[key] = [item for item in data[key] if item.get("id") not in set(ids)]
    return data


def render_contact(meta):
    parts = []
    for field in ("phone", "email", "location", "portfolio", "years"):
        value = meta.get(field)
        if value:
            parts.append(f'<span>{esc(value)}</span>')
    return f'<div class="contact">{"".join(parts)}</div>' if parts else ""


def render_head(meta):
    """姓名 + 定位 + 联系方式头部，所有简历版本必出。"""
    name = meta.get("name") or "姓名"
    role = meta.get("title") or ""
    role_html = f'<div class="role">{esc(role)}</div>' if role else ""
    return (
        f'<header class="head"><h1>{esc(name)}</h1>'
        f'{role_html}{render_contact(meta)}</header>'
    )


def render_section(name, data):
    body = []
    if name == "summary" and data.get("summary"):
        body.append(f'<div class="summary"><p>{esc(data["summary"])}</p></div>')
    elif name == "skills":
        hard = data.get("skills", {}).get("hard", [])
        soft = data.get("skills", {}).get("soft", [])
        lines = []
        if hard:
            lines.append(f'<p class="hard"><b>硬技能：</b>{esc(" / ".join(hard))}</p>')
        if soft:
            lines.append(f'<p class="soft">软技能：{esc(" / ".join(soft))}</p>')
        if lines:
            body.append(f'<div class="skills">{"".join(lines)}</div>')
    elif name == "experience":
        for item in data.get("experience", []):
            what = " · ".join(x for x in (item.get("company"), item.get("role")) if x)
            points = "".join(f"<li>{esc(p)}</li>" for p in item.get("points", []))
            tags = item.get("tags")
            tags_html = f'<div class="tags">{esc(" · ".join(tags))}</div>' if tags else ""
            body.append(
                f'<div class="entry"><div class="entry-head"><span class="what">{esc(what)}</span>'
                f'<span class="when">{esc(item.get("period", ""))}</span></div>'
                f'<ul>{points}</ul>{tags_html}</div>'
            )
    elif name == "projects":
        for item in data.get("projects", []):
            what = item.get("name", "")
            if item.get("role"):
                what = f"{what}（{item['role']}）"
            points = "".join(f"<li>{esc(p)}</li>" for p in item.get("points", []))
            link = item.get("link")
            link_html = f'<div class="tags">链接：{esc(link)}</div>' if link else ""
            body.append(
                f'<div class="entry"><div class="entry-head"><span class="what">{esc(what)}</span>'
                f'<span class="when">{esc(item.get("period", ""))}</span></div>'
                f'<ul>{points}</ul>{link_html}</div>'
            )
    elif name == "education":
        for item in data.get("education", []):
            what = " · ".join(x for x in (item.get("school"), item.get("degree")) if x)
            body.append(
                f'<div class="edu-line"><span>{esc(what)}</span>'
                f'<span class="when">{esc(item.get("period", ""))}</span></div>'
            )
    elif name == "certifications":
        for item in data.get("certifications", []):
            body.append(
                f'<div class="cert-line"><span>{esc(item.get("name", ""))}</span>'
                f'<span class="when">{esc(item.get("period", ""))}</span></div>'
            )
    elif name == "languages" and data.get("languages"):
        lines = "".join(f'<div class="lang-line">{esc(l)}</div>' for l in data["languages"])
        body.append(f'<div class="languages">{lines}</div>')
    if not body:
        return ""
    title = SECTION_TITLES.get(name, name)
    return f'<section><h2>{esc(title)}</h2>{"".join(body)}</section>'


def estimate_pages(data):
    """粗略估算打印页数（A4，11pt，中文每行约 46 字）。"""
    text_blocks = []
    text_blocks.append(" ".join(str(v) for v in data.get("meta", {}).values()))
    if data.get("summary"):
        text_blocks.append(data["summary"])
    for key in ("experience", "projects"):
        for item in data.get(key, []):
            text_blocks.append(" ".join(str(v) for v in item.values() if not isinstance(v, list)))
            text_blocks.extend(str(p) for p in item.get("points", []))
    for key in ("education", "certifications"):
        for item in data.get(key, []):
            text_blocks.append(" ".join(str(v) for v in item.values()))
    if data.get("languages"):
        text_blocks.append(" ".join(data["languages"]))
    total_chars = sum(len(b) for b in text_blocks)
    chars_per_line = 46
    lines = max(1, total_chars / chars_per_line)
    entries = sum(len(data.get(k, [])) for k in ("experience", "projects"))
    header_lines = 8 + len(data.get("meta", {})) + entries * 2
    total_lines = lines + header_lines
    return max(1, round(total_lines / 48))


def render_txt(data):
    """ATS 纯文本：无格式、关键词直接可解析。"""
    out = []
    meta = data.get("meta", {})
    out.append(meta.get("name", ""))
    out.append(" / ".join(x for x in (meta.get("title"), meta.get("phone"), meta.get("email"), meta.get("location")) if x))
    out.append("")
    if data.get("summary"):
        out.append("个人简介")
        out.append(data["summary"])
        out.append("")
    hard = data.get("skills", {}).get("hard", [])
    soft = data.get("skills", {}).get("soft", [])
    if hard or soft:
        out.append("专业技能")
        if hard:
            out.append("硬技能: " + ", ".join(hard))
        if soft:
            out.append("软技能: " + ", ".join(soft))
        out.append("")
    for key, title in (("experience", "工作经历"), ("projects", "项目经历")):
        items = data.get(key, [])
        if not items:
            continue
        out.append(title)
        for item in items:
            head = " · ".join(x for x in (item.get("company") or item.get("name"), item.get("role"), item.get("period")) if x)
            out.append(head)
            out.extend("- " + p for p in item.get("points", []))
            if item.get("tags"):
                out.append("关键词: " + ", ".join(item["tags"]))
            out.append("")
    for key, title in (("education", "教育背景"), ("certifications", "证书与荣誉")):
        items = data.get(key, [])
        if not items:
            continue
        out.append(title)
        for item in items:
            out.append(" · ".join(x for x in (item.get("school") or item.get("name"), item.get("degree"), item.get("period")) if x))
        out.append("")
    if data.get("languages"):
        out.append("语言能力")
        out.append(", ".join(data["languages"]))
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="简历母版渲染器")
    parser.add_argument("master", help="母版 JSON 路径")
    parser.add_argument("--custom", default=None, help="定制 JSON 路径（可选）")
    parser.add_argument("--out", default=None, help="输出 HTML 路径（默认与母版同目录 resume.html）")
    args = parser.parse_args()

    master = load_json(args.master)
    if not master:
        print("错误：母版 JSON 为空或不存在。", file=sys.stderr)
        sys.exit(1)

    custom = load_json(args.custom)
    data = merge_overrides(master, custom.get("overrides", {}))
    data = apply_exclude(data, custom.get("exclude"))

    order = custom.get("order") or SECTION_ORDER_DEFAULT
    order = [s for s in order if s in SECTION_TITLES]
    # 未出现在 order 中的剩余 section 追加到末尾，保持完整
    for s in SECTION_ORDER_DEFAULT:
        if s not in order:
            order.append(s)

    sections = []
    for name in order:
        section_html = render_section(name, data)
        if section_html:
            sections.append(section_html)
    body = render_head(data.get("meta", {})) + "".join(sections)
    if not sections:
        print("错误：渲染结果为空，请检查母版 JSON 内容。", file=sys.stderr)
        sys.exit(1)

    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "resume-template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    meta = data.get("meta", {})
    title = f"{meta.get('name', '简历')} - {meta.get('title', '')}".strip(" -")
    html_out = template.replace("__TITLE__", esc(title)).replace("__BODY__", body)

    out_path = args.out or os.path.join(os.path.dirname(os.path.abspath(args.master)), "resume.html")
    out_dir = os.path.dirname(os.path.abspath(out_path))
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    txt_path = os.path.splitext(out_path)[0] + ".txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(render_txt(data))

    pages = estimate_pages(data)
    custom_note = "（定制版）" if args.custom else "（母版全量版）"
    print(f"已生成：{out_path} {custom_note}")
    print(f"已生成：{txt_path}（ATS 纯文本）")
    print(f"估算打印页数：约 {pages} 页 A4")
    if pages > 1:
        print("提示：超过 1 页。优先用 custom.json 裁剪经历/项目，或压缩 summary 与 bullet 数量。")


if __name__ == "__main__":
    main()
