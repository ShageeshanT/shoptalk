from shoptalk.contact_channel_badge import contact_channel_badge

def test_contact_channel_badge_known_values():
    assert contact_channel_badge('whatsapp') == 'WhatsApp contact'
    assert contact_channel_badge('email') == 'Email contact'
    assert contact_channel_badge('phone') == 'Phone contact'

def test_contact_channel_badge_unknown_value():
    assert contact_channel_badge("") == 'No contact'
