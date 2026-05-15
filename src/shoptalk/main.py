from fastapi import FastAPI

from shoptalk.analyzer import analyze_message
from shoptalk.schemas import MessageAnalysis, MessageAnalyzeRequest

app = FastAPI(
    title="ShopTalk API",
    description="AI sales desk for WhatsApp-first small businesses.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "shoptalk"}


@app.post("/analyze", response_model=MessageAnalysis)
def analyze(payload: MessageAnalyzeRequest) -> MessageAnalysis:
    return analyze_message(payload)
