from shoptalk.delivery_fee_risk_score import delivery_fee_risk_score


def test_delivery_fee_risk_score_bounds():
    assert 0 <= delivery_fee_risk_score(1500, 4000, True) <= 100


def test_delivery_fee_risk_score_separates_strong_and_weak_signal():
    assert delivery_fee_risk_score(1500, 4000, True) > delivery_fee_risk_score(300, 20000, False)
