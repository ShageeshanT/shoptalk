from shoptalk.reply_delay_bucket import reply_delay_bucket

def test_reply_delay_bucket():
    assert reply_delay_bucket(130) == "late"
