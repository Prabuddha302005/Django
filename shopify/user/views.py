from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "user/home.html")
def register(request):
    data={}
    is_staff = False
    if(request.method=="POST"):
        uname = request.POST['username']
        upass = request.POST['password']
        cpass = request.POST['cpassword']
        utype = request.POST['type']
        print(uname, upass, utype)

        if(utype=='seller'):
            is_staff = True
        
        if(uname=="" or upass=="" or cpass==""):
         data['error_msg'] = "fields cannot be empty"
         return render(request, 'user/register.html', context=data)
        elif(upass != cpass):
         data['error_msg'] = "Password did not match"
         return render(request, 'user/register.html', context=data)
        elif(User.objects.filter(username=uname).exists()):
         data['error_msg'] = uname+" username already exists"
         return render(request, 'user/register.html', context=data)
        else:
         user = User.objects.create(username=uname, is_staff=is_staff)
         user.set_password(upass)
         user.save()
         return redirect("/login")
       
    return render(request, "user/register.html", context=data)

def user_login(request):
   data={}
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      # print(username,password,cpassowrd)
      if(uname=="" or upass==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'user/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         # print(uname + " is already exist")
         data['error_msg']=uname + " is does not exist"
         return render(request,'user/login.html',context=data)
      else:
         user=authenticate(username=uname, password=upass)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request, "user/login.html", context=data)
         else:
            login(request, user)
            if(user.is_staff==True):
            #   return render(request, "seller/dashboard.html")
                return redirect("/dashboard")
            else:
             return redirect('/')

   return render(request, "user/login.html")

def user_logout(request):
   logout(request)
   return redirect("/")