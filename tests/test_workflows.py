from shoptalk.analyzer import analyze_message
from shoptalk.catalog import CatalogItem, match_catalog_items
from shoptalk.schemas import MessageAnalyzeRequest


def test_home_bakery_message_becomes_order_intent() -> None:
    analysis = analyze_message(
        MessageAnalyzeRequest(
            text="Hi, I want 2 chocolate cake boxes tomorrow."
        )
    )

    assert analysis.intent == "new_order"
    assert analysis.urgency in {"normal", "high"}
    assert analysis.customer_needs_reply is True


def test_catalog_match_finds_relevant_product() -> None:
    catalog = [
        CatalogItem(name="Chocolate Brownie Box", tags=["brownie", "chocolate"]),
        CatalogItem(name="Ribbon Cake", tags=["cake"]),
    ]
    matches = match_catalog_items("Do you have brownies?", catalog)

    assert matches
    assert matches[0].item.name == "Chocolate Brownie Box"
