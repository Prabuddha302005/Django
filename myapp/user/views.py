from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def register_User(request):
    if(request.method == "POST"):
        uName = request.POST['username']
        uPassword = request.POST['password']
        # uConpassword = request.POST['confirm-password']
        # print(uName, uPassword, uConpassword)
        user = User(
            username = uName,
            # password = uPassword,
            password =  make_password(uPassword)
        )
        user.save()
        # return HttpResponse("User registerd successully")

        return redirect("/user/showUser")
    return render(request, "myapp/register.html")


def show_user(request):
    user = User.objects.all()
    data = {}
    data['users'] = user

    return render(request, 'myapp/showUser.html', context=data)