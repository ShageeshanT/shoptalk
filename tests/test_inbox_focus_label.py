    from shoptalk.inbox_focus_label import classify_inbox_focus


    def test_classify_inbox_focus_labels_key_states():
        assert classify_inbox_focus(-1) == 'Clear'
assert classify_inbox_focus(1) == 'Focus'
assert classify_inbox_focus(30) == 'Overflow'
