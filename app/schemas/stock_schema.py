from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class StockBase(BaseModel):
    """Base schema for Stock"""
    product: str
    category: str
    quantity: int
    product_price: float
    product_buy: Optional[float] = None


class StockCreate(StockBase):
    """Schema for creating a new Stock item"""
    pass


class StockUpdate(BaseModel):
    """Schema for updating Stock item (all fields optional)"""
    product: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    product_price: Optional[float] = None
    product_buy: Optional[float] = None


class StockResponse(StockBase):
    """Schema for Stock response"""
    id: int

    model_config = ConfigDict(from_attributes=True)


# Legacy alias for backward compatibility
StockOut = StockResponse