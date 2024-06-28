from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showView(reqest):
    return HttpResponse(
        '<h1>Train near you</h1>'
    )
