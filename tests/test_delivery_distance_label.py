from shoptalk.delivery_distance_label import label_delivery_distance


def test_delivery_distance_label():
    assert label_delivery_distance(2) == "near"
