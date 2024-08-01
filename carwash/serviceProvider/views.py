from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from serviceProvider.models import Services
from serviceProvider.models import Business_details
from bookings.models import Bookings
from users.models import Address


# Create your views here.
def home(request):
    data={}
    if(request.user.is_staff==True):
        provider_services = Services.objects.filter(sid=request.user)
        
        get_bookings = Bookings.objects.filter(service__in=provider_services)
        data['bookings'] = get_bookings
        
        return render(request, "serviceProvider/home.html", context=data)
    else:
        return redirect("/")
    
def add_services(request):
    data={}
    user_id = request.user.id
    provider_id = User.objects.get(id=user_id)
    if(request.user.is_staff==True):
        if(request.method=="POST"):
            service = request.POST['service']
            price = request.POST['price']
            print(service, price)
            save_services = Services.objects.create(name=service, price=price, sid=provider_id)
            save_services.save()
            return redirect("/provider/business-details/")


        return render(request, "serviceProvider/add_service.html")
    else:
        return redirect("/")


def add_details(request):
    data={}
    user_id = request.user.id
    provider_id = User.objects.get(id=user_id)
    if(not Business_details.objects.filter(id=user_id)):

        if(request.user.is_staff==True):
                if(request.method=="POST"):
                    carwash_name = request.POST['carwash_name']
                    owner_name = request.POST['owner_name']
                    phone_number = request.POST['phone']
                    address = request.POST['address']
                    print(carwash_name, owner_name, phone_number, address)

                    save_details= Business_details.objects.create(carwash_name=carwash_name, address=address, owner_name=owner_name, sid=provider_id, phone_number=phone_number)
                    save_details.save()
                    return redirect("/provider/business-details/")


                return render(request, "serviceProvider/business_details.html")
    else:
        return HttpResponse("You already have a business registered ")
        # return HttpResponse("Sorry")

def show_business_details(request):
    user_id = request.user.id
    provider_id = User.objects.get(id=user_id)
    data={}
    business_details = Business_details.objects.filter(sid=provider_id)
    data['details'] = business_details
    service_details = Services.objects.filter(sid=provider_id)
    data['services'] = service_details
    return render(request, "serviceProvider/details.html", context=data)


def update_info(request):

    user_id = request.user.id
    provider_id = User.objects.get(id=user_id)
    data={}
    business_details = Business_details.objects.filter(sid=provider_id)
    data['details'] = business_details

    if(request.method=="POST"):
        carwash_name = request.POST['carwash_name']
        owner_name = request.POST['owner_name']
        phone = request.POST['phone']
        address = request.POST['address']

        print(carwash_name, owner_name, phone, address)
        update_details = business_details[0]
        data['update'] = update_details
        business_details.update(carwash_name=carwash_name, owner_name=owner_name, phone_number=phone, address=address)
        return redirect("/provider/business-details/")

    return render(request, "serviceProvider/update_info.html", context=data)

def update_service(request):
   pass