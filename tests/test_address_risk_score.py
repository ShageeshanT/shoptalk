from shoptalk.address_risk_score import address_risk_score


def test_address_risk_score_bounds():
    assert 0 <= address_risk_score(3, 2, False) <= 100


def test_address_risk_score_separates_strong_and_weak_signal():
    assert address_risk_score(3, 2, False) > address_risk_score(0, 0, True)
