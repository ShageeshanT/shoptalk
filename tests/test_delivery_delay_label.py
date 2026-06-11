from shoptalk.delivery_delay_label import classify_delivery_delay


def test_classify_delivery_delay_labels_key_states():
    assert classify_delivery_delay(-1) == 'On time'
    assert classify_delivery_delay(1) == 'Late'
    assert classify_delivery_delay(70) == 'Critical'
