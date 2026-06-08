"""Wishlist schemas"""
from pydantic import BaseModel
from app.schemas.product import ProductResponse
from datetime import datetime


class WishlistResponse(BaseModel):
    """Wishlist response schema"""
    id: str
    user_id: str
    product: ProductResponse
    created_at: datetime

    class Config:
        """Config"""
        from_attributes = True