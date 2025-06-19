from django.contrib import admin
from django.urls import path, include
from . import views

# for media setup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # this name key or property will help you latter
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("miniapp/", include("miniapp.urls")),
    #
    # FOR DEV ENV ONLY
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
