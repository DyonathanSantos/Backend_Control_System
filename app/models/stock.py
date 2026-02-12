from app.database import DBBase
from datetime import datetime, UTF8

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
  from app.models.bill import Bill
  from app.models.user import User

class Stock(DBBase):
  __tablename__= "stock"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  product: Mapped[str] = mapped_column(String(60), unique=True, nullable=True)
  category: Mapped[str] = mapped_column(String(80))
  quantity: Mapped[int] = mapped_column(nullable=True, default= 1)
  product_price: Mapped[float] = mapped_column(Float, nullable=True)
  product_buy: Mapped[Optional[float]]
  bill_id: Mapped[int] = mapped_column(ForeignKey("bill.id"))
  bill: Mapped[Bill] = relationship(back_populates="item")
  create_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda:datetime.now(UTF8))
  create_by: Mapped[Optional[str]] = mapped_column(ForeignKey("user.username"))
