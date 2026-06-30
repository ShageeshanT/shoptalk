from shoptalk.customer_reply_mood_label import classify_customer_reply_mood


def test_classify_customer_reply_mood_labels_key_states():
    assert classify_customer_reply_mood(39) == "Tense reply"
    assert classify_customer_reply_mood(40) == "Neutral reply"
    assert classify_customer_reply_mood(75) == "Warm reply"
