from django.urls import path
from users import views

urlpatterns = [
    path('', views.home),
    path('register/', views.user_registration),
    path('login/', views.user_login),
    path('logout/', views.user_logout),
    path('services/', views.services),
    path('view/<sid>/', views.view_services),
    path('service-book/<id>/', views.bookService),
    # path('booking-details/<id>', views.booknow),
    path('your-bookings/', views.booking_summary),
    path('settings/', views.settings),
    path('add-address/', views.add_address),
    path('update-details/', views.update_details),

    # path('paynow/<service_id>', views.pay_now),
]

