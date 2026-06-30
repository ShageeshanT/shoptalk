from shoptalk.handoff_sla_label import classify_handoff_sla


def test_classify_handoff_sla_labels_key_states():
    assert classify_handoff_sla(14) == "Normal handoff"
    assert classify_handoff_sla(15) == "Watch handoff"
    assert classify_handoff_sla(45) == "Urgent handoff"
