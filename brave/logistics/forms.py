from django import forms
from .models import *

class RegistervehicleForm(forms.ModelForm):
    class Meta():
        model = Vehicle
        fields = ['plate_number','driver', 'vehicle_make_and_model','vehicle_colour','vehicle_purpose']

class TripLogForm(forms.ModelForm):
    class Meta():
        model = TripLog
        fields = ['plate_number','production_name','date','driver','odometer_start','odometer_stop','trip_distance','fuel_station_used','trip_information']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datetime-input'})
        }

class MileageForm(forms.ModelForm):
    class Meta():
        model = Mileage
        fields = ['plate_number','odometer_reading','refuel_date','fuel_added','fuel_cost']
        widgets = {
            'refuel_date': forms.DateInput(attrs={'class': 'datetime-input'})
        }