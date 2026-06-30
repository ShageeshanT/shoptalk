from shoptalk.customer_tag_suggestor import customer_tag_suggestor

def test_customer_tag_suggestor():
    assert customer_tag_suggestor(10) == "vip"
    assert customer_tag_suggestor(1) == "new"
