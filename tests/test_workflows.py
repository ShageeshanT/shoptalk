from shoptalk.analyzer import analyze_message
from shoptalk.catalog import match_catalog_items
from shoptalk.schemas import CatalogMatchRequest, MessageAnalyzeRequest


def test_home_bakery_message_becomes_order_intent() -> None:
    analysis = analyze_message(
        MessageAnalyzeRequest(
            text="Hi, need 2 chocolate cake boxes tomorrow. Can I pay after confirming?"
        )
    )

    assert analysis.intent == "order"
    assert analysis.urgency in {"normal", "high"}
    assert "payment" in analysis.suggested_actions


def test_catalog_match_finds_relevant_product() -> None:
    matches = match_catalog_items(
        CatalogMatchRequest(
            message="Do you have brownies?",
            catalog=[
                {"name": "Chocolate Brownie Box", "tags": ["brownie", "chocolate"]},
                {"name": "Ribbon Cake", "tags": ["cake"]},
            ],
        )
    )

    assert matches
    assert matches[0].item["name"] == "Chocolate Brownie Box"
