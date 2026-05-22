from shoptalk.analyzer import analyze_message
from shoptalk.demo_scenarios import HOME_BAKER_SCENARIOS
from shoptalk.schemas import MessageAnalyzeRequest


def test_home_baker_demo_scenarios_match_expected_intents() -> None:
    for scenario in HOME_BAKER_SCENARIOS:
        analysis = analyze_message(MessageAnalyzeRequest(text=scenario.customer_message))
        assert analysis.intent == scenario.expected_intent
