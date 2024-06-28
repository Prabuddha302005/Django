
from django.urls import path
from cart import views

urlpatterns = [
    path('showCart', views.showCart),
   
]
