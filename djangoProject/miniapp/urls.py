from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "", views.mini_app_home, name="mini-app"
    ),  # this name key or property will help you latter1
]
