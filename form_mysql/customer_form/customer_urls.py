from django.urls import path
from customer_form import views

urlpatterns = [
    path('add/', views.add),
]