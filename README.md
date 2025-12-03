# 🧰 Job Board Backend (Django + DRF + JWT + Docker)

A robust backend API for a Job Board platform built with **Django**, **Django REST Framework**, **JWT Authentication**, **PostgreSQL**, and **Docker**.

## 📌 Features
- JWT Authentication (Register, Login, Logout, Refresh)
- Role-Based Access Control
- Job Posting CRUD
- Company Management
- Applicants & Applications
- PostgreSQL Database
- Docker & Docker Compose Support

## 📁 Project Structure
```
project/
│── manage.py
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── .env.example
│── .env
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── users/
│   ├── jobs/
│   └── companies/
```

## 🔐 Environment Variables
Copy `.env.example` → `.env`:
```
cp .env.example .env
```

### Required Variables
```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=*

DATABASE_NAME=jobboard_db
DATABASE_USER=postgres
DATABASE_PASSWORD=password123
DATABASE_HOST=localhost
DATABASE_PORT=5432

JWT_ACCESS_TOKEN_LIFETIME=5
JWT_REFRESH_TOKEN_LIFETIME=1440
```

## 🚀 Installation
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🐳 Docker
```
docker-compose up --build
```

## 🔑 API Routes (JWT)
- POST /api/auth/register/
- POST /api/auth/login/
- POST /api/auth/logout/
- POST /api/auth/token/refresh/
