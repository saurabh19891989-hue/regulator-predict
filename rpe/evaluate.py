"""Evaluator: joins frozen forecasts (ledger) with sealed labels and computes pre-registered metrics.

Usage: python3 -m rpe.evaluate [--primary-runs R1,R2] [--ablation-runs R3,...] [--title-runs R4] [--probe probe.jsonl]
Writes reports/metrics.json and reports/METRICS.md
"""
import argparse
import json
import math
import os
from collections import defaultdict

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score

from .baselines import HORIZONS, all_baselines, features
from .common import DATA, ROOT, read_jsonl
from .ledger import CONTENT, LEDGER
from .snapshots import select_items

RNG = np.random.default_rng(20260925)
K_H = {"K@2026-06-26": 90, "K@2026-07-26": 60, "K@2026-08-25": 30}


# ---------------------------------------------------------------- metrics
def brier(p, y):
    p, y = np.asarray(p, float), np.asarray(y, float)
    return float(np.mean((p - y) ** 2)) if len(y) else float("nan")


def logloss(p, y, eps=1e-3):
    p = np.clip(np.asarray(p, float), eps, 1 - eps)
    y = np.asarray(y, float)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))) if len(y) else float("nan")


def auroc(p, y):
    return float(roc_auc_score(y, p)) if len(set(y)) == 2 else float("nan")


def auprc(p, y):
    return float(average_precision_score(y, p)) if len(set(y)) == 2 else float("nan")


def ece(p, y, bins=10):
    p, y = np.asarray(p, float), np.asarray(y, float)
    if not len(y):
        return float("nan")
    b = np.minimum((p * bins).astype(int), bins - 1)
    return float(sum(abs(p[b == i].mean() - y[b == i].mean()) * (b == i).mean() for i in range(bins) if (b == i).any()))


def cal_slope(p, y):
    p = np.clip(np.asarray(p, float), 1e-3, 1 - 1e-3)
    y = np.asarray(y, float)
    if len(set(y)) < 2:
        return float("nan"), float("nan")
    x = np.log(p / (1 - p))
    w = np.array([0.0, 1.0])
    for _ in range(50):  # Newton-Raphson logistic regression y ~ a + b*x
        z = w[0] + w[1] * x
        mu = 1 / (1 + np.exp(-z))
        g = np.array([np.sum(y - mu), np.sum((y - mu) * x)])
        Wd = mu * (1 - mu)
        Hm = -np.array([[Wd.sum(), (Wd * x).sum()], [(Wd * x).sum(), (Wd * x * x).sum()]])
        try:
            w = w - np.linalg.solve(Hm, g)
        except np.linalg.LinAlgError:
            break
    return float(w[1]), float(w[0])


def reliability(p, y, bins=5):
    p, y = np.asarray(p, float), np.asarray(y, float)
    edges = np.linspace(0, 1, bins + 1)
    out = []
    for i in range(bins):
        m = (p >= edges[i]) & ((p < edges[i + 1]) if i < bins - 1 else (p <= 1))
        if m.any():
            out.append({"bin": f"{edges[i]:.1f}-{edges[i+1]:.1f}", "n": int(m.sum()), "mean_p": float(p[m].mean()),
                        "obs_rate": float(y[m].mean())})
    return out


def prec_rec(p, y, th):
    p, y = np.asarray(p, float), np.asarray(y, int)
    pos = p >= th
    tp = int(((y == 1) & pos).sum())
    return {"threshold": th, "flagged": int(pos.sum()), "precision": (tp / pos.sum()) if pos.sum() else float("nan"),
            "recall": (tp / (y == 1).sum()) if (y == 1).sum() else float("nan")}


def summary(p, y):
    s, i = cal_slope(p, y)
    return {"n": len(y), "base_rate": float(np.mean(y)) if len(y) else float("nan"), "brier": brier(p, y),
            "logloss": logloss(p, y), "auroc": auroc(p, y), "auprc": auprc(p, y), "ece": ece(p, y),
            "cal_slope": s, "cal_intercept": i, "mean_p": float(np.mean(p)) if len(p) else float("nan"),
            "prec_rec": [prec_rec(p, y, t) for t in (0.5, 0.7, 0.8)]}


