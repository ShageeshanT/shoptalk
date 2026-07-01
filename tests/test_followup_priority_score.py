from shoptalk.followup_priority_score import followup_priority_score

def test_followup_priority_score_bounds():
    assert 0 <= followup_priority_score(0, 0, 0) <= 100

def test_followup_priority_score_increases_for_riskier_input():
    assert followup_priority_score(0, 20, 2) > followup_priority_score(12, 0, 0)
