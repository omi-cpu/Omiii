from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','department','shifts_per_roster','roles']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]

class NewDeptForm(forms.ModelForm):
    class Meta():
        model = Department
        fields = ['name',]


class Settings(forms.ModelForm):
    class Meta():
        model = Organization
        fields = '__all__'

class CreateUserForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ['username', 'password','first_name','last_name','email','department', 'roles']