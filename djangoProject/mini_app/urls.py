from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.index, name="mini-app"
    ),  # this name key or property will help you latter
]