def boot(groups, stat, reps=2000):
    """Thread-clustered bootstrap. stat(indices)->float. Returns (point, lo5, hi95)."""
    groups = np.asarray(groups)
    ug = np.unique(groups)
    by = {g: np.where(groups == g)[0] for g in ug}
    point = stat(np.arange(len(groups)))
    vals = []
    for _ in range(reps):
        pick = RNG.choice(ug, size=len(ug), replace=True)
        ix = np.concatenate([by[g] for g in pick])
        v = stat(ix)
        if not math.isnan(v):
            vals.append(v)
    if not vals:
        return point, float("nan"), float("nan")
    return point, float(np.percentile(vals, 5)), float(np.percentile(vals, 95))


# ---------------------------------------------------------------- data
def load(runs=None):
    idx = {r["snapshot_id"]: r for r in read_jsonl(os.path.join(DATA, "snapshots", "index.jsonl"))}
    rows = []
    for r in read_jsonl(LEDGER):
        if runs and r["run"] not in runs:
            continue
        s = idx.get(r["snapshot_id"])
        if s is None:
            continue
        rows.append({**s, "run": r["run"], "model": r["model"], "fc": r["forecast"]})
    return rows, idx


def horizon_for(row, h):
    if row["design"] == "K":
        return K_H[row["offset"]] if h == "K" else h
    return h


def feature_rows(idx):
    """Feature rows for every available ALL-arm snapshot (baselines are arm-independent)."""
    threads = {t["thread_id"]: t for t in read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))}
    ev = defaultdict(list)
    for e in read_jsonl(os.path.join(DATA, "evidence", "evidence.jsonl")):
        ev[e["thread_id"]].append(e)
    rows = []
    for s in idx.values():
        if s["arm"] != "ALL" or not s["available"]:
            continue
        items, _, _, _ = select_items(ev[s["thread_id"]], "ALL", s["cutoff_date"])
        rows.append({"snapshot_id": s["snapshot_id"], "thread_id": s["thread_id"], "cutoff_date": s["cutoff_date"],
                     "f": features(threads[s["thread_id"]], items, s["cutoff_date"]), "y": s["labels"]})
    return rows


def baseline_lookup(idx):
    frows = feature_rows(idx)
    bl = all_baselines(frows)
    look = defaultdict(dict)   # (thread, cutoff) -> {name: {h: p}}
    for name, per_h in bl.items():
        for h, mp in per_h.items():
            for i, p in mp.items():
                r = frows[i]
                look[(r["thread_id"], r["cutoff_date"])].setdefault(name, {})[h] = p
    return look, frows


# ---------------------------------------------------------------- analyses
def action_block(rows, look, h, label):
    """LLM vs baselines on the same snapshots for horizon h (K rows use their own horizon if h=='K')."""
    data = []
    for r in rows:
        hh = horizon_for(r, h) if h == "K" else h
        y = r["labels"].get(str(hh))
        if y is None:
            continue
        p = r["fc"]["timing"][f"{hh}d"]
        b = look.get((r["thread_id"], r["cutoff_date"]), {})
        data.append((r["thread_id"], y, p, {n: v.get(hh) for n, v in b.items()}))
    if not data:
        return {"label": label, "n": 0}
    g = [x[0] for x in data]
    y = np.array([x[1] for x in data])
    p = np.array([x[2] for x in data])
    out = {"label": label, "horizon": h, "llm": summary(p, y), "threads": len(set(g)), "baselines": {}}
    best, best_b = None, 1e9
    for name in ("base_rate_elapsed", "stage_transition", "heuristic", "logit_features"):
        m = [i for i, x in enumerate(data) if x[3].get(name) is not None]
        if len(m) < max(10, 0.8 * len(data)):
            continue
        bp = np.array([data[i][3][name] for i in m])
        yy, pp, gg = y[m], p[m], [g[i] for i in m]
        bs = summary(bp, yy)
        bss = boot(gg, lambda ix: 1 - brier(pp[ix], yy[ix]) / brier(bp[ix], yy[ix]) if brier(bp[ix], yy[ix]) > 0 else float("nan"))
        dauc = boot(gg, lambda ix: auroc(pp[ix], yy[ix]) - auroc(bp[ix], yy[ix]))
        bs["llm_brier_skill_vs_this"] = bss
        bs["llm_auroc_minus_this"] = dauc
        out["baselines"][name] = bs
        if bs["brier"] < best_b:
            best, best_b = name, bs["brier"]
    out["best_baseline"] = best
    out["llm_auroc_ci"] = boot(g, lambda ix: auroc(p[ix], y[ix]))
    return out


