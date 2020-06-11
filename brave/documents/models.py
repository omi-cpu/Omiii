from django.db import models

# Create your models here.
class Doc(models.Model):
    document_title = models.CharField(max_length=250)
    document = models.FileField()