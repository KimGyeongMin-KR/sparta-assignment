from django.shortcuts import render, redirect
from django.contrib import auth

from .models import User

# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, 'user/signup.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        
        User.objects.create(
            username = username,
            phone = phone,
            password = password,
            address = address,
        )
        return render(request, 'user/login.html')


def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(username=username, password = password)
            auth.login(request, user)
        except User.DoesNotExist:
            context = {
                'error' : 'Check your ID or PW'
            }
            return render(request, 'user/login.html', context)
        return redirect('/')