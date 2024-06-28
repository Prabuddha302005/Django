from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import ProductModel
# from product import forms
# Create your views here.
def addProduct(request):
    if(request.method=="POST"):
     pname=request.POST['name']
     pprice=request.POST['price']
     pcategory=request.POST['category']
     pdescription=request.POST['description']
     print(pname,pprice,pcategory, pdescription)
     product=ProductModel.objects.create(name=pname,price=pprice,category=pcategory, description=pdescription)
     product.save()
     return redirect("/product/show")

    return render(request, "product/add.html")

def ShowProduct(request):
         products = ProductModel.objects.all()
         data={}
         data['products'] = products
         
         return render(request, "product/show.html", context=data)


def updateProduct(request, product_id):
     products = ProductModel.objects.filter(id=product_id)
     product = products[0]
     data={}
     data['products'] = product
     if(request.method=="POST"):
          pname=request.POST['name']
          pprice=request.POST['price']
          pcategory=request.POST['category']
          pdescription=request.POST['description']
          print(pname,pprice,pcategory, pdescription)
          products.update(name=pname,price=pprice,category=pcategory, description=pdescription)
          return redirect("/product/show")

     return render(request, "product/update.html", context=data)

def deleteProduct(request, product_id):
     product = ProductModel.objects.get(id=product_id)
     product.delete()
     return redirect("/product/show")


