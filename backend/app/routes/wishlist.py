"""Wishlist routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.dependencies import get_current_user
from app.schemas import WishlistResponse
from app.services.wishlist_service import WishlistService

router = APIRouter(prefix="/wishlist", tags=["wishlist"])


@router.get("", response_model=List[WishlistResponse])
def get_wishlist(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get user wishlist"""
    wishlist = WishlistService.get_user_wishlist(db, current_user.id)
    return wishlist


@router.post("/{product_id}", status_code=status.HTTP_201_CREATED)
def add_to_wishlist(
    product_id: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add product to wishlist"""
    wishlist = WishlistService.add_to_wishlist(db, current_user.id, product_id)
    if not wishlist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to add to wishlist",
        )
    return {"message": "Added to wishlist"}


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
def remove_from_wishlist(
    product_id: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Remove product from wishlist"""
    success = WishlistService.remove_from_wishlist(db, current_user.id, product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not in wishlist",
        )
    return {"message": "Removed from wishlist"}