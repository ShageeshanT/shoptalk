from shoptalk.reply_tone import choose_reply_tone


def test_choose_apologetic_tone():
    assert choose_reply_tone("This is bad, I want refund") == "apologetic"


def test_choose_warm_tone():
    assert choose_reply_tone("Thank you") == "warm"


def test_choose_helpful_or_neutral_tone():
    assert choose_reply_tone("How much is it?") == "helpful"
    assert choose_reply_tone("ok") == "neutral"
