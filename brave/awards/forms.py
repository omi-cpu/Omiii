from django import forms

from .models import *

class ShowWeekForm(forms.ModelForm):
    class Meta():
        model = ShowOfTheWeek
        fields = ['show_title','show_location','showing_time','photo']

class AwardeeForm(forms.ModelForm):
    class Meta():
        model = Awardees
        fields = ['name','photo','description']

class TeamForm(forms.ModelForm):
    class Meta():
        model = TeamCollaboration
        fields = ['full_name_1','image_1','full_name_2','image_2','commendation']