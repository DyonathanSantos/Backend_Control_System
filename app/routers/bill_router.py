from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.bill_schema import BillCreate, BillResponse, BillUpdate
from app.crud.bill_crud import (
    create_bill,
    get_all_bills,
    get_bill_by_id,
    update_bill,
    delete_bill
)

router = APIRouter(prefix="/bills", tags=["Bills"])


@router.post("", response_model=BillResponse, status_code=status.HTTP_201_CREATED)
def create_bill_endpoint(
    bill_data: BillCreate,
    db: Annotated[Session, Depends(get_db)]
) -> BillResponse:
    """
    Create a new bill for a customer.

    Args:
        bill_data: Bill creation data
        db: Database session

    Returns:
        Created Bill instance
    """
    return create_bill(db=db, bill_data=bill_data)


@router.get("", response_model=list[BillResponse])
def list_all_bills(db: Annotated[Session, Depends(get_db)]) -> list[BillResponse]:
    """
    Retrieve all bills.

    Args:
        db: Database session

    Returns:
        List of all bills
    """
    return get_all_bills(db=db)


@router.get("/{bill_id}", response_model=BillResponse)
def get_bill_endpoint(
    bill_id: int,
    db: Annotated[Session, Depends(get_db)]
) -> BillResponse:
    """
    Retrieve a specific bill by ID.

    Args:
        bill_id: ID of the bill
        db: Database session

    Returns:
        Bill instance
    """
    return get_bill_by_id(db=db, bill_id=bill_id)


@router.put("/{bill_id}", response_model=BillResponse)
def update_bill_endpoint(
    bill_id: int,
    bill_data: BillUpdate,
    db: Annotated[Session, Depends(get_db)]
) -> BillResponse:
    """
    Update a bill with partial data.

    Args:
        bill_id: ID of the bill
        bill_data: Bill update data
        db: Database session

    Returns:
        Updated Bill instance
    """
    return update_bill(db=db, bill_id=bill_id, bill_data=bill_data)


@router.delete("/{bill_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bill_endpoint(
    bill_id: int,
    db: Annotated[Session, Depends(get_db)]
) -> None:
    """
    Delete a bill by ID.

    Args:
        bill_id: ID of the bill
        db: Database session
    """
    delete_bill(db=db, bill_id=bill_id)
