import pytest
import math

from rpe import evaluate


def test_baseline_features_exclude_other_cohort_labels(monkeypatch):
    records = {
        "threads.jsonl": [{"thread_id": "audited"}, {"thread_id": "unverified"}],
        "evidence.jsonl": [],
    }
    monkeypatch.setattr(evaluate, "read_jsonl", lambda path: records[path.replace("\\", "/").split("/")[-1]])
    monkeypatch.setattr(evaluate, "features", lambda t, items, cutoff: {})
    idx = {tid: {"snapshot_id": tid, "thread_id": tid, "cutoff_date": "2026-01-01",
                 "arm": "ALL", "available": True, "labels": {"180": y}}
           for tid, y in [("audited", 0), ("unverified", 1)]}
    result = evaluate.feature_rows(idx, {"audited"})
    assert [r["thread_id"] for r in result] == ["audited"]
    assert result[0]["y"] == {"180": 0}


def row(arm, model="astra", run="primary", design="T"):
    return {"thread_id": "matter", "cutoff_date": "2026-01-01", "design": design,
            "model": model, "arm": arm, "run": run, "snapshot_id": arm,
            "labels": {"180": 1}}


def test_ablation_cannot_pair_different_models_or_designs():
    result = evaluate.paired_arms([row("B_PLUS_C"), row("B_ONLY", model="sol")], "B_PLUS_C", "B_ONLY")
    assert result["n"] == 0
    result = evaluate.paired_arms([row("B_PLUS_C"), row("B_ONLY", design="C")], "B_PLUS_C", "B_ONLY")
    assert result["n"] == 0


def test_ablation_rejects_unselected_replicate_runs():
    with pytest.raises(ValueError, match="select one run"):
        evaluate.paired_arms([row("B_PLUS_C"), row("B_PLUS_C", run="repeat"), row("B_ONLY")],
                             "B_PLUS_C", "B_ONLY")


def test_separated_calibration_has_no_finite_slope():
    assert all(math.isnan(x) for x in evaluate.cal_slope([.1, .2, .8, .9], [0, 0, 1, 1]))
    assert all(math.isnan(x) for x in evaluate.cal_slope([.1, .2, .2, .8], [0, 0, 1, 1]))
    assert all(math.isfinite(x) for x in evaluate.cal_slope([.1, .3, .7, .9], [0, 1, 0, 1]))


def test_primary_comparator_excludes_backfill_and_control_only_threads():
    rows = [
        {"thread_id": "population", "run": "core", "arm": "B_PLUS_C", "sampling_origin": "precursor_population"},
        {"thread_id": "outcome_selected", "run": "core", "arm": "B_PLUS_C", "sampling_origin": "outcome_backfill"},
        {"thread_id": "title_without_core", "run": "core", "arm": "TITLE_ONLY", "sampling_origin": "precursor_population"},
        {"thread_id": "another_run", "run": "other", "arm": "B_PLUS_C", "sampling_origin": "precursor_population"},
    ]
    assert evaluate.primary_cohort_threads(rows, ["core"], "B_PLUS_C") == {"population"}


def test_lead_precision_uses_frozen_thresholds_and_180_day_window():
    rows = []
    for n in range(5):
        rows.append({"thread_id": f"positive{n}", "design": "T", "offset": "T-30",
                     "labels": {"180": 1}, "is_pseudo_anchor": False,
                     "fc": {"action_probability_180d": .6}})
        rows.append({"thread_id": f"long{n}", "design": "T", "offset": "T-270",
                     "labels": {"180": 0}, "is_pseudo_anchor": True,
                     "fc": {"action_probability_180d": .9}})
    result = evaluate.lead_time(rows)
    assert [x["threshold"] for x in result["thresholds"]] == [.5, .7, .8]
    assert result["at_precision_0.8"]["precision"] == 1
    assert result["at_precision_0.8"]["flagged"] == 5
    assert result["at_precision_0.8"]["median_lead_days_first_cross"] == 30


def test_bootstrap_auc_matches_reference_with_ties_and_repeated_rows():
    import numpy as np
    from sklearn.metrics import roc_auc_score
    rng = np.random.default_rng(42)
    for _ in range(50):
        n = int(rng.integers(4, 80))
        y = rng.integers(0, 2, n)
        y[:2] = [0, 1]
        p = rng.choice([.1, .3, .5, .7, .9], n)
        assert evaluate.auroc(p, y) == pytest.approx(roc_auc_score(y, p))
    assert math.isnan(evaluate.auroc([.1, .9], [1, 1]))


def test_logistic_preprocessing_is_fitted_only_on_training_threads(monkeypatch):
    import numpy as np
    from rpe import baselines
    fitted = []

    class CheckedLogit:
        def __init__(self, **kwargs):
            pass

        def fit(self, x, y):
            # Global preprocessing leaks held-out feature values into these moments.
            assert np.allclose(x.mean(0), 0, atol=1e-8)
            assert np.allclose(x.std(0), 1, atol=1e-8)
            fitted.append(len(y))
            return self

        def predict_proba(self, x):
            return np.tile([.5, .5], (len(x), 1))

    monkeypatch.setattr(baselines, "LogisticRegression", CheckedLogit)
    monkeypatch.setattr(baselines, "_X", lambda rows, fams: np.array([[r['f']['value']] for r in rows], float))
    rows = [{'thread_id': f't{n}', 'f': {'family': 'one', 'value': value}, 'y': {'90': n % 2}}
            for n, value in enumerate([0, 1, 3, 9, 30, 1000])]
    result = baselines.grouped_logit(rows, 90, folds=3)
    assert fitted == [4, 4, 4]
    assert result == {n: .5 for n in range(6)}
