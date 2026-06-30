from shoptalk.seller_reply_effort_label import classify_seller_reply_effort


def test_classify_seller_reply_effort_labels_key_states():
    assert classify_seller_reply_effort(19) == "Quick reply"
    assert classify_seller_reply_effort(20) == "Normal reply"
    assert classify_seller_reply_effort(60) == "Long reply"
