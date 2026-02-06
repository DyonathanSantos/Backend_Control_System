from pydantic import BaseModel
from typing import List, Optional
from schemas.stock_schema import StockOut


class BillCreate(BaseModel):
  
  id: int
  customer_name: str

class BillUpdate(BaseModel):
  
  customer_name: str | None = None
  item: List [StockOut]  | None = None
  class config:
    from_attributes= True

class BillOut(BaseModel):

  id: int
  customer_name: str
  # This field represents the "joined" data
  item: List[StockOut]

  class Config:
    from_attributes = True
