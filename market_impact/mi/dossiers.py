"""Fetch compact screener.in dossiers per company (no LLM).

Run: python3 -m market_impact.mi.dossiers  → data/dossiers/<SYMBOL>.md
"""
import csv
import os
import re
import sys
import time
import urllib.request

from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"}


def get(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode("utf-8", "ignore")
    except Exception:
        return None


def table_rows(soup, sec_id, keep=("Sales", "Revenue", "Operating Profit", "OPM", "Net Profit", "EPS", "Financing Profit", "Interest", "Expenses"), last=6):
    sec = soup.find("section", id=sec_id)
    if not sec or not sec.find("table"):
        return ""
    t = sec.find("table")
    head = [th.get_text(" ", strip=True) for th in t.find("thead").find_all("th")] if t.find("thead") else []
    out = []
    if head:
        out.append(" | ".join(["item"] + head[-last:]))
    for tr in t.find("tbody").find_all("tr"):
        cells = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
        if cells and any(cells[0].startswith(k) for k in keep):
            out.append(" | ".join([cells[0].replace("+", "").strip()] + cells[-last:]))
    return "\n".join(out)


def dossier(sym, name):
    html = get(f"https://www.screener.in/company/{sym}/consolidated/")
    if not html or "top-ratios" not in html:
        html = get(f"https://www.screener.in/company/{sym}/")
    if not html:
        return None
    s = BeautifulSoup(html, "lxml")
    about = s.select_one("div.about") or s.select_one("div.company-profile")
    about = re.sub(r"\s+", " ", about.get_text(" ", strip=True))[:1500] if about else ""
    kr = s.select_one("div.sub.show-more-box") or s.select_one(".commentary")
    ratios = []
    for li in s.select("ul#top-ratios li"):
        n = li.select_one(".name"); v = li.select_one(".value")
        if n and v:
            val = re.sub(r"\s+", " ", v.get_text(" ", strip=True))
            ratios.append(n.get_text(strip=True) + ": " + val)
    pros = [li.get_text(" ", strip=True) for li in s.select("div.pros li")][:5]
    cons = [li.get_text(" ", strip=True) for li in s.select("div.cons li")][:5]
    md = [f"# {sym} — {name}", f"Source: screener.in (retrieved by script; figures in INR crore unless stated)", "",
          "## About", about, "", "## Key ratios", "; ".join(ratios), ""]
    if pros or cons:
        md += ["## Screener pros/cons (machine-generated)", "Pros: " + " / ".join(pros), "Cons: " + " / ".join(cons), ""]
    q = table_rows(s, "quarters")
    if q:
        md += ["## Quarterly results (last 6)", q, ""]
    p = table_rows(s, "profit-loss")
    if p:
        md += ["## Annual P&L (last 6)", p, ""]
    sh = table_rows(s, "shareholding", keep=("Promoters", "FIIs", "DIIs", "Government", "Public"), last=3)
    if sh:
        md += ["## Shareholding % (last 3 quarters)", sh, ""]
    return "\n".join(md)


def main():
    uni = list(csv.DictReader(open(os.path.join(HERE, "data", "raw", "nifty200.csv"))))
    only = set(sys.argv[1:])
    ok = fail = 0
    for r in uni:
        sym = r["Symbol"]
        if only and sym not in only:
            continue
        path = os.path.join(HERE, "data", "dossiers", f"{sym}.md")
        if os.path.exists(path) and os.path.getsize(path) > 500:
            ok += 1
            continue
        md = dossier(sym, r["Company Name"])
        if md:
            open(path, "w").write(md)
            ok += 1
        else:
            fail += 1
        time.sleep(2.0)
    print({"ok": ok, "fail": fail})


if __name__ == "__main__":
    main()