def paired_arms(rows, arm_a, arm_b, h=180, restrict=None):
    """ΔBrier (a − b) on snapshots available in both arms (same model/run family)."""
    A = {(r["thread_id"], r["cutoff_date"]): r for r in rows if r["arm"] == arm_a}
    B = {(r["thread_id"], r["cutoff_date"]): r for r in rows if r["arm"] == arm_b}
    keys = [k for k in A if k in B and A[k]["labels"].get(str(h)) is not None]
    if restrict:
        keys = [k for k in keys if restrict(A[k])]
    if len(keys) < 5:
        return {"a": arm_a, "b": arm_b, "n": len(keys)}
    y = np.array([A[k]["labels"][str(h)] for k in keys])
    pa = np.array([A[k]["fc"]["timing"][f"{h}d"] for k in keys])
    pb = np.array([B[k]["fc"]["timing"][f"{h}d"] for k in keys])
    g = [k[0] for k in keys]
    return {"a": arm_a, "b": arm_b, "n": len(keys), "threads": len(set(g)), "brier_a": brier(pa, y),
            "brier_b": brier(pb, y), "delta_brier_a_minus_b": boot(g, lambda ix: brier(pa[ix], y[ix]) - brier(pb[ix], y[ix])),
            "auroc_a": auroc(pa, y), "auroc_b": auroc(pb, y),
            "delta_logloss": boot(g, lambda ix: logloss(pa[ix], y[ix]) - logloss(pb[ix], y[ix]))}


def lead_time(rows):
    """Design-T, horizon 180. Earliest k<=180 with p>=θ; precision over all T snapshots with 180d label."""
    T = [r for r in rows if r["design"] == "T" and r["labels"].get("180") is not None]
    p = np.array([r["fc"]["action_probability_180d"] for r in T])
    y = np.array([r["labels"]["180"] for r in T])
    by_thread = defaultdict(list)
    for r in T:
        if not r["is_pseudo_anchor"]:
            by_thread[r["thread_id"]].append((int(r["offset"].split("-")[1]), r["fc"]["action_probability_180d"]))
    res = {"thresholds": []}
    for th in [round(x, 2) for x in np.arange(0.3, 0.96, 0.05)]:
        pr = prec_rec(p, y, th)
        leads, persist = [], []
        for tid, lst in by_thread.items():
            lst = sorted([x for x in lst if x[0] <= 180], reverse=True)
            if not lst:
                continue
            first = next((k for k, pp in lst if pp >= th), 0)
            leads.append(first)
            per = 0
            for k, pp in lst:  # largest k from which all later cutoffs stay >= th
                if all(q >= th for kk, q in lst if kk <= k):
                    per = k
                    break
            persist.append(per)
        res["thresholds"].append({**pr, "positives": len(leads),
                                  "detected_share": float(np.mean([x > 0 for x in leads])) if leads else float("nan"),
                                  "median_lead_days_first_cross": float(np.median(leads)) if leads else float("nan"),
                                  "median_lead_days_persistent": float(np.median(persist)) if persist else float("nan")})
    ok = [t for t in res["thresholds"] if not math.isnan(t["precision"]) and t["precision"] >= 0.8 and t["flagged"] >= 5]
    res["at_precision_0.8"] = ok[0] if ok else None
    return res


