from shoptalk.customer_question_label import classify_customer_question


def test_classify_customer_question_labels_key_states():
    assert classify_customer_question(-1) == 'None'
    assert classify_customer_question(1) == 'Simple'
    assert classify_customer_question(3) == 'Many'
