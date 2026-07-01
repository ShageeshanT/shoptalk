from shoptalk.pickup_readiness_score import pickup_readiness_score


def test_pickup_readiness_score_bounds():
    assert 0 <= pickup_readiness_score(10, 10, 90) <= 100


def test_pickup_readiness_score_separates_strong_and_weak_signal():
    assert pickup_readiness_score(10, 10, 90) > pickup_readiness_score(1, 10, 5)
