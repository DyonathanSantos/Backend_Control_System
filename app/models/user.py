from app.database import DBBase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BIGINT, DateTime
from sqlalchemy.sql import func

from typing import Optional

class User(DBBase):
  __tablename__ = "user"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  username: Mapped[str] = mapped_column(String(70), unique=True, nullable=True)
  fullname: Mapped[Optional[str]] = mapped_column(String(100), default= None)
  phone: Mapped[Optional[int]] = mapped_column(BIGINT, default= 0000000)
  create_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=True)
