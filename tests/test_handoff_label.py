from shoptalk.handoff_label import handoff_label

def test_handoff_label():
    assert handoff_label(True)=="Human review needed"