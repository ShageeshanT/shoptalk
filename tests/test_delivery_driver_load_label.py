from shoptalk.delivery_driver_load_label import classify_delivery_driver_load


def test_classify_delivery_driver_load_labels_key_states():
    assert classify_delivery_driver_load(3) == "Light route"
    assert classify_delivery_driver_load(4) == "Normal route"
    assert classify_delivery_driver_load(9) == "Heavy route"
