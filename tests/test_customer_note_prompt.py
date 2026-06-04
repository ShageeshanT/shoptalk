from shoptalk.customer_note_prompt import customer_note_prompt


def test_customer_note_prompt_basic():
    assert customer_note_prompt("Amal") == "Note anything important about Amal."


def test_customer_note_prompt_last_order():
    assert customer_note_prompt("Amal", "cupcake") == "Note anything important about Amal's cupcake order."
