from shoptalk.seller_burnout_score import seller_burnout_score

def test_seller_burnout_score_stays_in_bounds():
    assert 0 <= seller_burnout_score(0, 0, 0) <= 100
    assert 0 <= seller_burnout_score(5, 5, 5) <= 100

def test_seller_burnout_score_responds_to_stronger_signal():
    assert seller_burnout_score(5, 5, 5) >= seller_burnout_score(0, 0, 0)
