from shoptalk.conversation_health_label import conversation_health_label

def test_conversation_health_label():
    assert conversation_health_label(0, 1) == "recovery"
