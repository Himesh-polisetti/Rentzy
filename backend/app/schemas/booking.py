"""Booking schemas"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingCreate(BaseModel):
    """Booking create schema"""
    product_id: str
    start_date: datetime
    end_date: datetime


class BookingResponse(BaseModel):
    """Booking response schema"""
    id: str
    user_id: str
    product_id: str
    start_date: datetime
    end_date: datetime
    total_amount: float
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        """Config"""
        from_attributes = True