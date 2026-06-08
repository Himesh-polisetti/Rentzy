"""Pydantic schemas"""
from app.schemas.user import UserRegister, UserLogin, UserResponse
from app.schemas.category import CategoryResponse
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.schemas.wishlist import WishlistResponse
from app.schemas.booking import BookingCreate, BookingResponse

__all__ = [
    "UserRegister",
    "UserLogin",
    "UserResponse",
    "CategoryResponse",
    "ProductCreate",
    "ProductUpdate",
    "ProductResponse",
    "WishlistResponse",
    "BookingCreate",
    "BookingResponse",
]