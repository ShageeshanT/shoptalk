from shoptalk.packing_delay_score import packing_delay_score


def test_packing_delay_score_bounds():
    assert 0 <= packing_delay_score(12, 20, False) <= 100


def test_packing_delay_score_separates_strong_and_weak_signal():
    assert packing_delay_score(12, 20, False) > packing_delay_score(1, 300, True)
