from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import  *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic import DetailView, View, TemplateView
from django.views.generic import CreateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class GenerateTicket(generic.CreateView):
    form_class = TicketForm
    template_name = 'issues/form.html'


    def get_success_url(self, ):
        return reverse_lazy('il2',)

    def form_valid(self, form):
        form.instance.raised_by = self.request.user
        form.instance.date_of_report = datetime.now()
        return super().form_valid(form)


class TicketView(ListView):
    model = Ticket
    template_name = 'issues/all_issues_list.html'
    redirect_field_name = 'redirect_to'

class Ticket2View(ListView):
    model = Ticket
    template_name = 'issues/raised_issue.html'
    redirect_field_name = 'redirect_to'

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ['']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('il')

    def form_valid(self, form):
        return super().form_valid(form)