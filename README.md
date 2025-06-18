# Django Tutorial: A Concise Guide

[Day 1](#day-01) | 
[Day 2](#day-02) | 
[Day 3](#day-03) | 
[Day 4](#day-04) | 
[Day 5](#day-05)


This guide provides a quick overview of Django, including project structure, folder explanations, and how to work with mini-apps and templates.

<a id="day-01"></a>
## 📅 Day 01: Introduction

## Prerequisites

*   Basic knowledge of Python, HTML, CSS, and JavaScript
*   Python 3.10 or later
*   uv (Install with `pip install uv`)

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


</br></br></br>

---
---
---

</br></br></br>



<a id="day-02"></a>
## 📅 Day 2: Creating Views and URLs
### Django Project and File Structure

This section will guide you through creating views and connecting them to URLs.

*   **views.py:** This file contains the view functions that handle requests and return responses. The name `views.py` is a convention; if you name it differently, Django won't automatically recognize it as the views module.

*   **Creating a view:** A view is a Python function that receives a request and returns a response. For example:

    ```python
    from django.http import HttpResponse

    def my_view(request):
        return HttpResponse("Hello, world!")
    ```

*   **Connecting a view to a URL:** To access a view in a browser, you need to map it to a URL in `urls.py`. For example:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("my-url/", views.my_view, name="my_view"),
    ]
    ```

    The `path()` function takes three arguments:

    *   `route`: The URL pattern to match.
    *   `view`: The view function to call.
    *   `name`: A unique name for the URL, which can be used to refer to it in templates and other parts of the code.

    The `name` property is important because it allows you to change the URL without breaking any links to it. If you don't use the `name` property, you'll have to manually update all the links whenever you change the URL.

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


</br></br></br>

---
---
---

</br></br></br>

<a id="day-03"></a>
## 📅 **Day 3: Create Mini-App and Use Jinja Templates in Django**

In Django, a **mini-app** (often just called an "app") is a modular piece of your project that handles a specific feature or domain (like polls, blog, users, etc). Django encourages breaking your project into multiple apps for better **separation of concerns**, **reusability**, and **scalability**.

---

## 🎯 What Is a Mini-App in Django?

A mini-app is a Python package inside your Django project that contains its own `models.py`, `views.py`, `urls.py`, and optionally `templates/`, `static/`, etc. It helps keep your code **organized** and **modular**.

### ✅ When to Create a New App

* When a feature is **logically independent** (e.g., blog, forum, authentication).
* When it may be **reused** in other projects or parts of the project.
* When the existing app is becoming **too large** or **unmanageable**.

---

## 🛠️ Step-by-Step Guide: Create and Integrate a Mini-App

### 1️⃣ Create the App

```bash
py manage.py startapp my_mini_app
```

This will create a folder `my_mini_app` with:

```
my_mini_app/
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py   # (you may need to create this manually)
├── templates/
│   └── my_mini_app/
│       └── index.html
```

---

### 2️⃣ Define Views (`my_mini_app/views.py`)

```python
from django.shortcuts import render

def index(request):
    return render(request, 'my_mini_app/index.html')

def about(request):
    return render(request, 'my_mini_app/about.html')
```

---

### 3️⃣ Define URLs (`my_mini_app/urls.py`)

Create this file if it doesn’t exist.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

---

### 4️⃣ Connect to Main Project

#### a. Add App to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_mini_app',  # 👈 Register the mini-app here
]
```

#### b. Include App’s URLs in Main `urls.py`

In `project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('miniapp/', include('my_mini_app.urls')),  # 👈 Connect the mini-app
]
```

Now, visiting `http://127.0.0.1:8000/miniapp/` will show your mini-app's homepage.

---

## 📄 5️⃣ Add Jinja-style Templates

Create the HTML files inside:

```
my_mini_app/templates/my_mini_app/index.html
my_mini_app/templates/my_mini_app/about.html
```

### Example: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Mini App Home</title>
</head>
<body>
    <h1>Welcome to the Mini App!</h1>
    <p>This is the index page.</p>
</body>
</html>
```

Django by default supports its own templating language, which is very similar to Jinja (e.g., `{% %}` and `{{ }}` syntax). You can also use pure Jinja2 if you explicitly configure it, but in most Django projects, the default engine is sufficient and similar.

---

## 🚀 6️⃣ Run the Development Server

```bash
py manage.py runserver
```

Visit:

* `http://127.0.0.1:8000/miniapp/` – for index
* `http://127.0.0.1:8000/miniapp/about/` – for about page

---

## 📌 Summary

| Step | Action                                 |
| ---- | -------------------------------------- |
| 1    | `startapp my_mini_app`                 |
| 2    | Write `views.py` functions             |
| 3    | Add URLs in `urls.py`                  |
| 4    | Register app in `settings.py`          |
| 5    | Include app’s URL in project `urls.py` |
| 6    | Add templates and use them in views    |
| 7    | `runserver` and test the routes        |





</br></br></br>

---
---
---

</br></br></br>



<a id="day-04"></a>
## 📅 Day 4: Integrating Tailwind CSS with Django (Enhanced with Node/NPM Support)

Tailwind CSS is a utility-first CSS framework for rapidly building custom user interfaces. Here’s how to integrate it into your Django project **with support for npm and automatic setup**.


* A check for Node.js before installing Tailwind dependencies.
* Automatic setting of the `TAILWIND_CSS_BIN` path in `settings.py` if necessary.
* A fallback for users who do not have Node.js installed.
* Clear instructions for `uv` virtual environments.

---

### 🔧 Step 1: Install Required Packages

First, install `django-tailwind`:

```bash
uv pip install 'django-tailwind[reload]'
```

> ⚠️ If `uv` doesn't work (e.g., says "audited 1" but nothing installs), fallback to regular pip:

```bash
python -m pip install --upgrade pip
pip install 'django-tailwind[reload]'
```

> ✅ Make sure you're inside a **`.venv`** or **`.uv`** virtual environment before installing!

---

### 🛠️ Step 2: Check Node.js & Install Dependencies

Before continuing, make sure Node.js is installed:

```bash
node -v
npm -v
```

If not installed, download it from: [https://nodejs.org/](https://nodejs.org/)

**💡 Linux Quick Install:**

```bash
sudo apt install nodejs npm -y
```

> ✅ You *must* have Node.js for Tailwind CSS to compile!

---

### 🧱 Step 3: Create and Configure Theme App

Create the Tailwind app:

```bash
python manage.py tailwind init theme
```

Then in your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'tailwind',
    'theme',
    ...
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
```

---

### 🔧 Step 4: Set NPM Binary Path (Optional but Recommended)
if you face this Error during tailwind CSS installation command :
    
        CommandError:
        It looks like node.js and/or npm is not installed or cannot be found.

        Visit <https://nodejs.org> to download and install node.js for your system.

        If you have npm installed and still getting this error message, set NPM_BIN_PATH variable in settings.py to match path of NPM executable in your system.

        Example:
        NPM_BIN_PATH = "/usr/local/bin/npm"
    

🚩 You have to download [Nodejs](https://nodejs.org/en/download) and install it on your device 


If you have Node.js but `tailwind install` fails, you may need to set the full npm binary path:

Find the npm path:

```bash
which npm
```

Then add this to `settings.py`:

```python
import os
NPM_BIN_PATH = os.getenv("NPM_BIN_PATH", "/usr/bin/npm")  # Update this if different
```

You can also set it manually like this:

```python
NPM_BIN_PATH = "/usr/bin/npm"  # Linux
# NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"  # Windows
```

This helps Django find the `npm` binary when building assets.

---

### 📦 Step 5: Install Tailwind CSS Dependencies

Now install the Tailwind dependencies:

```bash
python manage.py tailwind install
```

This will install packages like `tailwindcss`, `autoprefixer`, and `postcss`.

---



### ✅ **Step-by-Step Template Setup**

#### 1. **At the Top of `base.html` (Template File)**

Load the required Tailwind template tags:

```django
{% load static tailwind_tags %}
```

✅ This line enables Django to use Tailwind-related template tags.

---

#### 2. **Inside `<head>` Tag (Usually at the top of HTML)**

Insert the Tailwind CSS stylesheet link:

```django
{% tailwind_css %}
```

✅ This line injects the compiled Tailwind CSS into your HTML.

---

### 🔧 Example `base.html` (Basic Setup)

```html
{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Site{% endblock %}</title>
    {% tailwind_css %}
</head>
<body>
    {% block content %}
    <!-- Your content here -->
    {% endblock %}
</body>
</html>
```



Now you can use Tailwind utility classes in your HTML:

```html
<h1 class="text-3xl font-bold text-blue-600">Hello, Tailwind!</h1>
```

---

Absolutely! Here's the revised section of your guide that replaces **Step 8** and clarifies the usage of the Tailwind dev server vs. production build — ideal for a `README.md`:

---

### 🧪 Step 8: Run Tailwind CSS Compiler (Development Only)

During **development**, open a **new integrated terminal** (you can name it `tailwind`) and start the Tailwind compiler:

```bash
python manage.py tailwind start
```

This watches your templates and CSS files for changes and **automatically recompiles your Tailwind CSS** with hot-reload support.

> ✅ Keep this terminal running in the background while developing your frontend!

---

### 🚀 Production Setup: Compile Once, No Extra Terminal Needed

When you're ready to deploy or no longer need hot-reload:

1. Run the Tailwind build command:

   ```bash
   python manage.py tailwind build
   ```

2. Then collect static files:

   ```bash
   python manage.py collectstatic
   ```

3. Now Django will serve the final, compiled Tailwind CSS without needing a separate terminal or `tailwind start`.

> ⚠️ **Important:** Never use `tailwind start` in production — it's only for development.

---

### ✅ Summary

| Environment     | Command                           | Purpose                         |
| --------------- | --------------------------------- | ------------------------------- |
| Development     | `python manage.py tailwind start` | Live-reloading CSS compiler     |
| Production      | `python manage.py tailwind build` | One-time CSS compilation        |
| Production step | `python manage.py collectstatic`  | Gathers static files for Django |


---

## 🧠 Why Use `django-tailwind`?

* **Live reload support**: Tailwind styles update in real-time.
* **Isolation**: Keeps Tailwind config separate from your backend logic.
* **Cleaner organization**: Your custom CSS and JS live inside the theme app.

---

## 🧭 When Should You Use a Separate Tailwind App?

You should create a separate app like `theme` when:

* You want to **modularize your front-end styling**.
* You're building a **custom UI** that heavily uses Tailwind classes.
* You're working with a **team** that handles frontend and backend separately.
* You plan to integrate **Alpine.js, Flowbite, or other Tailwind plugins**.

---


### **🔥 Tailwind Hot Reload Integration**


✅ **Why Use Auto Reloading?**

During development, tools like `django-browser-reload` automatically refresh the browser when you change Tailwind CSS or templates. This speeds up your workflow and saves you from manual reloading.

---


🛠 **2. Update `INSTALLED_APPS`**

```python
INSTALLED_APPS = [
    ...
    "django_browser_reload",
]
```

⚙️ **3. Update `MIDDLEWARE`**

```python
MIDDLEWARE = [
    ...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
```

🌐 **4. Add URL pattern**

```python
from django.urls import path, include

urlpatterns = [
    ...
    path("__reload__/", include("django_browser_reload.urls")),
]
```


---

## ✅ Conclusion

By integrating Tailwind CSS with Django using `django-tailwind`, you get a powerful frontend setup that stays clean, efficient, and highly customizable. Your styling is now organized, hot-reloaded, and ready for production.

</br>

---
<center>Break For 5 minutes</center>

---
</br>

Here's a clear explanation of the terminal messages, what the warning means, and how to fix it — including applying migrations and setting up the Django admin:

---

## ⚠️ **Fixing: “Unapplied Migrations” Warning**

You're seeing this message:

> `You have 18 unapplied migration(s)... Your project may not work properly...`

This means Django has changes in its internal apps (`auth`, `admin`, `sessions`, etc.) that haven't been applied to your database yet.

---

### ✅ **Fix Step 1: Apply Migrations**

Run this command in your terminal:

```bash
python manage.py migrate
```

This will apply all pending migrations and set up the database tables properly.

---

### ✅ **Fix Step 2: Create Superuser for Admin Panel**

If you want access to Django’s admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

It will prompt you for:

* Username
* Email
* Password

Once created, you can log in at:

```
http://127.0.0.1:8000/admin/
```

---

### 🧪 Development Notes

* This message is **normal** during development and not an error.
* You only need to run `migrate` once (or when models change).
* The warning:

  > `WARNING: This is a development server. Do not use it in a production setting.`

  just reminds you **not to use `runserver` in production**. Use **Gunicorn**, **uWSGI**, or **Daphne** for deployment instead.



---

### ✅ **Fix Step 3: Reset User Password (Admin CLI)**

If you forgot your admin password or want to reset any user's password via the terminal, use:

```bash
python manage.py changepassword <username>
```

For example:

```bash
python manage.py changepassword admin
```

It will prompt you to enter a new password securely.

---

> 💡 If you don’t remember the username, you can check it in the database (e.g., via SQLite browser) or log in to the Django shell:


 ```bash
 python manage.py shell
 ```

 ```python
 from django.contrib.auth.models import User
 User.objects.all()
 ```


</br></br></br>

---
---
---
</br></br></br>

<a id="day-05"></a>
## 📅 Day 5: Handling Models and URLs in Django (With Best Practices)

In real-world projects, organizing your Django code **properly from the beginning** is crucial. Here's how to do that professionally.

---

### 📦 1. ❌ Don’t Put Models in the Project's Main App

✅ **Best Practice:**
Create separate Django **apps for each logical domain** (e.g., `blog`, `accounts`, `products`).

Instead of putting models in `project/models.py` (which doesn’t even exist by default), organize like this:

```
myproject/
│
├── blog/
│   ├── models.py  ← BlogPost, Category, etc.
│   └── views.py
│
├── accounts/
│   ├── models.py  ← UserProfile, OTPVerification, etc.
│   └── views.py
```

This makes your code modular and easier to scale.

---

### 🌐 2. Modular URL Structure

✅ **Each app should have its own `urls.py`**, and you should `include()` it in your main project’s `urls.py`.

**Main Project (`myproject/urls.py`):**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),       # Blog routes
    path('accounts/', include('accounts.urls')),  # Auth routes
]
```

---

### 🧱 3. One Responsibility per App

**Think of apps like reusable modules**:

| App Name   | Responsibility                             |
| ---------- | ------------------------------------------ |
| `blog`     | Handles posts, categories, comments        |
| `accounts` | Registration, login, user profiles         |
| `store`    | Products, orders, inventory                |
| `core`     | Shared utilities, context processors, etc. |

---

### 🔐 4. Don’t Mix Admin Logic with Business Logic

Avoid putting too much logic inside `admin.py`. Only register models or define admin customizations there. Keep real logic in:

* `models.py` (e.g., `save()` overrides)
* `signals.py` (e.g., post-save operations)
* `services.py` (for business logic)

---

### 🧪 5. Use Class-Based Views in Complex Cases

For real projects, **prefer Class-Based Views** (`ListView`, `DetailView`, `CreateView`, etc.) for reusability and built-in form support.

Example:

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
```

---

### 📋 Summary: Real-World Django Practices

| Best Practice                    | Why It Matters                 |
| -------------------------------- | ------------------------------ |
| Use separate apps                | Modular, reusable, scalable    |
| Keep models inside specific apps | Cleaner structure              |
| Use `include()` for app URLs     | Organized URL routing          |
| Avoid bloating `admin.py`        | Better separation of concerns  |
| Prefer class-based views         | Reusability, built-in features |

---

🛠 Want to go further? Add:

* `services.py` → For business logic
* `forms.py` → Custom form handling
* `signals.py` → Decouple actions like sending emails or logs

---
