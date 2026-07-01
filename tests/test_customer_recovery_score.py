from shoptalk.customer_recovery_score import customer_recovery_score


def test_customer_recovery_score_bounds():
    assert 0 <= customer_recovery_score(0, 0) <= 100


def test_customer_recovery_score_prioritizes_good_lapsed_customers():
    assert customer_recovery_score(120, 6, 5) > customer_recovery_score(5, 1, 2)
