from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    plate_number = models.CharField(max_length=150)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null=True, blank=True)
    vehicle_make_and_model = models.CharField(max_length=250)
    vehicle_colour = models.CharField(max_length=100)
    vehicle_purpose = models.CharField(max_length=150)

    def __str__(self):
        return self.plate_number

class TripLog(models.Model):
    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    production_name = models.CharField(max_length=150)
    date = models.DateField()
    odometer_start = models.CharField(max_length=150)
    odometer_stop = models.CharField(max_length=150)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null=True, blank=True)
    trip_distance = models.CharField(max_length=250)
    fuel_station_used = models.CharField(max_length=250)
    trip_information = models.CharField(max_length=250)

class Mileage(models.Model):
    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    odometer_reading = models.CharField(max_length=100)
    refuel_date = models.DateField()
    fuel_added = models.CharField(max_length=100)
    fuel_cost = models.CharField(max_length=150)
