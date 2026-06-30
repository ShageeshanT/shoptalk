from shoptalk.batch_prep_label import classify_batch_prep


def test_classify_batch_prep_labels_key_states():
    assert classify_batch_prep(1) == "Single prep"
    assert classify_batch_prep(2) == "Batch prep"
    assert classify_batch_prep(7) == "Large batch prep"
