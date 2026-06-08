"""Product image model"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class ProductImage(Base):
    """Product image model"""
    __tablename__ = "product_images"

    id = Column(String, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    image_url = Column(String, nullable=False)
    display_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    product = relationship("Product", back_populates="images")