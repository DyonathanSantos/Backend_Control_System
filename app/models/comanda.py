from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from sqlalchemy.sql import func

class Comanda(Base):
    __tablename__ = 'comandas'

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default='open')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

 
