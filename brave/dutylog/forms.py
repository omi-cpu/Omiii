from django import forms

from .models import *

class CreateDLForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['additional_comments']