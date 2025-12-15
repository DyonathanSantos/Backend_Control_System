from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Float
from app.database import Base
from app.models.comanda import Comanda
from app.models.stock import Stock

class ItemComanda(Base):
    __tablename__ = 'item_comandas'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)
    price: Mapped[float] = mapped_column(nullable=False, default=0.0)
    comanda_id: Mapped[int] = mapped_column(ForeignKey('comandas.id'), onupdate="CASCADE", nullable=False)
    stock_id: Mapped[int] = mapped_column(ForeignKey('stock.id'), onupdate="CASCADE", nullable=False)

    comanda: Mapped["Comanda"] = relationship("Comanda", back_populates="items")
    stock: Mapped["Stock"] = relationship("Stock", back_populates="item_comandas")
    
   
    
    
    
    
    
    
    
    # id = Column(Integer, primary_key=True)
    # comandas_id = Column(Integer, ForeignKey('comandas.id'), nullable=False)
    # products_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    # product = Column(String(100), nullable=False, unique= True)
    # quantity = Column(Integer, nullable=False, default=1)
    # price = Column(Float, nullable=False, default=0.0)
 
