from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    # return HttpResponse("Hello User, You are at Django Home Page")
    return render(req, "website/index.html")


def about(req):
    return HttpResponse("This is about page")


def contact(req):
    return HttpResponse("This is contact page")
