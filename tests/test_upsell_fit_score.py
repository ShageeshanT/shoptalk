from shoptalk.upsell_fit_score import upsell_fit_score


def test_upsell_fit_score_bounds():
    assert 0 <= upsell_fit_score(0) <= 100


def test_upsell_fit_score_rewards_repeat_large_orders():
    assert upsell_fit_score(12000, True, 4) > upsell_fit_score(500, False, 1)
