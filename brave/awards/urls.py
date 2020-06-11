from django.urls import path, include, re_path

from awards import views
from .views import *

urlpatterns = [
    path('l/', views.AwardsView.as_view(), name='l'),
    path('sow/', views.ShowWeekView.as_view(), name='sow'),
    path('aw/', views.CreateAwardeeView.as_view(), name='aw'),
    path('tcfif/', views.TeamCollaboView.as_view(), name='tcfif'),
]