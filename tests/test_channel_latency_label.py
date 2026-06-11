from shoptalk.channel_latency_label import classify_channel_latency


def test_classify_channel_latency_labels_key_states():
    assert classify_channel_latency(-1) == 'Live'
    assert classify_channel_latency(6) == 'Delayed'
    assert classify_channel_latency(70) == 'Dormant'
