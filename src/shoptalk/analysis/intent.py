"""Intent extraction for customer messages.

This module extracts the intent and urgency from raw customer message text.
The production implementation calls an LLM with structured JSON output.
The stub implementation uses rule-based heuristics so the API is runnable
without API keys during development.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class IntentResult:
    """The result of intent extraction for a single message.

    Attributes
    ----------
    intent:
        The primary intent detected in the message.
        One of: new_order, payment_question, delivery_question,
        product_inquiry, complaint, general, unknown.
    urgency:
        The urgency level of the message. One of: high, normal, low.
    confidence:
        A float between 0.0 and 1.0 indicating extraction confidence.
        Rule-based extraction returns 0.7; LLM extraction returns the
        model's self-reported confidence.
    keywords:
        The keywords or phrases that triggered the detected intent.
    raw_text:
        The original message text that was analysed.

    Example
    -------
    >>> result = IntentResult(
    ...     intent="new_order",
    ...     urgency="normal",
    ...     confidence=0.9,
    ...     keywords=["order", "cake"],
    ...     raw_text="Hi, can I order a chocolate cake?",
    ... )
    """

    intent: str
    urgency: str
    confidence: float
    keywords: list[str] = field(default_factory=list)
    raw_text: str = ""


# ---------------------------------------------------------------------------
# Rule-based implementation (development stub)
# ---------------------------------------------------------------------------

_ORDER_MARKERS = [
    "order", "i want", "can i get", "can i have", "book", "need",
    "i'd like", "i would like", "place an order", "want to buy",
]

_COMPLAINT_MARKERS = [
    "refund", "angry", "bad review", "complain", "wrong", "late",
    "disappointed", "terrible", "awful", "unacceptable",
]

_PAYMENT_MARKERS = [
    "pay", "payment", "paid", "deposit", "bank transfer",
    "transfer", "invoice", "receipt", "how much",
]

_DELIVERY_MARKERS = [
    "deliver", "delivery", "pickup", "pick up", "where is my order",
    "when will", "tracking", "shipped", "dispatch",
]

_INQUIRY_MARKERS = [
    "available", "price", "how much", "do you have", "stock",
    "catalogue", "catalog", "what do you sell", "menu",
]

_URGENCY_HIGH_MARKERS = [
    "urgent", "today", "asap", "bad review", "now", "immediately",
    "right now", "emergency", "as soon as possible",
]

_URGENCY_LOW_MARKERS = [
    "whenever", "no rush", "take your time", "not urgent",
]


def _match_markers(text: str, markers: list[str]) -> list[str]:
    """Return the markers found in text."""
    lowered = text.lower()
    return [m for m in markers if re.search(rf"\b{re.escape(m)}\b", lowered)]


def extract_intent(text: str) -> IntentResult:
    """Extract intent and urgency from a customer message.

    This is a rule-based stub implementation. The production version
    calls an LLM with a structured JSON prompt and validates the output
    against the IntentResult schema.

    Parameters
    ----------
    text:
        The raw customer message text to analyse.

    Returns
    -------
    IntentResult
        The detected intent, urgency, confidence, and matched keywords.

    Example
    -------
    >>> result = extract_intent("Hi, can I order a chocolate cake for Saturday?")
    >>> result.intent
    'new_order'
    >>> result.urgency
    'normal'
    """
    if not text or not text.strip():
        return IntentResult(
            intent="unknown",
            urgency="normal",
            confidence=0.0,
            raw_text=text,
        )

    complaint_hits = _match_markers(text, _COMPLAINT_MARKERS)
    order_hits = _match_markers(text, _ORDER_MARKERS)
    payment_hits = _match_markers(text, _PAYMENT_MARKERS)
    delivery_hits = _match_markers(text, _DELIVERY_MARKERS)
    inquiry_hits = _match_markers(text, _INQUIRY_MARKERS)

    high_urgency_hits = _match_markers(text, _URGENCY_HIGH_MARKERS)
    low_urgency_hits = _match_markers(text, _URGENCY_LOW_MARKERS)

    # Determine intent by priority
    if complaint_hits:
        intent = "complaint"
        keywords = complaint_hits
    elif order_hits:
        intent = "new_order"
        keywords = order_hits
    elif payment_hits:
        intent = "payment_question"
        keywords = payment_hits
    elif delivery_hits:
        intent = "delivery_question"
        keywords = delivery_hits
    elif inquiry_hits:
        intent = "product_inquiry"
        keywords = inquiry_hits
    else:
        intent = "general"
        keywords = []

    # Determine urgency
    if high_urgency_hits:
        urgency = "high"
    elif low_urgency_hits:
        urgency = "low"
    else:
        urgency = "normal"

    return IntentResult(
        intent=intent,
        urgency=urgency,
        confidence=0.7,  # Rule-based confidence
        keywords=keywords,
        raw_text=text,
    )
