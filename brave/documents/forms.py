from django import forms

from .models import *

class CreateDocForm(forms.ModelForm):
    class Meta():
        model = Doc
        fields = ['document_title', 'document']