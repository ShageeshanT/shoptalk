from shoptalk.customer_trust_score import customer_trust_score


def test_customer_trust_score_bounds():
    assert 0 <= customer_trust_score(8, 0, 0) <= 100


def test_customer_trust_score_separates_strong_and_weak_signal():
    assert customer_trust_score(8, 0, 0) > customer_trust_score(1, 3, 2)
