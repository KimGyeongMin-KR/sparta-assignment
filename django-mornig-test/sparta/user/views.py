from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import views as auth_views


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
        
        User.objects.create_user(
            username = username,
            phone = phone,
            password = password,
            address = address,
        )
        return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            context = {
                'error' : 'Check your ID or PW'
            }
            return render(request, 'user/login.html', context)