from django import forms

from .models import *

class CreateReportForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['project_name','team_lead','genre','start_date','end_date','delivery_date','country','venue_location','status','distribution_platform','project_brief']