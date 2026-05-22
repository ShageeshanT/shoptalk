from shoptalk.ai_provider import MessageAnalyzerProvider
from shoptalk.analyzer import analyze_message
from shoptalk.schemas import MessageAnalyzeRequest


class RuleBasedProvider:
    def analyze(self, payload: MessageAnalyzeRequest):
        return analyze_message(payload)


def test_rule_based_provider_matches_analyzer_protocol() -> None:
    provider: MessageAnalyzerProvider = RuleBasedProvider()
    assert provider.analyze(MessageAnalyzeRequest(text="need cake")).intent == "new_order"
