from shoptalk.conversation_stage import detect_conversation_stage


def test_detects_ordering_stage():
    assert detect_conversation_stage("How much is the brownie box?") == "ordering"


def test_detects_payment_stage():
    assert detect_conversation_stage("I paid the deposit") == "payment"


def test_detects_fulfillment_stage():
    assert detect_conversation_stage("Can you deliver to Colombo?") == "fulfillment"


def test_defaults_to_general():
    assert detect_conversation_stage("hello") == "general"
