from shoptalk.delivery_route_score import delivery_route_score


def test_delivery_route_score_bounds():
    assert 0 <= delivery_route_score(12, 3, 3) <= 100


def test_delivery_route_score_separates_strong_and_weak_signal():
    assert delivery_route_score(12, 3, 3) > delivery_route_score(1, 0, 0)
