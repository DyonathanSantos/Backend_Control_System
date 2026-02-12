from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class StockInfo(BaseModel):
    """Nested schema for Stock information in BillItem response"""
    id: int
    product: str
    product_price: float

    model_config = ConfigDict(from_attributes=True)


class BillItemBase(BaseModel):
    """Base schema for BillItem"""
    quantity: int
    unit_price: float


class BillItemCreate(BillItemBase):
    """Schema for creating a new BillItem"""
    bill_id: int
    stock_id: int


class BillItemResponse(BillItemBase):
    """Schema for BillItem response with nested Stock information"""
    id: int
    bill_id: int
    stock_id: int
    created_at: datetime
    stock: StockInfo

    model_config = ConfigDict(from_attributes=True)
