# Library Management API

A professional RESTful API built with Django REST Framework for managing library operations.

## Features

- User Registration
- JWT Authentication
- Role-Based Access Control
- Book Management
- Borrowing System
- Return System
- Borrowing History
- Search Functionality
- Pagination
- Swagger Documentation
- Unit Testing

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- drf-spectacular (Swagger)

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into project folder

```bash
cd library_management_api
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Run development server

```bash
python manage.py runserver
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

## Author

Idah Onuh John