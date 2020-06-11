from django.db import models
from user.models import Organization
from django.conf import settings
import os

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=150)
    team_lead = models.CharField(max_length=150)
    genre = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    delivery_date = models.DateField()
    country = models.ForeignKey(Organization, on_delete=models.CASCADE)
    venue_location = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    distribution_platform = models.CharField(max_length=250)
    project_brief = models.CharField(max_length=250)