"""Helper utilities"""
import uuid
from datetime import datetime


def generate_id(prefix: str = "") -> str:
    """Generate unique ID"""
    unique_id = str(uuid.uuid4())
    return f"{prefix}{unique_id}" if prefix else unique_id


def calculate_booking_amount(rent_price_per_day: float, start_date: datetime, end_date: datetime) -> float:
    """Calculate total booking amount"""
    days = (end_date - start_date).days
    return rent_price_per_day * days if days > 0 else 0