from collectors import us_fr


def test_live_comment_count_is_not_backdated_into_backtest():
    anchor = {"regulations_dot_gov_info": {"comments_count": 200}}
    assert us_fr.build_stakeholder_evidence("US-FR-H-0001", 2, anchor, ["2020-01-01"], None) is None