def content_block(rows, outcomes):
    """content_direction for positives: model vs leave-one-thread-out base-rate distribution."""
    om = {o["thread_id"]: o for o in outcomes}
    pos = [r for r in rows if om[r["thread_id"]]["decisive_action"] and om[r["thread_id"]]["content_direction"] in CONTENT
           and om[r["thread_id"]].get("content_label_confidence", "medium") != "low"]
    if len(pos) < 5:
        return {"n": len(pos)}
    thr = sorted({r["thread_id"] for r in pos})
    lab = {t: om[t]["content_direction"] for t in thr}
    tot = defaultdict(int)
    for t in thr:
        tot[lab[t]] += 1
    rows_out, mb, bb, acc_m, acc_b, g = [], [], [], [], [], []
    for r in pos:
        t = r["thread_id"]
        onehot = np.array([1.0 if c == lab[t] else 0.0 for c in CONTENT])
        pm = np.array([r["fc"]["content_direction_probs"][c] for c in CONTENT])
        loo = np.array([(tot[c] - (1 if lab[t] == c else 0) + 0.5) for c in CONTENT])
        loo = loo / loo.sum()
        mb.append(np.sum((pm - onehot) ** 2))
        bb.append(np.sum((loo - onehot) ** 2))
        acc_m.append(float(CONTENT[int(pm.argmax())] == lab[t]))
        acc_b.append(float(CONTENT[int(loo.argmax())] == lab[t]))
        g.append(t)
    mb, bb, acc_m, acc_b = map(np.array, (mb, bb, acc_m, acc_b))
    return {"n_snapshots": len(pos), "threads": len(thr), "label_dist": dict(tot),
            "model_multiclass_brier": float(mb.mean()), "baserate_multiclass_brier": float(bb.mean()),
            "brier_skill": boot(g, lambda ix: 1 - mb[ix].mean() / bb[ix].mean()),
            "model_top1": float(acc_m.mean()), "baserate_top1": float(acc_b.mean()),
            "top1_gain": boot(g, lambda ix: acc_m[ix].mean() - acc_b[ix].mean())}


