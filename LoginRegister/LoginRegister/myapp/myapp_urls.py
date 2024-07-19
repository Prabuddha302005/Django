from django.urls import path
from myapp import views
urlpatterns = [
    path('register/', views.register),
    path('login/', views.user_login),
    path('home/', views.home),
    path('update-profile/', views.update_user_details),
    path('update-password/', views.update_user_password),
]