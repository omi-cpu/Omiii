from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    path('dash2', views.dashboard2, name='dashboard_with_pivot2'),
    path('data2', views.pivot_data2, name='pivot_data2'),
    path('indexf/', views.IndexView.as_view(), name='indexf'),
]