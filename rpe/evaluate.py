"""Evaluator: joins frozen forecasts (ledger) with sealed labels and computes pre-registered metrics.

Usage: python3 -m rpe.evaluate [--primary-runs R1,R2] [--ablation-runs R3,...] [--title-runs R4] [--probe probe.jsonl]
Writes reports/metrics.json and reports/METRICS.md
"""
import argparse
import hashlib
import json
import math
import os
from collections import defaultdict

import numpy as np
from scipy.special import expit
from scipy.stats import rankdata
from sklearn.metrics import average_precision_score, roc_auc_score

from .baselines import HORIZONS, all_baselines, features
from .common import DATA, ROOT, frozen_data_hashes, read_jsonl
from .ledger import CONTENT, LEDGER
from .snapshots import select_items

RNG = np.random.default_rng(20260925)


# ---------------------------------------------------------------- metrics
def brier(p, y):
    p, y = np.asarray(p, float), np.asarray(y, float)
    return float(np.mean((p - y) ** 2)) if len(y) else float("nan")


def logloss(p, y, eps=1e-3):
    p = np.clip(np.asarray(p, float), eps, 1 - eps)
    y = np.asarray(y, float)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))) if len(y) else float("nan")


def auroc(p, y):
    if len(set(y)) != 2:
        return float("nan")
    p, y = np.asarray(p, float), np.asarray(y, int)
    if len(p) != len(y) or not np.isfinite(p).all():
        raise ValueError("AUROC requires matching labels and finite probabilities")
    # Rank-sum AUROC is identical to the ROC integral, including half credit for ties.
    # Avoid repeated sklearn validation/sorting overhead in 2,000-replicate clustered CIs.
    positive = y == 1
    npos, nneg = int(positive.sum()), int((~positive).sum())
    return float((rankdata(p, method="average")[positive].sum() - npos * (npos + 1) / 2) / (npos * nneg))


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
    # A finite unpenalized calibration MLE does not exist under complete/quasi separation.
    if (np.ptp(x) == 0 or np.max(x[y == 0]) <= np.min(x[y == 1])
            or np.max(x[y == 1]) <= np.min(x[y == 0])):
        return float("nan"), float("nan")
    w = np.array([0.0, 1.0])
    for _ in range(100):  # Newton-Raphson logistic regression y ~ a + b*x
        z = w[0] + w[1] * x
        mu = expit(z)
        g = np.array([np.sum(y - mu), np.sum((y - mu) * x)])
        Wd = mu * (1 - mu)
        Hm = -np.array([[Wd.sum(), (Wd * x).sum()], [(Wd * x).sum(), (Wd * x * x).sum()]])
        try:
            step = np.linalg.solve(Hm, g)
            w = w - step
        except np.linalg.LinAlgError:
            return float("nan"), float("nan")
        if np.max(np.abs(step)) < 1e-8 and np.isfinite(w).all():
            return float(w[1]), float(w[0])
    return float("nan"), float("nan")


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
    # Fail before joining immutable forecasts to labels that may have changed during a rebuild.
    if runs:
        with open(os.path.join(DATA, "snapshots", "index.jsonl"), "rb") as f:
            index_hash = hashlib.sha256(f.read()).hexdigest()
        for run in sorted(set(runs)):
            with open(os.path.join(DATA, "forecasts", "runs", run + ".json"), encoding="utf-8") as f:
                manifest = json.load(f)
            if manifest.get("invalidated"):
                raise ValueError(f"run {run} was invalidated: {manifest.get('invalid_reason', '')}")
            if manifest.get("snapshot_index_sha256") != index_hash:
                raise ValueError(f"run {run} has no matching frozen snapshot index")
            if manifest.get("dataset_sha256") and frozen_data_hashes(DATA) != manifest["dataset_sha256"]:
                raise ValueError(f"run {run} refers to a different frozen canonical dataset")
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


