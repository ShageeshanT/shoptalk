from shoptalk.reply_queue_label import reply_queue_label


def test_reply_queue_label():
    assert reply_queue_label(12) == "overloaded"
