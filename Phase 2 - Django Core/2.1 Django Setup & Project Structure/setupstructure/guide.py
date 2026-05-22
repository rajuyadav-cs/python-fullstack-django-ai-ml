# ============================================
# DJANGO LEARNING NOTES
# ============================================

# --------------------------------------------
# 1. What is Django?
# --------------------------------------------

# Django is a Python web framework.
# It is used to build websites and web applications.

# Django already provides many built-in features:
# - URL routing
# - Database handling
# - Authentication system
# - Admin panel
# - Security features
# - Template engine

# Because of this, development becomes faster
# and more organized.


# --------------------------------------------
# 2. Installing Django
# --------------------------------------------

# Command:
# pip install django

# pip is Python's package manager.
# This command installs Django into your system.

# Check installed version:
# django-admin --version


# --------------------------------------------
# 3. Creating a Django Project
# --------------------------------------------

# Command:
# django-admin startproject myproject

# This creates a new Django project.

# Project structure:

"""
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
"""


# --------------------------------------------
# 4. What does manage.py do?
# --------------------------------------------

# manage.py is Django's command-line utility.

# It is used to run Django commands such as:

# python manage.py runserver
# python manage.py startapp blog
# python manage.py migrate

# Simple understanding:
# manage.py = remote control of the Django project


# --------------------------------------------
# 5. Running the Development Server
# --------------------------------------------

# Move inside the project folder:

# cd myproject

# Run the server:
# python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/


# --------------------------------------------
# 6. Stopping the Server
# --------------------------------------------

# In terminal:
# Ctrl + C

# This stops the running Django process.

# Internally:
# Ctrl + C sends an interrupt signal
# which terminates the Python server process.


# ============================================
# END OF CURRENT NOTES
# ============================================


# --------------------------------------------
# 7. __init__.py
# --------------------------------------------

# This file tells Python that the folder
# should be treated as a Python package.

# It is usually empty.


# --------------------------------------------
# 8. settings.py
# --------------------------------------------

# Main configuration file of Django project.

# Contains:
# - Installed apps
# - Database settings
# - Security settings
# - Static files settings
# - Template settings
# - Middleware settings

# Example:
# DEBUG = True

# True  -> development mode
# False -> production mode


# --------------------------------------------
# INSTALLED_APPS
# --------------------------------------------

# List of active Django apps.

# Example:
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'blog',
# ]


# --------------------------------------------
# DATABASES
# --------------------------------------------

# Database configuration.

# Default database:
# SQLite

# Example:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# --------------------------------------------
# STATIC_URL
# --------------------------------------------

# Used for static files:
# - CSS
# - JavaScript
# - Images


# --------------------------------------------
# MEDIA_ROOT and MEDIA_URL
# --------------------------------------------

# Used for uploaded media files.

# Examples:
# profile pictures
# uploaded PDFs
# videos


# --------------------------------------------
# 9. urls.py
# --------------------------------------------

# Handles URL routing.

# Example flow:
# Browser Request -> urls.py -> View -> Response


# --------------------------------------------
# 10. wsgi.py
# --------------------------------------------

# Used in production deployment.

# WSGI = Web Server Gateway Interface

# Connects Django with traditional web servers.


# --------------------------------------------
# 11. asgi.py
# --------------------------------------------

# Modern async interface.

# ASGI = Asynchronous Server Gateway Interface

# Used for:
# - WebSockets
# - Real-time apps
# - Live chat
# - Notifications


# --------------------------------------------
# WSGI vs ASGI
# --------------------------------------------

# WSGI:
# - synchronous
# - traditional applications

# ASGI:
# - asynchronous
# - modern real-time applications


# --------------------------------------------
# 12. Django Project vs App
# --------------------------------------------

# Project:
# Complete website/application.

# App:
# A specific module or feature.

# Example:
# E-commerce project may contain:
# - users app
# - products app
# - orders app


# --------------------------------------------
# 13. Creating an App
# --------------------------------------------

# Command:
# python manage.py startapp blog


# --------------------------------------------
# 14. App Structure
# --------------------------------------------

"""
blog/
│
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
"""


# --------------------------------------------
# 15. views.py
# --------------------------------------------

# Handles request and returns response.

# Example:
#
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("Hello World")


# --------------------------------------------
# 16. models.py
# --------------------------------------------

# Defines database structure.

# Example:
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()


# --------------------------------------------
# ORM (Object Relational Mapping)
# --------------------------------------------

# Python classes are converted into database tables.


# --------------------------------------------
# 17. admin.py
# --------------------------------------------

# Registers models into Django admin panel.

