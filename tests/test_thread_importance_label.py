from shoptalk.thread_importance_label import classify_thread_importance


def test_classify_thread_importance_labels_key_states():
    assert classify_thread_importance(-1) == 'Low'
    assert classify_thread_importance(30) == 'Medium'
    assert classify_thread_importance(70) == 'High'
