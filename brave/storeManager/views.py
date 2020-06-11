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
class SaveStore(generic.CreateView):
    form_class = SaveToStore
    template_name = 'issues/form.html'


    def get_success_url(self, ):
        return reverse_lazy('sl',)

    def form_valid(self, form):
        form.instance.raised_by = self.request.user
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


class StoreList(ListView):
    model = Store
    template_name = 'store/request.html'
    redirect_field_name = 'redirect_to'

class StoreList2(ListView):
    model = Store
    template_name = 'store/list.html'
    redirect_field_name = 'redirect_to'

class UpdateStore(UpdateView):
    model = Store
    fields = ['']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('sl')

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        form.instance.requested_by = self.request.user
        return super().form_valid(form)