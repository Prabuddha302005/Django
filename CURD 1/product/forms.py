from django import forms
from product import models

class ProductForm(forms.Form):

    name = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    price = forms.FloatField()