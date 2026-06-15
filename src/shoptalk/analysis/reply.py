"""Reply drafting for customer messages.

This module generates suggested reply drafts based on the analysis of
a customer message. The production implementation calls an LLM with
the message context and business tone settings.

The stub implementation returns template-based replies so the API is
runnable without API keys during development.
"""

from __future__ import annotations

from dataclasses import dataclass

from shoptalk.analysis.intent import IntentResult


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class ReplyDraft:
    """A suggested reply draft for a customer message.

    Attributes
    ----------
    text:
        The suggested reply text, ready to send or edit.
    tone:
        The tone applied to this reply (e.g. "friendly", "professional").
    intent:
        The intent this reply was drafted for.
    requires_review:
        Whether this reply should be reviewed before sending.
        Always True in the current implementation — ShopTalk never
        sends replies autonomously.

    Example
    -------
    >>> draft = ReplyDraft(
    ...     text="Hi! Yes, we can make that for you. What size would you like?",
    ...     tone="friendly",
    ...     intent="new_order",
    ... )
    """

    text: str
    tone: str
    intent: str
    requires_review: bool = True


# ---------------------------------------------------------------------------
# Template-based implementation (development stub)
# ---------------------------------------------------------------------------

_TEMPLATES: dict[str, str] = {
    "new_order": (
        "Hi! Thanks for reaching out. I'd love to help with your order. "
        "Could you share a few more details so I can confirm everything for you?"
    ),
    "payment_question": (
        "Hi! Happy to help with payment details. "
        "Our payment options are bank transfer and cash on delivery. "
        "Would you like me to send the bank details?"
    ),
    "delivery_question": (
        "Hi! Let me check on that for you. "
        "Could you share your order details so I can give you an update?"
    ),
    "product_inquiry": (
        "Hi! Thanks for your interest. "
        "I'd be happy to share more details about what we have available. "
        "What are you looking for?"
    ),
    "complaint": (
        "Hi, I'm really sorry to hear about your experience. "
        "This is not the standard we aim for. "
        "Could you share more details so I can make this right for you?"
    ),
    "general": (
        "Hi! Thanks for getting in touch. "
        "How can I help you today?"
    ),
    "unknown": (
        "Hi! Thanks for your message. "
        "How can I help you today?"
    ),
}


def draft_reply(
    intent_result: IntentResult,
    tone: str = "friendly",
    business_name: str | None = None,
) -> ReplyDraft:
    """Draft a suggested reply for a customer message.

    This is a template-based stub implementation. The production version
    calls an LLM with the full message context, business tone settings,
    and catalog information to generate a contextual reply.

    Parameters
    ----------
    intent_result:
        The result of intent extraction for the customer message.
    tone:
        The desired reply tone. Passed to the LLM in production.
        Currently unused in the stub implementation.
    business_name:
        Optional business name to personalise the reply.

    Returns
    -------
    ReplyDraft
        The suggested reply text and metadata.

    Example
    -------
    >>> from shoptalk.analysis.intent import extract_intent
    >>> intent = extract_intent("Hi, can I order a chocolate cake?")
    >>> reply = draft_reply(intent, tone="friendly")
    >>> reply.requires_review
    True
    """
    template = _TEMPLATES.get(intent_result.intent, _TEMPLATES["general"])

    # In production: call LLM with full context and tone instructions
    # For now: return the template as-is
    return ReplyDraft(
        text=template,
        tone=tone,
        intent=intent_result.intent,
        requires_review=True,  # Always require seller review
    )