def run_eval(primary, ablation, title, probe_path=None, extra_filters=None):
    rows_all, idx = load()
    look, frows = baseline_lookup(idx)
    outcomes = read_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"))
    P = [r for r in rows_all if r["run"] in primary]
    res = {"primary_runs": primary, "n_primary_forecasts": len(P)}
    recog = set()
    if probe_path and os.path.exists(probe_path):
        for x in read_jsonl(probe_path):
            if x.get("recalled_correctly"):
                recog.add(x["thread_id"])
    res["probe_recalled_threads"] = len(recog)

    def sub(fn):
        return [r for r in P if fn(r)]
    blocks = {}
    blocks["HIST_T_180"] = action_block(sub(lambda r: r["stratum"] == "HIST" and r["design"] == "T"), look, 180, "HIST design-T 180d")
    blocks["ALL_T_180"] = action_block(sub(lambda r: r["design"] == "T"), look, 180, "All strata design-T 180d")
    blocks["CLEAN_K"] = action_block(sub(lambda r: r["design"] == "K"), look, "K", "CLEAN design-K (horizon to censor)")
    blocks["CLEAN_T_short"] = action_block(sub(lambda r: r["stratum"] == "CLEAN" and r["clean_snapshot"] and r["design"] == "T"), look, 30, "CLEAN post-cutoff design-T 30d")
    for fam in sorted({r["family"] for r in P}):
        blocks[f"FAM_{fam}_T_180"] = action_block(sub(lambda r, fam=fam: r["family"] == fam and r["design"] == "T"), look, 180, f"{fam} design-T 180d")
    blocks["US_T_180"] = action_block(sub(lambda r: r["family"].startswith("US") and r["design"] == "T"), look, 180, "US design-T 180d")
    blocks["IN_T_180"] = action_block(sub(lambda r: r["family"].startswith("IN") and r["design"] == "T"), look, 180, "India design-T 180d")
    blocks["HIST_T_180_not_selfrecognised"] = action_block(sub(lambda r: r["stratum"] == "HIST" and r["design"] == "T" and not r["fc"]["recognised_outcome"]), look, 180, "HIST T 180d excluding self-recognised")
    if recog:
        blocks["HIST_T_180_not_probe_recalled"] = action_block(sub(lambda r: r["stratum"] == "HIST" and r["design"] == "T" and r["thread_id"] not in recog), look, 180, "HIST T 180d excluding probe-recalled threads")
    if extra_filters:
        for name, fn in extra_filters.items():
            blocks[name] = action_block(sub(fn), look, 180, name)
    res["action"] = blocks
    # timing calibration per horizon (design T, all strata; K rows at their horizon)
    tim = {}
    for h in HORIZONS:
        d_ = [(r["fc"]["timing"][f"{h}d"], r["labels"][str(h)], r["thread_id"]) for r in P if r["design"] == "T" and r["labels"].get(str(h)) is not None]
        if d_:
            p, y = np.array([x[0] for x in d_]), np.array([x[1] for x in d_])
            tim[f"{h}d"] = {**summary(p, y), "reliability": reliability(p, y)}
    res["timing"] = tim
    res["lead_time"] = lead_time([r for r in P if r["arm"] == "ALL"])
    res["content"] = content_block([r for r in P if r["design"] == "T"], outcomes)
    res["content_CLEAN"] = content_block([r for r in P if r["stratum"] == "CLEAN"], outcomes)
    res["recognition"] = {"self_recognised_share": float(np.mean([r["fc"]["recognised_outcome"] for r in P])) if P else float("nan"),
                          "insufficient_share": float(np.mean([r["fc"]["insufficient_evidence"] for r in P])) if P else float("nan")}
    # same-model TITLE_ONLY control
    if title:
        TT = [r for r in rows_all if r["run"] in title] + [r for r in P]
        res["title_only_control"] = {
            "ALL_vs_TITLE_HIST": paired_arms([r for r in TT if r["stratum"] == "HIST" and r["design"] == "T"], "ALL", "TITLE_ONLY", 180),
            "ALL_vs_TITLE_all_T": paired_arms([r for r in TT if r["design"] == "T"], "ALL", "TITLE_ONLY", 180),
            "ALL_vs_TITLE_CLEAN_K": paired_arms([dict(r, labels={"180": r["labels"].get(str(K_H[r["offset"]]))}, fc=dict(r["fc"], timing={**r["fc"]["timing"], "180d": r["fc"]["timing"][f"{K_H[r['offset']]}d"]})) for r in TT if r["design"] == "K"], "ALL", "TITLE_ONLY", 180),
        }
    # ablations (single model)
    if ablation:
        A = [r for r in rows_all if r["run"] in ablation]
        abl = {}
        pairs = [("B_PLUS_C", "B_ONLY", "tierC_increment"), ("C_ONLY", "B_ONLY", "C_alone_vs_B_alone"),
                 ("B_C_STAKEHOLDERS", "B_PLUS_C", "stakeholder_increment"),
                 ("B_C_STAKEHOLDERS_PLUS_NEWS", "B_C_STAKEHOLDERS", "news_increment_over_BCS"),
                 ("B_C_STAKEHOLDERS_PLUS_NEWS", "B_PLUS_C", "news_plus_stakeholder_increment_over_BC"),
                 ("B_PLUS_C", "LATEST_DOCUMENT_ONLY", "full_trajectory_vs_latest_only"),
                 ("ALL", "TITLE_ONLY", "evidence_vs_title_only"), ("B_ONLY", "TITLE_ONLY", "B_vs_title_only"),
                 ("C_ONLY", "TITLE_ONLY", "C_vs_title_only")]
        for a, b, name in pairs:
            abl[name] = paired_arms([r for r in A if r["design"] == "T"], a, b, 180)
            abl[name + "_30d"] = paired_arms([r for r in A if r["design"] == "T"], a, b, 30)
        arm_sum = {}
        for arm in sorted({r["arm"] for r in A}):
            d_ = [(r["fc"]["action_probability_180d"], r["labels"]["180"]) for r in A if r["arm"] == arm and r["design"] == "T" and r["labels"].get("180") is not None]
            if d_:
                arm_sum[arm] = summary(np.array([x[0] for x in d_]), np.array([x[1] for x in d_]))
        abl["per_arm"] = arm_sum
        res["ablation"] = abl
    return res


def fmt(x):
    if isinstance(x, (list, tuple)) and len(x) == 3:
        return f"{x[0]:.3f} [{x[1]:.3f}, {x[2]:.3f}]"
    if isinstance(x, float):
        return f"{x:.3f}"
    return str(x)


