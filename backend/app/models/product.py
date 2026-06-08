"""Product model"""
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Product(Base):
    """Product model"""
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    category_id = Column(String, ForeignKey("categories.id"), nullable=False)
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)
    brand = Column(String)
    original_price = Column(Float, nullable=False)
    rent_price_per_day = Column(Float, nullable=False)
    city = Column(String, index=True, nullable=False)
    state = Column(String, nullable=False)
    latitude = Column(String)
    longitude = Column(String)
    availability = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    category = relationship("Category", back_populates="products")
    owner = relationship("User", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    wishlists = relationship("Wishlist", back_populates="product", cascade="all, delete-orphan")
    bookings = relationship("Booking", back_populates="product", cascade="all, delete-orphan")