def feature_rows(idx, thread_ids=None):
    """Feature rows for every available ALL-arm snapshot (baselines are arm-independent)."""
    threads = {t["thread_id"]: t for t in read_jsonl(os.path.join(DATA, "threads", "threads.jsonl"))}
    ev = defaultdict(list)
    for e in read_jsonl(os.path.join(DATA, "evidence", "evidence.jsonl")):
        ev[e["thread_id"]].append(e)
    rows = []
    for s in idx.values():
        if thread_ids is not None and s["thread_id"] not in thread_ids:
            continue
        if s["arm"] != "ALL" or not s["available"]:
            continue
        items, _, _, _ = select_items(ev[s["thread_id"]], "ALL", s["cutoff_date"])
        rows.append({"snapshot_id": s["snapshot_id"], "thread_id": s["thread_id"], "cutoff_date": s["cutoff_date"],
                     "f": features(threads[s["thread_id"]], items, s["cutoff_date"]), "y": s["labels"]})
    return rows


def baseline_lookup(idx, thread_ids=None):
    frows = feature_rows(idx, thread_ids)
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
        hh = h
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
    def keyed(arm):
        out = {}
        for r in rows:
            if r["arm"] != arm:
                continue
            k = (r["thread_id"], r["cutoff_date"], r["design"], r["model"])
            if k in out and (out[k]["run"], out[k]["snapshot_id"]) != (r["run"], r["snapshot_id"]):
                raise ValueError(f"Multiple forecasts for {arm} at {k}; select one run per comparison")
            out[k] = r
        return out
    A, B = keyed(arm_a), keyed(arm_b)
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
    T = [r for r in rows if r["design"] == "T" and r["labels"].get("180") is not None
         and int(r["offset"].split("-")[1]) <= 180]
    p = np.array([r["fc"]["action_probability_180d"] for r in T])
    y = np.array([r["labels"]["180"] for r in T])
    by_thread = defaultdict(list)
    for r in T:
        if not r["is_pseudo_anchor"]:
            by_thread[r["thread_id"]].append((int(r["offset"].split("-")[1]), r["fc"]["action_probability_180d"]))
    res = {"thresholds": []}
    for th in (0.5, 0.7, 0.8):
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
    majority = max(CONTENT, key=lambda c: tot[c])
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
            "majority_class": majority, "majority_rate_threads": tot[majority] / len(thr),
            "majority_top1_snapshot": float(np.mean([lab[r["thread_id"]] == majority for r in pos])),
            "model_multiclass_brier": float(mb.mean()), "baserate_multiclass_brier": float(bb.mean()),
            "brier_skill": boot(g, lambda ix: 1 - mb[ix].mean() / bb[ix].mean()),
            "model_top1": float(acc_m.mean()), "baserate_top1": float(acc_b.mean()),
            "top1_gain": boot(g, lambda ix: acc_m[ix].mean() - acc_b[ix].mean())}


