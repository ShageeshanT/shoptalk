from shoptalk.seller_sla_label import classify_seller_sla


def test_classify_seller_sla_labels_key_states():
    assert classify_seller_sla(29) == "On track"
    assert classify_seller_sla(30) == "Watch"
    assert classify_seller_sla(120) == "Late"
