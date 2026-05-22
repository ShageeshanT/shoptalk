from shoptalk.analyzer import analyze_message
from shoptalk.order_titles import title_from_analysis
from shoptalk.schemas import MessageAnalyzeRequest


def test_title_from_analysis_uses_product_quantity_and_size() -> None:
    analysis = analyze_message(MessageAnalyzeRequest(text="I need 2 cupcakes box of 6"))
    assert title_from_analysis(analysis) == "2X Cupcakes Box Of 6"
