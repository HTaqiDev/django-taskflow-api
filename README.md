# 🚀 TaskFlow API — Modern Task & Project Management REST API

A production-ready, clean-architecture RESTful API built with **Python 3.12, Django 4.2, and Django REST Framework (DRF)**. Designed for secure, scalable task management with token-based authentication, filtering, pagination, and automated unit testing.

Developed by **[Hossein Taghi (HTaqiDev)](https://github.com/HTaqiDev)**.

---

## 🌟 Features

- **🔐 Token Authentication & Authorization:** Secure user registration, login, and token-based API access.
- **📋 Task Management (CRUD):** Create, retrieve, update, and delete tasks with ownership permissions.
- **🏷️ Category System:** Organize tasks into custom categories.
- **🔍 Filtering, Search & Ordering:** Filter tasks by status (`pending`, `in_progress`, `completed`), priority (`low`, `medium`, `high`), or category. Full-text search on titles and descriptions.
- **⚡ Pagination:** Built-in page-number pagination for optimized API responses.
- **🧪 Automated Test Suite:** 100% test coverage for auth endpoints, task CRUD, and permission boundaries.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Framework:** Django 4.2 & Django REST Framework (DRF)
- **Database:** SQLite (Development) / PostgreSQL compatible
- **Filtering:** `django-filter`
- **Version Control:** Git & GitHub

---

## 📁 Architecture Overview

```
django-taskflow-api/
├── core/                  # Django project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                 # Task Management Application
│   ├── models.py          # Category and Task models
│   ├── serializers.py     # DRF serializers & validations
│   ├── views.py           # ViewSets & Auth API views
│   ├── urls.py            # API routes
│   └── tests.py           # Unit test suite
├── manage.py
└── requirements.txt
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/HTaqiDev/django-taskflow-api.git
cd django-taskflow-api
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Test Suite
```bash
python manage.py test
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
The API will be live at `http://127.0.0.1:8000/api/`.

---

## 📡 API Endpoints Reference

### 🔐 Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/auth/register/` | Register a new user account | No |
| `POST` | `/api/auth/login/` | Login and receive API Token | No |

#### Register Sample Request
```json
POST /api/auth/register/
{
  "username": "developer",
  "email": "dev@example.com",
  "password": "securepassword123"
}
```

#### Login Sample Response
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "username": "developer"
}
```

---

### 📋 Task Endpoints (Requires `Authorization: Token <your_token>`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/` | List user's tasks (supports `status`, `priority`, `search`) |
| `POST` | `/api/tasks/` | Create a new task |
| `GET` | `/api/tasks/{id}/` | Retrieve task details |
| `PUT/PATCH` | `/api/tasks/{id}/` | Update a task |
| `DELETE` | `/api/tasks/{id}/` | Delete a task |

#### Create Task Sample Request
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Build Django REST API Portfolio",
    "description": "Implement authentication, filtering, and tests",
    "status": "in_progress",
    "priority": "high"
  }'
```

#### Filter & Search Tasks
```bash
# Filter by status and priority
GET /api/tasks/?status=in_progress&priority=high

# Search by keyword
GET /api/tasks/?search=portfolio
```

---

## 👨‍💻 Author

**Hossein Taghi**  
- **GitHub:** [@HTaqiDev](https://github.com/HTaqiDev)  
- **Role:** Computer Science Student & Backend Developer  
- **Specialization:** Python, Django, REST APIs, Web Architecture
