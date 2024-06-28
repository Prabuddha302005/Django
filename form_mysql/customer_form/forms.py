from django import forms
from customer_form import models


class Form(forms.ModelForm):
      class Meta:
            model = models.CustomerModel
            fields = ('name', 'phone', 'city')
    
    