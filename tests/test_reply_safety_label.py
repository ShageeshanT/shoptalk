    from shoptalk.reply_safety_label import classify_reply_safety


    def test_classify_reply_safety_labels_key_states():
        assert classify_reply_safety(-1) == 'Safe'
assert classify_reply_safety(1) == 'Review'
assert classify_reply_safety(3) == 'Block'
