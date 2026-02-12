from fastapi import HTTPException, status, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.stock import Stock
from app.schemas.stock_schema import StockCreate, StockUpdate, StockResponse


def create_stock(db: Session, stock_data: StockCreate) -> Stock:
    """
    Create a new stock item after verifying product doesn't already exist.

    Args:
        db: Database session
        stock_data: Stock creation data

    Returns:
        Created Stock instance

    Raises:
        HTTPException: If product already exists
    """
    # Verification if product already exists
    existing = db.query(Stock).filter(Stock.product == stock_data.product).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already exists in stock"
        )

    # Create and add stock to database
    stock = Stock(**stock_data.model_dump())
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


def get_all_stock(db: Session) -> list[Stock]:
    """
    Retrieve all stock items.

    Args:
        db: Database session

    Returns:
        List of all Stock instances
    """
    return db.query(Stock).all()


def get_stock_by_id(db: Session, stock_id: int) -> Stock:
    """
    Retrieve a stock item by ID.

    Args:
        db: Database session
        stock_id: ID of the stock item

    Returns:
        Stock instance if found

    Raises:
        HTTPException: If stock item not found
    """
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock item not found"
        )
    return stock


def update_stock_partial(
    db: Session,
    stock_id: int,
    stock_data: StockUpdate
) -> Stock:
    """
    Update stock item with partial data.

    Args:
        db: Database session
        stock_id: ID of the stock item to update
        stock_data: Stock update data

    Returns:
        Updated Stock instance

    Raises:
        HTTPException: If stock not found or validation fails
    """
    # Check if stock exists
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock item not found"
        )

    # Convert to dict and filter out unset fields
    update_data = stock_data.model_dump(exclude_unset=True)

    # Validate numeric fields
    if "quantity" in update_data and update_data["quantity"] < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must be greater than zero"
        )
    if "product_price" in update_data and update_data["product_price"] < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product price cannot be negative"
        )
    if "product_buy" in update_data and update_data["product_buy"] < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Purchase price cannot be negative"
        )

    # Update stock instance with new values
    for field, value in update_data.items():
        setattr(stock, field, value)

    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


def delete_stock(db: Session, stock_id: int) -> None:
    """
    Delete a stock item by ID.

    Args:
        db: Database session
        stock_id: ID of the stock item to delete

    Raises:
        HTTPException: If stock item not found
    """
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock item not found"
        )

    db.delete(stock)
    db.commit()