def gate_assessment(res):
    """Decision inputs only: absent audit and mechanism results can never become a GO."""
    action = res["action"]
    title = res.get("title_only_control", {})
    arm = res["primary_arm"]
    hist = action.get("C_90_HIST", {})
    late = action.get("C_90_LATE", {})
    best_h = hist.get("baselines", {}).get(hist.get("best_baseline"), {})
    best_l = late.get("baselines", {}).get(late.get("best_baseline"), {})
    bss_h = best_h.get("llm_brier_skill_vs_this")
    bss_l = best_l.get("llm_brier_skill_vs_this")
    title_h = title.get(f"{arm}_vs_TITLE_C_90_HIST", {}).get("delta_brier_a_minus_b")
    late_auc = late.get("llm", {}).get("auroc")

    def finite(x):
        return isinstance(x, (int, float)) and math.isfinite(x)

    def band(x, boundary, higher=True):
        return {f"{boundary + shift:.2f}": (x >= boundary + shift if higher else x <= boundary + shift)
                for shift in (-0.05, 0, 0.05)} if finite(x) else None

    g1_ready = (bss_h and title_h and bss_l and finite(late_auc)
                and all(finite(x) for x in (bss_h[0], bss_h[1], title_h[2], bss_l[0])))
    g1_pass = (bss_h[0] >= 0.05 and bss_h[1] > 0 and title_h[2] < 0
               and late_auc >= 0.70 and bss_l[0] >= 0) if g1_ready else None
    g2_values = {h: res["timing"].get(f"POOLED_{h}d", {}) for h in (30, 90, 180)}
    g2_ready = all(finite(v.get("ece")) and finite(v.get("cal_slope")) for v in g2_values.values())
    g2_pass = all(v["ece"] <= 0.10 and 0.6 <= v["cal_slope"] <= 1.4 for v in g2_values.values()) if g2_ready else None
    lead = res["lead_time"].get("at_precision_0.8")
    g4_ready = bool(lead and finite(lead.get("median_lead_days_first_cross")))
    g4_pass = lead["median_lead_days_first_cross"] >= 30 if g4_ready else None
    direction = res["content"]
    dir_accuracy = direction.get("model_top1")
    dir_majority = direction.get("majority_top1_snapshot")
    dir_bss = direction.get("brier_skill")
    dir_pass = ((finite(dir_accuracy) and finite(dir_majority) and dir_accuracy >= dir_majority + 0.10)
                or (dir_bss and finite(dir_bss[0]) and dir_bss[0] >= 0.05))
    hist_auc = hist.get("llm", {}).get("auroc")
    us_auc = action.get("US_C_90", {}).get("llm", {}).get("auroc")
    india_auc = action.get("IN_C_90", {}).get("llm", {}).get("auroc")
    self_hist = action.get("C_90_HIST_not_selfrecognised", {})
    self_late = action.get("C_90_LATE_not_selfrecognised", {})
    self_h_best = self_hist.get("baselines", {}).get(self_hist.get("best_baseline"), {})
    self_l_best = self_late.get("baselines", {}).get(self_late.get("best_baseline"), {})
    return {
        "basis": "Design C 90d for G1; pooled C/T timing for G2; frozen Design-T thresholds for G4",
        "G1": {"passes_numeric_checks": g1_pass, "HIST_brier_skill": bss_h,
               "HIST_title_delta_brier": title_h, "LATE_auroc": late_auc,
               "LATE_brier_skill": bss_l,
               "sensitivity_pm_0.05": {"HIST_skill_band": band(bss_h[0], 0.05) if bss_h else None,
                                        "LATE_auroc_band": band(late_auc, 0.70),
                                        "LATE_skill_band": band(bss_l[0], 0) if bss_l else None}},
        "G2": {"passes_numeric_checks": g2_pass,
               "pooled": {str(h): {"n": v.get("n"), "ece": v.get("ece"), "slope": v.get("cal_slope"),
                                   "ece_sensitivity_pm_0.05": band(v.get("ece"), 0.10, False),
                                   "slope_interval_sensitivity_pm_0.05": {
                                       "wider_0.55_1.45": 0.55 <= v["cal_slope"] <= 1.45,
                                       "frozen_0.60_1.40": 0.60 <= v["cal_slope"] <= 1.40,
                                       "narrower_0.65_1.35": 0.65 <= v["cal_slope"] <= 1.35,
                                   } if finite(v.get("cal_slope")) else None}
                          for h, v in g2_values.items()}},
        "G3": {"status": "unassessed: blinded GOLD/LATE mechanism judgment absent",
               "direction_numeric_pass": bool(dir_pass), "direction_accuracy": dir_accuracy,
               "direction_majority_snapshot": dir_majority, "direction_brier_skill": dir_bss,
               "direction_gain_band_sensitivity_pm_0.05":
                   band(dir_accuracy - dir_majority, 0.10) if finite(dir_accuracy) and finite(dir_majority) else None,
               "direction_brier_skill_band_sensitivity_pm_0.05":
                   band(dir_bss[0], 0.05) if dir_bss else None},
        "G4": {"passes_numeric_checks": g4_pass, "selected_threshold": lead,
               "lead_days_sensitivity_pm_0.05": band(
                   lead.get("median_lead_days_first_cross") if lead else None, 30),
               "precision_band_sensitivity_pm_0.05": {
                   f"{bound:.2f}": next((t["median_lead_days_first_cross"] >= 30 for t in res["lead_time"]["thresholds"]
                                          if t["flagged"] >= 5 and finite(t["precision"]) and t["precision"] >= bound
                                          and finite(t["median_lead_days_first_cross"])), None)
                   for bound in (0.75, 0.80, 0.85)}},
        "G5": {"status": "unassessed: audited-snapshot contamination denominator and full exclusion robustness absent",
               "HIST_minus_LATE_auroc": hist_auc - late_auc if finite(hist_auc) and finite(late_auc) else None,
               "US_auroc": us_auc, "India_auroc": india_auc,
               "HIST_LATE_gap_sensitivity_pm_0.05":
                   band(hist_auc - late_auc, 0.10, False) if finite(hist_auc) and finite(late_auc) else None,
               "US_auroc_band_sensitivity_pm_0.05": band(us_auc, 0.65),
               "India_auroc_band_sensitivity_pm_0.05": band(india_auc, 0.65),
               "self_recognition_exclusion": {
                   "HIST_brier_skill": self_h_best.get("llm_brier_skill_vs_this"),
                   "LATE_brier_skill": self_l_best.get("llm_brier_skill_vs_this"),
                   "HIST_title_delta_brier": title.get(
                       f"{arm}_vs_TITLE_C_90_HIST_not_selfrecognised", {}).get("delta_brier_a_minus_b")}},
        "decision": "UNASSESSED: G3 mechanism and G5 audit inputs are missing; numeric passes alone cannot establish GO",
    }


