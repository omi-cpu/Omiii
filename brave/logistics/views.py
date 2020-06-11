from django.shortcuts import render
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from datetime import datetime, timedelta, timezone
from django.views.generic import UpdateView, TemplateView, DeleteView, CreateView

# Create your views here.

class VehicleList(ListView):
    model = Vehicle
    template_name = 'logistics/vehicle.html'

class RegisterVehicle(generic.CreateView):
    form_class = RegistervehicleForm
    template_name = 'logistics/create_vehicle.html'

    def get_success_url(self, ):
        return reverse_lazy('v')

    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        return super().form_valid(form)

class UpdateVehicle(UpdateView):
    model = Vehicle
    fields = ['name']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('v')

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)

class TripLogView(ListView):
    model = TripLog
    template_name = 'logistics/triplog.html'

class CreateTripLog(generic.CreateView):
    form_class = TripLogForm
    template_name = 'logistics/triplog_form.html'

    def get_success_url(self, ):
        return reverse_lazy('tr')

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        form.instance.created_at = datetime.now()
        return super().form_valid(form)

class UpdateTripLog(UpdateView):
    model = TripLog
    fields = ['name']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('tr')

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)

class MileageTrackerView(ListView):
    model = TripLog
    template_name = 'logistics/mileage.html'

class CreateMileage(generic.CreateView):
    form_class = MileageForm
    template_name = 'logistics/mileage_form.html'

    def get_success_url(self, ):
        return reverse_lazy('mt')