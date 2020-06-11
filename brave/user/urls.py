from user import views
from .forms import *
from .models import *
from .views import *
from django.urls import path, include, re_path

from django.conf.urls import include, url

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='home'),
    path('ho/', CommunicationList.as_view(), name='ho'),
    path('p/', views.PrView.as_view(), name='p'),
    path('signup/', views.NewSignUpView.as_view(), name='signup'),
    url(r'^password/$', views.change_password, name='change_password'),
    path('us/', views.NewUsersView.as_view(), name='us'),
    path('usc/', views.CreateUsersView.as_view(), name='usc'),
    path('dept/', views.DepartmentListView.as_view(),name='dept'),
    path('deptf/', views.NewDepartmentView.as_view(),name='deptf'),
    re_path('updated/(?P<pk>[\w-]+)$', views.UpdateDept.as_view(), name='updated'),
    path("user/<int:pk>/edit/", UserUpdateView.as_view(), name="user_edit"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path(
        "user/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"
    ),
    path("user/new/", UserCreateView.as_view(), name="user_new"),
    path("user/", UserListView.as_view(), name="user_list"),
]