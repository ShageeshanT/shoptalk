from shoptalk.message_priority import (
    message_priority_label,
    message_priority_score,
    normalize_priority_label,
)


def test_message_priority_scores_urgent_negative_replies_high() -> None:
    assert message_priority_score("high", "negative", True) == 100


def test_priority_label_marks_critical_messages() -> None:
    assert message_priority_label("high", "negative", True) == "critical"


def test_priority_label_marks_normal_messages() -> None:
    assert message_priority_label("normal", "neutral", False) == "normal"


def test_normalize_priority_label_handles_low_scores() -> None:
    assert normalize_priority_label(0) == "low"
