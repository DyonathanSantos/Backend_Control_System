from pydantic import BaseModel, ConfigDict, Field, EmailStr

from typing import List, Optional
from app.schemas.stock_schema import StockOut


class BillBase(BaseModel):
  id: int
  customer_name: str

class BillCreate(BillBase):
  pass

class BillUpdate(BaseModel):
  
  customer_name: Optional[str] | None = None
  item: Optional[List[StockOut]]  | None = None
  class config:
    from_attributes= True

class BillResponse(BillCreate):
  model_config= ConfigDict(from_attributes=True)
  id: int
  customer_name: str
  # This field represents the "joined" data
  item: List[StockOut]

  class Config:
    from_attributes = True
