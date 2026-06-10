from shoptalk.seller_mood_label import seller_mood_label

def test_seller_mood_label_thresholds():
    assert seller_mood_label(80) == 'Great day'
    assert seller_mood_label(50) == 'Steady day'
    assert seller_mood_label(20) == 'Needs attention'

def test_seller_mood_label_invalid_value():
    assert seller_mood_label("bad") == 'Rough day'
