import html
import json
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
WORK_DIR = SKILL_DIR / "work"
OUT_DIR = SKILL_DIR.parents[2]
RAW = WORK_DIR / "raw.json"
PICKS = WORK_DIR / "picks.json"


def fetch_page(since):
    req = urllib.request.Request(
        f"https://github.com/trending?since={since}",
        headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US"},
    )
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8")


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def to_int(s):
    return int(s.replace(",", ""))


def parse(page):
    items = []
    for art in re.findall(r'<article class="Box-row">(.*?)</article>', page, re.S):
        owner, repo = re.search(r'<h2[^>]*>.*?href="/([^/"]+)/([^/"]+)"', art, re.S).groups()
        desc = re.search(r"<p [^>]*>(.*?)</p>", art, re.S)
        lang = re.search(r'itemprop="programmingLanguage">([^<]+)<', art)
        stars = re.search(r'/stargazers"[^>]*>.*?</svg>\s*([\d,]+)', art, re.S)
        delta = re.search(r"([\d,]+) stars (?:today|this week)", art)
        items.append({
            "owner": owner,
            "repo": repo,
            "lang": lang.group(1).strip() if lang else "-",
            "stars": to_int(stars.group(1)) if stars else 0,
            "delta": to_int(delta.group(1)) if delta else 0,
            "desc_en": text(desc.group(1)) if desc else "",
        })
    return items


def previous_reports(today):
    return sorted(
        p for p in OUT_DIR.glob("*/github_trending_*.html")
        if p.stem.removeprefix("github_trending_") < today
    )


def fetch():
    today = datetime.now(timezone(timedelta(hours=9))).date().isoformat()
    prev = previous_reports(today)
    prev_text = [p.read_text(encoding="utf-8") for p in prev]
    raw = {"date": today, "prev": [p.stem.removeprefix("github_trending_") for p in prev]}
    for period in ("daily", "weekly"):
        items = parse(fetch_page(period))
        if not items:
            sys.exit(f"{period}: 저장소를 하나도 파싱하지 못했습니다. GitHub 페이지 구조를 확인하세요.")
        for it in items:
            key = f'owner: "{it["owner"]}", repo: "{it["repo"]}"'
            it["streak"] = sum(key in t for t in prev_text)
        raw[period] = items
    WORK_DIR.mkdir(exist_ok=True)
    RAW.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
    print(RAW.read_text(encoding="utf-8"))


def js_array(items):
    s = lambda v: json.dumps(v, ensure_ascii=False)
    rows = [
        f'{{ owner: {s(it["owner"])}, repo: {s(it["repo"])}, lang: {s(it["lang"])}, '
        f'stars: {it["stars"]}, delta: {it["delta"]}, streak: {it["streak"]},\n'
        f'      desc: {s(it["desc"])} }}'
        for it in items
    ]
    return ("[\n    " + ",\n    ".join(rows) + "\n  ]").replace("</", "<\\/")


def markdown(day, prev_label, daily, analysis, report_link):
    kept, dropped, total = daily
    lines = [
        f"# GitHub AI 트렌드 {day} (Daily)",
        "",
        f"Daily 트렌딩 {total}개 중 AI 관련 {len(kept)}개",
        "",
        "## 분석",
        "",
        *[f"- {a}" for a in analysis],
        "",
        "## Daily AI 저장소",
        "",
        f"이전 등장: 이전 리포트({prev_label})에 등장한 횟수",
        "",
        "| 저장소 | 언어 | 전체 ★ | 오늘 ★ | 이전 등장 | 설명 |",
        "|---|---|---:|---:|---:|---|",
    ]
    for it in sorted(kept, key=lambda it: -it["streak"]):
        name = f'{it["owner"]}/{it["repo"]}'
        desc = it["desc"].replace("|", "\\|")
        lines.append(f'| [{name}](https://github.com/{name}) | {it["lang"]} | {it["stars"]:,} | +{it["delta"]:,} | {it["streak"]} | {desc} |')
    lines += [
        "",
        f'제외(AI 아님): {" · ".join(dropped) or "없음"}',
        "",
        f"전체 리포트(Weekly 포함): [{Path(report_link).name}]({report_link})",
        "",
    ]
    return "\n".join(lines)


