from django import forms
from employee_form import models

class EmployeeForm(forms.Form):
    
        name = forms.CharField(max_length=50)
        phone = forms.CharField(max_length=50)
        city = forms.CharField(max_length=50)
        salary = forms.FloatField()
