from shoptalk.promo_readiness_score import promo_readiness_score

def test_promo_readiness_score_stays_in_bounds():
    assert 0 <= promo_readiness_score(0, 0, 0) <= 100
    assert 0 <= promo_readiness_score(5, 5, 5) <= 100

def test_promo_readiness_score_responds_to_stronger_signal():
    assert promo_readiness_score(5, 5, 5) >= promo_readiness_score(0, 0, 0)