def primary_cohort_threads(rows, primary, primary_arm):
    return {r["thread_id"] for r in rows if r["run"] in primary and r["arm"] == primary_arm
            and r["sampling_origin"] == "precursor_population"}


def run_eval(primary, ablation, title, probe_path=None, primary_arm="B_PLUS_C", masked=None):
    """primary: runs holding the broad B_ONLY/B_PLUS_C forecasts (same model). Primary action metrics use
    `primary_arm` on precursor-population threads only; backfilled/purposive threads reported separately."""
    rows_all, idx = load(set(primary) | set(ablation) | set(title) | set(masked or []))
    # Audited-cohort results must not train comparators on unrelated, unaudited labels.
    cohort_threads = primary_cohort_threads(rows_all, primary, primary_arm)
    look, frows = baseline_lookup(idx, cohort_threads)
    outcomes = read_jsonl(os.path.join(DATA, "outcomes", "outcomes.jsonl"))
    R = [r for r in rows_all if r["run"] in primary]
    P = [r for r in R if r["arm"] == primary_arm and r["sampling_origin"] == "precursor_population"]
    PB = [r for r in R if r["arm"] == primary_arm and r["sampling_origin"] != "precursor_population"]
    res = {"primary_runs": primary, "primary_arm": primary_arm, "n_primary_forecasts": len(P),
           "n_backfill_or_purposive_forecasts": len(PB),
           "baseline_training_threads": sorted(cohort_threads),
           "baseline_training_scope": "Selected primary-arm precursor-population threads; thread-grouped cross-validation"}
    recog = set()
    if probe_path and os.path.exists(probe_path):
        for x in read_jsonl(probe_path):
            if x.get("recalled_correctly"):
                recog.add(x["thread_id"])
    res["probe_recalled_threads"] = len(recog)

    def sub(fn, rows=P):
        return [r for r in rows if fn(r)]
    B = {}
    B["T_180_all"] = action_block(sub(lambda r: r["design"] == "T"), look, 180, "Design T (outcome-anchored), 180d, all strata")
    B["T_180_HIST"] = action_block(sub(lambda r: r["design"] == "T" and r["stratum"] == "HIST"), look, 180, "Design T, 180d, HIST")
    for h in (30, 60, 90, 180):
        B[f"C_{h}_all"] = action_block(sub(lambda r: r["design"] == "C"), look, h, f"Design C (calendar-forward), {h}d")
    B["C_90_HIST"] = action_block(sub(lambda r: r["design"] == "C" and r["stratum"] == "HIST"), look, 90, "Design C, 90d, HIST")
    B["C_90_LATE"] = action_block(sub(lambda r: r["design"] == "C" and r["stratum"] == "LATE"), look, 90, "Design C, 90d, LATE")
    B["T_180_LATE"] = action_block(sub(lambda r: r["design"] == "T" and r["stratum"] == "LATE"), look, 180, "Design T, 180d, LATE")
    for quality in ("RAPID", "GOLD"):
        for design, h in (("C", 90), ("T", 180)):
            B[f"{design}_{h}_{quality}"] = action_block(
                sub(lambda r, q=quality, ds=design: r["design"] == ds and r["quality"] == q),
                look, h, f"Design {design}, {h}d, {quality}")
            for stratum in ("HIST", "LATE"):
                B[f"{design}_{h}_{quality}_{stratum}"] = action_block(
                    sub(lambda r, q=quality, ds=design, st=stratum:
                        r["design"] == ds and r["quality"] == q and r["stratum"] == st),
                    look, h, f"Design {design}, {h}d, {quality}, {stratum}")
    B["C_30_postcutoff"] = action_block(sub(lambda r: r["design"] == "C" and r["post_cutoff_snapshot"]), look, 30, "Design C checkpoints after stated model cutoff, 30d")
    B["C_60_postcutoff"] = action_block(sub(lambda r: r["design"] == "C" and r["post_cutoff_snapshot"]), look, 60, "Design C checkpoints after stated model cutoff, 60d")
    for fam in sorted({r["family"] for r in P}):
        B[f"FAM_{fam}_C_90"] = action_block(sub(lambda r, fam=fam: r["family"] == fam and r["design"] == "C"), look, 90, f"{fam} design C 90d")
        B[f"FAM_{fam}_T_180"] = action_block(sub(lambda r, fam=fam: r["family"] == fam and r["design"] == "T"), look, 180, f"{fam} design T 180d")
    B["US_C_90"] = action_block(sub(lambda r: r["family"].startswith("US") and r["design"] == "C"), look, 90, "US design C 90d")
    B["IN_C_90"] = action_block(sub(lambda r: r["family"].startswith("IN") and r["design"] == "C"), look, 90, "India design C 90d")
    B["C_90_not_selfrecognised"] = action_block(sub(lambda r: r["design"] == "C" and not r["fc"]["recognised_outcome"]), look, 90, "Design C 90d excluding self-recognised")
    for design, h in (("C", 90), ("T", 180)):
        for stratum in ("HIST", "LATE"):
            B[f"{design}_{h}_{stratum}_not_selfrecognised"] = action_block(
                sub(lambda r, ds=design, st=stratum: r["design"] == ds and r["stratum"] == st
                    and not r["fc"]["recognised_outcome"]), look, h,
                f"Design {design} {h}d {stratum} excluding self-recognised")
    if recog:
        B["C_90_not_probe_recalled"] = action_block(sub(lambda r: r["design"] == "C" and r["thread_id"] not in recog), look, 90, "Design C 90d excluding probe-recalled threads")
        B["T_180_not_probe_recalled"] = action_block(sub(lambda r: r["design"] == "T" and r["thread_id"] not in recog), look, 180, "Design T 180d excluding probe-recalled threads")
    if PB:
        B["C_90_backfill_only"] = action_block([r for r in PB if r["design"] == "C"], look, 90, "Design C 90d, backfilled/purposive threads only")
    res["action"] = B
    tim = {}
    for design in ("C", "T"):
        for h in HORIZONS:
            d_ = [(r["fc"]["timing"][f"{h}d"], r["labels"][str(h)]) for r in P if r["design"] == design and r["labels"].get(str(h)) is not None]
            if d_:
                p, y = np.array([x[0] for x in d_]), np.array([x[1] for x in d_])
                tim[f"{design}_{h}d"] = {**summary(p, y), "reliability": reliability(p, y)}
    for h in (30, 90, 180):
        pooled = [(r["fc"]["timing"][f"{h}d"], r["labels"][str(h)]) for r in P
                  if r["labels"].get(str(h)) is not None]
        if pooled:
            p, y = np.array([x[0] for x in pooled]), np.array([x[1] for x in pooled])
            tim[f"POOLED_{h}d"] = {**summary(p, y), "reliability": reliability(p, y)}
    res["timing"] = tim
    res["lead_time"] = lead_time([r for r in P if r["design"] == "T"])
    res["content"] = content_block([r for r in P if r["design"] in ("T", "C")], outcomes)
    res["content_LATE"] = content_block([r for r in P if r["stratum"] == "LATE"], outcomes)
    res["recognition"] = {"self_recognised_share": float(np.mean([r["fc"]["recognised_outcome"] for r in P])) if P else float("nan"),
                          "insufficient_share": float(np.mean([r["fc"]["insufficient_evidence"] for r in P])) if P else float("nan")}
    # B vs B+C lift (same model, same snapshots, only where tier C exists at the cutoff)
    RR = [r for r in R if r["sampling_origin"] == "precursor_population"]
    hasC = lambda r: r["classes_present"].get("C", 0) > 0
    res["b_vs_bc"] = {
        "T_180": paired_arms([r for r in RR if r["design"] == "T"], "B_PLUS_C", "B_ONLY", 180, restrict=hasC),
        "T_30": paired_arms([r for r in RR if r["design"] == "T"], "B_PLUS_C", "B_ONLY", 30, restrict=hasC),
        "C_90": paired_arms([r for r in RR if r["design"] == "C"], "B_PLUS_C", "B_ONLY", 90, restrict=hasC),
        "C_180": paired_arms([r for r in RR if r["design"] == "C"], "B_PLUS_C", "B_ONLY", 180, restrict=hasC),
        "C_alone_vs_B_alone_C_90": paired_arms([r for r in RR if r["design"] == "C"], "C_ONLY", "B_ONLY", 90),
    }
    if title:
        TT = [r for r in rows_all if r["run"] in title or r["run"] in primary]
        TT = [r for r in TT if r["sampling_origin"] == "precursor_population"]
        res["title_only_control"] = {
            f"{primary_arm}_vs_TITLE_C_90": paired_arms([r for r in TT if r["design"] == "C"], primary_arm, "TITLE_ONLY", 90),
            f"{primary_arm}_vs_TITLE_T_180": paired_arms([r for r in TT if r["design"] == "T"], primary_arm, "TITLE_ONLY", 180),
            f"{primary_arm}_vs_TITLE_C_30_postcutoff": paired_arms([r for r in TT if r["design"] == "C" and r["post_cutoff_snapshot"]], primary_arm, "TITLE_ONLY", 30),
            f"{primary_arm}_vs_TITLE_C_90_HIST": paired_arms([r for r in TT if r["design"] == "C" and r["stratum"] == "HIST"], primary_arm, "TITLE_ONLY", 90),
            f"{primary_arm}_vs_TITLE_T_180_HIST": paired_arms([r for r in TT if r["design"] == "T" and r["stratum"] == "HIST"], primary_arm, "TITLE_ONLY", 180),
            f"{primary_arm}_vs_TITLE_C_90_HIST_not_selfrecognised": paired_arms(
                [r for r in TT if r["design"] == "C" and r["stratum"] == "HIST"],
                primary_arm, "TITLE_ONLY", 90, restrict=lambda r: not r["fc"]["recognised_outcome"]),
        }
    if masked:
        MM = [r for r in rows_all if r["run"] in masked or r["run"] in primary]
        res["masking_control"] = {
            "C_90": paired_arms([r for r in MM if r["design"] == "C"], "MASKED_B_PLUS_C", "B_PLUS_C", 90),
            "T_180": paired_arms([r for r in MM if r["design"] == "T"], "MASKED_B_PLUS_C", "B_PLUS_C", 180),
        }
    if ablation:
        A = [r for r in rows_all if r["run"] in ablation]
        abl = {}
        pairs = [("B_C_STAKEHOLDERS", "B_PLUS_C", "stakeholder_increment"),
                 ("B_C_STAKEHOLDERS_PLUS_NEWS", "B_C_STAKEHOLDERS", "news_increment_over_BCS"),
                 ("B_C_STAKEHOLDERS_PLUS_NEWS", "B_PLUS_C", "stakeholders_plus_news_over_BC"),
                 ("B_PLUS_C", "LATEST_DOCUMENT_ONLY", "full_trajectory_vs_latest_only"),
                 ("C_ONLY", "B_ONLY", "C_alone_vs_B_alone"), ("B_PLUS_C", "B_ONLY", "tierC_increment")]
        for a, b, name in pairs:
            for design, h in (("C", 90), ("T", 180)):
                abl[f"{name}_{design}{h}"] = paired_arms([r for r in A + R if r["design"] == design], a, b, h)
        res["ablation"] = abl
    res["gate_assessment"] = gate_assessment(res)
    return res


