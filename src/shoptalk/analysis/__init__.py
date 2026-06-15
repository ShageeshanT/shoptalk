"""ShopTalk analysis pipeline.

This package provides the core AI analysis functions for ShopTalk.
Each module handles a specific analysis task and can be used independently
or as part of the full analysis pipeline.

Modules
-------
intent
    Extract customer intent and urgency from raw message text.
reply
    Draft suggested replies based on analysis results.
order_extractor
    Extract structured order details from customer messages.

Example
-------
>>> from shoptalk.analysis.intent import extract_intent
>>> result = extract_intent("Hi, can I order a chocolate cake for Saturday?")
>>> result.intent
'new_order'
"""

from shoptalk.analysis.intent import IntentResult, extract_intent
from shoptalk.analysis.order_extractor import OrderExtraction, extract_order_details
from shoptalk.analysis.reply import draft_reply

__all__ = [
    "IntentResult",
    "OrderExtraction",
    "draft_reply",
    "extract_intent",
    "extract_order_details",
]
