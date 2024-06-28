from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showUser(request):
    return render(request, 'user/index.html')

# Create your views here.
