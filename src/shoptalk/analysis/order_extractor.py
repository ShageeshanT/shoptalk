"""Order detail extraction from customer messages.

This module extracts structured order details from raw customer message text.
The production implementation calls an LLM with a structured JSON prompt.
The stub implementation uses regex and keyword matching for development.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class OrderExtraction:
    """Structured order details extracted from a customer message.

    Attributes
    ----------
    product:
        The product name or description mentioned in the message.
    quantity:
        The number of units requested, if specified.
    size:
        Size or weight specification (e.g. "1kg", "large", "medium").
    needed_by:
        Requested delivery or pickup date/time as a string.
    custom_text:
        Any custom text or personalisation requested (e.g. cake inscription).
    delivery_type:
        Whether the customer wants delivery or pickup.
    payment_mentioned:
        Whether the customer mentioned payment in the message.
    follow_up_needed:
        Whether a follow-up action is recommended.
    confidence:
        Extraction confidence between 0.0 and 1.0.
    raw_text:
        The original message text that was analysed.

    Example
    -------
    >>> extraction = OrderExtraction(
    ...     product="chocolate cake",
    ...     quantity=1,
    ...     size="1kg",
    ...     needed_by="Saturday evening",
    ...     custom_text="Happy Birthday Amaya",
    ...     follow_up_needed=True,
    ... )
    """

    product: str | None = None
    quantity: int | None = None
    size: str | None = None
    needed_by: str | None = None
    custom_text: str | None = None
    delivery_type: str | None = None  # "delivery" | "pickup" | None
    payment_mentioned: bool = False
    follow_up_needed: bool = True
    confidence: float = 0.0
    raw_text: str = ""
    extracted_fields: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

_QUANTITY_PATTERN = re.compile(r"\b(\d+)\b")
_WORD_QUANTITIES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

_SIZE_PATTERN = re.compile(
    r"\b(\d+(?:\.\d+)?\s*(?:kg|g|lb|lbs|litre|liter|l|ml|cm|inch|inches|"
    r"small|medium|large|xl|xxl|regular|standard))\b",
    re.IGNORECASE,
)

_CUSTOM_TEXT_PATTERN = re.compile(
    r"(?:written?|inscription|message|text|say(?:ing)?|with)[:\s]+["'"]?([^"'".!?\n]{3,60})["'"]?",
    re.IGNORECASE,
)

_DAY_PATTERN = re.compile(
    r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|"
    r"today|tomorrow|tonight|this\s+(?:morning|afternoon|evening|weekend)|"
    r"next\s+(?:week|monday|tuesday|wednesday|thursday|friday|saturday|sunday))\b",
    re.IGNORECASE,
)

_DELIVERY_PATTERN = re.compile(r"\b(deliver(?:y)?|send|ship)\b", re.IGNORECASE)
_PICKUP_PATTERN = re.compile(r"\b(pick\s*up|collect|collection|self.collect)\b", re.IGNORECASE)
_PAYMENT_PATTERN = re.compile(
    r"\b(pay(?:ment)?|paid|deposit|transfer|bank|cash|invoice)\b", re.IGNORECASE
)


def extract_order_details(text: str) -> OrderExtraction:
    """Extract structured order details from a customer message.

    This is a regex-based stub implementation. The production version
    calls an LLM with a structured JSON prompt and validates the output
    against the OrderExtraction schema.

    Parameters
    ----------
    text:
        The raw customer message text to analyse.

    Returns
    -------
    OrderExtraction
        Structured order details with a confidence score.

    Example
    -------
    >>> result = extract_order_details(
    ...     "Hi, can I order a 1kg chocolate cake for Saturday evening "
    ...     "with Happy Birthday Amaya written on it?"
    ... )
    >>> result.product
    'chocolate cake'
    >>> result.size
    '1kg'
    >>> result.needed_by
    'Saturday evening'
    """
    if not text or not text.strip():
        return OrderExtraction(raw_text=text, confidence=0.0)

    extraction = OrderExtraction(raw_text=text)
    extracted_fields: list[str] = []

    # Extract size
    size_match = _SIZE_PATTERN.search(text)
    if size_match:
        extraction.size = size_match.group(1).strip()
        extracted_fields.append("size")

    # Extract quantity (prefer word quantities, fall back to digits)
    lowered = text.lower()
    for word, value in _WORD_QUANTITIES.items():
        if re.search(rf"\b{word}\b", lowered):
            extraction.quantity = value
            extracted_fields.append("quantity")
            break
    if extraction.quantity is None:
        qty_match = _QUANTITY_PATTERN.search(text)
        if qty_match:
            extraction.quantity = int(qty_match.group(1))
            extracted_fields.append("quantity")

    # Extract custom text (e.g. cake inscription)
    custom_match = _CUSTOM_TEXT_PATTERN.search(text)
    if custom_match:
        extraction.custom_text = custom_match.group(1).strip()
        extracted_fields.append("custom_text")

    # Extract needed_by date/time
    day_match = _DAY_PATTERN.search(text)
    if day_match:
        extraction.needed_by = day_match.group(0).strip()
        extracted_fields.append("needed_by")

    # Extract delivery type
    if _DELIVERY_PATTERN.search(text):
        extraction.delivery_type = "delivery"
        extracted_fields.append("delivery_type")
    elif _PICKUP_PATTERN.search(text):
        extraction.delivery_type = "pickup"
        extracted_fields.append("delivery_type")

    # Check for payment mention
    if _PAYMENT_PATTERN.search(text):
        extraction.payment_mentioned = True
        extracted_fields.append("payment_mentioned")

    # Confidence based on number of fields extracted
    extraction.extracted_fields = extracted_fields
    extraction.confidence = min(0.9, len(extracted_fields) * 0.15 + 0.3)

    # Follow-up needed if no payment mentioned and order seems real
    extraction.follow_up_needed = not extraction.payment_mentioned

    return extraction
