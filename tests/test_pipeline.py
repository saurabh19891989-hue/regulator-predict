import json
import os

from rpe.common import read_jsonl, d


def test_validate_clean(dataset):
    from rpe.validate import validate_dir
    errs, warns, stats = validate_dir(dataset["ws"], quiet=True)
    assert errs == [], errs
    assert stats["threads"] == 12 and stats["positives"] == 8


def test_lint_catches_post_decision_evidence_and_outcome_words():
    from rpe.lint import lint_evidence, lint_thread_text
    from tests.conftest import ev, outcome, thread
    o = outcome("IN-TST-H-0099", True, ddate="2023-01-01")
    bad = ev("IN-TST-H-0099", 5, "2023-01-02")
    assert any(l == "error" for l, _ in lint_evidence(bad, o))
    t = thread("IN-TST-H-0099", "2022-01-01")
    t["issue_summary_neutral"] = "The proposal was later adopted by the board in 2024."
    msgs = [m for _, m in lint_thread_text(t)]
    assert any("later" in m for m in msgs) and any("2024" in m for m in msgs)


def test_build_and_snapshots_point_in_time(dataset):
    from rpe.build import build
    from rpe.snapshots import build_index
    s = build(verbose=False)
    assert s["threads"] == 12
    rows, _ = build_index()
    ev = {e["evidence_id"]: e for e in read_jsonl(os.path.join(dataset["root"], "evidence", "evidence.jsonl"))}
    th = {t["thread_id"]: t for t in read_jsonl(os.path.join(dataset["root"], "threads", "threads.jsonl"))}
    om = {o["thread_id"]: o for o in read_jsonl(os.path.join(dataset["root"], "outcomes", "outcomes.jsonl"))}
    assert rows
    for r in rows:
        assert d(r["cutoff_date"]) >= d(th[r["thread_id"]]["anchor_date"])       # no pre-anchor cutoffs
        o = om[r["thread_id"]]
        res = o.get("decisive_date") or o.get("withdrawal_date")
        if res:
            assert d(r["cutoff_date"]) < d(res)                                   # never at/after resolution
        for eid in r["evidence_ids"]:
            assert d(ev[eid]["publication_date"]) <= d(r["cutoff_date"])          # no future evidence
        if r["arm"] == "LATEST_DOCUMENT_ONLY" and r["available"]:
            assert len(r["evidence_ids"]) == 1
        if r["arm"] == "TITLE_ONLY":
            assert r["evidence_ids"] == []
        if r["design"] == "T" and not r["is_pseudo_anchor"]:
            k = int(r["offset"].split("-")[1])
            assert r["labels"]["180"] == (1 if k <= 180 else 0)
    # withdrawn negative: pseudo-anchor strictly before withdrawal
    w = [r for r in rows if r["thread_id"] == "IN-TST-H-0012"]
    assert all(d(r["anchor_T"]) < d("2023-06-01") for r in w)


def test_packets_contain_no_outcome_information(dataset):
    from rpe.packets import make_run
    m = make_run("testrun", ["ALL", "TITLE_ONLY", "B_ONLY"], ["T"], size=5)
    assert m["batches"]
    idx = {r["snapshot_id"]: r for r in read_jsonl(os.path.join(dataset["root"], "snapshots", "index.jsonl"))}
    for b in m["batches"]:
        txt = open(b["packet"]).read()
        assert "FINAL SECRET TITLE" not in txt and "OUTCOME-SUMMARY-SENTINEL" not in txt
        assert "example.gov/final" not in txt and "IN-TST-H-" not in txt
        assert "T-180" not in txt and "is_pseudo" not in txt and "stratum" not in txt
        tids = [idx[s]["thread_id"] for s in b["snapshot_ids"]]
        assert len(tids) == len(set(tids))   # one snapshot per thread per batch


def test_ledger_append_only_and_coherence(dataset):
    from rpe import ledger
    from rpe.packets import FC_ROOT
    m = json.load(open(os.path.join(dataset["root"], "forecasts", "runs", "testrun.json")))
    b = m["batches"][0]
    fcs = [{"id": s, "p": {"7d": 0.2, "30d": 0.1, "60d": 0.3, "90d": 0.4, "180d": 0.6},
            "next": {"final_action": 1, "revised_or_further_consultation": 1, "formal_withdrawal": 0, "no_further_official_step": 0},
            "content": {"as_proposed": 0.5, "softened": 0.5, "tightened": 0, "mixed": 0, "different_mechanism": 0},
            "scenarios": [], "notes": "x", "missing": [], "recognised_outcome": False, "insufficient_evidence": False}
           for s in b["snapshot_ids"]]
    open(b["output"], "w").write(json.dumps({"forecasts": fcs}))
    r1 = ledger.ingest("testrun", "test-model")
    assert r1["ingested"] >= len(b["snapshot_ids"])
    r2 = ledger.ingest("testrun", "test-model")
    assert r2["ingested"] == 0                      # no double ingestion / rewrite
    assert ledger.verify()["ok"]
    rec = read_jsonl(ledger.LEDGER)[0]
    t = rec["forecast"]["timing"]
    assert t["7d"] <= t["30d"] <= t["60d"] <= t["90d"] <= t["180d"]
    assert abs(sum(rec["forecast"]["next_step_probabilities"].values()) - 1) < 1e-9
    assert abs(rec["forecast"]["delay_or_no_action_probability"] + rec["forecast"]["action_probability_180d"] - 1) < 1e-9
    # tamper detection
    rows = open(ledger.LEDGER).read().splitlines()
    x = json.loads(rows[0]); x["forecast"]["action_probability_180d"] = 0.99
    rows[0] = json.dumps(x)
    open(ledger.LEDGER, "w").write("\n".join(rows) + "\n")
    assert not ledger.verify()["ok"]


def test_metrics_sanity():
    import numpy as np
    from rpe.evaluate import auroc, brier, cal_slope, ece
    y = np.array([0, 0, 1, 1]); p = np.array([0.1, 0.2, 0.8, 0.9])
    assert brier(p, y) < 0.05 and auroc(p, y) == 1.0 and ece(p, y) < 0.25
    rng = np.random.default_rng(0); p = rng.uniform(0.01, 0.99, 5000); y = (rng.uniform(size=5000) < p).astype(int)
    s, i = cal_slope(p, y)
    assert 0.85 < s < 1.15 and abs(i) < 0.15


def test_audit_patch_moves_decisive_date_and_drops_leaked_evidence(dataset):
    import json as _j
    from rpe.build import build
    pdir = os.path.join(dataset["root"], "audits", "patches")
    os.makedirs(pdir, exist_ok=True)
    # thread 0001: anchor 2022-02-10, E02 2022-03-20 (C), E03 2022-04-05 (D), decisive 2023-02-15 → move to 2022-04-01
    with open(os.path.join(pdir, "test.jsonl"), "w") as f:
        f.write(_j.dumps({"op": "set_outcome", "thread_id": "IN-TST-H-0001", "field": "decisive_date", "value": "2022-04-01", "reason": "earlier board approval"}) + "\n")
    build(verbose=False)
    ev = [e for e in read_jsonl(os.path.join(dataset["root"], "evidence", "evidence.jsonl")) if e["thread_id"] == "IN-TST-H-0001"]
    assert all(d(e["publication_date"]) < d("2022-04-01") for e in ev)
    assert any(e["evidence_id"].endswith("E02") for e in ev) and not any(e["evidence_id"].endswith("E03") for e in ev)
    os.remove(os.path.join(pdir, "test.jsonl"))
    build(verbose=False)
