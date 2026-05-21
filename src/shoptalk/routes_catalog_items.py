from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.catalog_store import create_catalog_item, list_catalog_items, update_catalog_item
from shoptalk.schemas import CatalogItemCreate, CatalogItemRecord
from shoptalk.state import state

router = APIRouter(prefix="/catalog-items", tags=["catalog"])


@router.post("", response_model=CatalogItemRecord, status_code=status.HTTP_201_CREATED)
def create_item(payload: CatalogItemCreate) -> CatalogItemRecord:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return create_catalog_item(payload)


@router.get("", response_model=list[CatalogItemRecord])
def list_items(business_id: UUID, available_only: bool = True, search: str | None = None) -> list[CatalogItemRecord]:
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return list_catalog_items(business_id, available_only=available_only, search=search)


@router.put("/{item_id}", response_model=CatalogItemRecord)
def update_item(item_id: UUID, payload: CatalogItemCreate) -> CatalogItemRecord:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    item = update_catalog_item(item_id, payload)
    if item is None:
        raise HTTPException(status_code=404, detail="Catalog item not found")
    return item
