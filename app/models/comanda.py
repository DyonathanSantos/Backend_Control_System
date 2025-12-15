from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String
from app.database import Base
from sqlalchemy.sql import func
from typing import List
from app.models.user import User
from app.models.item_comanda import ItemComanda

class Comanda(Base):
    __tablename__ = 'comandas'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    custumer: Mapped[str] = mapped_column(String(50), nullable=False)
    items: Mapped[List]["ItemComanda"] = relationship("Itemcomanda", back_populates="comanda", cascade="all, delete-orphan")
    created_by: Mapped["User"] = relationship("User", back_populates="comandas")
    created_at: Mapped = mapped_column(server_default=func.now(), timezone=True, nullable=False)

 
