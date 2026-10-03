from collectors import us_fr


def test_live_comment_count_is_not_backdated_into_backtest():
    anchor = {"regulations_dot_gov_info": {"comments_count": 200}}
    assert us_fr.build_stakeholder_evidence("US-FR-H-0001", 2, anchor, ["2020-01-01"], None) is None


def test_masking_preserves_the_event_being_forecast():
    from rpe.packets import render_snapshot
    thread = {"regulator": "FDA", "jurisdiction": "US", "neutral_title": "A draft",
              "masked_topic": "A generic topic", "process_type": "draft_guidance_to_final"}
    snap = {"snapshot_id": "S1", "cutoff_date": "2024-01-01", "arm": "B_PLUS_C"}
    plain = render_snapshot(snap, thread, [])
    masked = render_snapshot(dict(snap, arm="MASKED_B_PLUS_C"), thread, [])
    assert "publishes the FINAL version of this guidance" in plain
    assert "publishes the FINAL version of this guidance" in masked
    thread.update(regulator="RBI", jurisdiction="IN", process_type="draft_direction_to_final")
    masked = render_snapshot(dict(snap, arm="MASKED_B_PLUS_C"), thread, [])
    assert "issues FINAL directions/circular" in masked
    assert "central bank" not in masked
