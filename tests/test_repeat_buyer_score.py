from shoptalk.repeat_buyer_score import repeat_buyer_score


def test_repeat_buyer_score_bounds():
    assert 0 <= repeat_buyer_score(6, 10, 0) <= 100


def test_repeat_buyer_score_separates_strong_and_weak_signal():
    assert repeat_buyer_score(6, 10, 0) > repeat_buyer_score(1, 400, 3)
