from shoptalk.draft_safety_label import draft_safety_label

def test_draft_safety_label():
    assert draft_safety_label("hello") == "safe"
    assert draft_safety_label("stupid") == "needs review"
