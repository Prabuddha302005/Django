from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    sid=models.ForeignKey(User, on_delete=models.CASCADE, db_column="sid")

class Business_details(models.Model):
    carwash_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    sid=models.ForeignKey(User, on_delete=models.CASCADE, db_column="sid")
    