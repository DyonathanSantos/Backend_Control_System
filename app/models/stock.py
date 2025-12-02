from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key= True, index=True)
    product = Column(String(100), unique= True, nullable= False)
    category = Column(String(50))
    quantity = Column(Integer, nullable= False, default= 0)
    buy = Column(Float, nullable= False, default= 0.0)
    sell = Column(Float, nullable= False, default= 0.0)

 
