from django import forms

from .models import *

class TicketForm(forms.ModelForm):
    class Meta():
        model = Ticket
        fields = ['item_name', 'fault_description','location','cause_of_breakdown','status']