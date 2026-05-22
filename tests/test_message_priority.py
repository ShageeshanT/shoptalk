from shoptalk.message_priority import message_priority_score


def test_message_priority_scores_urgent_negative_replies_high() -> None:
    assert message_priority_score("high", "negative", True) == 100
