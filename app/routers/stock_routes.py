from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.stock_schema import StockCreate, StockUpdate, StockResponse
from app.crud.stock_crud import (
    create_stock,
    get_all_stock,
    get_stock_by_id,
    update_stock_partial,
    delete_stock
)

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.post("", response_model=StockResponse, status_code=status.HTTP_201_CREATED)
def create_stock_endpoint(
    stock_data: StockCreate,
    db: Annotated[Session, Depends(get_db)]
) -> StockResponse:
    """
    Create a new stock item.

    Args:
        stock_data: Stock creation data
        db: Database session

    Returns:
        Created Stock instance
    """
    return create_stock(db=db, stock_data=stock_data)


@router.get("", response_model=list[StockResponse])
def list_all_stocks(db: Annotated[Session, Depends(get_db)]) -> list[StockResponse]:
    """
    Retrieve all stock items.

    Args:
        db: Database session

    Returns:
        List of all Stock instances
    """
    return get_all_stock(db=db)


@router.get("/{stock_id}", response_model=StockResponse)
def get_stock_endpoint(
    stock_id: int,
    db: Annotated[Session, Depends(get_db)]
) -> StockResponse:
    """
    Retrieve a specific stock item by ID.

    Args:
        stock_id: ID of the stock item
        db: Database session

    Returns:
        Stock instance
    """
    return get_stock_by_id(db=db, stock_id=stock_id)


@router.patch("/{stock_id}", response_model=StockResponse)
def update_stock_endpoint(
    stock_id: int,
    stock_data: StockUpdate,
    db: Annotated[Session, Depends(get_db)]
) -> StockResponse:
    """
    Update a stock item with partial data.

    Args:
        stock_id: ID of the stock item
        stock_data: Stock update data
        db: Database session

    Returns:
        Updated Stock instance
    """
    return update_stock_partial(db=db, stock_id=stock_id, stock_data=stock_data)


@router.delete("/{stock_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stock_endpoint(
    stock_id: int,
    db: Annotated[Session, Depends(get_db)]
) -> None:
    """
    Delete a stock item by ID.

    Args:
        stock_id: ID of the stock item
        db: Database session
    """
    delete_stock(db=db, stock_id=stock_id)