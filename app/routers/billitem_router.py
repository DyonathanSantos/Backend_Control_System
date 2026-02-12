from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.billitem_schema import BillItemCreate, BillItemResponse
from app.crud.billitem_crud import create_bill_item

router = APIRouter(prefix="/bills", tags=["bill-items"])


@router.post(
    "/{bill_id}/items",
    response_model=BillItemResponse,
    status_code=status.HTTP_201_CREATED
)
def add_item_to_bill(
    bill_id: int,
    item_data: BillItemCreate,
    db: Annotated[Session, Depends(get_db)]
) -> BillItemResponse:
    """
    Add an item to a bill.

    Args:
        bill_id: ID of the bill
        item_data: BillItem creation data containing stock_id, quantity, and unit_price
        db: Database session

    Returns:
        Created BillItem with nested Stock information
    """
    bill_item = create_bill_item(
        db=db,
        bill_id=bill_id,
        stock_id=item_data.stock_id,
        quantity=item_data.quantity,
        unit_price=item_data.unit_price
    )
    return bill_item
