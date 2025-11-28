# FastAPI Blog REST API

A RESTful API for blog management built with FastAPI, featuring JWT authentication and SQLAlchemy ORM.

## Features

- User authentication with JWT (register, login)
- Blog posts CRUD with categories
- SQLAlchemy ORM with SQLite
- Pydantic validation and settings
- Swagger/OpenAPI documentation

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (python-jose)
- **Password Hashing**: passlib with bcrypt
- **Validation**: Pydantic

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository
```bash
git clone https://github.com/fupenglove2000/fastapi-blog-api.git
cd fastapi-blog-api
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run the server
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token
- `GET /auth/me` - Get current user info

### Posts
- `GET /posts` - List all posts
- `GET /posts/{id}` - Get a single post
- `POST /posts` - Create a new post (auth required)
- `PUT /posts/{id}` - Update a post (auth required)
- `DELETE /posts/{id}` - Delete a post (auth required)

### Categories
- `GET /categories` - List all categories
- `POST /categories` - Create a new category (auth required)
- `DELETE /categories/{id}` - Delete a category (auth required)
