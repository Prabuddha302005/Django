from django.shortcuts import render
from customer_form import forms
from django.http import HttpResponse
# Create your views here.
def add(request):
    if(request.method == "GET"):
       customer_form = forms.Form()
       data={}
       data['form']=customer_form
       print(data['form'])
       return render(request, 'customer/index.html', context=data)
    else:
          customer_data = forms.Form(request.POST)
          if(customer_data.is_valid):
            customer_data.save(commit=True)
            return HttpResponse("Customer added sucessfully, please check your table")