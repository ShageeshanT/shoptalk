from shoptalk.thread_summary_label import classify_thread_summary


def test_classify_thread_summary_labels_key_states():
    assert classify_thread_summary(-1) == 'Missing'
    assert classify_thread_summary(1) == 'Short'
    assert classify_thread_summary(4) == 'Detailed'
