# RENTZY Backend

FastAPI-based REST API for the RENTZY rental marketplace platform.

## Setup

### Prerequisites
- Python 3.8+
- PostgreSQL

### Installation

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
```

Edit `.env` with your database credentials and JWT secret.

4. Run migrations:
```bash
alembic upgrade head
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`
Swagger docs: `http://localhost:8000/docs`
ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
app/
├── main.py           # FastAPI application
├── config.py         # Configuration
├── database.py       # Database setup
├── dependencies.py   # Dependency injection
├── models/           # SQLAlchemy models
├── schemas/          # Pydantic schemas
├── routes/           # API endpoints
├── services/         # Business logic
└── utils/            # Utilities
```

## API Endpoints

See main README for full API documentation.

## Database

PostgreSQL is used as the database. Alembic is used for migrations.

### Creating migrations:
```bash
alembic revision --autogenerate -m "Migration message"
alembic upgrade head
```

## Authentication

JWT tokens are used for authentication. Token is required in the `Authorization` header as `Bearer <token>`.
