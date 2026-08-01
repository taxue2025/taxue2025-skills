#!/usr/bin/env python3
"""meme_search.py — 梗解读定向检索 CLI

内置三个专门解梗数据源的直接查询，免认证、内置缓存。
萌娘百科 API 已关闭、微信指数无公开接口，这两个不在此脚本内，用 web_search 定向查询。

用法:
  python3 meme_search.py geng <query>    # itotii 梗百科（中文流行语释义）
  python3 meme_search.py ud <term>       # Urban Dictionary（英文俚语）
  python3 meme_search.py kym <query>     # Know Your Meme（英文 meme 溯源）
  python3 meme_search.py all <query>     # 三源并行聚合
  python3 meme_search.py cache-clear     # 清空缓存

缓存: ~/.cache/meme_search/，TTL 6 小时。梗词条更新慢，6 小时足够新。
"""

import argparse
import hashlib
import html as html_mod
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

CACHE_DIR = os.path.expanduser("~/.cache/meme_search")
TTL = 6 * 3600
TIMEOUT = 12
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def cache_get(key):
    path = os.path.join(CACHE_DIR, key + ".json")
    if not os.path.exists(path):
        return None
    try:
        with open(path) as f:
            data = json.load(f)
        if time.time() - data.get("ts", 0) < TTL:
            return data.get("payload")
    except Exception:
        pass
    return None


def cache_set(key, payload):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, key + ".json")
    with open(path, "w") as f:
        json.dump({"ts": time.time(), "payload": payload}, f, ensure_ascii=False)


def http_get(url, timeout=TIMEOUT):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def cached_call(source, query, fn):
    key = source + "_" + hashlib.md5(query.encode()).hexdigest()[:16]
    hit = cache_get(key)
    if hit is not None:
        return hit
    try:
        payload = fn()
    except Exception as e:
        return {"error": f"{source} 查询失败: {e}"}
    cache_set(key, payload)
    return payload


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


# ---------- itotii 梗百科（WordPress REST API，免认证） ----------

def search_geng(query, limit=5):
    url = (
        "https://geng.itotii.com/wp-json/wp/v2/posts?search="
        + urllib.parse.quote(query)
        + f"&per_page={limit}"
    )

    def run():
        data = json.loads(http_get(url))
        out = []
        for p in data:
            out.append({
                "source": "itotii 梗百科",
                "title": p.get("title", {}).get("rendered", ""),
                "date": p.get("date", ""),
                "summary": strip_tags(p.get("content", {}).get("rendered", ""))[:200],
                "url": p.get("link", ""),
            })
        return out

    return cached_call("geng", query, run)


# ---------- Urban Dictionary（官方 API，免认证） ----------

def search_ud(term, limit=3):
    url = "https://api.urbandictionary.com/v0/define?term=" + urllib.parse.quote(term)

    def run():
        data = json.loads(http_get(url))
        out = []
        for d in data.get("list", [])[:limit]:
            out.append({
                "source": "Urban Dictionary",
                "word": d.get("word", ""),
                "definition": d.get("definition", "").replace("\r\n", " ")[:300],
                "example": d.get("example", "").replace("\r\n", " ")[:200],
                "date": d.get("written_on", ""),
                "url": d.get("permalink", ""),
            })
        return out

    return cached_call("ud", term, run)


# ---------- Know Your Meme（HTML 解析，带 UA 即可） ----------

def search_kym(query, limit=5):
    url = "https://knowyourmeme.com/search?q=" + urllib.parse.quote(query)

    def run():
        page = http_get(url)
        out = []
        for m in re.finditer(r'<a class="item"[^>]*>', page):
            href = re.search(r'href="([^"]+)"', m.group(0))
            alt = re.search(r'alt="([^"]*)"', m.group(0))
            author = re.search(r'data-author="([^"]*)"', m.group(0))
            if not href:
                continue
            path = href.group(1)
            if path.startswith("/sensitive/"):
                continue  # 受限内容，跳过
            out.append({
                "source": "Know Your Meme",
                "title": html_mod.unescape(alt.group(1) if alt else path.rsplit("/", 1)[-1]).strip(),
                "author": author.group(1) if author else "",
                "url": "https://knowyourmeme.com" + path,
            })
            if len(out) >= limit:
                break
        return out

    return cached_call("kym", query, run)


# ---------- 输出 ----------

def fmt_geng(r):
    return f"- [{r['date'][:10]}] {r['title']} — {r['summary']} | {r['url']}"


def fmt_ud(r):
    ex = f"  例: {r['example']}" if r["example"] else ""
    return f"- [{r['date'][:10]}] {r['word']}: {r['definition']}\n{ex}\n  {r['url']}"


def fmt_kym(r):
    author = f" ({r['author']})" if r["author"] else ""
    return f"- {r['title']}{author} | {r['url']}"


def render(results, query):
    lines = [f"## {query}\n"]
    order = [
        ("itotii 梗百科", fmt_geng),
        ("Urban Dictionary", fmt_ud),
        ("Know Your Meme", fmt_kym),
    ]
    for src, fmt in order:
        items = [r for r in results if r.get("source") == src and "error" not in r]
        errs = [r for r in results if r.get("source") == src and "error" in r]
        if items:
            lines.append(f"### {src}")
            lines.extend(fmt(r) for r in items)
            lines.append("")
        elif errs:
            lines.append(f"### {src}")
            lines.append(errs[0]["error"])
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description="梗解读定向检索")
    ap.add_argument("cmd", choices=["geng", "ud", "kym", "all", "cache-clear"])
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--limit", type=int, default=5)
    args = ap.parse_args()

    if args.cmd == "cache-clear":
        if os.path.isdir(CACHE_DIR):
            for f in os.listdir(CACHE_DIR):
                os.remove(os.path.join(CACHE_DIR, f))
            print("缓存已清空")
        else:
            print("无缓存")
        return

    if not args.query:
        print("缺少查询词", file=sys.stderr)
        sys.exit(1)

    q = args.query.strip()
    if args.cmd == "all":

        def is_cjk(t):
            return sum(1 for ch in t if "\u4e00" <= ch <= "\u9fff") >= len(t) * 0.3

        with ThreadPoolExecutor(max_workers=3) as ex:
            if is_cjk(q):
                # 中文词只查 itotii，避免英文源返回无关内容
                futs = [ex.submit(search_geng, q, args.limit)]
            else:
                # 英文词查 Urban Dictionary + Know Your Meme
                futs = [
                    ex.submit(search_ud, q, 3),
                    ex.submit(search_kym, q, args.limit),
                ]
            results = [f.result() for f in futs]
        flat = []
        for r in results:
            flat.extend(r if isinstance(r, list) else [r])
        print(render(flat, q))
    elif args.cmd == "geng":
        print(render(search_geng(q, args.limit), q))
    elif args.cmd == "ud":
        print(render(search_ud(q, 3), q))
    elif args.cmd == "kym":
        print(render(search_kym(q, args.limit), q))


if __name__ == "__main__":
    main()
