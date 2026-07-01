from shoptalk.inventory_risk_score import inventory_risk_score

def test_inventory_risk_score_bounds():
    assert 0 <= inventory_risk_score(0, 0, 0) <= 100

def test_inventory_risk_score_increases_for_riskier_input():
    assert inventory_risk_score(2, 1, 2) > inventory_risk_score(100, 0, 2)
