from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    price = forms.FloatField()