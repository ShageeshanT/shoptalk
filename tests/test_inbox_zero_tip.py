from shoptalk.inbox_zero_tip import inbox_zero_tip


def test_inbox_zero_tip_clear():
    assert inbox_zero_tip(0, 0) == "Inbox is clear."


def test_inbox_zero_tip_overdue():
    assert inbox_zero_tip(5, 1) == "Start with overdue customer threads."
