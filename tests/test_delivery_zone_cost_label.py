from shoptalk.delivery_zone_cost_label import classify_delivery_zone_cost


def test_classify_delivery_zone_cost_labels_key_states():
    assert classify_delivery_zone_cost(2) == "Near zone"
    assert classify_delivery_zone_cost(3) == "Standard zone"
    assert classify_delivery_zone_cost(10) == "Far zone"
