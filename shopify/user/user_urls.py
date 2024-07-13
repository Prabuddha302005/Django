from django.urls import path
from user import views
urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('add-to-cart/<product_id>', views.add_to_cart)
]