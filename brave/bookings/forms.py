from django import forms

from .models import *

class BoardRoomForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = ['user', 'start_date', 'end_date', 'start_time', 'end_time', 'created_on', 'show_description', 'boardroom']

class StudioForm(forms.ModelForm):
    class Meta():
        model = Book2
        fields = ['user', 'start_date', 'end_date', 'start_time', 'end_time', 'created_on', 'show_description', 'studio']