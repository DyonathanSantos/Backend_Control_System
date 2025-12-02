from pydantic import BaseModel
from typing import Optional

# -------- Base usado como referência
class StockBase(BaseModel):
    product: str
    category: str
    quantity: int
    buy: float
    sell: float


# -------- Criar novo item (tudo obrigatório)
class StockCreate(StockBase):
    pass


# -------- Atualizar item (tudo opcional)
class StockUpdate(BaseModel):
    product: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    buy: Optional[float] = None
    sell: Optional[float] = None


# -------- Resposta
class StockOut(StockBase):
    id: int

    class Config:
        orm_mode = True