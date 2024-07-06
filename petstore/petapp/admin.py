from django.contrib import admin
from petapp import models
# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'petName', 'category', 'details', 'price')
admin.site.register(models.Pet_model, PetAdmin )