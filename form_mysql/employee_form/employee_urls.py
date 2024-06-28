from django.urls import path
from employee_form import views
urlpatterns = [
    path('add/', views.add),
]
