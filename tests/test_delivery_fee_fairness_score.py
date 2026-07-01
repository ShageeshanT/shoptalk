from shoptalk.delivery_fee_fairness_score import delivery_fee_fairness_score

def test_delivery_fee_fairness_score_stays_in_bounds():
    assert 0 <= delivery_fee_fairness_score(0, 0, 0) <= 100
    assert 0 <= delivery_fee_fairness_score(5, 5, 5) <= 100

def test_delivery_fee_fairness_score_penalizes_cost_pressure():
    assert delivery_fee_fairness_score(5, 5, 0) <= delivery_fee_fairness_score(0, 0, 0)
