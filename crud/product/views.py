from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductModel
# Create your views here.

def add(request):
    if(request.method == "POST"):
        product_name=request.POST['name']
        product_price=request.POST['price']
        product_category=request.POST['category']
        print(product_name, product_price, product_category)
        product = ProductModel.objects.create(name=product_name,price=product_price,category=product_category)
        # product.save()
        # product.save(): This saves the new product instance to the database. However, since we used .create(), the save() method is not strictly necessary here as create() already saves the instance. 
        return HttpResponse("Check your terminal")
    return render(request, "product/add.html")