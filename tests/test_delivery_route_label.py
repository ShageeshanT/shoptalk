from shoptalk.delivery_route_label import classify_delivery_route


def test_classify_delivery_route_labels_key_states():
    assert classify_delivery_route(-1) == 'Direct'
    assert classify_delivery_route(2) == 'Route'
    assert classify_delivery_route(6) == 'Batch'