def write_md(res, path):
    L = ["# METRICS (auto-generated by rpe.evaluate — do not edit by hand)", ""]
    L.append("## Action prediction (LLM ALL-arm vs no-LLM baselines)")
    L.append("| block | n | thr | base rate | LLM Brier | LLM AUROC [90% CI] | best baseline | its Brier | its AUROC | BSS vs best [90% CI] |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for k, b in res["action"].items():
        if not b.get("llm"):
            continue
        bb = b["baselines"].get(b.get("best_baseline") or "", {})
        L.append(f"| {k} | {b['llm']['n']} | {b['threads']} | {fmt(b['llm']['base_rate'])} | {fmt(b['llm']['brier'])} | "
                 f"{fmt(b['llm_auroc_ci'])} | {b.get('best_baseline')} | {fmt(bb.get('brier', float('nan')))} | "
                 f"{fmt(bb.get('auroc', float('nan')))} | {fmt(bb.get('llm_brier_skill_vs_this', 'n/a'))} |")
    L.append("\n## Timing calibration (design T)")
    L.append("| horizon | n | base rate | mean p | Brier | ECE | slope | AUROC |")
    L.append("|---|---|---|---|---|---|---|---|")
    for h, t in res["timing"].items():
        L.append(f"| {h} | {t['n']} | {fmt(t['base_rate'])} | {fmt(t['mean_p'])} | {fmt(t['brier'])} | {fmt(t['ece'])} | {fmt(t['cal_slope'])} | {fmt(t['auroc'])} |")
    L.append("\n## Lead time (design T, 180d)")
    L.append("| θ | flagged | precision | recall | detected share | median lead (first) | median lead (persistent) |")
    L.append("|---|---|---|---|---|---|---|")
    for t in res["lead_time"]["thresholds"]:
        L.append(f"| {t['threshold']} | {t['flagged']} | {fmt(t['precision'])} | {fmt(t['recall'])} | {fmt(t['detected_share'])} | {fmt(t['median_lead_days_first_cross'])} | {fmt(t['median_lead_days_persistent'])} |")
    L.append(f"\nAt precision ≥ 0.80: {json.dumps(res['lead_time']['at_precision_0.8'])}")
    L.append("\n## Content direction (positives)")
    L.append("```\n" + json.dumps({"design_T": res["content"], "CLEAN": res["content_CLEAN"]}, indent=1) + "\n```")
    if "title_only_control" in res:
        L.append("\n## Same-model TITLE_ONLY memorisation/prior control (ΔBrier ALL − TITLE; negative = evidence helps)")
        for k, v in res["title_only_control"].items():
            L.append(f"- {k}: n={v.get('n')} Brier ALL={fmt(v.get('brier_a', float('nan')))} TITLE={fmt(v.get('brier_b', float('nan')))} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))}")
    if "ablation" in res:
        L.append("\n## Ablations (single model; ΔBrier a − b, negative = a better)")
        for k, v in res["ablation"].items():
            if k == "per_arm":
                continue
            L.append(f"- {k}: n={v.get('n')} thr={v.get('threads')} Brier a={fmt(v.get('brier_a', float('nan')))} b={fmt(v.get('brier_b', float('nan')))} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))} AUROC a={fmt(v.get('auroc_a', float('nan')))} b={fmt(v.get('auroc_b', float('nan')))}")
        L.append("\n| arm | n | base | Brier | AUROC | ECE |")
        L.append("|---|---|---|---|---|---|")
        for arm, s in res["ablation"]["per_arm"].items():
            L.append(f"| {arm} | {s['n']} | {fmt(s['base_rate'])} | {fmt(s['brier'])} | {fmt(s['auroc'])} | {fmt(s['ece'])} |")
    L.append("\n## Recognition\n" + json.dumps(res["recognition"]) + f"\nprobe-recalled threads: {res.get('probe_recalled_threads')}")
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--primary-runs", default="")
    ap.add_argument("--ablation-runs", default="")
    ap.add_argument("--title-runs", default="")
    ap.add_argument("--probe", default=os.path.join(DATA, "audits", "memorisation_probe.jsonl"))
    a = ap.parse_args()
    sp = lambda s: [x for x in s.split(",") if x]
    res = run_eval(sp(a.primary_runs), sp(a.ablation_runs), sp(a.title_runs), a.probe)
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    json.dump(res, open(os.path.join(ROOT, "reports", "metrics.json"), "w"), indent=1, default=str)
    write_md(res, os.path.join(ROOT, "reports", "METRICS.md"))
    print("wrote reports/metrics.json and reports/METRICS.md")
