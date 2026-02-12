from app.database import DBBase
from datetime import datetime, UTC

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BIGINT, DateTime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.billitem import BillItem


class Bill(DBBase):
    __tablename__ = "bill"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String(70), unique=True, nullable=True)
    status: Mapped[str] = mapped_column(String(40), default="Aberto")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    # Relationship to BillItem
    items: Mapped[list["BillItem"]] = relationship(back_populates="bill")
