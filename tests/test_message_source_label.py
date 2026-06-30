from shoptalk.message_source_label import message_source_label

def test_message_source_label():
    assert message_source_label("wa") == "WhatsApp"
