from shoptalk.handoff_risk_score import handoff_risk_score

def test_handoff_risk_score_stays_in_bounds():
    assert 0 <= handoff_risk_score(0, 0, 0) <= 100
    assert 0 <= handoff_risk_score(5, 5, 5) <= 100

def test_handoff_risk_score_responds_to_stronger_signal():
    assert handoff_risk_score(5, 5, 5) >= handoff_risk_score(0, 0, 0)
