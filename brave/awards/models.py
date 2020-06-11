from django.db import models

# Create your models here.

class ShowOfTheWeek(models.Model):
    show_title = models.CharField(max_length=250)
    show_location = models.CharField(max_length=250)
    showing_time = models.TimeField()
    photo = models.ImageField(upload_to='awards/',blank=True)


class Awardees(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='awards/',blank=True)
    description = models.TextField()

class TeamCollaboration(models.Model):
    full_name_1 = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='awards/',blank=True)
    full_name_2 = models.CharField(max_length=250)
    image_2 = models.ImageField(upload_to='awards/',blank=True)
    commendation = models.TextField()