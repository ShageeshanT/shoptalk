from shoptalk.refund_urgency_score import refund_urgency_score

def test_refund_urgency_score_stays_in_bounds():
    assert 0 <= refund_urgency_score(0, 0, 0) <= 100
    assert 0 <= refund_urgency_score(5, 5, 5) <= 100

def test_refund_urgency_score_responds_to_stronger_signal():
    assert refund_urgency_score(5, 5, 5) >= refund_urgency_score(0, 0, 0)
