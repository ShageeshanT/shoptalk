from shoptalk.payment_risk_score import payment_risk_score

def test_payment_risk_score_bounds():
    assert 0 <= payment_risk_score(0, 0, 0) <= 100

def test_payment_risk_score_increases_for_riskier_input():
    assert payment_risk_score(5, 2, 5000) > payment_risk_score(0, 0, 0)
