from django.views.generic.edit import UpdateView
from .models import *
from django.views.generic import ListView,CreateView,DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class vehicleListView(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name='vehicle_list.html'

class vehicleCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Vehicle
    fields = '__all__'
    success_message = "New vehicle data successfully added."
    template_name = 'vehicle_form.html'


class vehicleUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Vehicle
    fields = '__all__'
    success_message = "Vehicle data updated successfully."
    template_name = 'vehicle_form.html'

class vehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'

class vehicleDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')