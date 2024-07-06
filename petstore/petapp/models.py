from django.db import models

# Create your models here.
class Pet_model(models.Model):
    petName = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    price = models.FloatField()
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.petName} - {self.category}"         