from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import views as auth_views

from .serializer import CustomTokenObtainPairSerializer, UserSerializer
from .models import User

# Create your views here.

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'가입완료'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg" : f"{serializer.errors}"}, status = status.HTTP_400_BAD_REQUEST)



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


from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response('get rq')