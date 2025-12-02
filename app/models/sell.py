from sqlalchemy import Column, Integer, String, Float
from app.database import Base
from sqlalchemy.sql import func

class Sell(Base):
    __tablename__ = 'sells'

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(String(50), server_default=func.now())
    product = Column(String(100), unique=True, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False, default=0.0)
    total = Column(Float, nullable=False, default=0.0)