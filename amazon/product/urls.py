
from django.urls import path
from product import views

urlpatterns = [
    path('showProduct', views.showProduct),
   
]