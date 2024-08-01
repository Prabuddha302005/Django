from django.db import models
from serviceProvider.models import Services
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Bookings(models.Model):
    x = datetime.datetime.now()
    service = models.ForeignKey(Services, on_delete=models.CASCADE, db_column="service")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(x)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ])
