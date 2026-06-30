from shoptalk.payment_proof_label import classify_payment_proof


def test_classify_payment_proof_labels_key_states():
    assert classify_payment_proof(49) == "Proof unclear"
    assert classify_payment_proof(50) == "Proof likely"
    assert classify_payment_proof(80) == "Proof strong"
