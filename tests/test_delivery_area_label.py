from shoptalk.delivery_area_label import delivery_area_label


def test_delivery_area_label():
    assert delivery_area_label(7) == "city"
