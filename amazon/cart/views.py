from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showCart(request):
    return render(request, 'cart/index.html')
