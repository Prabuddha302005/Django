from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
