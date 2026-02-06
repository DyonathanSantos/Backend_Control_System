from typing import Annotated

from app.database import Sessao_, get_db
from schemas.bill_schema import BillCreate, BillOut, BillUpdate
from models.bill import Bill, bill_stock


from fastapi import HTTPException, Depends, status


def all_see_bill(db: Annotated[Sessao_, Depends(get_db)]):
  return db.query(Bill).all()


def create_bill(db: Annotated[Sessao_, Depends(get_db)], bill_data: BillCreate):

  existing = db.query(Bill).filter(Bill.id == bill_data.id).first()

  if existing:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente já cadastrado.")
  
  bill = Bill(**bill_data.model_dump())
  db.add(bill)
  db.commit()
  db.refrash(Bill)
  return Bill



