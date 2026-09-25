"""No-LLM baselines on cutoff-valid structured features (pre-registered 2026-09-25, before results).

All fitted baselines use thread-grouped K-fold CV: a thread's own snapshots never train its prediction.
Heuristic rules below are FIXED (written before any forecast/outcome was examined) — do not tune.
"""
import math
import re
from collections import defaultdict

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold

from .common import add_days, d, days_between
from .snapshots import available_date

HORIZONS = [7, 30, 60, 90, 180]
ELAPSED_BUCKETS = [0, 90, 180, 365, 730, 10 ** 6]
AGENDA_RE = re.compile(r"final\s+(?:rule|action)[^0-9]{0,40}?(\d{1,2})/(\d{1,2})/(\d{4})", re.I)
COUNT_RE = re.compile(r"(\d[\d,]*)\s+(?:public\s+)?comments?", re.I)


def features(thread, items, cutoff):
    """items: ALL-class evidence visible at cutoff (already filtered)."""
    c = cutoff
    n = defaultdict(int)
    for e in items:
        n[e["tier"]] += 1
    official = [e for e in items if e["tier"] in ("B", "C")]
    latest = max((available_date(e) for e in official), default=thread["anchor_date"])
    since_anchor = max(0, days_between(thread["anchor_date"], c))
    followup_b = sum(1 for e in items if e["tier"] == "B" and d(available_date(e)) > d(thread["anchor_date"])
                     and e["document_type"] not in ("regulatory_agenda_entry", "oira_review_received", "oira_review_concluded"))
    oira_final = any(e["document_type"] in ("oira_review_received", "oira_review_concluded")
                     and re.search(r"Stage:\s*(Interim\s+)?Final", e.get("content_excerpt", ""), re.I) for e in items)
    agenda = sorted([e for e in items if e["document_type"] == "regulatory_agenda_entry"], key=available_date)
    ag_within, ag_long, ag_any = 0, 0, 0
    if agenda:
        ag_any = 1
        txt = agenda[-1].get("content_excerpt", "")
        if re.search(r"long[- ]term", txt, re.I):
            ag_long = 1
        m = AGENDA_RE.search(txt)
        if m:
            mm, yy = int(m.group(1)), int(m.group(3))
            if 1 <= mm <= 12:
                proj = f"{yy:04d}-{mm:02d}-28"
                if d(c) < d(proj) <= d(add_days(c, 180)) or (d(proj) <= d(c)):
                    ag_within = 1   # projected date inside horizon, or already overdue
    cc = 0
    for e in items:
        if e["tier"] == "S":
            m = COUNT_RE.search(e.get("content_excerpt", "") + " " + e.get("title", ""))
            if m:
                cc = max(cc, int(m.group(1).replace(",", "")))
    recent_soft = sum(1 for e in items if e["tier"] in ("C", "D") and days_between(available_date(e), c) <= 60)
    return {
        "family": thread["family"], "since_anchor": since_anchor, "log_since_anchor": math.log1p(since_anchor),
        "since_latest": max(0, days_between(latest, c)), "nB": n["B"], "nC": n["C"], "nS": n["S"], "nD": n["D"],
        "followup_b": followup_b, "oira_final": int(oira_final), "agenda_any": ag_any, "agenda_within": ag_within,
        "agenda_long": ag_long, "log_comments": math.log1p(cc), "recent_soft": recent_soft,
    }


def heuristic_p180(f):
    """FIXED rule-based recency/deadline heuristic (pre-registered)."""
    if f["family"].startswith("US-FR"):
        if f["oira_final"]:
            return 0.85
        if f["agenda_within"]:
            return 0.55
        if f["agenda_long"]:
            return 0.10
        return 0.45 if f["since_anchor"] <= 365 else 0.20
    p = 0.55 if f["since_anchor"] <= 180 else (0.35 if f["since_anchor"] <= 365 else 0.15)
    if f["recent_soft"] > 0:
        p += 0.15
    if f["followup_b"] > 0:
        p += 0.05
    return min(p, 0.9)


