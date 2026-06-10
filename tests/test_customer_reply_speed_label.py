from shoptalk.customer_reply_speed_label import customer_reply_speed_label

def test_customer_reply_speed_label_thresholds():
    assert customer_reply_speed_label(5) == 'Instant reply'
    assert customer_reply_speed_label(60) == 'Same hour reply'
    assert customer_reply_speed_label(1440) == 'Same day reply'

def test_customer_reply_speed_label_invalid_value():
    assert customer_reply_speed_label("bad") == 'Slow reply'
