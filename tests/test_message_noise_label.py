from shoptalk.message_noise_label import classify_message_noise


def test_classify_message_noise_labels_key_states():
    assert classify_message_noise(2) == "Clean thread"
    assert classify_message_noise(3) == "Some noise"
    assert classify_message_noise(8) == "Noisy thread"
