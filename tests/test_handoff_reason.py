from shoptalk.handoff_reason import handoff_reason


def test_handoff_reason_angry_wins():
    assert handoff_reason(True, True, True) == "angry_customer"


def test_handoff_reason_none():
    assert handoff_reason(False, False, False) == "no_handoff_needed"
