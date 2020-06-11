from django.urls import path, include, re_path

from documents import views
from .views import *

urlpatterns = [
    path('docf/', views.CreateDoc.as_view(), name='docf'),
    path('doc/', views.DocView.as_view(), name='doc'),
]