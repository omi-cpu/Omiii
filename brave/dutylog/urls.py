from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('df/', views.CreateLog.as_view(), name='df'),
    path('dl/', views.DutyLogView.as_view(), name='dl'),
    re_path('updatedl/(?P<pk>[\w-]+)$', views.UpdateDutyLog.as_view(), name='updatedl'),
]