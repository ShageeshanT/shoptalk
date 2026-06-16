"""Service for analysing customer messages using OpenAI."""

from __future__ import annotations

import json
import logging

from shoptalk.config import Settings
from shoptalk.schemas.analysis import AnalyzeRequest, AnalyzeResponse

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """
You are ShopTalk, an AI assistant that helps small business owners manage customer orders
received via WhatsApp and other messaging channels.

Given a raw customer message, extract the following fields as JSON:
- intent: one of new_order, order_inquiry, price_inquiry, complaint, cancellation, general_inquiry, greeting, unknown
- urgency: one of low, normal, high, urgent
- sentiment: one of positive, neutral, negative
- product: string or null
- quantity: integer or null
- size: string or null
- needed_by: string or null (human-readable deadline)
- follow_up_needed: boolean
- suggested_reply: a short, friendly reply the seller can send
- confidence: float 0-1

Respond ONLY with valid JSON. No markdown, no explanation.
"""


class AnalysisService:
    """Wraps OpenAI calls for message analysis."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = None

    def _get_client(self):
        """Lazily initialise the OpenAI client."""
        if self._client is None:
            try:
                from openai import OpenAI  # type: ignore
                self._client = OpenAI(api_key=self._settings.openai_api_key)
            except ImportError:
                logger.warning("openai package not installed; analysis will use fallback")
        return self._client

    async def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        """Analyse a customer message and return structured data."""
        client = self._get_client()
        if client is None:
            return self._fallback_response(request)

        try:
            response = client.chat.completions.create(
                model=self._settings.openai_model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": request.raw_message},
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
            )
            data = json.loads(response.choices[0].message.content)
            return AnalyzeResponse(**data)
        except Exception as exc:
            logger.error("OpenAI analysis failed: %s", exc)
            return self._fallback_response(request)

    @staticmethod
    def _fallback_response(request: AnalyzeRequest) -> AnalyzeResponse:
        """Return a safe default when AI is unavailable."""
        return AnalyzeResponse(
            intent="unknown",
            urgency="normal",
            sentiment="neutral",
            follow_up_needed=True,
            suggested_reply="Thanks for your message! We will get back to you shortly.",
            confidence=0.0,
        )
