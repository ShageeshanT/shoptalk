from shoptalk.fulfillment_delay_label import label_fulfillment_delay


def test_fulfillment_delay_label():
    assert label_fulfillment_delay(3) == "delayed"
