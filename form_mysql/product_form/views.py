from django.shortcuts import render
from product_form import forms
from django.http import HttpResponse
from product_form import models
# Create your views here.
def addProduct(request):
    product_form = forms.ProductForm() 
    data={}
    data['form']=product_form

    if(request.method == "POST"):
        pname = request.POST['name'] 
        pdescription = request.POST['description'] 
        pprice = request.POST['price'] 
        print(pname, pdescription, pprice)

        product = models.ProductModel.objects.create(name=pname, description=pdescription, price=pprice)
        return HttpResponse("Check your console/ database")

    return render(request, 'product/product.html', context=data)