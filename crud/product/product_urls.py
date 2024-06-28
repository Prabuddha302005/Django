from django.urls import path
from product import views


urlpatterns = [
    path('add/', views.add),
]