def fmt(x):
    if isinstance(x, (list, tuple)) and len(x) == 3:
        return f"{x[0]:.3f} [{x[1]:.3f}, {x[2]:.3f}]"
    if isinstance(x, float):
        return f"{x:.3f}"
    return str(x)


def write_md(res, path):
    L = ["# METRICS (auto-generated by rpe.evaluate — do not edit by hand)", ""]
    L.append(f"## Action prediction (LLM {res.get('primary_arm', 'B_PLUS_C')} vs no-LLM baselines)")
    L.append("| block | n | thr | base rate | LLM Brier | LLM AUROC [90% CI] | best baseline | its Brier | its AUROC | BSS vs best [90% CI] |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for k, b in res["action"].items():
        if not b.get("llm"):
            continue
        bb = b["baselines"].get(b.get("best_baseline") or "", {})
        L.append(f"| {k} | {b['llm']['n']} | {b['threads']} | {fmt(b['llm']['base_rate'])} | {fmt(b['llm']['brier'])} | "
                 f"{fmt(b['llm_auroc_ci'])} | {b.get('best_baseline')} | {fmt(bb.get('brier', float('nan')))} | "
                 f"{fmt(bb.get('auroc', float('nan')))} | {fmt(bb.get('llm_brier_skill_vs_this', 'n/a'))} |")
    L.append("\n## Timing calibration (design C = calendar-forward; design T = outcome-anchored)")
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
    L.append("```\n" + json.dumps({"all": res["content"], "LATE": res["content_LATE"]}, indent=1) + "\n```")
    L.append("\n## B vs B+C lift (same model; snapshots where tier C exists; Δ = B+C − B, negative = C helps)")
    for k, v in res.get("b_vs_bc", {}).items():
        L.append(f"- {k}: n={v.get('n')} thr={v.get('threads')} Brier B+C={fmt(v.get('brier_a', float('nan')))} B={fmt(v.get('brier_b', float('nan')))} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))} AUROC B+C={fmt(v.get('auroc_a', float('nan')))} B={fmt(v.get('auroc_b', float('nan')))}")
    if "masking_control" in res:
        L.append("\n## Entity/title masking control (Δ = masked − unmasked; a near-zero difference does not establish absence of memorisation)")
        for k, v in res["masking_control"].items():
            L.append(f"- {k}: n={v.get('n')} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))} AUROC masked={fmt(v.get('auroc_a', float('nan')))} unmasked={fmt(v.get('auroc_b', float('nan')))}")
    if "title_only_control" in res:
        L.append("\n## Same-model TITLE_ONLY memorisation/prior control (ΔBrier ALL − TITLE; negative = evidence helps)")
        for k, v in res["title_only_control"].items():
            L.append(f"- {k}: n={v.get('n')} Brier ALL={fmt(v.get('brier_a', float('nan')))} TITLE={fmt(v.get('brier_b', float('nan')))} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))}")
    if "ablation" in res:
        L.append("\n## Ablations (single model; ΔBrier a − b, negative = a better)")
        for k, v in res["ablation"].items():
            L.append(f"- {k}: n={v.get('n')} thr={v.get('threads')} Brier a={fmt(v.get('brier_a', float('nan')))} b={fmt(v.get('brier_b', float('nan')))} Δ={fmt(v.get('delta_brier_a_minus_b', 'n/a'))} AUROC a={fmt(v.get('auroc_a', float('nan')))} b={fmt(v.get('auroc_b', float('nan')))}")
    L.append("\n## Frozen-gate assessment inputs")
    L.append("```json\n" + json.dumps(res["gate_assessment"], indent=2, default=str) + "\n```")
    L.append("\n## Recognition\n" + json.dumps(res["recognition"]) + f"\nprobe-recalled threads: {res.get('probe_recalled_threads')}")
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--primary-runs", default="")
    ap.add_argument("--ablation-runs", default="")
    ap.add_argument("--title-runs", default="")
    ap.add_argument("--masked-runs", default="")
    ap.add_argument("--primary-arm", default="B_PLUS_C")
    ap.add_argument("--probe", default=os.path.join(DATA, "audits", "memorisation_probe.jsonl"))
    a = ap.parse_args()
    sp = lambda s: [x for x in s.split(",") if x]
    res = run_eval(sp(a.primary_runs), sp(a.ablation_runs), sp(a.title_runs), a.probe, a.primary_arm, sp(a.masked_runs))
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    json.dump(res, open(os.path.join(ROOT, "reports", "metrics.json"), "w"), indent=1, default=str)
    write_md(res, os.path.join(ROOT, "reports", "METRICS.md"))
    print("wrote reports/metrics.json and reports/METRICS.md")
