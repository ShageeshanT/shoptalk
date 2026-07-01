from shoptalk.lead_quality_score import lead_quality_score

def test_lead_quality_score_stays_in_bounds():
    assert 0 <= lead_quality_score(0, 0, 0) <= 100
    assert 0 <= lead_quality_score(5, 5, 5) <= 100

def test_lead_quality_score_responds_to_stronger_signal():
    assert lead_quality_score(5, 5, 5) >= lead_quality_score(0, 0, 0)
