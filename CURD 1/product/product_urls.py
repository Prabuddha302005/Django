from django.urls import path
from product import views

urlpatterns = [
    path('add/', views.addProduct),
    path('show/', views.ShowProduct),
    path('update/<product_id>', views.updateProduct),
    path('delete/<product_id>', views.deleteProduct),
]
