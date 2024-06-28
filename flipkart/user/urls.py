from django.urls import path
from user import views

urlpatterns = [
    path('', views.show_user),
    path('update/', views.update_user),
    path('delete/', views.delete_user),
]
