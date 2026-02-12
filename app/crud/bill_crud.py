from typing import Annotated
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.bill_schema import BillCreate, BillOut, BillUpdate
from app.models.bill import Bill


from fastapi import HTTPException, Depends, status, FastAPI

app = FastAPI()


def all_see_bill(db: Annotated[Session, Depends(get_db)]):
  return db.query(Bill).all()


def create_bill(db: Annotated[Session, Depends(get_db)], bill_data: BillCreate):

  existing = db.query(Bill).filter(Bill.id == bill_data.id).first()

  if existing:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cliente já cadastrado.")
  
  bill = Bill(**bill_data.model_dump())
  db.add(bill)
  db.commit()
  db.refrash(Bill)
  return Bill



