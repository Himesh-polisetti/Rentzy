# RENTZY - Rental Marketplace Platform

A scalable rental marketplace platform built with React + Vite, FastAPI, and PostgreSQL. Phase 1 focuses on core functionality: user authentication, product management, bookings, and wishlist features.

## 🎯 Phase 1 Features

- **User Authentication**: Register, Login, JWT-based auth with role-based access (USER, OWNER, ADMIN)
- **Product Management**: Owners can add, edit, delete products with multiple images
- **Bookings**: Users can book products; Owners can approve/reject requests
- **Wishlist**: Users can save favorite products
- **Location Services**: Geolocation support for filtering products
- **Categories**: 12 predefined rental categories
- **Responsive UI**: Amazon/Flipkart/Airbnb-inspired design

## 📋 Tech Stack

**Frontend:**
- React 18 + Vite
- Tailwind CSS
- Redux Toolkit
- React Router DOM
- Axios

**Backend:**
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic (migrations)
- Pydantic
- JWT Authentication

## 🚀 Quick Start

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your database URL and JWT secret

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

Backend runs on `http://localhost:8000`
Swagger docs: `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env

# Start development server
npm run dev
```

Frontend runs on `http://localhost:5173`

## 📁 Project Structure

```
rentzy/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry
│   │   ├── config.py            # Configuration
│   │   ├── database.py          # Database connection
│   │   ├── dependencies.py      # Shared dependencies
│   │   ├── schemas/             # Pydantic models
│   │   ├── models/              # SQLAlchemy models
│   │   ├── routes/              # API endpoints
│   │   ├── services/            # Business logic
│   │   └── utils/               # Helpers
│   ├── alembic/                 # Database migrations
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx             # Entry point
│   │   ├── App.jsx              # Root component
│   │   ├── components/
│   │   │   ├── common/          # Reusable components
│   │   │   ├── layout/          # Layout components
│   │   │   └── pages/           # Page components
│   │   ├── pages/
│   │   ├── store/               # Redux setup
│   │   ├── hooks/               # Custom hooks
│   │   ├── utils/
│   │   ├── services/            # API calls
│   │   ├── styles/              # Global styles
│   │   └── App.css
│   ├── index.html
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── package.json
│   ├── .env.example
│   └── README.md
│
└── README.md
```

## 🔒 Authentication

- JWT-based authentication with access tokens
- Password hashing with bcrypt
- Role-based access control (RBAC)
- Protected routes on frontend and backend

## 📦 Database Schema

- **users**: User accounts with roles
- **categories**: Product categories
- **products**: Rental products with pricing
- **product_images**: Multiple images per product
- **wishlists**: User favorites
- **bookings**: Rental requests with status tracking

## 🎨 UI Design Inspiration

- Amazon: Large search bar, category navigation
- Flipkart: Compact product cards, category browsing
- Airbnb: Booking flow, location services
- Croma: Professional marketplace styling

**Design Specs:**
- White background
- Professional marketplace layout
- Responsive (mobile, tablet, desktop)
- No dark theme
- No purple SaaS styling

## 📝 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### Products
- `GET /products` - List products with filters
- `GET /products/{id}` - Get product details
- `POST /products` - Create product (owner only)
- `PUT /products/{id}` - Update product (owner only)
- `DELETE /products/{id}` - Delete product (owner only)

### Wishlist
- `GET /wishlist` - Get user wishlist
- `POST /wishlist/{product_id}` - Add to wishlist
- `DELETE /wishlist/{product_id}` - Remove from wishlist

### Bookings
- `POST /bookings` - Create booking
- `GET /bookings/my` - Get user bookings
- `GET /bookings/owner` - Get owner's booking requests
- `PUT /bookings/{id}/approve` - Approve booking
- `PUT /bookings/{id}/reject` - Reject booking

### Categories
- `GET /categories` - List all categories

## 🔄 Future Phases

- Phase 2: ML-based recommendations
- Phase 3: AI chatbot support
- Phase 4: OCR verification
- Phase 5: Fraud detection & trust scores

## 📧 Support

For issues or questions, please create an issue on GitHub.

## 📄 License

MIT License