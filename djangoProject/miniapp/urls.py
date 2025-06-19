from django.urls import path, include
from . import views


app_name = "miniapp"

urlpatterns = [
    path(
        "", views.mini_app_home, name="mini-app"
    ),  # this name key or property will help you latter1
    path("<int:app_id>/", views.mini_app_detail, name="mini-app-detail"),
]
