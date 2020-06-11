from django.contrib.auth.decorators import login_required
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from user.models import Organization
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic import DetailView, View, TemplateView
from django.views.generic import CreateView
from datetime import datetime
from schedule.views import *



# Create your views here.
class CreateProject(generic.CreateView):
    form_class = CreateReportForm
    template_name = 'project/form.html'

    def get_success_url(self, ):
        return reverse_lazy('rl')

class CalendarMixin(CalendarViewPermissionMixin):
    model = Calendar
    slug_url_kwarg = "calendar_slug"

class ProjectList(TemplateView):
    template_name = "schedule/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org_list'] = Organization.objects.all()
        context['project_list'] = Project.objects.all()
        context["calendar_slug"] = self.kwargs.get("calendar_slug")
        return context


class ProjectList2(ListView):
    model = Project
    template_name = 'project/list.html'


