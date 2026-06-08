"""Booking service"""
from sqlalchemy.orm import Session
from app.models import Booking
from app.models.booking import BookingStatus
from app.schemas import BookingCreate
from app.utils.helpers import generate_id, calculate_booking_amount
from typing import List, Optional
from datetime import datetime


class BookingService:
    """Booking service for database operations"""

    @staticmethod
    def create_booking(db: Session, booking_data: BookingCreate, user_id: str, rent_price: float) -> Booking:
        """Create new booking"""
        total_amount = calculate_booking_amount(
            rent_price,
            booking_data.start_date,
            booking_data.end_date
        )
        booking = Booking(
            id=generate_id("book_"),
            user_id=user_id,
            product_id=booking_data.product_id,
            start_date=booking_data.start_date,
            end_date=booking_data.end_date,
            total_amount=total_amount,
            status=BookingStatus.PENDING,
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def get_booking_by_id(db: Session, booking_id: str) -> Optional[Booking]:
        """Get booking by ID"""
        return db.query(Booking).filter(Booking.id == booking_id).first()

    @staticmethod
    def get_user_bookings(db: Session, user_id: str) -> List[Booking]:
        """Get user bookings"""
        return db.query(Booking).filter(Booking.user_id == user_id).all()

    @staticmethod
    def get_owner_booking_requests(db: Session, owner_id: str) -> List[Booking]:
        """Get booking requests for owner's products"""
        from app.models import Product
        return db.query(Booking).join(Product).filter(
            Product.owner_id == owner_id,
            Booking.status == BookingStatus.PENDING
        ).all()

    @staticmethod
    def approve_booking(db: Session, booking: Booking) -> Booking:
        """Approve booking"""
        booking.status = BookingStatus.APPROVED
        db.commit()
        db.refresh(booking)
        return booking

    @staticmethod
    def reject_booking(db: Session, booking: Booking) -> Booking:
        """Reject booking"""
        booking.status = BookingStatus.REJECTED
        db.commit()
        db.refresh(booking)
        return booking