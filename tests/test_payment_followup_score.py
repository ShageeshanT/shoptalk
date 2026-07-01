from shoptalk.payment_followup_score import payment_followup_score


def test_payment_followup_score_bounds():
    assert 0 <= payment_followup_score(30000, 72, False) <= 100


def test_payment_followup_score_separates_strong_and_weak_signal():
    assert payment_followup_score(30000, 72, False) > payment_followup_score(1000, 1, True)
