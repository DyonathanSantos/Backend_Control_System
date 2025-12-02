from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class ItemComanda(Base):
    __tablename__ = 'item_comandas'

    id = Column(Integer, primary_key=True)
    comandas_id = Column(Integer, ForeignKey('comandas.id'), nullable=False)
    products_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    product = Column(String(100), nullable=False, unique= True)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False, default=0.0)
 
