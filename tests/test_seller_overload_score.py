from shoptalk.seller_overload_score import seller_overload_score


def test_seller_overload_score_bounds():
    assert 0 <= seller_overload_score(12, 9, 10) <= 100


def test_seller_overload_score_separates_strong_and_weak_signal():
    assert seller_overload_score(12, 9, 10) > seller_overload_score(1, 1, 1)
