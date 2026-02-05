settings.py

Think of settings.py as the brain/config center of your Django project.

It defines how your project behaves.

What lives inside settings.py?

a) Core configuration

DEBUG – development vs production mode
SECRET_KEY – cryptographic signing (sessions, cookies, tokens)
ALLOWED_HOSTS – which domains can access your app

b) Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'blog',
]

This tells Django:

“These are the apps I want active in this project”
No app works unless it’s listed here.

c) Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Switching from SQLite → PostgreSQL/MySQL happens here only (DRY in action).

d) Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

Middleware = request/response checkpoints

Examples:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

Security
Authentication
Sessions
CSRF protection

e) Templates & Static files

TEMPLATES

STATIC_URL

MEDIA_ROOT

These control HTML rendering, CSS, JS, images, etc.


In one line:

settings.py controls everything about configuration, not logic.

2. manage.py

manage.py is your command-line assistant for Django.
You don’t run Django directly—you run commands through manage.py.

python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp blog

What does manage.py actually do?

Sets the correct Django settings module
Acts as a wrapper around Django’s admin commands
Provides access to Django’s internals from the terminal

You can think of it as:
“The remote control for your Django project”

Important distinction

django-admin → generic Django tool
manage.py → project-specific version of django-admin

