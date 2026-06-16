"""Tests for analysis Pydantic schemas."""

import pytest
from pydantic import ValidationError

from shoptalk.schemas.analysis import AnalyzeRequest, AnalyzeResponse


def test_analyze_request_valid():
    req = AnalyzeRequest(
        business_id="biz_1",
        customer_id="cust_1",
        raw_message="I want to order a cake",
    )
    assert req.raw_message == "I want to order a cake"


def test_analyze_request_empty_message_fails():
    with pytest.raises(ValidationError):
        AnalyzeRequest(business_id="b", customer_id="c", raw_message="")


def test_analyze_response_defaults():
    resp = AnalyzeResponse(
        intent="new_order",
        suggested_reply="Thanks!",
    )
    assert resp.urgency == "normal"
    assert resp.sentiment == "neutral"
    assert resp.follow_up_needed is False
    assert resp.confidence == 1.0


def test_analyze_response_invalid_intent_fails():
    with pytest.raises(ValidationError):
        AnalyzeResponse(intent="buy_now", suggested_reply="ok")


def test_analyze_response_confidence_bounds():
    with pytest.raises(ValidationError):
        AnalyzeResponse(intent="greeting", suggested_reply="hi", confidence=1.5)
