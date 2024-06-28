from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_user(request):
    msg = "<h1>User Name<h1>"
    return HttpResponse(msg)

def update_user(request):
    msg = "<h1>Update user</h1>"
    return HttpResponse(msg)

def delete_user(request):
    msg = "<h1>Delete user</h1>"
    return HttpResponse(msg)


