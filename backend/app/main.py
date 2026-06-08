"""FastAPI application entry point"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.database import Base, engine
from app.routes import auth, products, categories, wishlist, bookings

# Create database tables
Base.metadata.create_all(bind=engine)

settings = get_settings()

app = FastAPI(
    title="RENTZY API",
    description="Rental Marketplace Platform API",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(wishlist.router)
app.include_router(bookings.router)


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "RENTZY API is running"}