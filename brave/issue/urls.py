from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('if/', views.GenerateTicket.as_view(), name='if'),
    path('il/', views.TicketView.as_view(), name='il'),
    path('il2/', views.Ticket2View.as_view(), name='il2'),
    re_path('updateil/(?P<pk>[\w-]+)$', views.UpdateTicket.as_view(), name='updateil'),
]