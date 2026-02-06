from app.database import DBBase

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BIGINT, ForeignKey, Float, DateTime
from sqlalchemy.sql import func

from typing import List

#from app.models.user import User
from app.models.itemsales import SaleItem

class Sales(DBBase):
  __tablename__ = "sales"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
  total: Mapped[float] = mapped_column(Float, nullable=True)
  created_at: Mapped[str] = mapped_column(DateTime(timezone=True),server_default=func.now())
  user: Mapped["User"] = relationship("User")
  items: Mapped[List["SaleItem"]] = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")