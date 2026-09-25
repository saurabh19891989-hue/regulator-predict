import json
import os
import sys
import tempfile

import pytest

_TMP = tempfile.mkdtemp(prefix="rpe_test_")
os.environ["RPE_DATA"] = os.path.join(_TMP, "data")
os.environ["RPE_FC_ROOT"] = os.path.join(_TMP, "fc")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def ev(tid, n, date, tier="B", dtype="consultation_paper", text="The regulator proposes a disclosure regime.", title=None):
    return {"evidence_id": f"{tid}-E{n:02d}", "thread_id": tid, "regulator": "TESTREG", "jurisdiction": "IN",
            "title": title or f"Document number {n}", "source_url": f"https://example.gov/{tid}/{n}",
            "publication_date": date, "first_known_date": None, "retrieval_date": "2026-09-25",
            "document_type": dtype, "tier": tier, "original_or_revised": "original", "version_confidence": "high",
            "date_verification": "dateline on document", "extracted_claims": [text], "content_excerpt": text,
            "source_hash": None, "stored_copy": None}


def thread(tid, anchor):
    return {"thread_id": tid, "workstream": "xx_test", "regulator": "TESTREG", "jurisdiction": "IN",
            "neutral_title": f"TESTREG consultation: topic {tid[-2:]}",
            "issue_summary_neutral": "The paper proposes a new disclosure regime for listed entities.",
            "process_type": "consultation_to_regulation", "anchor_evidence_id": f"{tid}-E01", "anchor_date": anchor,
            "sampling_frame": "test", "sampling_method": "census", "quality_tier_proposed": "RAPID", "created_by": "test"}


def outcome(tid, action, ddate=None, wdate=None, cls=None, direction=None):
    return {"thread_id": tid, "outcome_class": cls or ("action_as_proposed" if action else "stalled_no_action"),
            "decisive_action": action, "decisive_date": ddate, "decisive_document_title": "FINAL SECRET TITLE " + tid if action else None,
            "decisive_document_url": f"https://example.gov/final/{tid}" if action else None, "decisive_document_type": "circular",
            "withdrawal_date": wdate, "censor_date": "2026-09-25",
            "content_direction": direction or ("as_proposed" if action else "na"),
            "content_summary": "OUTCOME-SUMMARY-SENTINEL", "outcome_sources": ["https://example.gov"],
            "label_confidence": "high", "labeled_by": "test"}


@pytest.fixture(scope="session")
def dataset():
    root = os.environ["RPE_DATA"]
    ws = os.path.join(root, "raw", "xx_test")
    os.makedirs(ws, exist_ok=True)
    for sub in ("threads", "evidence", "outcomes", "snapshots", "forecasts", "audits", "derived"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)
    T, E, O = [], [], []
    # 8 positives, 4 negatives (one withdrawn)
    for i in range(1, 13):
        tid = f"IN-TST-H-{i:04d}"
        anchor = f"2022-{(i % 9) + 1:02d}-10"
        T.append(thread(tid, anchor))
        E.append(ev(tid, 1, anchor))
        E.append(ev(tid, 2, f"2022-{(i % 9) + 2:02d}-20", tier="C", dtype="speech", text="Chair said the regulator is examining the matter."))
        E.append(ev(tid, 3, f"2022-{(i % 9) + 3:02d}-05", tier="D", dtype="news_article", text="Regulator may act soon, says report."))
        if i <= 8:
            O.append(outcome(tid, True, ddate=f"2023-0{(i % 8) + 1}-15"))
        elif i == 12:
            O.append(outcome(tid, False, wdate="2023-06-01", cls="withdrawn"))
        else:
            O.append(outcome(tid, False))
    with open(os.path.join(ws, "threads.jsonl"), "w") as f:
        f.writelines(json.dumps(x) + "\n" for x in T)
    with open(os.path.join(ws, "evidence.jsonl"), "w") as f:
        f.writelines(json.dumps(x) + "\n" for x in E)
    with open(os.path.join(ws, "outcomes.jsonl"), "w") as f:
        f.writelines(json.dumps(x) + "\n" for x in O)
    return {"root": root, "ws": ws, "threads": T, "evidence": E, "outcomes": O}
