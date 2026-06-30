from shoptalk.customer_intent_bucket import customer_intent_bucket

def test_customer_intent_bucket():
    assert customer_intent_bucket("price please") == "pricing"
