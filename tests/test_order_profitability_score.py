from shoptalk.order_profitability_score import order_profitability_score

def test_order_profitability_score_stays_in_bounds():
    assert 0 <= order_profitability_score(0, 0, 0) <= 100
    assert 0 <= order_profitability_score(5, 5, 5) <= 100

def test_order_profitability_score_responds_to_stronger_signal():
    assert order_profitability_score(5, 5, 5) >= order_profitability_score(0, 0, 0)
