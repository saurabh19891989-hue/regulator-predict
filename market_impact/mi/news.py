"""Google News RSS headlines per company (last 60 days). No LLM.

Run: python3 -m market_impact.mi.news  → data/news/<SYMBOL>.json
"""
import csv
import json
import os
import re
import time
import urllib.parse
import urllib.request
from email.utils import parsedate_to_datetime

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0"}


def short(name):
    n = re.sub(r"\b(Ltd\.?|Limited|India|Industries|Company|Corporation|Corp\.?)\b", "", name, flags=re.I)
    return re.sub(r"\s+", " ", n).strip(" .&") or name


def headlines(q, days=60, n=20):
    u = "https://news.google.com/rss/search?q=" + urllib.parse.quote(f"{q} when:{days}d") + "&hl=en-IN&gl=IN&ceid=IN:en"
    try:
        x = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    except Exception:
        return []
    out = []
    for it in re.findall(r"<item>(.*?)</item>", x, re.S)[:n]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it)
        src = re.search(r"<source[^>]*>(.*?)</source>", it)
        try:
            dt = parsedate_to_datetime(d.group(1)).date().isoformat() if d else None
        except Exception:
            dt = None
        out.append({"date": dt, "title": re.sub(r"&amp;", "&", t.group(1)) if t else "", "source": src.group(1) if src else ""})
    return sorted(out, key=lambda z: z["date"] or "", reverse=True)


def main():
    uni = list(csv.DictReader(open(os.path.join(HERE, "data", "raw", "nifty200.csv"))))
    for r in uni:
        path = os.path.join(HERE, "data", "news", f"{r['Symbol']}.json")
        if os.path.exists(path):
            continue
        q = f"\"{short(r['Company Name'])}\" share OR stock OR results OR shares"
        json.dump({"query": q, "items": headlines(q)}, open(path, "w"), indent=1)
        time.sleep(1.0)
    print("done", len(os.listdir(os.path.join(HERE, "data", "news"))))


if __name__ == "__main__":
    main()
