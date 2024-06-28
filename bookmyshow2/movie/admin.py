from django.contrib import admin
from movie import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'release_date']
admin.site.register(models.Movie)
