# Ridelu Backend

A scalable, modular Django-based backend for a ride-hailing platform.  
Includes support for drivers, passengers, ride management, authentication, and real-time services.

---

## Project Structure
## Project Structure

- apps
  - authentication
    - __init__.py
    - models.py
    - api.py
  - drivers
    - models.py
  - passengers
    - models.py
  - rides
    - models.py
- core
  - settings
    - base.py
    - local.py
    - production.py
  - celery.py
  - exceptions.py
  - logging.py
  - metrics.py
  - tasks
    - cleanup.py
    - notifications.py
    - payments.py
    - rides.py
- shared
  - utils.py
  - cache.py
  - constants.py
  - location
    - distance.py
  - notifications
    - email.py
    - push.py
    - sms.py
- manage.py
- db.sqlite3
- requirements
  - base.txt
  - local.txt
  - production.txt
- requirements.txt
- ridelu_backend
  - __init__.py
  - asgi.py
  - urls.py
  - wsgi.py

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