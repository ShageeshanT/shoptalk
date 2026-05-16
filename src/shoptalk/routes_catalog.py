from fastapi import APIRouter

from shoptalk.catalog import CatalogItem, CatalogMatch, match_catalog_items
from shoptalk.schemas import CatalogMatchRequest

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.post("/match", response_model=list[CatalogMatch])
def match_catalog(payload: CatalogMatchRequest) -> list[CatalogMatch]:
    catalog = [CatalogItem(**item) for item in payload.catalog]
    return match_catalog_items(payload.message, catalog)
