from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.ImageField()
    is_active=models.BooleanField()
    image=models.ImageField(upload_to ='media')

