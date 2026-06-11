    from shoptalk.reply_clarity_label import classify_reply_clarity


    def test_classify_reply_clarity_labels_key_states():
        assert classify_reply_clarity(-1) == 'Too short'
assert classify_reply_clarity(3) == 'Clear'
assert classify_reply_clarity(50) == 'Too long'
