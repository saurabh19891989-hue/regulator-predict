"""Automatic leakage lint. Errors block a thread; warnings go to the human/LLM auditor."""
import re
from .common import d

OUTCOME_WORDS = [
    r"\bfinali[sz]ed\b", r"\bfinal rule\b", r"\badopted\b", r"\bapproved\b", r"\bnotified\b",
    r"\bwithdrawn\b", r"\bwithdrew\b", r"\bshelved\b", r"\babandoned\b", r"\blater\b", r"\beventually\b",
    r"\bsubsequently\b", r"\bwent on to\b", r"\bwhich led to\b", r"\bcame into (force|effect)\b",
    r"\brescinded\b", r"\bimplemented\b", r"\bin hindsight\b", r"\bultimately\b",
]
RETRO_WORDS = [r"\blater\b", r"\beventually\b", r"\bsubsequently\b", r"\bwent on to\b", r"\bwhich led to\b",
               r"\bultimately\b", r"\bin hindsight\b", r"\bwould later\b", r"\bwas later\b"]
MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec"
MNUM = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                       "september", "october", "november", "december"], 1)}
MNUM.update({"jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "sept": 9,
             "oct": 10, "nov": 11, "dec": 12})


def mentioned_dates(text):
    """Return (year, month) tuples mentioned in text (month may be None)."""
    out = []
    for m in re.finditer(r"\b(20\d\d)-(\d\d)-(\d\d)\b", text):
        out.append((int(m.group(1)), int(m.group(2))))
    for m in re.finditer(rf"\b({MONTHS})\.?\s+(\d{{1,2}},?\s+)?(20\d\d)\b", text, re.I):
        out.append((int(m.group(3)), MNUM[m.group(1).lower().rstrip('.')]))
    for m in re.finditer(rf"\b\d{{1,2}}\s+({MONTHS})\.?,?\s+(20\d\d)\b", text, re.I):
        out.append((int(m.group(2)), MNUM[m.group(1).lower().rstrip('.')]))
    for m in re.finditer(r"\b(20\d\d)\b", text):
        out.append((int(m.group(1)), None))
    return out


def future_mentions(text, pub_date):
    pd = d(pub_date)
    fut = []
    for y, mth in mentioned_dates(text):
        if mth is None:
            if y > pd.year:
                fut.append(str(y))
        elif (y, mth) > (pd.year, pd.month):
            fut.append(f"{y}-{mth:02d}")
    return sorted(set(fut))


def lint_thread_text(thread):
    issues = []
    txt = f"{thread.get('neutral_title','')} || {thread.get('issue_summary_neutral','')}"
    for w in OUTCOME_WORDS:
        if re.search(w, txt, re.I):
            issues.append(("warning", f"thread text contains outcome-suggestive word /{w}/"))
    fut = future_mentions(txt, thread["anchor_date"])
    if fut:
        issues.append(("warning", f"thread text mentions dates after anchor date: {fut}"))
    return issues


def lint_evidence(ev, outcome=None):
    issues = []
    txt = " ".join(ev.get("extracted_claims", [])) + " " + ev.get("content_excerpt", "") + " " + ev.get("title", "")
    for w in RETRO_WORDS:
        if re.search(w, txt, re.I):
            issues.append(("warning", f"retrospective wording /{w}/"))
    fut = future_mentions(txt, ev["publication_date"])
    if fut:
        issues.append(("warning", f"mentions dates after publication ({fut}) — legitimate only if proposed/projected dates"))
    fk = ev.get("first_known_date")
    if fk and d(fk) < d(ev["publication_date"]):
        issues.append(("warning", "first_known_date earlier than publication_date"))
    if outcome:
        dd = outcome.get("decisive_date")
        wd = outcome.get("withdrawal_date")
        if dd and d(ev["publication_date"]) >= d(dd):
            issues.append(("error", f"evidence published on/after decisive date {dd}: belongs in outcome store"))
        if wd and d(ev["publication_date"]) >= d(wd):
            issues.append(("error", f"evidence published on/after withdrawal date {wd}"))
        dt = (outcome.get("decisive_document_title") or "").strip().lower()
        if dt and len(dt) > 12 and dt == ev.get("title", "").strip().lower():
            issues.append(("error", "evidence title equals decisive document title"))
        du = (outcome.get("decisive_document_url") or "").strip()
        if du and du == ev.get("source_url", "").strip():
            issues.append(("error", "evidence URL equals decisive document URL"))
    if d(ev["publication_date"]) > d(ev["retrieval_date"]):
        issues.append(("error", "publication_date after retrieval_date"))
    return issues


def lint_outcome(o, thread):
    issues = []
    act = o["decisive_action"]
    if act and not o.get("decisive_date"):
        issues.append(("error", "decisive_action true but no decisive_date"))
    if not act and o.get("decisive_date"):
        issues.append(("error", "decisive_action false but decisive_date set"))
    cls = o["outcome_class"]
    if cls.startswith("action_") != bool(act):
        issues.append(("error", f"outcome_class {cls} inconsistent with decisive_action={act}"))
    if cls == "withdrawn" and not o.get("withdrawal_date"):
        issues.append(("warning", "withdrawn without withdrawal_date"))
    if (o["content_direction"] == "na") == bool(act):
        issues.append(("error", "content_direction must be 'na' iff no action"))
    if o.get("decisive_date"):
        if d(o["decisive_date"]) <= d(thread["anchor_date"]):
            issues.append(("error", "decisive_date not after anchor_date"))
        if d(o["decisive_date"]) > d(o["censor_date"]):
            issues.append(("error", "decisive_date after censor_date"))
    return issues
