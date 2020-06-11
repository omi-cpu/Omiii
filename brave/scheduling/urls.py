from django.conf.urls import url
from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('hs/', views.HomeV.as_view(), name='hs'),
]