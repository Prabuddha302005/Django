from django.views.generic import ListView
from .models import Pet_model

class PetListView(ListView):
    model = Pet_model
    template_name = 'pet_list.html'
    context_object_name = 'pets'
# Create your views here.

# from django.shortcuts import render
# from .models import Pet_model

# def pet_list(request):
#     pets = Pet_model.objects.all()
#     return render(request, 'pet_list.html', {'pets': pets})
