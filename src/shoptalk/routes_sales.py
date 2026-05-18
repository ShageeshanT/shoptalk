from fastapi import APIRouter

from shoptalk.sales import sales_funnel
from shoptalk.schemas import SalesFunnel

router = APIRouter(prefix="/sales", tags=["sales"])


@router.get("/funnel", response_model=SalesFunnel)
def get_sales_funnel() -> SalesFunnel:
    return sales_funnel()
