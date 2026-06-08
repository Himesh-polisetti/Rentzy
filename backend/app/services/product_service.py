"""Product service"""
from sqlalchemy.orm import Session
from app.models import Product, Category
from app.schemas import ProductCreate, ProductUpdate
from app.utils.helpers import generate_id
from typing import List, Optional


class ProductService:
    """Product service for database operations"""

    @staticmethod
    def create_product(db: Session, product_data: ProductCreate, owner_id: str) -> Product:
        """Create new product"""
        product = Product(
            id=generate_id("prod_"),
            title=product_data.title,
            description=product_data.description,
            category_id=product_data.category_id,
            owner_id=owner_id,
            brand=product_data.brand,
            original_price=product_data.original_price,
            rent_price_per_day=product_data.rent_price_per_day,
            city=product_data.city,
            state=product_data.state,
            latitude=product_data.latitude,
            longitude=product_data.longitude,
            availability=product_data.availability,
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_product_by_id(db: Session, product_id: str) -> Optional[Product]:
        """Get product by ID"""
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def get_products(
        db: Session,
        category_id: Optional[str] = None,
        city: Optional[str] = None,
        skip: int = 0,
        limit: int = 10,
    ) -> List[Product]:
        """Get products with optional filters"""
        query = db.query(Product).filter(Product.availability == True)
        if category_id:
            query = query.filter(Product.category_id == category_id)
        if city:
            query = query.filter(Product.city == city)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_product(db: Session, product: Product, product_data: ProductUpdate) -> Product:
        """Update product"""
        for field, value in product_data.dict(exclude_unset=True).items():
            setattr(product, field, value)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(db: Session, product: Product) -> None:
        """Delete product"""
        db.delete(product)
        db.commit()

    @staticmethod
    def get_owner_products(db: Session, owner_id: str) -> List[Product]:
        """Get products by owner"""
        return db.query(Product).filter(Product.owner_id == owner_id).all()