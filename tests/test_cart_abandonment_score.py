from shoptalk.cart_abandonment_score import cart_abandonment_score


def test_cart_abandonment_score_bounds():
    assert 0 <= cart_abandonment_score(0, 0, False) <= 100


def test_cart_abandonment_score_rises_with_stale_loaded_cart():
    assert cart_abandonment_score(300, 4, True) > cart_abandonment_score(10, 1, False)
