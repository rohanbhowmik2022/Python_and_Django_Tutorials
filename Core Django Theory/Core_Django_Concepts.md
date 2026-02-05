Django
----------

Django is a high-level Python web framework used to build secure, scalable, and maintainable web applications fast.

Django lets you go from idea → working web app without reinventing common things like login systems, databases, forms, or admin panels.

Why people love Django

1. Written in Python 🐍
2. Handles backend heavy lifting for you
3. Secure by default (SQL injection, CSRF, XSS protection)
4. Used by big platforms (Instagram, Pinterest, Mozilla)

2. Django’s MVT Architecture

Django follows MVT, not MVC.

MVT = Model – View – Template
--------------------------------
Model -> Database structure & business logic
View -> Handles request logic (what data to send)
Template -> UI (HTML + Django template language)

Flow (real-world analogy)
--------------------------
Think of ordering food 🍔:

User (Browser) → places order (HTTP request)
URL Dispatcher → decides which view should handle it
View → processes logic, fetches data from Model
Template → formats data into HTML
Response → sent back to browser

Key clarification (important!)
-------------------------------
In Django:

View = Controller (MVC)
Template = View (MVC)

3. Django Philosophy

Django has strong opinions about how web apps should be built.
a) DRY – “Don’t Repeat Yourself”
Every piece of knowledge should have one, and only one, authoritative place
Example:
Define a model once
Django automatically uses it for:
Database schema
Admin panel
Forms

APIs (with DRF)
No copy-pasting logic everywhere.

✅ Less bugs
✅ Easier maintenance
✅ Cleaner code

b) Batteries Included 🔋

Django ships with almost everything you need:

Authentication & Authorization

Admin panel

ORM (database abstraction)

Forms & validation

Security features

Middleware

Caching

Sessions

So instead of:

“Which library should I use for login?”

Django says:

“Relax. It’s already there.”

This is opposite of minimal frameworks like Flask.

4. Django Project vs Django App

This is a VERY common interview question.

Django Project

The entire website

Contains global configuration

Created using:

django-admin startproject myproject


Includes:

settings.py

urls.py

wsgi.py / asgi.py

Django App

A single feature/module

Created inside a project

Examples:

users

blog

payments

products

Created using:

python manage.py startapp blog

Real-world analogy 🏢

Project = Company

Apps = Departments (HR, Finance, Sales)

One project can have multiple apps, and apps can be reused across projects.

5. Why Django Is Opinionated
Django is called opinionated because:
It enforces a specific way of doing things
Examples:
You must define models in models.py
URLs go in urls.py
Views follow specific patterns
ORM usage is encouraged over raw SQL
Settings structure is predefined

Why this is GOOD

✅ Consistency across projects
✅ Easier onboarding for teams
✅ Best practices by default
✅ Fewer architectural decisions to stress over

Tradeoff

❌ Less flexibility compared to micro-frameworks
❌ You must “think the Django way”

But once you do—productivity 🚀
-------------------------------------------------
One-line summaries (great for exams/interviews)
-------------------------------------------------
Django: A high-level Python web framework for rapid development
MVT: Model handles data, View handles logic, Template handles UI
DRY: Avoid repetition, define logic once
Batteries included: Built-in tools for almost everything
Project vs App: Project = whole site, App = feature/module
Opinionated: Django enforces best practices and structure