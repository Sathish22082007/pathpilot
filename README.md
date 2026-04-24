# PathPilot

A full-stack web application built with Django.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML/CSS/JS
- **Database**: SQLite (development)

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Project Structure

```
pathpilot/
├── app/              # Main Django app
├── core/             # Django project settings
├── templates/         # HTML templates
├── frontend/         # Frontend assets
├── backend/          # Backend code
├── manage.py         # Django CLI
└── db.sqlite3        # Database
```

## Features

- User authentication
- Dashboard interface
- Landing page

---

Built with Django
