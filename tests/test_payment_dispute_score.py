from shoptalk.payment_dispute_score import payment_dispute_score


def test_payment_dispute_score_bounds():
    assert 0 <= payment_dispute_score(25000, 6, True) <= 100


def test_payment_dispute_score_separates_strong_and_weak_signal():
    assert payment_dispute_score(25000, 6, True) > payment_dispute_score(0, 0, False)
