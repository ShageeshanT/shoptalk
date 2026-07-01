from shoptalk.stock_health_score import stock_health_score

def test_stock_health_score_stays_in_bounds():
    assert 0 <= stock_health_score(0, 0, 0) <= 100
    assert 0 <= stock_health_score(5, 5, 5) <= 100

def test_stock_health_score_responds_to_stronger_signal():
    assert stock_health_score(5, 5, 5) >= stock_health_score(0, 0, 0)
