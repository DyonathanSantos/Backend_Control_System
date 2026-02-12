from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.billitem import BillItem
from app.models.bill import Bill
from app.models.stock import Stock


def create_bill_item(
    db: Session,
    bill_id: int,
    stock_id: int,
    quantity: int,
    unit_price: float
) -> BillItem:
    """
    Create a new BillItem with validation and stock quantity reduction.

    Args:
        db: Database session
        bill_id: ID of the bill
        stock_id: ID of the stock item
        quantity: Quantity to add to the bill
        unit_price: Unit price of the item

    Returns:
        Created BillItem instance

    Raises:
        HTTPException: If bill, stock not found or insufficient stock quantity
    """
    # Verify if bill exists
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found"
        )

    # Verify if stock exists
    stock = db.query(Stock).filter(Stock.id == stock_id).first()
    if not stock:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock item not found"
        )

    # Verify if stock quantity is sufficient
    if stock.quantity < quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Insufficient stock quantity. Available: {stock.quantity}, Requested: {quantity}"
        )

    # Create BillItem
    bill_item = BillItem(
        bill_id=bill_id,
        stock_id=stock_id,
        quantity=quantity,
        unit_price=unit_price
    )

    # Decrease stock quantity
    stock.quantity -= quantity

    # Add to session and commit
    db.add(bill_item)
    db.add(stock)
    db.commit()
    db.refresh(bill_item)

    return bill_item
