from shoptalk.queue_pressure_label import classify_queue_pressure


def test_classify_queue_pressure_labels_key_states():
    assert classify_queue_pressure(-1) == 'Clear'
    assert classify_queue_pressure(1) == 'Light'
    assert classify_queue_pressure(4) == 'Busy'
    assert classify_queue_pressure(10) == 'Overloaded'
