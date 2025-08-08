# Little Lemon

A Django web application capstone project from the Meta Back-End Developer Professional Certificate (coursera.org).

## Overview

Little Lemon is a restaurant reservation and menu management web app built using Django. It includes dynamic views, user authentication, and supports managing menu items and bookings.

## Features

- Django backend following the MVT (Model-View-Template) pattern  
- Manage menu items and reservations via templates and views  
- User authentication and admin interface  
- SQLite for development (easily switchable to MySQL or PostgreSQL)

## Installation & Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd littlelemon

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```
