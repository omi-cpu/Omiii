from django.db import models
from user.models import Department

# Create your models here.
class Store(models.Model):
    item_name = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    serial_no = models.CharField(max_length=250)
    NI = 'New Item'
    OI = 'OI'
    STA = (
        (NI, 'New Item'),
        (OI, 'Old Item')
    )
    state = models.CharField(max_length=250, choices=STA, default=False)
    assigned_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    requested = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    close_request = models.BooleanField(default=False)
    requested_by = models.CharField(max_length=250, blank=False, default='user')
    return_date = models.DateField()


