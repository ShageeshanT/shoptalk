from shoptalk.customer_reply_gap_label import label_customer_reply_gap


def test_customer_reply_gap_label():
    assert label_customer_reply_gap(130) == "urgent"
