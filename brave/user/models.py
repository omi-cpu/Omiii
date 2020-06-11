"""User models."""
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from rosters.models import Role

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    """Custom user model."""

    class Meta:
        """Meta."""

        ordering = ('last_name', 'first_name')

    available = models.BooleanField(null=False, blank=False, default=True)
    shifts_per_roster = models.IntegerField(null=False, blank=False, default=0)
    max_shifts = models.BooleanField(null=False, blank=False, default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    roles = models.ManyToManyField('rosters.Role')

    def __str__(self):
        """How a user object is displayed."""
        return self.last_name + "," + self.first_name

    def get_absolute_url(self):
        """URL."""
        return reverse("user_detail", args=[str(self.id)])


class Organization(models.Model):
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return str(self.country)