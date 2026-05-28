from shoptalk.inbox_badges import inbox_badges


def test_inbox_badges_empty():
    assert inbox_badges(False, False, False) == []


def test_inbox_badges_ordered_by_importance():
    assert inbox_badges(True, True, True) == ["needs_reply", "order", "payment"]
