from shoptalk.chat_source_label import label_chat_source


def test_chat_source_label():
    assert label_chat_source("wa-web") == "whatsapp"
