from shoptalk.tag_normalizer import tag_normalizer

def test_tag_normalizer():
    assert tag_normalizer([" VIP ","vip","New Lead"])==["vip","new_lead"]