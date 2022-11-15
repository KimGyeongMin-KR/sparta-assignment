from django.shortcuts import render
from .models import AccessLog
# Create your views here.

def index(request):
    AccessLog.objects.create(location='introduce')
    return render(request, 'introduce/index.html')