from django.urls import path
from bus import views

urlpatterns = [
    # path('', views.homeVie),
    path('bus/', views.showView),
]
