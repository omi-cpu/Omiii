from datetime import datetime, timedelta, timezone
from django.views.generic import UpdateView, TemplateView, DeleteView, CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *

class AwardsView(generic.ListView):
    model = ShowOfTheWeek
    template_name = 'awards/list.html'
    context_object_name = 'sotw_list'
    queryset = ShowOfTheWeek.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AwardsView, self).get_context_data(**kwargs)
        context['awards_list'] = Awardees.objects.all()
        context['tc_list'] = TeamCollaboration.objects.all()
        return context

class ShowWeekView(generic.CreateView):
    form_class = ShowWeekForm
    template_name = 'awards/sow_form.html'

    def get_success_url(self, ):
        return reverse_lazy('l')

class TeamCollaboView(generic.CreateView):
    form_class = TeamForm
    template_name = 'awards/create_teamcollabo.html'

    def get_success_url(self, ):
        return reverse_lazy('l')

class CreateAwardeeView(generic.CreateView):
    form_class = AwardeeForm
    template_name = 'awards/create_awardee.html'

    def get_success_url(self, ):
        return reverse_lazy('l')

