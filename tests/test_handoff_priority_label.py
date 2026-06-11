    from shoptalk.handoff_priority_label import classify_handoff_priority


    def test_classify_handoff_priority_labels_key_states():
        assert classify_handoff_priority(-1) == 'Normal'
assert classify_handoff_priority(3) == 'Important'
assert classify_handoff_priority(10) == 'Urgent'
