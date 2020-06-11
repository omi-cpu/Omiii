from django.db import models
from user.models import Department


# Create your models here.

class DigitalEditor(models.Model):
    digital_editor = models.ForeignKey(Department, on_delete=models.CASCADE)

class GraphicEditor(models.Model):
    graphic_editor = models.ForeignKey(Department, on_delete=models.CASCADE)

class VideoEditor(models.Model):
    video_editor = models.ForeignKey(Department, on_delete=models.CASCADE)

class DigitalSchedule(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    NO = 'Normal'
    IM = 'Important'
    CR = 'Critical'
    STA = (
        (NO, 'Normal'),
        (IM, 'Important'),
        (CR, 'Critical'),
    )
    state = models.CharField(max_length=250, choices=STA)
    digital_editor = models.ForeignKey(DigitalEditor, on_delete=models.SET_NULL, null=True)
    others = models.TextField()
    description = models.TextField()

class VideoEditorSchedule(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    NO = 'Normal'
    IM = 'Important'
    CR = 'Critical'
    STA = (
        (NO, 'Normal'),
        (IM, 'Important'),
        (CR, 'Critical'),
    )
    state = models.CharField(max_length=250, choices=STA)
    video_editor = models.ForeignKey(VideoEditor, on_delete=models.SET_NULL, null=True)
    others = models.TextField()
    description = models.TextField()

class GraphicSchedule(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    NO = 'Normal'
    IM = 'Important'
    CR = 'Critical'
    STA = (
        (NO, 'Normal'),
        (IM, 'Important'),
        (CR, 'Critical'),
    )
    state = models.CharField(max_length=250, choices=STA)
    graphic_editor = models.ForeignKey(GraphicEditor, on_delete=models.SET_NULL, null=True)
    others = models.TextField()
    description = models.TextField()

class PreProductionSchedule(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    NO = 'Normal'
    IM = 'Important'
    CR = 'Critical'
    STA = (
        (NO, 'Normal'),
        (IM, 'Important'),
        (CR, 'Critical'),
    )
    state = models.CharField(max_length=250, choices=STA)
    production_cost = models.CharField(max_length=150)
    producer_1 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='producer_1')
    producer_2 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='producer_2')
    director_of_photography_1 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='director_of_photography_1')
    director_of_photography_2 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='director_of_photography_2')
    director_of_photography_3 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='director_of_photography_3')
    director_of_photography_4 = models.ManyToManyField(Department, max_length=250, blank=True, related_name='director_of_photography_4')