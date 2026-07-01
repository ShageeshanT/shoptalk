from shoptalk.promo_fatigue_score import promo_fatigue_score


def test_promo_fatigue_score_bounds():
    assert 0 <= promo_fatigue_score(6, 0, 0) <= 100


def test_promo_fatigue_score_separates_strong_and_weak_signal():
    assert promo_fatigue_score(6, 0, 0) > promo_fatigue_score(1, 5, 2)
