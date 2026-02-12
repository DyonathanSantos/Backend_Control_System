from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.bill import Bill
from app.schemas.bill_schema import BillCreate, BillUpdate


def create_bill(db: Session, bill_data: BillCreate) -> Bill:
    """
    Create a new bill after verifying customer doesn't already exist.

    Args:
        db: Database session
        bill_data: Bill creation data

    Returns:
        Created Bill instance

    Raises:
        HTTPException: If customer already has a bill
    """
    # Check if bill with same customer already exists
    existing = db.query(Bill).filter(Bill.customer_name == bill_data.customer_name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer already registered"
        )

    # Create and add bill to database
    bill = Bill(**bill_data.model_dump())
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


def get_all_bills(db: Session) -> list[Bill]:
    """
    Retrieve all bills.

    Args:
        db: Database session

    Returns:
        List of all Bill instances
    """
    return db.query(Bill).all()


def get_bill_by_id(db: Session, bill_id: int) -> Bill:
    """
    Retrieve a bill by ID.

    Args:
        db: Database session
        bill_id: ID of the bill

    Returns:
        Bill instance if found

    Raises:
        HTTPException: If bill not found
    """
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found"
        )
    return bill


def update_bill(db: Session, bill_id: int, bill_data: BillUpdate) -> Bill:
    """
    Update a bill with partial data.

    Args:
        db: Database session
        bill_id: ID of the bill to update
        bill_data: Bill update data

    Returns:
        Updated Bill instance

    Raises:
        HTTPException: If bill not found
    """
    # Check if bill exists
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found"
        )

    # Update bill instance with new values
    update_data = bill_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(bill, field, value)

    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


def delete_bill(db: Session, bill_id: int) -> None:
    """
    Delete a bill by ID.

    Args:
        db: Database session
        bill_id: ID of the bill to delete

    Raises:
        HTTPException: If bill not found
    """
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found"
        )

    db.delete(bill)
    db.commit()



