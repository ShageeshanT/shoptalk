from shoptalk.sla import response_sla_label


def test_response_sla_label_marks_high_scores_reply_now() -> None:
    assert response_sla_label(85) == "reply_now"
    assert response_sla_label(45) == "reply_today"
