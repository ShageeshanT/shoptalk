    from shoptalk.followup_window_label import classify_followup_window


    def test_classify_followup_window_labels_key_states():
        assert classify_followup_window(-1) == 'Overdue'
assert classify_followup_window(0) == 'Soon'
assert classify_followup_window(10) == 'Later'
