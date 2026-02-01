from app.database import DBBase

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, String, Float, DateTime
from sqlalchemy.sql import func

from typing import List, Optional

from app.models.user import User

class Stock(DBBase):
  __tablename__= "stock"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  product: Mapped[str] = mapped_column(String(60), unique=True, nullable=True)
  category: Mapped[str] = mapped_column(String(80))
  quantity: Mapped[int] = mapped_column(nullable=True, default= 1)
  product_price: Mapped[float] = mapped_column(Float, nullable=True)
  product_buy: Mapped[Optional[float]]
  create_at: Mapped[str] = mapped_column(DateTime(timezone=True),server_default=func.now())
  create_by: Mapped["User"] = relationship("User")
