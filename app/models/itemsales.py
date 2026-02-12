from app.database import DBBase

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Float, String, ForeignKey, BIGINT

from typing import List

from app.models.stock import Stock

class SaleItem(DBBase):
  __tablename__ = "saleitems"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  sale_id: Mapped[int] = mapped_column(ForeignKey("sales.id", ondelete="CASCADE"), nullable=True)
  stock_id: Mapped[int] = mapped_column(ForeignKey("stock.id", ondelete="CASCADE"),nullable=True)

  product_name: Mapped[str] = mapped_column(String(60), unique=True, nullable=True)
  unit_price: Mapped[float] = mapped_column(Float, nullable=True)
  total: Mapped[float] = mapped_column(Float, nullable=True)

  sale: Mapped["Sales"] = relationship("Sales", back_populates="items")
  stock: Mapped["Stock"] = relationship("Stock")