from shoptalk.order_channel_label import order_channel_label

def test_order_channel_label_known_channels():
    assert order_channel_label("whatsapp") == "WhatsApp"
    assert order_channel_label("web") == "Website"

def test_order_channel_label_unknown_channel():
    assert order_channel_label("sms") == "Manual"
