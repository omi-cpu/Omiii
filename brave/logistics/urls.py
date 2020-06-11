from logistics import views
from .forms import *
from .models import *
from .views import *
from django.urls import path, include, re_path

from django.conf.urls import include, url

urlpatterns = [
    path('ve/', views.RegisterVehicle.as_view(), name='ve'),
    path('v/', views.VehicleList.as_view(), name='v'),
    re_path('updated/(?P<pk>[\w-]+)$', views.UpdateVehicle.as_view(), name='updated'),
    path('trf/', views.CreateTripLog.as_view(), name='trf'),
    path('tr/', views.TripLogView.as_view(), name='tr'),
    re_path('update/(?P<pk>[\w-]+)$', views.UpdateTripLog.as_view(), name='update'),
    path('mtf/', views.CreateMileage.as_view(), name='mtf'),
    path('mt/', views.MileageTrackerView.as_view(), name='mt'),
]