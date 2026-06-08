"""User schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    """User registration schema"""
    email: EmailStr
    username: str
    full_name: str
    password: str
    role: str = "USER"
    city: Optional[str] = None
    state: Optional[str] = None


class UserLogin(BaseModel):
    """User login schema"""
    email: str
    password: str


class UserResponse(BaseModel):
    """User response schema"""
    id: str
    email: str
    username: str
    full_name: str
    role: str
    city: Optional[str]
    state: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: datetime

    class Config:
        """Config"""
        from_attributes = True