# Example:
#
# admin.site.register(Post)


# --------------------------------------------
# 18. apps.py
# --------------------------------------------

# App configuration file.


# --------------------------------------------
# 19. tests.py
# --------------------------------------------

# Used for automated testing.


# --------------------------------------------
# 20. migrations/
# --------------------------------------------

# Stores database migration files.


# --------------------------------------------
# 21. Migration Commands
# --------------------------------------------

# Create migration files:
# python manage.py makemigrations

# Apply migrations:
# python manage.py migrate


# --------------------------------------------
# 22. Register App
# --------------------------------------------

# Add app inside INSTALLED_APPS in settings.py

# Example:
# INSTALLED_APPS = [
#     'blog',
# ]


# --------------------------------------------
# 23. Django Request Flow
# --------------------------------------------

# Browser Request
#       ↓
# urls.py
#       ↓
# views.py
#       ↓
# models.py
#       ↓
# Response

# --------------------------------------------
# 36. settings.py
# --------------------------------------------

# Main configuration file of Django project.


# --------------------------------------------
# INSTALLED_APPS
# --------------------------------------------

# Contains all active Django apps.

# Built-in apps example:
#
# 'django.contrib.admin'
# 'django.contrib.auth'

# Custom app example:
#
# 'blog'

# If an app is not added here,
# Django will not recognize it.


# --------------------------------------------
# DATABASES
# --------------------------------------------

# Database configuration section.

# Default SQLite example:
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Django ORM uses this configuration
# to communicate with the database.


# --------------------------------------------
# STATIC_URL
# --------------------------------------------

# Used for static files:
# - CSS
# - JavaScript
# - logos
# - icons

# Example:
# STATIC_URL = '/static/'


# --------------------------------------------
# MEDIA_ROOT
# --------------------------------------------

# Physical folder path for uploaded files.

# Example:
# MEDIA_ROOT = BASE_DIR / 'media'


# --------------------------------------------
# MEDIA_URL
# --------------------------------------------

# URL path for uploaded files.

# Example:
# MEDIA_URL = '/media/'


# --------------------------------------------
# Static vs Media Files
# --------------------------------------------

# Static files:
# developer-provided assets

# Media files:
# user-uploaded files


# --------------------------------------------
# Development vs Production
# --------------------------------------------

# Development:
# DEBUG = True

# Production:
# DEBUG = False

# DEBUG=True should NEVER be used
# in production.


# --------------------------------------------
# ALLOWED_HOSTS
# --------------------------------------------

# Security setting for allowed domains.

# Example:
# ALLOWED_HOSTS = ['example.com']


# --------------------------------------------
# Environment-Specific Settings
# --------------------------------------------

# Large projects often use:
#
# settings/
#     base.py
#     development.py
#     production.py
#
# Different environments use
# different configurations.

# --------------------------------------------
# 37. Environment-Specific Settings
# --------------------------------------------

# Large Django projects often separate settings
# for development and production environments.


# Example structure:
#
# settings/
#     ├── base.py
#     ├── development.py
#     └── production.py


# --------------------------------------------
# base.py
# --------------------------------------------

# Contains common/shared settings.


# --------------------------------------------
# development.py
# --------------------------------------------

# Development environment settings.

# Example:
#
# from .base import *
#
# DEBUG = True

# Usually uses SQLite database.


# --------------------------------------------
# production.py
# --------------------------------------------

# Production/live server settings.

# Example:
#
# from .base import *
#
# DEBUG = False
# ALLOWED_HOSTS = ['example.com']

# Usually uses PostgreSQL database.


# --------------------------------------------
# Running Specific Settings
# --------------------------------------------

# Development:
#
# python manage.py runserver
# --settings=myproject.settings.development

# Production:
#
# python manage.py runserver
# --settings=myproject.settings.production


# --------------------------------------------
# Environment Variables
# --------------------------------------------

# Sensitive values should not be hardcoded.

# Bad:
# SECRET_KEY = "mysecret"

# Better:
#
# import os
# SECRET_KEY = os.getenv("SECRET_KEY")


# --------------------------------------------
# Common Environment Variables
# --------------------------------------------

# SECRET_KEY
# DB_NAME
# DB_USER
# DB_PASSWORD


# --------------------------------------------
# .env Files
# --------------------------------------------

# Example:
#
# SECRET_KEY=mysecret
# DEBUG=False
# DB_NAME=mydb


# --------------------------------------------
# Benefits of Environment-Specific Settings
# --------------------------------------------

# - better security
# - cleaner architecture
# - easier deployment
# - scalable configuration