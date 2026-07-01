from shoptalk.customer_risk_score import customer_risk_score

def test_customer_risk_score_bounds():
    assert 0 <= customer_risk_score(0, 0, 0) <= 100

def test_customer_risk_score_increases_for_riskier_input():
    assert customer_risk_score(3, 2, 1) > customer_risk_score(0, 0, 0)
