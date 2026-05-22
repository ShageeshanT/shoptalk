from typing import Protocol

from shoptalk.schemas import MessageAnalysis, MessageAnalyzeRequest


class MessageAnalyzerProvider(Protocol):
    def analyze(self, payload: MessageAnalyzeRequest) -> MessageAnalysis:
        """Return structured analysis for a customer message."""
