"""Booking routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.dependencies import get_current_user, get_owner_user
from app.schemas import BookingCreate, BookingResponse
from app.services.booking_service import BookingService
from app.services.product_service import ProductService

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(
    booking_data: BookingCreate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create new booking"""
    product = ProductService.get_product_by_id(db, booking_data.product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    booking = BookingService.create_booking(db, booking_data, current_user.id, product.rent_price_per_day)
    return booking


@router.get("/my", response_model=List[BookingResponse])
def get_my_bookings(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get user's bookings"""
    bookings = BookingService.get_user_bookings(db, current_user.id)
    return bookings


@router.get("/owner", response_model=List[BookingResponse])
def get_owner_bookings(current_user = Depends(get_owner_user), db: Session = Depends(get_db)):
    """Get owner's booking requests"""
    bookings = BookingService.get_owner_booking_requests(db, current_user.id)
    return bookings


@router.put("/{booking_id}/approve", response_model=BookingResponse)
def approve_booking(
    booking_id: str,
    current_user = Depends(get_owner_user),
    db: Session = Depends(get_db),
):
    """Approve booking (owner only)"""
    booking = BookingService.get_booking_by_id(db, booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found",
        )
    product = ProductService.get_product_by_id(db, booking.product_id)
    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only approve your own bookings",
        )
    booking = BookingService.approve_booking(db, booking)
    return booking


@router.put("/{booking_id}/reject", response_model=BookingResponse)
def reject_booking(
    booking_id: str,
    current_user = Depends(get_owner_user),
    db: Session = Depends(get_db),
):
    """Reject booking (owner only)"""
    booking = BookingService.get_booking_by_id(db, booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found",
        )
    product = ProductService.get_product_by_id(db, booking.product_id)
    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only reject your own bookings",
        )
    booking = BookingService.reject_booking(db, booking)
    return booking