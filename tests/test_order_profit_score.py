from shoptalk.order_profit_score import order_profit_score


def test_order_profit_score_bounds():
    assert 0 <= order_profit_score(10000, 5000, 500) <= 100


def test_order_profit_score_separates_strong_and_weak_signal():
    assert order_profit_score(10000, 5000, 500) > order_profit_score(10000, 9500, 1000)
