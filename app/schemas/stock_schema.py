from pydantic import BaseModel, ConfigDict, EmailStr, Field

from typing import Optional

# -------- Base usado como referência
class StockBase(BaseModel):
    product: str
    category: str
    quantity: int
    product_price: float
    product_buy: Optional[float] = None


# -------- Criar novo item (tudo obrigatório)
class StockCreate(StockBase):
    pass


# -------- Atualizar item (tudo opcional)
class StockUpdate(BaseModel):
    product: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    product_price: Optional[float] = None
    product_buy: Optional[float] = None


# -------- Resposta
class StockResponse(StockBase):
    product: str
    quantity: int
    product_price: float
    category: str
    class Config:
        orm_mode = True
        from_attributes= True