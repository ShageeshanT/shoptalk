from shoptalk.buyer_intent import buyer_intent


def test_buyer_intent_detects_purchase():
    assert buyer_intent("Can I order two cakes?") == "purchase"


def test_buyer_intent_defaults_general():
    assert buyer_intent("hello there") == "general"
