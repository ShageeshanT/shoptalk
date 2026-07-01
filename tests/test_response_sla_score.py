from shoptalk.response_sla_score import response_sla_score

def test_response_sla_score_stays_in_bounds():
    assert 0 <= response_sla_score(0, 0, 0) <= 100
    assert 0 <= response_sla_score(5, 5, 5) <= 100

def test_response_sla_score_responds_to_stronger_signal():
    assert response_sla_score(5, 5, 5) >= response_sla_score(0, 0, 0)
