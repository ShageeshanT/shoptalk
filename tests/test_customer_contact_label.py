from shoptalk.customer_contact_label import customer_contact_label


def test_customer_contact_label():
    assert customer_contact_label(phone="+9477") == "Phone available"
    assert customer_contact_label(email="a@example.com") == "Email available"
    assert customer_contact_label() == "No contact details"