from shoptalk.seller_reliability_score import seller_reliability_score

def test_seller_reliability_score_stays_in_bounds():
    assert 0 <= seller_reliability_score(0, 0, 0) <= 100
    assert 0 <= seller_reliability_score(5, 5, 5) <= 100

def test_seller_reliability_score_responds_to_stronger_signal():
    assert seller_reliability_score(5, 5, 5) >= seller_reliability_score(0, 0, 0)
