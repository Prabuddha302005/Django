from django.contrib import admin
from django.urls import path,include
from train import views as train_views
from hotels import views as hotels_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', hotels_views.showView),
    path('train/', train_views.showView),
    path('bus/', include('bus.urls'))
]
