from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField( max_length=50)
    category=models.CharField(max_length=50)
    price=models.FloatField()


