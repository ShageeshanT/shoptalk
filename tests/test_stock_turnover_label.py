from shoptalk.stock_turnover_label import stock_turnover_label

def test_stock_turnover_label_thresholds():
    assert stock_turnover_label(7) == 'Fast moving'
    assert stock_turnover_label(30) == 'Normal moving'
    assert stock_turnover_label(90) == 'Slow moving'

def test_stock_turnover_label_invalid_value():
    assert stock_turnover_label("bad") == 'Stale stock'
