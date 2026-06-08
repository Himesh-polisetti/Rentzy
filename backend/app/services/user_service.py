"""User service"""
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserRegister
from app.utils.security import get_password_hash, verify_password
from app.utils.helpers import generate_id
from app.models.user import UserRole


class UserService:
    """User service for database operations"""

    @staticmethod
    def create_user(db: Session, user_data: UserRegister) -> User:
        """Create new user"""
        user = User(
            id=generate_id("user_"),
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=get_password_hash(user_data.password),
            role=UserRole(user_data.role),
            city=user_data.city,
            state=user_data.state,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> User:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def verify_user_credentials(db: Session, email: str, password: str) -> User:
        """Verify user credentials"""
        user = UserService.get_user_by_email(db, email)
        if user and verify_password(password, user.hashed_password):
            return user
        return None