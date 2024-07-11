from django.shortcuts import render, redirect
from seller.models import Product
def dashboard(request):
    data={}
    if(request.user.is_authenticated):
        added_products = Product.objects.all()
        data['products'] = added_products

        return render(request, "seller/dashboard.html", context=data)

    else:
        return redirect("/")
    
def app_product(request):
    
    if(request.method=="POST"):
        name=request.POST['name']
        category=request.POST['category']
        description=request.POST['description']
        price=request.POST['price']
        quantity=request.POST['quantity']
        is_available=request.POST.get('is_available') and ('is_available' in request.POST)
        image = request.FILES.get('image')
        print(name,price,description,quantity,category,is_available)

        created_product=Product.objects.create(name=name,price=price,category=category,description=description,quantity=quantity,is_active=is_available,image=image)
        created_product.save
        return redirect("/dashboard")

    return render(request, "seller/add_product.html")