from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *


# Create your views here.
class CreateDoc(generic.CreateView):
    form_class = CreateDocForm
    template_name = 'docs/create_doc.html'

    def get_success_url(self, ):
        return reverse_lazy('doc')

class DocView(ListView):
    model = Doc
    template_name = 'docs/doc_list.html'