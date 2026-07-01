from shoptalk.order_exception_score import order_exception_score


def test_order_exception_score_bounds():
    assert 0 <= order_exception_score(3, True, True) <= 100


def test_order_exception_score_separates_strong_and_weak_signal():
    assert order_exception_score(3, True, True) > order_exception_score(0, False, False)
