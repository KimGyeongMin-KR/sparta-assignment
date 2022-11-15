from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth import views as auth_views

from .serializer import CustomTokenObtainPairSerializer, UserProfileSerializer, UserSerializer
from .models import User

# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = request.user
        serializer = UserSerializer(users)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'가입완료'}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg" : f"{serializer.errors}"}, status = status.HTTP_400_BAD_REQUEST)

class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        me = request.user
        you = get_object_or_404(User, pk = user_id)
        if me in you.followers.all():
            you.followers.remove(me)
            return Response('언팔', status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response('팔로우',status = status.HTTP_200_OK)


class ProfileView(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(User, pk = user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)



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
        print(request.user)
        return Response('get rq')