from shoptalk.customer_profile_score import customer_profile_score


def test_customer_profile_score_bounds():
    assert 0 <= customer_profile_score(True, True, True, True) <= 100


def test_customer_profile_score_separates_strong_and_weak_signal():
    assert customer_profile_score(True, True, True, True) > customer_profile_score(True, False, False, False)
