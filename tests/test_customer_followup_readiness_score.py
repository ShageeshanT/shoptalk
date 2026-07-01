from shoptalk.customer_followup_readiness_score import customer_followup_readiness_score


def test_customer_followup_readiness_score_bounds():
    assert 0 <= customer_followup_readiness_score(True, True, True, True, True) <= 100


def test_customer_followup_readiness_score_separates_strong_and_weak_signal():
    assert customer_followup_readiness_score(True, True, True, True, True) > customer_followup_readiness_score(True, False, False, False, False)
