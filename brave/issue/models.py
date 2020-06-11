from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from user.models import Department
# Create your models here.

class Ticket(models.Model):
    item_name = models.CharField(max_length=150)
    fault_description = models.CharField(max_length=150)
    date_of_report = models.DateField()
    location = models.CharField(max_length=250)
    raised_by = models.CharField(max_length=255)
    fixed_by = models.CharField(max_length=250, null=True, blank=True)
    action_taken = models.CharField(max_length=250, null=True, blank=True)
    cause_of_breakdown = models.CharField(max_length=255, blank=True)
    engineer_comment = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    OP = 'Open'
    CL = 'Close'
    BR = 'Being Reviewed'
    STA = (
        (OP, 'Open'),
        (CL, 'Closed'),
        (BR, 'Being Reviewed')
    )
    status = models.CharField(max_length=250,default=False,choices=STA)