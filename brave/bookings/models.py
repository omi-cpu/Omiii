from django.db import models

# Create your models here.

class Studio(models.Model):
    name = models.CharField(max_length=250)

class BoardRoom(models.Model):
    name = models.CharField(max_length=250)

class Book(models.Model):
    user = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_on = models.DateTimeField()
    show_description = models.TextField()
    boardroom = models.ForeignKey(BoardRoom, on_delete=models.SET_NULL, null=True)

class Book2(models.Model):
    user = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_on = models.DateTimeField()
    show_description = models.TextField()
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)
