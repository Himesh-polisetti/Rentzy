"""Product routes"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database import get_db
from app.dependencies import get_current_user, get_owner_user
from app.schemas import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=List[ProductResponse])
def get_products(
    category_id: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    skip: int = Query(0),
    limit: int = Query(10),
    db: Session = Depends(get_db),
):
    """Get products with optional filters"""
    products = ProductService.get_products(db, category_id, city, skip, limit)
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    """Get product by ID"""
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    current_user = Depends(get_owner_user),
    db: Session = Depends(get_db),
):
    """Create new product (owners only)"""
    product = ProductService.create_product(db, product_data, current_user.id)
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: str,
    product_data: ProductUpdate,
    current_user = Depends(get_owner_user),
    db: Session = Depends(get_db),
):
    """Update product (owner only)"""
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own products",
        )
    product = ProductService.update_product(db, product, product_data)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: str,
    current_user = Depends(get_owner_user),
    db: Session = Depends(get_db),
):
    """Delete product (owner only)"""
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    if product.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own products",
        )
    ProductService.delete_product(db, product)
    return None