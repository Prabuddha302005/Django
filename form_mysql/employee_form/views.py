from django.shortcuts import render
from django.http import HttpResponse
from employee_form import forms
from employee_form import models

# Create your views here.
def add(request):
    employee_form=forms.EmployeeForm() #to show form
    data={}
    data['form']=employee_form
    if(request.method=="POST"):
              employeeFormData=forms.EmployeeForm(request.POST) #to collect data from form
              employee=models.EmployeeModel() #object of model class
              if(employeeFormData.is_valid()):
                     employee.name = employeeFormData.cleaned_data['name']
                     employee.phone = employeeFormData.cleaned_data['phone']
                     employee.salary = employeeFormData.cleaned_data['salary']
                     employee.city = employeeFormData.cleaned_data['city']
                     print(employee.name,employee.phone,employee.salary,employee.city)
                     employee.save()
                     return HttpResponse("Employee added, please check your table")
    return render(request,'employee/index.html',context=data)
