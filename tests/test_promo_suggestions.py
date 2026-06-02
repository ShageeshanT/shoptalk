from shoptalk.promo_suggestions import promo_suggestion


def test_promo_suggestion_rewards_repeat_customers():
    assert "loyalty" in promo_suggestion("in_stock", repeat_customer=True)


def test_promo_suggestion_avoids_unavailable_items():
    assert "unavailable" in promo_suggestion("out_of_stock")
