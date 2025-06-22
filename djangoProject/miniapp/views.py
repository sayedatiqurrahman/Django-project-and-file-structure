from django.shortcuts import render
from .models import AppVariety, AppStore
from django.shortcuts import get_object_or_404
from .forms import AppVarietiesForm


# Create your views here.
def mini_app_home(req):
    apps = AppVariety.objects.all()
    return render(req, "miniapp/all_mini_app.html", {"apps": apps})


def mini_app_detail(req, app_id):
    # app = AppVariety.objects.get(id=app_id)
    # or
    app = get_object_or_404(AppVariety, id=app_id)
    return render(req, "miniapp/app_details.html", {"app": app})


def app_stores(req):
    stores = None
    if req.method == "POST":
        form = AppVarietiesForm(req.POST)
        if form.is_valid():
            app_variety = form.cleaned_data["app_variety"]
            stores = AppStore.objects.filter(app_varieties=app_variety)
    else:
        form = AppVarietiesForm()
    return render(req, "miniapp/app_stores.html", {"stores": stores, "form": form})
