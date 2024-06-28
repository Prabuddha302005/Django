from django.urls import path
from product import views

urlpatterns = [
    path('', views.show_product),
    path('update/', views.update_product),
    path('delete/', views.delete_product),
]
