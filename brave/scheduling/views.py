from django.shortcuts import render
#from schedule.models import Event, EventRelation, Calendar
from .models import *
from .forms import *

from django.views.generic.list import ListView
from django.views.generic import DetailView, View, TemplateView
from django.views.generic import CreateView

# Create your views here.

class HomeV(ListView):
    model = VideoEditor
    template_name = 'scheduling/home.html'