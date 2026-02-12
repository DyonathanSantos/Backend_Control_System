from app.database import DBBase
from datetime import datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, String, Float, DateTime, ForeignKey
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.billitem import BillItem
    from app.models.user import User


class Stock(DBBase):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
    product: Mapped[str] = mapped_column(String(60), unique=True, nullable=True)
    category: Mapped[str] = mapped_column(String(80))
    quantity: Mapped[int] = mapped_column(nullable=True, default=1)
    product_price: Mapped[float] = mapped_column(Float, nullable=True)
    product_buy: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )
    created_by: Mapped[Optional[str]] = mapped_column(ForeignKey("user.username"), nullable=True)

    # Relationships
    bill_items: Mapped[list["BillItem"]] = relationship(back_populates="stock")