def heuristic(f, h):
    return heuristic_p180(f) * min(1.0, h / 180.0)


def _bucket(x):
    for i in range(len(ELAPSED_BUCKETS) - 1):
        if ELAPSED_BUCKETS[i] <= x < ELAPSED_BUCKETS[i + 1]:
            return i
    return len(ELAPSED_BUCKETS) - 2


def _stage(f):
    if f["oira_final"]:
        return "final_review"
    if f["followup_b"] > 0:
        return "followup"
    return "proposal"


def grouped_rate(rows, keyfn, h, folds=5, alpha=1.0):
    """rows: dicts with 'thread_id','f','y'(label dict). Returns {row_index: p}."""
    idx = [i for i, r in enumerate(rows) if r["y"].get(str(h)) is not None]
    groups = [rows[i]["thread_id"] for i in idx]
    out = {}
    if len(set(groups)) < folds:
        return out
    for tr, te in GroupKFold(n_splits=folds).split(idx, groups=groups):
        tri = [idx[j] for j in tr]
        prior = np.mean([rows[i]["y"][str(h)] for i in tri]) if tri else 0.5
        cnt = defaultdict(lambda: [0.0, 0.0])
        for i in tri:
            k = keyfn(rows[i]["f"])
            cnt[k][0] += rows[i]["y"][str(h)]
            cnt[k][1] += 1
        for j in te:
            i = idx[j]
            s, n = cnt[keyfn(rows[i]["f"])]
            out[i] = (s + alpha * prior) / (n + alpha)
    return out


NUM = ["log_since_anchor", "since_latest", "nB", "nC", "nS", "nD", "followup_b", "oira_final", "agenda_any",
       "agenda_within", "agenda_long", "log_comments", "recent_soft"]


def _X(rows, fams):
    X = []
    for r in rows:
        f = r["f"]
        v = [f[k] for k in NUM]
        v[1] = math.log1p(v[1])
        v += [1.0 if f["family"] == fm else 0.0 for fm in fams]
        X.append(v)
    return np.array(X, dtype=float)


def grouped_logit(rows, h, folds=5):
    idx = [i for i, r in enumerate(rows) if r["y"].get(str(h)) is not None]
    groups = [rows[i]["thread_id"] for i in idx]
    out = {}
    if len(set(groups)) < folds:
        return out
    fams = sorted({r["f"]["family"] for r in rows})
    X = _X([rows[i] for i in idx], fams)
    y = np.array([rows[i]["y"][str(h)] for i in idx])
    mu, sd = X.mean(0), X.std(0) + 1e-9
    X = (X - mu) / sd
    for tr, te in GroupKFold(n_splits=folds).split(X, y, groups):
        if len(set(y[tr])) < 2:
            p = np.full(len(te), y[tr].mean() if len(tr) else 0.5)
        else:
            m = LogisticRegression(C=0.5, max_iter=2000).fit(X[tr], y[tr])
            p = m.predict_proba(X[te])[:, 1]
        for j, pj in zip(te, p):
            out[idx[j]] = float(pj)
    return out


def all_baselines(rows):
    """Return {baseline_name: {h: {row_index: p}}}."""
    res = {"base_rate_elapsed": {}, "stage_transition": {}, "heuristic": {}, "logit_features": {}}
    for h in HORIZONS:
        res["base_rate_elapsed"][h] = grouped_rate(rows, lambda f: (f["family"], _bucket(f["since_anchor"])), h)
        res["stage_transition"][h] = grouped_rate(rows, lambda f: (f["family"], _stage(f)), h)
        res["heuristic"][h] = {i: heuristic(r["f"], h) for i, r in enumerate(rows) if r["y"].get(str(h)) is not None}
        res["logit_features"][h] = grouped_logit(rows, h)
    return res
