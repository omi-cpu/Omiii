from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.models import Department


# Create your models here.

class Comment(models.Model):
    additional_comments = models.TextField(null=True)
    created_at = models.DateTimeField(null=True)
    username = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
