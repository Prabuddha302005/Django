from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_product(request):
    msg = "<h1>Product Name<h1>"
    return HttpResponse(msg)

def update_product(request):
    msg = "<h1>Update Product</h1>"
    return HttpResponse(msg)

def delete_product(request):
    msg = "<h1>Delete Product</h1>"
    return HttpResponse(msg)


