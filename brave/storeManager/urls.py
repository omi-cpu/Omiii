from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    path('sf/', views.SaveStore.as_view(), name='sf'),
    path('sl/', views.StoreList.as_view(), name='sl'),
    path('sl2/', views.StoreList2.as_view(), name='sl2'),
    re_path('update/(?P<pk>[\w-]+)$', views.UpdateStore.as_view(), name='update'),
]