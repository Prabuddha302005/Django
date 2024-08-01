from django.urls import path
from serviceProvider import views

urlpatterns = [
    path('home/', views.home),
    path('add-service/', views.add_services),
    path('add-details/', views.add_details),
    path('business-details/', views.show_business_details),
    path('update-info/', views.update_info),

]

