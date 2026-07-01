from shoptalk.seller_response_load_score import seller_response_load_score


def test_seller_response_load_score_bounds():
    assert 0 <= seller_response_load_score(8, 3, 0, False, True) <= 100


def test_seller_response_load_score_separates_strong_and_weak_signal():
    assert seller_response_load_score(8, 3, 0, False, True) > seller_response_load_score(1, 0, 3, True, False)
