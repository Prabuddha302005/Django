from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showView(req):
    return HttpResponse(
        '<h1>Bus near you</h1>'
    )
