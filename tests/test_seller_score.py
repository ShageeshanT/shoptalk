from shoptalk.seller_score import seller_health_label, seller_health_score


def test_seller_health_score_penalizes_open_work() -> None:
    assert seller_health_score(open_followups=0, pending_payments=0, unanswered_messages=0) == 100
    assert seller_health_score(open_followups=2, pending_payments=1, unanswered_messages=3) == 38
    assert seller_health_score(open_followups=20, pending_payments=20, unanswered_messages=20) == 0


def test_seller_health_label() -> None:
    assert seller_health_label(90) == "healthy"
    assert seller_health_label(70) == "needs_attention"
    assert seller_health_label(30) == "at_risk"
