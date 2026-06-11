    from shoptalk.message_intent_label import classify_message_intent


    def test_classify_message_intent_labels_key_states():
        assert classify_message_intent(-1) == 'Unclear'
assert classify_message_intent(40) == 'Likely'
assert classify_message_intent(80) == 'Clear'
