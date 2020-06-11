from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import *
from django.views.generic import DetailView, View, TemplateView
from django.views.generic import CreateView
from datetime import datetime
from .forms import *
from schedule.views import *

# Create your views here.

class CalendarMixin(CalendarViewPermissionMixin):
    model = Calendar
    slug_url_kwarg = "calendar_slug"

class BoardRoomList(ListView):
    template_name = "schedule/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['boardroom_list'] = Book.objects.all()
        context["calendar_slug"] = self.kwargs.get("calendar_slug")
        return context

class CreateBoardRoom(generic.CreateView):
    form_class = BoardRoomForm
    template_name = 'bookings/createboardroom.html'

    def form_valid(self, form):
        form.instance.created_on = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

class StudioList(CalendarMixin, DetailView):
    template_name = "schedule/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["calendar_slug"] = self.kwargs.get("calendar_slug")
        return context

class CreateStudio(generic.CreateView):
    form_class = StudioForm
    template_name = 'booking/createstudio.html'

    def form_valid(self, form):
        form.instance.created_on = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form)