from shoptalk.conversation_flags import conversation_flags


def test_conversation_flags_detects_attention_and_time():
    flags = conversation_flags("urgent refund needed today")
    assert "needs_owner_attention" in flags
    assert "time_sensitive" in flags


def test_conversation_flags_detects_payment_related():
    assert "payment_related" in conversation_flags("I paid and sent the receipt")
