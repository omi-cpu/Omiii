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
class CreateLog(generic.CreateView):
    form_class = CreateDLForm
    template_name = 'dutylog/dl_form.html'


    def get_success_url(self, ):
        return reverse_lazy('dl',)

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


class DutyLogView(ListView):
    model = Comment
    template_name = 'dutylog/dl_list.html'
    redirect_field_name = 'redirect_to'

class UpdateDutyLog(UpdateView):
    model = Comment
    fields = ['additional_comments']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('dl')

    def form_valid(self, form):
        form.instance.date = datetime.now()
        return super().form_valid(form)
