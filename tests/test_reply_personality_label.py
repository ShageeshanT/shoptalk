    from shoptalk.reply_personality_label import classify_reply_personality


    def test_classify_reply_personality_labels_key_states():
        assert classify_reply_personality(-1) == 'Plain'
assert classify_reply_personality(1) == 'Friendly'
assert classify_reply_personality(4) == 'Too much'
