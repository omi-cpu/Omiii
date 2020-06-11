from django import forms

from .models import *

class DigitalScheduleForm(forms.ModelForm):
    class Meta():
        model = DigitalSchedule
        fields = ['name', 'start_date', 'end_date', 'state', 'digital_editor', 'others', 'description']

class VideoEditorForm(forms.ModelForm):
    class Meta():
        model = VideoEditorSchedule
        fields = ['name', 'start_date', 'end_date', 'state', 'video_editor', 'others', 'description']

class GraphicScheduleForm(forms.ModelForm):
    class Meta():
        model = GraphicSchedule
        fields = ['name', 'start_date', 'end_date', 'state', 'graphic_editor', 'others', 'description']

class PreProForm(forms.ModelForm):
    class Meta():
        model = PreProductionSchedule
        fields = ['name', 'start_date', 'end_date', 'state', 'production_cost', 'producer_1', 'producer_2', 'director_of_photography_1', 'director_of_photography_2', 'director_of_photography_3', 'director_of_photography_4']