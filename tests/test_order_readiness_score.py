from shoptalk.order_readiness_score import order_readiness_score

def test_order_readiness_score_stays_in_bounds():
    assert 0 <= order_readiness_score(0, 0, 0) <= 100
    assert 0 <= order_readiness_score(5, 5, 5) <= 100

def test_order_readiness_score_responds_to_stronger_signal():
    assert order_readiness_score(5, 5, 5) >= order_readiness_score(0, 0, 0)
