from shoptalk.intent_label import intent_label

def test_intent_label():
    assert intent_label("new_order")=="New Order"