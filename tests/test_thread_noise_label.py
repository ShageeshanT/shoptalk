    from shoptalk.thread_noise_label import classify_thread_noise


    def test_classify_thread_noise_labels_key_states():
        assert classify_thread_noise(-1) == 'Quiet'
assert classify_thread_noise(3) == 'Active'
assert classify_thread_noise(30) == 'Noisy'
