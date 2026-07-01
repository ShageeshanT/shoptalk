from shoptalk.return_risk_score import return_risk_score


def test_return_risk_score_bounds():
    assert 0 <= return_risk_score(2, 2, True, 8, False) <= 100


def test_return_risk_score_separates_strong_and_weak_signal():
    assert return_risk_score(2, 2, True, 8, False) > return_risk_score(0, 0, False, 1, True)
