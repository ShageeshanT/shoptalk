from shoptalk.delivery_promise_score import delivery_promise_score


def test_delivery_promise_score_bounds():
    assert 0 <= delivery_promise_score(-5, False, False) <= 100


def test_delivery_promise_score_separates_strong_and_weak_signal():
    assert delivery_promise_score(-5, False, False) > delivery_promise_score(180, True, True)
