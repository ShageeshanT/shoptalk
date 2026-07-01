from shoptalk.customer_save_score import customer_save_score


def test_customer_save_score_bounds():
    assert 0 <= customer_save_score(7, True, 4) <= 100


def test_customer_save_score_separates_strong_and_weak_signal():
    assert customer_save_score(7, True, 4) > customer_save_score(1, False, 0)
