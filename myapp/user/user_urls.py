from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.register_User),
    path('showUser/', views.show_user),
]
