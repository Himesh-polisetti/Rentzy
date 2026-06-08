"""Category service"""
from sqlalchemy.orm import Session
from app.models import Category
from typing import List


class CategoryService:
    """Category service for database operations"""

    @staticmethod
    def get_all_categories(db: Session) -> List[Category]:
        """Get all categories"""
        return db.query(Category).all()

    @staticmethod
    def get_category_by_id(db: Session, category_id: str) -> Category:
        """Get category by ID"""
        return db.query(Category).filter(Category.id == category_id).first()