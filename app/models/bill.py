
from app.database import DBBase

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, String, BIGINT

from typing import List

from app.models.stock import Stock


#Assoction Table for Join
bill_stock = Table(
  'bill_stock',DBBase.metadata,
  Column("bill_id", ForeignKey("bill.id"), primary_key=True, index=True),
  Column("product_id", ForeignKey("stock.id"), primary_key=True, index=True), 
)

#Table of Bill
class Bill(DBBase):
  __tablename__= "bill"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  customer_name: Mapped[str] = mapped_column(String(70), unique=True, nullable=True)
  status: Mapped[str] = mapped_column(String(40), default= "Aberto")
  item: Mapped[List["Stock"]] = relationship(secondary=bill_stock)