def render():
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    picks = json.loads(PICKS.read_text(encoding="utf-8"))
    ko, excluded = picks["ko"], picks["excluded"]
    analysis = picks.get("analysis")
    if not analysis:
        sys.exit("picks.json에 analysis(Daily 분석)가 없습니다.")
    seen_excluded = set()
    out = {}
    for period in ("daily", "weekly"):
        kept, dropped = [], []
        for it in raw[period]:
            name = f'{it["owner"]}/{it["repo"]}'
            if name in ko:
                kept.append({**it, "desc": ko[name]})
            elif name in excluded:
                dropped.append(name if name in seen_excluded else f"{name}({excluded[name]})")
                seen_excluded.add(name)
            else:
                sys.exit(f"picks.json에 분류되지 않은 저장소: {name}")
        out[period] = (kept, dropped, len(raw[period]))

    prev = raw["prev"]
    prev_label = " · ".join(d[5:] for d in prev) if prev else "없음"
    page = (SKILL_DIR / "template.html").read_text(encoding="utf-8")
    replacements = {
        "__DATE__": raw["date"],
        "__PREV__": prev_label,
        "__DAILY__": js_array(out["daily"][0]),
        "__WEEKLY__": js_array(out["weekly"][0]),
        "__DAILY_AI__": str(len(out["daily"][0])),
        "__DAILY_TOTAL__": str(out["daily"][2]),
        "__WEEKLY_AI__": str(len(out["weekly"][0])),
        "__WEEKLY_TOTAL__": str(out["weekly"][2]),
        "__EX_DAILY_N__": str(len(out["daily"][1])),
        "__EX_WEEKLY_N__": str(len(out["weekly"][1])),
        "__EX_DAILY__": " · ".join(out["daily"][1]) or "없음",
        "__EX_WEEKLY__": " · ".join(out["weekly"][1]) or "없음",
    }
    for k, v in replacements.items():
        page = page.replace(k, v)
    month = raw["date"][:7]
    (OUT_DIR / month).mkdir(exist_ok=True)
    target = OUT_DIR / month / f'github_trending_{raw["date"]}.html'
    target.write_text(page, encoding="utf-8", newline="\n")
    md = target.with_suffix(".md")
    md.write_text(markdown(raw["date"], prev_label, out["daily"], analysis, target.name), encoding="utf-8", newline="\n")
    readme = OUT_DIR / "README.md"
    readme.write_text(markdown(raw["date"], prev_label, out["daily"], analysis, f"{month}/{target.name}"), encoding="utf-8", newline="\n")
    print(f'{target}  (Daily {len(out["daily"][0])}/{out["daily"][2]}, Weekly {len(out["weekly"][0])}/{out["weekly"][2]})')
    print(md)
    print(readme)


def publish():
    day = json.loads(RAW.read_text(encoding="utf-8"))["date"]
    files = [f"{day[:7]}/github_trending_{day}.html", f"{day[:7]}/github_trending_{day}.md", "README.md"]
    git = ["git", "-C", str(OUT_DIR)]
    subprocess.run([*git, "add", "--", *files], check=True)
    if subprocess.run([*git, "diff", "--cached", "--quiet", "--", *files]).returncode == 0:
        print("변경 사항이 없어 커밋은 건너뜁니다.")
    else:
        message = f"{day}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
        subprocess.run([*git, "commit", "-m", message, "--", *files], check=True)
    subprocess.run([*git, "push"], check=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    {"fetch": fetch, "render": render, "publish": publish}[sys.argv[1]]()
