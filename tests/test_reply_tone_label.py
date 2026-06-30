from shoptalk.reply_tone_label import label_reply_tone


def test_reply_tone_label():
    assert label_reply_tone(True) == "soft"
