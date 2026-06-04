from shoptalk.catalog_gap_prompt import catalog_gap_prompt


def test_catalog_gap_prompt_item():
    assert catalog_gap_prompt("brownie box") == "Add price, availability, and delivery notes for brownie box."


def test_catalog_gap_prompt_default():
    assert catalog_gap_prompt("") == "Add price, availability, and delivery notes for this item."
