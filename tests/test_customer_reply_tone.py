from shoptalk.customer_reply_tone import customer_reply_tone

def test_customer_reply_tone():
    assert customer_reply_tone("refund please") == "calm recovery"
    assert customer_reply_tone("thanks") == "warm appreciation"
