from shoptalk.payment_collection_score import payment_collection_score

def test_payment_collection_score_stays_in_bounds():
    assert 0 <= payment_collection_score(0, 0, 0) <= 100
    assert 0 <= payment_collection_score(5, 5, 5) <= 100

def test_payment_collection_score_responds_to_stronger_signal():
    assert payment_collection_score(5, 5, 5) >= payment_collection_score(0, 0, 0)
