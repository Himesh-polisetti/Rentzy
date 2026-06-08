"""Wishlist service"""
from sqlalchemy.orm import Session
from app.models import Wishlist, Product
from app.utils.helpers import generate_id
from typing import List, Optional


class WishlistService:
    """Wishlist service for database operations"""

    @staticmethod
    def add_to_wishlist(db: Session, user_id: str, product_id: str) -> Optional[Wishlist]:
        """Add product to wishlist"""
        existing = db.query(Wishlist).filter(
            Wishlist.user_id == user_id,
            Wishlist.product_id == product_id
        ).first()
        if existing:
            return existing
        
        wishlist = Wishlist(
            id=generate_id("wish_"),
            user_id=user_id,
            product_id=product_id,
        )
        db.add(wishlist)
        db.commit()
        db.refresh(wishlist)
        return wishlist

    @staticmethod
    def get_user_wishlist(db: Session, user_id: str) -> List[Wishlist]:
        """Get user wishlist"""
        return db.query(Wishlist).filter(Wishlist.user_id == user_id).all()

    @staticmethod
    def remove_from_wishlist(db: Session, user_id: str, product_id: str) -> bool:
        """Remove product from wishlist"""
        wishlist = db.query(Wishlist).filter(
            Wishlist.user_id == user_id,
            Wishlist.product_id == product_id
        ).first()
        if wishlist:
            db.delete(wishlist)
            db.commit()
            return True
        return False