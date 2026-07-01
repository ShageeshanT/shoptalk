from shoptalk.stock_pressure_score import stock_pressure_score


def test_stock_pressure_score_bounds():
    assert 0 <= stock_pressure_score(10, 0, 4) <= 100


def test_stock_pressure_score_separates_strong_and_weak_signal():
    assert stock_pressure_score(10, 0, 4) > stock_pressure_score(1, 20, 0)
