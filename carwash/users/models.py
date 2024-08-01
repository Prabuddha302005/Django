from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)