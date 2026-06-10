from shoptalk.handoff_priority_label import handoff_priority_label

def test_handoff_priority_label_thresholds():
    assert handoff_priority_label(3) == 'Urgent handoff'
    assert handoff_priority_label(2) == 'Normal handoff'
    assert handoff_priority_label(1) == 'Low handoff'

def test_handoff_priority_label_invalid_value():
    assert handoff_priority_label("bad") == 'No handoff'
