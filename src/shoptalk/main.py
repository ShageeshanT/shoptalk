from fastapi import FastAPI

from shoptalk.analyzer import analyze_message
from shoptalk.reply import build_suggested_reply
from shoptalk.metrics import business_metrics
from shoptalk.demo import seed_demo_data
from shoptalk.routes_approvals import router as approvals_router
from shoptalk.routes_businesses import router as businesses_router
from shoptalk.routes_catalog import router as catalog_router
from shoptalk.routes_catalog_items import router as catalog_items_router
from shoptalk.routes_customers import router as customers_router
from shoptalk.routes_checkout import router as checkout_router
from shoptalk.routes_conversations import router as conversations_router
from shoptalk.routes_dashboard import router as dashboard_router
from shoptalk.routes_followups import router as followups_router
from shoptalk.routes_messages import router as messages_router
from shoptalk.routes_orders import router as orders_router
from shoptalk.routes_profiles import router as profiles_router
from shoptalk.routes_sales import router as sales_router
from shoptalk.routes_tasks import router as tasks_router
from shoptalk.routes_threads import router as threads_router
from shoptalk.schemas import MessageAnalysis, MessageAnalyzeRequest, ReplyDraft
from shoptalk.seeds import seed_demo_data

app = FastAPI(
    title="ShopTalk API",
    description="AI sales desk for WhatsApp-first small businesses.",
    version="0.1.0",
)
app.include_router(approvals_router)
app.include_router(businesses_router)
app.include_router(catalog_router)
app.include_router(catalog_items_router)
app.include_router(customers_router)
app.include_router(checkout_router)
app.include_router(conversations_router)
app.include_router(orders_router)
app.include_router(profiles_router)
app.include_router(sales_router)
app.include_router(tasks_router)
app.include_router(followups_router)
app.include_router(messages_router)
app.include_router(dashboard_router)
app.include_router(threads_router)


@app.post("/demo/seed")
def seed_demo() -> dict[str, str]:
    seed_demo_data()
    return {"status": "seeded"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "shoptalk"}


@app.post("/analyze", response_model=MessageAnalysis)
def analyze(payload: MessageAnalyzeRequest) -> MessageAnalysis:
    return analyze_message(payload)


@app.post("/draft-reply", response_model=ReplyDraft)
def draft_reply(request: MessageAnalyzeRequest) -> ReplyDraft:
    analysis = analyze_message(request)
    return ReplyDraft(analysis=analysis, suggested_reply=build_suggested_reply(analysis))


@app.get("/dashboard/metrics")
def dashboard_metrics() -> dict[str, int]:
    return business_metrics()
