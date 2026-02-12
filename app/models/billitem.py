from app.database import DBBase
from datetime import datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, DateTime, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.bill import Bill
    from app.models.stock import Stock


class BillItem(DBBase):
    __tablename__ = "bill_item"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
    bill_id: Mapped[int] = mapped_column(ForeignKey("bill.id"), nullable=False)
    stock_id: Mapped[int] = mapped_column(ForeignKey("stock.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    # Relationships
    bill: Mapped["Bill"] = relationship(back_populates="items")
    stock: Mapped["Stock"] = relationship(back_populates="bill_items")
