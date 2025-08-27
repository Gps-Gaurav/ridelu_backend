# Ridelu Backend

A scalable, modular Django-based backend for a ride-hailing platform.  
Includes support for drivers, passengers, ride management, authentication, and real-time services.

---

## Project Structure

├── apps
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── models.cpython-313.pyc
│   │   ├── api.py
│   │   ├── migrations
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-313.pyc
│   │   │   │   └── 0001_initial.cpython-313.pyc
│   │   │   └── 0001_initial.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── google_auth.py
│   │   │   └── otp_auth.py
│   │   ├── tasks.py
│   │   └── urls.py
│   ├── drivers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── apps.cpython-313.pyc
│   │   │   └── models.cpython-313.pyc
│   │   ├── api.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── availability.py
│   │   │   ├── earnings.py
│   │   │   └── vehicle.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── profile.py
│   │       └── rides.py
│   ├── passengers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── models.cpython-313.pyc
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── booking.py
│   │   │   └── payment.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── profile.py
│   │       └── rides.py
│   └── rides
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-313.pyc
│       │   └── models.cpython-313.pyc
│       ├── api.py
│       ├── models.py
│       ├── permissions.py
│       ├── serializers.py
│       ├── services
│       │   ├── __init__.py
│       │   ├── matching.py
│       │   ├── pricing.py
│       │   └── tracking.py
│       └── tasks.py
├── core
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-313.pyc
│   ├── celery.py
│   ├── exceptions.py
│   ├── logging.py
│   ├── metrics.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   └── base.cpython-313.pyc
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   └── tasks
│       ├── __init__.py
│       ├── cleanup.py
│       ├── notifications.py
│       ├── payments.py
│       └── rides.py
├── db.sqlite3
├── manage.py
├── README.md
├── requirements
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── requirements.txt
├── ridelu_backend
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── wsgi.cpython-313.pyc
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
└── shared
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-313.pyc
    ├── cache.py
    ├── constants.py
    ├── location
    │   ├── __init__.py
    │   └── distance.py
    ├── notifications
    │   ├── __init__.py
    │   ├── email.py
    │   ├── push.py
    │   └── sms.py
    └── utils.py

---


---

## Features

- Authentication: OTP login and Google OAuth support
- Drivers: Profile management, availability, earnings, vehicles
- Passengers: Ride booking, payments, profile management
- Rides: Matching, pricing, and real-time tracking
- Async Tasks: Celery and Redis integration
- Notifications: Email, SMS, and push support
- Environment-specific settings: Local and production separation
- Modular architecture: Shared utilities and domain-driven apps

---

### Create virtual environment

python -m venv .venv
source .venv/bin/activate

## Install dependencies

## Base dependencies

pip install -r requirements/base.txt


## Local (development)

pip install -r requirements/local.txt


## Production:

pip install -r requirements/production.txt

Apply migrations
python manage.py migrate

## Run development server
python manage.py runserver

## Tech Stack

Backend: Django, Django REST Framework

Async Tasks: Celery, Redis

Database: PostgreSQL (recommended), SQLite (local dev)

Storage: AWS S3 (via django-storages)

Auth: Google OAuth, OTP-based login

Monitoring: Custom logging and metrics

## API Endpoints

/auth/ → Authentication APIs

/drivers/ → Driver-related APIs

/passengers/ → Passenger-related APIs

/rides/ → Ride management APIs

(Detailed API docs can be generated with DRF + drf-yasg or Swagger)

## Deployment

Production server: Gunicorn + Nginx

Task queue: Celery + Redis

Static & Media files: AWS S3 via django-storages

Env management: .env files with django-environ