from django import forms

from .models import *

class SaveToStore(forms.ModelForm):
    class Meta():
        model = Store
        fields = ['item_name', 'serial_no', 'state','assigned_department']

class RequestFromStore(forms.ModelForm):
    class Meta():
        model = Store
        fields = ['item_name', 'serial_no']