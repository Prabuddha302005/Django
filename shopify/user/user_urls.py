from django.urls import path
from user import views
urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.user_login)
]