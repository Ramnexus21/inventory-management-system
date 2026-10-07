# Inventory Management System

A full-stack inventory management application built with **React, FastAPI, SQLAlchemy, and PostgreSQL**.

## Tech Stack

- **Frontend:** React, JavaScript
- **Backend:** Python, FastAPI, Uvicorn
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic

## Architecture

```text
React Frontend
     │
     │ HTTP / JSON
     ▼
FastAPI Backend
     │
     │ SQLAlchemy
     ▼
PostgreSQL Database
```

## Features

- View products
- Add products
- Search products
- PostgreSQL persistent storage
- REST API
- API validation with Pydantic
- CORS-enabled React ↔ FastAPI communication

## Project Structure

```text
PRODUCT INVENTARY MANAGEMENT/
│
├── frontend_model/       # React frontend
│
├── main.py               # FastAPI application & API routes
├── database.py           # Database connection & SQLAlchemy setup
├── database_models.py    # SQLAlchemy database models
├── models.py             # Pydantic API models
├── .env                  # Database configuration
├── .gitignore
└── README.md
```

## Database

Database:

```text
inventory_db
```

Main table:

```text
products
├── id
├── name
├── description
├── price
└── quantity
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Health/root endpoint |
| GET | `/products/` | Get all products |
| GET | `/products/{id}` | Get one product |
| POST | `/products/` | Create a product |

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Setup

### Backend

Create and activate virtual environment:

```bash
python -m venv env
env\Scriptsctivate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv
```

Configure `.env`:

```env
db_url=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/inventory_db
```

Run backend:

```bash
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend_model
npm install
npm start
```

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://127.0.0.1:8000
```

## Important

- Keep the PostgreSQL password in `.env`.
- Add `.env` to `.gitignore`.
- Run **both frontend and backend** during development.
- CORS must allow the React frontend origin.

## Learning Goal

This project demonstrates the core full-stack flow:

```text
React
  ↓
HTTP Request
  ↓
FastAPI
  ↓
Pydantic Validation
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
  ↓
HTTP Response
  ↓
React
```

## Future Improvements

- Complete CRUD
- Authentication & authorization
- Pagination and filtering
- Database migrations with Alembic
- Automated tests
- Docker
- CI/CD
- Production deployment
