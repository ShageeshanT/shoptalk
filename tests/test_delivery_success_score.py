from shoptalk.delivery_success_score import delivery_success_score

def test_delivery_success_score_stays_in_bounds():
    assert 0 <= delivery_success_score(0, 0, 0) <= 100
    assert 0 <= delivery_success_score(5, 5, 5) <= 100

def test_delivery_success_score_responds_to_stronger_signal():
    assert delivery_success_score(5, 5, 5) >= delivery_success_score(0, 0, 0)
