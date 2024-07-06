from django.urls import path
from product_form import views
urlpatterns = [
    path('add/', views.addProduct),
]
