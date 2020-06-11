from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from user.models import CustomUser
from storeManager.models import Store
from django.views.generic.list import ListView
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'analytics/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = CustomUser.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

class IndexView(ListView):
    model = CustomUser
    template_name = 'analytics/index.html'

def dashboard2(request):
    return render(request, 'analytics/dash2.html', {})

def pivot_data2(request):
    dataset = Store.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)