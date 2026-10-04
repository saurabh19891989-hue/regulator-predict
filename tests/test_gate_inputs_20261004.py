import math

from rpe import baselines, evaluate


def item(eid, date, tier="B", **kwargs):
    return {"evidence_id": eid, "thread_id": "matter", "publication_date": date,
            "first_known_date": None, "tier": tier, "document_type": "consultation_paper",
            "content_excerpt": "", **kwargs}


def test_deadline_feature_uses_only_cutoff_visible_official_explicit_dates():
    thread = {"family": "IN-SEBI", "anchor_date": "2026-06-01"}
    original = item("E1", "2026-06-01", comment_deadline="2026-07-01")
    extension = item("E2", "2026-07-02", content_excerpt="Comments due by 2026-08-01.")
    news = item("E3", "2026-06-10", tier="D", comment_deadline="2026-06-11")
    unlabeled = item("E4", "2026-06-12", content_excerpt="The report was dated 2026-06-13.")
    future = item("E5", "2026-09-01", comment_deadline="2026-09-10")
    assert baselines.features(thread, [original, news, unlabeled, future], "2026-06-30")["comment_deadline_passed"] == 0
    assert baselines.features(thread, [original, news, unlabeled, future], "2026-07-01")["comment_deadline_passed"] == 0
    assert baselines.features(thread, [original, news, unlabeled, future], "2026-07-03")["comment_deadline_passed"] == 1
    assert baselines.features(thread, [original, extension], "2026-07-03")["comment_deadline_passed"] == 0
    assert baselines.features(thread, [original, extension], "2026-08-02")["comment_deadline_passed"] == 1
    assert "comment_deadline_passed" in baselines.NUM


def test_deadline_feature_rejects_invalid_and_prepublication_deadlines():
    thread = {"family": "IN-SEBI", "anchor_date": "2026-06-01"}
    bad = [item("E1", "2026-06-01", comment_deadline="2026-02-30"),
           item("E2", "2026-06-05", comment_deadline="2026-06-03")]
    assert baselines.features(thread, bad, "2026-07-01")["comment_deadline_passed"] == 0


def test_gate_assessment_keeps_missing_inputs_unassessed():
    res = {"primary_arm": "B_PLUS_C", "action": {}, "timing": {}, "content": {},
           "lead_time": {"thresholds": [], "at_precision_0.8": None}}
    got = evaluate.gate_assessment(res)
    assert got["G1"]["passes_numeric_checks"] is None
    assert got["G2"]["passes_numeric_checks"] is None
    assert got["G4"]["passes_numeric_checks"] is None
    assert got["G5"]["status"].startswith("unassessed")
    assert got["decision"].startswith("UNASSESSED")
