from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.billitem_schema import BillItemCreate, BillItemResponse
from app.crud.billitem_crud import create_bill_item

# Router is mounted under /api/v1/bills in main, so this router handles
# the `/ {bill_id}/items` sub-path
router = APIRouter(prefix='/{bill_id}/items', tags=["Bill Items"])


@router.post(
    "/",
    response_model=BillItemResponse,
    status_code=status.HTTP_201_CREATED
)
def add_item_to_bill(
    bill_id: int,
    item_data: BillItemCreate,
    db: Annotated[Session, Depends(get_db)]
) -> BillItemResponse:
    """Add an item to a bill using only `stock_id` and `quantity`.

    The item's `unit_price` and stock information are taken from the stock
    record automatically.
    """
    bill_item = create_bill_item(
        db=db,
        bill_id=bill_id,
        stock_id=item_data.stock_id,
        quantity=item_data.quantity,
    )
    return bill_item
