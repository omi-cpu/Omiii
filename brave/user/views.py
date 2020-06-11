from datetime import datetime, timedelta, timezone

from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, DeleteView, CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from rosters.models import Role


# Create your views here.

class IndexView(ListView):
    model = Organization
    template_name = 'index.html'

class CommunicationList(ListView):
    model = Organization
    template_name = 'communication/list.html'

class PrView(ListView):
    model = CustomUser
    template_name = 'user/profile.html'

class NewSignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/signup.html'

    def get_success_url(self, ):
        return reverse_lazy('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })

class NewUsersView(ListView):
    model = CustomUser
    template_name = 'user/userslist.html'

class CreateUsersView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'user/create_user.html'

    def get_success_url(self, ):
        return reverse_lazy('us')

class NewDepartmentView(generic.CreateView):
    form_class = NewDeptForm
    template_name = 'user/create_dept.html'

    def get_success_url(self, ):
        return reverse_lazy('dept')

    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        return super().form_valid(form)

class DepartmentListView(ListView):
    model = Department
    template_name = 'user/deptlist.html'

class UpdateDept(UpdateView):
    model = Department
    fields = ['name']
    template_name = 'update_form.html'

    def get_success_url(self, ):
        return reverse_lazy('depts')

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "roster/user_list.html"
    login_url = "login"

    def get_queryset(self):
        return CustomUser.objects.order_by("last_name", "first_name")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "roster/user_detail.html"
    login_url = "login"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "roster/user_edit.html"
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "department",
        "shifts_per_roster",
        "max_shifts",
        "available",
        "roles",
    )
    login_url = "login"


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "roster/user_delete.html"
    success_url = reverse_lazy("user_list")
    login_url = "login"


class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "roster/user_new.html"
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "department",
        "shifts_per_roster",
        "max_shifts",
        "available",
        "roles",
    )
    login_url = "login"
