from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showView(reqest):
    return HttpResponse(
        '<h1>Hotels near you</h1>'
    )

def homeView(req):
    return HttpResponse(
        "<h1>Home page</h1>"
    )
