from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
   data={}
   if(request.method == "POST"):
      uname = request.POST['username']
      uemail = request.POST['email']
      upassword = request.POST['password']
      cpassword = request.POST['cpassword']
      print(uname, uemail, upassword, cpassword)

      if(uname=="" or uemail=="" or upassword=="" or cpassword==""):
         data['error_msg'] = "fields cannot be empty"
         return render(request, 'myapp/register.html', context=data)
      elif(upassword != cpassword):
         data['error_msg'] = "Password did not match"
         return render(request, 'myapp/register.html', context=data)
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg'] = uname+" username already exists"
         return render(request, 'myapp/register.html', context=data)
      else:
         user = User.objects.create(username=uname)
         user.set_password(upassword)
         user.save()
         return redirect("/myapp/login")
   return render(request,'myapp/register.html',context=data)

def user_login(request):
   data={}
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      # print(username,password,cpassowrd)
      if(uname=="" or upass==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'myapp/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         # print(uname + " is already exist")
         data['error_msg']=uname + " is does not exist"
         return render(request,'myapp/login.html',context=data)
      else:
         user=authenticate(username=uname, password=upass)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request, "myapp/login.html", context=data)
         else:
            login(request, user)
            return redirect('/myapp/home')

   return render(request, "myapp/login.html")

def home(request):
   return render(request, "myapp/home.html")

# Update username 
def update_user_details(request):
   if(request.user.is_authenticated):
      if(request.method=="POST"):
         update_username = request.POST['username']
         print(update_username)

         user = User.objects.get(id=request.user.id)
         user.username = update_username
         user.save()
         return HttpResponse("Username Updated please check your database")
   else:
      return redirect("/myapp/login")
   return render(request, "myapp/update_details.html")

# update password 
def update_user_password(request):
   if(request.user.is_authenticated):
      if(request.method=="POST"):
         update_password = request.POST['password']
         print(update_password)

         user = User.objects.get(username=request.user.username)
         user.password = update_password
         user.set_password(update_password)
         user.save()
         
         return HttpResponse("Password Updated please check your database")
   else:
      return redirect("/myapp/login")
   return render(request, "myapp/update_pass.html")
