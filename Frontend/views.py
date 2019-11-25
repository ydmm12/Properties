from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from API.models import APIModel

# Create your views here.

model_fields = ['name', 'address', 'area', 'email']

class PropertyList(ListView):
    model = APIModel

class PropertyView(DetailView):
    model = APIModel

class PropertyCreate(CreateView):
    model = APIModel
    fields = model_fields
    success_url = reverse_lazy('list')

class PropertyUpdate(UpdateView):
    model = APIModel
    fields = model_fields
    success_url = reverse_lazy('list')

class PropertyDelete(DeleteView):
    model = APIModel
    success_url = reverse_lazy('list')

