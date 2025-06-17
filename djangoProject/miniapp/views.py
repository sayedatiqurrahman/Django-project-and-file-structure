from django.shortcuts import render


# Create your views here.
def mini_app_home(req):
    return render(req, "miniapp/all_mini_app.html")
