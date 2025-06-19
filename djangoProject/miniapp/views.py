from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404


# Create your views here.
def mini_app_home(req):
    apps = AppVariety.objects.all()
    return render(req, "miniapp/all_mini_app.html", {"apps": apps})


def mini_app_detail(req, app_id):
    # app = AppVariety.objects.get(id=app_id)
    # or
    app = get_object_or_404(AppVariety, id=app_id)
    return render(req, "miniapp/app_details.html", {"app": app})
