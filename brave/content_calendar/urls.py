from django.conf.urls import url
from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('rf/', views.CreateProject.as_view(), name='rf'),
    path('rl/', views.ProjectList.as_view(), name='rl'),
    path('r2l/', views.ProjectList2.as_view(), name='r2l'),
    re_path('calendar/(?P<calendar_slug>[-\w]+)/$', views.ProjectList.as_view(), name='project'),

]