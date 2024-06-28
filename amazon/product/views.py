from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showProduct(request):
    return render(request, 'product/index.html')
# Create your views here.
