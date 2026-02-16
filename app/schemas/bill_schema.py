from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

from app.schemas.billitem_schema import BillItemResponse


class BillBase(BaseModel):
    """Base schema for Bill"""
    customer_name: str


class BillCreate(BillBase):
    """Schema for creating a new Bill"""
    pass


class BillUpdate(BaseModel):
    """Schema for updating Bill (all fields optional)"""
    customer_name: Optional[str] = None
    status: Optional[str] = None


class BillResponse(BillBase):
    """Schema for Bill response including nested items"""
    id: int
    status: str
    created_at: datetime
    items: List[BillItemResponse] = []

    model_config = ConfigDict(from_attributes=True)


# Legacy aliases for backward compatibility
BillOut = BillResponse
