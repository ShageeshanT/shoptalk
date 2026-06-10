from shoptalk.reply_tone_label import reply_tone_label

def test_reply_tone_label_known_values():
    assert reply_tone_label('friendly') == 'Friendly'
    assert reply_tone_label('formal') == 'Formal'
    assert reply_tone_label('urgent') == 'Urgent'

def test_reply_tone_label_unknown_value():
    assert reply_tone_label("") == 'Neutral'
