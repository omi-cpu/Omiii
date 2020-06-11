from django.conf.urls import url
from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('kk/', views.BoardRoomList.as_view(), name='kk'),
    path('bk', views.CreateBoardRoom.as_view(), name='bk'),
    path('ssl/', views.StudioList.as_view(), name='ssl'),
    #url(r"^calendar/year/(?P<calendar_slug>[-\w]+)/$", ListView.as_view(model=Calendar), name="calendar_list"),
    re_path('calendar/(?P<calendar_slug>[-\w]+)/$', views.StudioList.as_view(), name='studio'),
    re_path('calendar/(?P<calendar_slug>[-\w]+)/$', views.BoardRoomList.as_view(), name='boardroom'),
]