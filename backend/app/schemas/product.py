"""Product schemas"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductImageSchema(BaseModel):
    """Product image schema"""
    id: str
    image_url: str
    display_order: int

    class Config:
        """Config"""
        from_attributes = True


class ProductCreate(BaseModel):
    """Product create schema"""
    title: str
    description: str
    category_id: str
    brand: str
    original_price: float
    rent_price_per_day: float
    city: str
    state: str
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    availability: bool = True


class ProductUpdate(BaseModel):
    """Product update schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[str] = None
    brand: Optional[str] = None
    original_price: Optional[float] = None
    rent_price_per_day: Optional[float] = None
    city: Optional[str] = None
    state: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    availability: Optional[bool] = None


class ProductResponse(BaseModel):
    """Product response schema"""
    id: str
    title: str
    description: str
    category_id: str
    owner_id: str
    brand: str
    original_price: float
    rent_price_per_day: float
    city: str
    state: str
    latitude: Optional[str]
    longitude: Optional[str]
    availability: bool
    images: List[ProductImageSchema] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        """Config"""
        from_attributes = True