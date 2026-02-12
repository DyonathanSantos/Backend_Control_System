
from app.database import DBBase
from datetime import UTF8, datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, String, BIGINT, DateTime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.stock import Stock

#Table of Bill with relationship one-to-many
class Bill(DBBase):
  __tablename__= "bill"

  id: Mapped[int] = mapped_column(BIGINT, primary_key=True, index=True)
  customer_name: Mapped[str] = mapped_column(String(70), unique=True, nullable=True)
  status: Mapped[str] = mapped_column(String(40), default= "Aberto")
  item: Mapped[list[Stock]] = relationship(back_populates="bill")
  created_at: Mapped[datetime] =  mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTF8))
