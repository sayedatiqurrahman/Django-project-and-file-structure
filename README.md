# Django Tutorial: A Concise Guide

This guide provides a quick overview of creating a basic Django poll application.

## Prerequisites

*   Python 3.10 or later
*   uv (Install with `pip install uv`)
*   Django (Install with `uv pip install Django` after activating the virtual environment)

## Creating a Virtual Environment with uv

1.  Create a virtual environment:

    ```bash
    uv venv
    ```

2.  Activate the virtual environment:

    *   Linux/macOS and Git Bash on Windows:

        ```bash
        source .venv/bin/activate
        ```

    *   Windows:

        ```bash
        .venv\Scripts\activate
        ```

3.  Install Django:

    ```bash
    uv pip install Django
    ```

## Creating a Project

1.  Bootstrap a new Django project (this command will create a nested folder structure: `your-project-name/your-project-name`):

    ```bash
    django-admin startproject mysite your-project-name
    ```

2.  Change directory to the outer project folder:

    ```bash
    cd your-project-name
    ```

## Running the Development Server

1.  Start the development server:

    ```bash
    py manage.py runserver
    ```
    (You may see a warning about unapplied migrations; you can ignore this for now.)
2.  Visit `http://127.0.0.1:8000/` in your browser to see the "Congratulations!" page.

## Creating the Polls App

1.  Create the polls app:

    ```bash
    py manage.py startapp polls
    ```

## Write your first view

1.  Open the file `polls/views.py` and put the following Python code in it:

    ```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    ```

2.  To define a URLconf for the polls app, create a file `polls/urls.py` with the following content:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```

3.  To do this, add an import for `django.urls.include` in `mysite/urls.py` and insert an `include()` in the `urlpatterns` list, so you have:

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("polls/", include("polls.urls")),
        path("admin/", admin.site.urls),
    ]
    ```

4.  Verify it’s working with the following command:

    ```bash
    py manage.py runserver
    ```

    Go to `http://localhost:8000/polls/` in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

## Django Project and File Structure

### Project Structure (mysite)

*   `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
*   `mysite/`: A directory that is the actual Python package for your project.
    *   `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
    *   `settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
    *   `urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
    *   `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
    *   `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.

### App Structure (polls)

*   `polls/`: This directory structure will house the poll application.
    *   `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
    *   `admin.py`: Files for configuration for the Django admin interface.
    *   `apps.py`: Files for configuration for the polls application.
    *   `migrations/`: Directory for database migrations.
        *   `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
    *   `models.py`: Files for Data models for the polls application.
    *   `tests.py`: Files for tests for the polls application.
    *   `views.py`: Files for view functions that handle requests and return responses.
    *   `urls.py`: Files for URL configurations for the polls application.


How Django Work Behind the scene
![Django Workflow](django-workflow.jpg)
